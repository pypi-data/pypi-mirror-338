"""
global polarizability matrix (GPM) module

see:
Bertrand, M., Devilez, A., Hugonin, J.-P., Lalanne, P. & Vynck, K.
*Global polarizability matrix method for efficient modeling of light scattering by dense ensembles of non-spherical particles in stratified media.*
JOSA A 37, 70-83 (2020)
DOI: 10.1364/JOSAA.37.000070

author: P. Wiecha, 03/2025
"""

import warnings

import torch
from torchgdm.constants import DTYPE_FLOAT, DTYPE_COMPLEX
from torchgdm.struct.base_classes import StructBase
from torchgdm.tools.geometry import get_enclosing_sphere_radius
from torchgdm.tools.geometry import test_structure_distances
from torchgdm.tools.geometry import rotation_x, rotation_y, rotation_z
from torchgdm.tools import interp
from torchgdm.tools.misc import ptp


class StructGPM3D(StructBase):
    """3D global polarizability matrix structure

    Defines a GPM-based structure
    """

    __name__ = "global polarizability matrix 3D structure class"

    def __init__(
        self,
        positions: torch.Tensor,
        gpm_dicts: list,
        radiative_correction: bool = True,
        device: torch.device = None,
        environment=None,
        shift_z_to_r0: bool = True,
        progress_bar=True,
    ):
        """3D global polarizability matrix (GPM) class

        The main information is provided in the `gpm_dicts` argument, which is a list of dicts with the full global polarizability matrix definitions. Each dict defines one structure and must contain following:
            - 'wavelengths': wavelengths at which the polarizabilities are calculated
            - 'alpha_6x6':
                6x6 polarizability tensors of shape [len(wavelengths),6,6]. Coupling terms:
                    - pE: [:, :3, :3]
                    - mH: [:, 3:, 3:]
                    - mE: [:, 3:, :3]
                    - pH: [:, :3, 3:]
            optional keys:
            - 'full_geometry': the original volume discretization of the represented geometry
            - 'r0': the origin of the effective polarizabilities with respect to optional 'full_geometry'
            - 'enclosing_radius': enclosing radius of the original structure

        Args:
            positions (torch.Tensor): positions of the individual GPMs (same size as `gpm_dicts`)
            gpm_dicts (list): list of polarizability model dictionaries (same size as `positions`)
            radiative_correction (bool, optional): Whether to add raditative correction for cross section calculations. Defaults to True.
            device (torch.device, optional): Defaults to "cpu".
            environment (environment instance, optional): 3D environment class. Defaults to None.
            shift_z_to_r0 (bool, optional): If True, if a position z-value is zero, each polarizability model's z position will be shifted to the height of the effective dipole development center. Defaults to True.
            progress_bar (bool optional): whether to show progress bars on internal compute. Defaults to True.

        Raises:
            ValueError: _description_
        """
        super().__init__(device=device)

        self.n_dim = 3
        self.evaluation_terms = ["E", "H", "GPM"]

        # expand positions, put single scatterer in list
        move_positions = torch.as_tensor(
            positions, dtype=DTYPE_FLOAT, device=self.device
        )
        move_positions = torch.atleast_2d(move_positions)
        assert move_positions.shape[1] == 3

        self.radiative_correction = radiative_correction

        # single alpha_dict: put in list
        if type(gpm_dicts) == dict:
            gpm_dicts = [gpm_dicts] * len(move_positions)
        for _gd in gpm_dicts:
            assert type(_gd) == dict

        # environment at which alpha has been extracted (if given):
        if environment is None:
            self.environment = gpm_dicts[0]["environment"]
        else:
            warnings.warn("Using different environment than specified in GPM-dict.")
            self.environment = environment
        self.progress_bar = progress_bar

        for _adict in gpm_dicts:
            assert "wavelengths" in _adict
            if "GPM_N6xN6" not in _adict:
                raise ValueError(
                    "Global polarizability matrix description dicts must contain GPM tensors "
                    + "under the dict key: 'GPM_N6xN6'."
                )
            if "r_gpm" not in _adict:
                raise ValueError(
                    "Global polarizability matrix description dicts must contain GPM position tensors "
                    + "under the dict key: 'r_gpm'."
                )

        # use first pola-tensor wavelength range
        wavelengths = gpm_dicts[0]["wavelengths"]
        n_dp_gpm = len(gpm_dicts[0]["r_gpm"])
        self.wavelengths_data = torch.as_tensor(
            wavelengths, dtype=DTYPE_FLOAT, device=self.device
        )

        for _adict in gpm_dicts:
            _wls = torch.as_tensor(
                _adict["wavelengths"], dtype=DTYPE_FLOAT, device=self.device
            )
            if len(_adict["r_gpm"]) != n_dp_gpm:
                raise ValueError(
                    "All GPMs must have the same number of dipoles, if several GPMs are combined in one structure."
                )
            if not torch.all(torch.isin(self.wavelengths_data, _wls)):
                warnings.warn(
                    "Pre-calculated wavelengths of the structures are not identical. "
                    + "Try to use linear interpolation to fill missing values. "
                    + "This may be inaccurate."
                )
            if (torch.min(_wls) > torch.min(self.wavelengths_data)) or (
                torch.max(_wls) < torch.max(self.wavelengths_data)
            ):
                raise ValueError(
                    "Interpolation not possible. Pre-calculated wavelengths of the structures "
                    + "must be within the same range to allow interpolation."
                )

        # optionally shift z such that 'bottom' is at z=0. Do only if z=0
        if shift_z_to_r0:
            for i, p in enumerate(move_positions):
                if p[2] == 0:
                    p[2] = torch.as_tensor(
                        gpm_dicts[i]["r0"][2], dtype=p.dtype, device=p.device
                    )

        # populate polarizability tensors database for each position at
        # pre-calculated wavelengths. if necessary, interpolate between data points
        gpm_pos = []
        gpm_data = []
        reduced_step = []
        full_geometries = []
        for i, _adict in enumerate(gpm_dicts):
            gpm_pos.append(
                _adict["r_gpm"] - _adict["r0"] + move_positions[i].unsqueeze(0)
            )
            if torch.all(_adict["wavelengths"] == self.wavelengths_data):
                _gpm = _adict["GPM_N6xN6"]
            else:
                # if requested other wavelengths than given, interpolate
                _gpm = self._interpolate_single_alpha(
                    wls=self.wavelengths_data,
                    gpm_data=_adict["GPM_N6xN6"],
                    wl_data=_adict["wavelengths"],
                )
            gpm_data.append(_gpm)

            # optional values
            if "full_geometry" in _adict:
                full_geometries.append(
                    torch.as_tensor(
                        _adict["full_geometry"] - _adict["r0"],
                        dtype=DTYPE_FLOAT,
                        device=self.device,
                    )
                    + move_positions[i]
                )

            if "enclosing_radius" in _adict:
                _rstep = _adict["enclosing_radius"] * 2
            else:
                if "full_geometry" in _adict:
                    _r_eff = get_enclosing_sphere_radius(full_geometries[-1])
                    _rstep = _r_eff
                else:
                    _rstep = 0
            reduced_step += [_rstep / n_dp_gpm**0.66] * n_dp_gpm

        self.full_geometries = full_geometries

        # effective polarizabilities of each meshpoint at each wavelength: shape (Npos, Nwl, 6, 6)
        if len(gpm_data) != 0:
            self.gpm_data = torch.stack(gpm_data)
            self.gpm_pos = torch.stack(gpm_pos)
        else:
            raise ValueError("Unexpected error: Not GPM data.")

        # selfterms are zero. This acts as a placeholder and is not being used
        self.selfterms_data = torch.zeros_like(self.gpm_data)

        # populate lookup tables
        self.create_lookup()

        # other parameters ("step" corresponds to the effective diameter divided by nr of GPM dipole pairs)
        self.step = torch.as_tensor(reduced_step, dtype=DTYPE_FLOAT, device=self.device)

        # center of gravity of ensemble of all points
        self.r0 = self.get_center_of_mass()

        # set device
        self.set_device(self.device)

    def __repr__(self, verbose=False):
        """description about structure"""
        out_str = ""
        out_str += "------ 3D Global Polarizability Matrix nano-object -------"
        out_str += "\n" + " nr. of GPM structures:  {}".format(self.gpm_pos.shape[0])
        out_str += "\n" + " nr. of dipoles per GPM: {} (each {} ED and MD)".format(
            self.gpm_pos.shape[1] * 2, self.gpm_pos.shape[1]
        )
        out_str += "\n" + " total nr. of dipoles:   {} (each {} ED and MD)".format(
            self.gpm_pos.shape[0] * self.gpm_pos.shape[1] * 2,
            self.gpm_pos.shape[0] * self.gpm_pos.shape[1],
        )
        if len(self.full_geometries) > 0:
            pos = torch.cat(self.full_geometries)
            out_str += "\n" + " original geometry: "
            out_str += "\n" + "  - replacing nr. of meshpoints: {}".format(len(pos))
            bnds = ptp(pos, dim=0)
            out_str += "\n" + "  - size & position:"
            out_str += "\n" + "        X-extension    : {:.1f} (nm)".format(bnds[0])
            out_str += "\n" + "        Y-extension    : {:.1f} (nm)".format(bnds[1])
            out_str += "\n" + "        Z-extension    : {:.1f} (nm)".format(bnds[2])
            out_str += "\n" + "  - center of mass : ({:.1f}, {:.1f}, {:.1f})".format(
                *[float(f) for f in self.get_center_of_mass()]
            )

        return out_str

    def get_all_positions(self) -> torch.Tensor:
        return torch.reshape(self.gpm_pos, (-1, 3))

    def get_r_pm(self):
        """positions of electric and magnetic polarizable dipoles"""
        r_p = self.get_all_positions()
        r_m = self.get_all_positions()
        return r_p, r_m

    def get_e_selfconsistent(self, wavelength, **kwargs):
        if float(wavelength) not in self.fields_inside:
            raise ValueError(
                f"Inside field not available at wl={wavelength}nm. "
                + "Run the simulation."
            )
        return self.fields_inside[float(wavelength)].get_efield()

    def get_h_selfconsistent(self, wavelength, **kwargs):
        if float(wavelength) not in self.fields_inside:
            raise ValueError(
                f"Inside field not available at wl={wavelength}nm. "
                + "Run the simulation."
            )
        return self.fields_inside[float(wavelength)].get_hfield()

    def get_e_h_selfconsistent(self, wavelength, **kwargs) -> torch.Tensor:
        e = self.get_e_selfconsistent(wavelength)
        h = self.get_h_selfconsistent(wavelength)
        return torch.cat([e, h], dim=-1)

    def get_pm(self, wavelength):
        """self-consistent electric and magnetic dipole moments"""
        gpm = self.get_gpm(wavelength, self.environment)
        f_in = self.get_e_h_selfconsistent(wavelength)
        f_per_gpm = f_in.chunk(chunks=len(self.gpm_pos), dim=1)
        p = []
        m = []
        for i, _f in enumerate(f_per_gpm):
            _f = _f.reshape(len(_f), -1)
            _pm = torch.matmul(gpm[i], _f.unsqueeze(-1))[..., 0]
            _pm = _pm.reshape(len(_pm), -1, 6)
            p.append(_pm[..., :3])
            m.append(_pm[..., 3:])

        p = torch.cat(p, dim=1)
        m = torch.cat(m, dim=1)

        return p, m

    def get_center_of_mass(self) -> torch.Tensor:
        # use full geometries if available
        if len(self.full_geometries) == len(self.gpm_pos):
            r0 = [_pos.mean(dim=0) for _pos in self.full_geometries]
            r0 = torch.stack(r0, axis=0).mean(dim=0)
        else:
            r0 = self.gpm_pos.mean(dim=(0, 1))
        return r0

    def create_lookup(self):
        """Create a lookup table for the polarizability tensors"""
        # populate lookup tables with pre-calculated data
        self.lookup = {}
        for i_wl, wl in enumerate(self.wavelengths_data):
            self.lookup[float(wl)] = self.gpm_data[:, i_wl, :, :]

    def set_device(self, device):
        """move all tensors of the class to device"""
        super().set_device(device)
        if self.environment is not None:
            self.environment.set_device(device)

        if len(self.full_geometries) > 0:
            self.full_geometries = [_g.to(device) for _g in self.full_geometries]

        self.step = self.step.to(device)
        self.r0 = self.r0.to(device)
        self.wavelengths_data = self.wavelengths_data.to(device)

        self.gpm_data = self.gpm_data.to(device)
        self.gpm_pos = self.gpm_pos.to(device)
        self.selfterms_data = self.selfterms_data.to(device)

        # transfer the lookup tables
        for wl in self.lookup:
            self.lookup[wl] = self.lookup[wl].to(device)

    def _interpolate_single_alpha(self, wls, gpm_data, wl_data):

        # convert to tensor
        wls = torch.as_tensor(wls, dtype=DTYPE_FLOAT, device=self.device)
        wl_dat = torch.as_tensor(wl_data, dtype=DTYPE_FLOAT, device=self.device)
        gpm_dat = torch.as_tensor(gpm_data, dtype=DTYPE_COMPLEX, device=self.device)

        gpm_size = gpm_dat.shape[1]
        assert gpm_dat.shape[1] == gpm_dat.shape[2]

        # wavelength-interpolation of each tensor component
        a_ip = torch.zeros(
            (len(wls), gpm_size, gpm_size), dtype=DTYPE_COMPLEX, device=self.device
        )

        for i in range(gpm_size):
            for j in range(gpm_size):
                _func_ip = interp.RegularGridInterpolator([wl_dat], gpm_dat[:, i, j])
                _ip = _func_ip([wls])
                a_ip[:, i, j] = _ip

        return a_ip

    def interpolate_alpha(self, wls, a_data_many, wl_data, lookup=None):
        """interpolate the polarizabilities between available wavelengths"""
        from torchgdm.tools.misc import tqdm

        gpm_ip = torch.zeros(
            (self.gpm_data[0], len(wls), self.gpm_data[2], self.gpm_data[3])
        )

        # iterate all polarizabilities (different structures)
        for i_a, a_data in tqdm(
            enumerate(a_data_many),
            title="creating GPM lookup...",
            progress_bar=self.progress_bar,
        ):
            _gpm = self._interpolate_single_alpha(wls, a_data, wl_data)
            gpm_ip[i_a] = _gpm

        # optionally add to lookup
        if lookup is not None:
            for i_wl, wl in enumerate(wls):
                wl = float(wl)
                if wl not in lookup:
                    lookup[wl] = gpm_ip[:, i_wl, :, :]

        return gpm_ip

    # --- self-terms
    # self-terms are zero

    # --- polarizabilities
    def _call_interpolation(self, wavelength):
        warnings.warn(
            "Interpolating polarizabilities at wavelength {:.3f}.".format(
                float(wavelength)
            )
        )
        self.interpolate_alpha(
            [wavelength],
            self.gpm_data,
            self.wavelengths_data,
            lookup=self.lookup,
        )

    def get_gpm(self, wavelength: float, environment) -> torch.Tensor:
        """return list of GPM tensors (N_struct, 6N, 6N) of each GPM structure

        Args:
            wavelength (float): in nm

        Returns:
            list of torch.Tensor
        """
        if float(wavelength) not in self.lookup:
            self._call_interpolation(wavelength)

        return self.lookup[float(wavelength)]

    def get_polarizability_6x6(self, wavelength: float, environment) -> torch.Tensor:
        """return diagonal N6xN6 GPM

        warning: this does not return 6x6 tensors but
        GPMs of shape (N_structure, 6N, 6N)
        """
        return self.get_gpm(wavelength, environment)

    def get_selfterm_6x6(self, wavelength: float, environment) -> torch.Tensor:
        """return diagonal N6xN6 self-terms (zero)

        warning: this does not return 6x6 tensors but
        zeros of shape (N_structure, 6N, 6N)
        """
        return torch.zeros_like(self.gpm_data[:, 0])

    def get_polarizability_pE(self, wavelength: float, environment) -> torch.Tensor:
        raise Exception("GPM does not provide single, local polarizabilities")

    def get_polarizability_mE(self, wavelength: float, environment) -> torch.Tensor:
        raise Exception("GPM does not provide single, local polarizabilities")

    def get_polarizability_pH(self, wavelength: float, environment) -> torch.Tensor:
        raise Exception("GPM does not provide single, local polarizabilities")

    def get_polarizability_mH(self, wavelength: float, environment) -> torch.Tensor:
        raise Exception("GPM does not provide single, local polarizabilities")

    # --- geometry operations
    def translate(self, vector):
        """return a copy moved by `vector`"""
        vector = torch.as_tensor(vector, dtype=DTYPE_FLOAT, device=self.device)
        vector = torch.atleast_2d(vector)
        _shifted = self.copy()

        # shift effective dipole positions of each GPM
        _shifted.gpm_pos = self.gpm_pos + vector.unsqueeze(0)

        # shift center of mass positions
        _shifted.r0 = _shifted.get_center_of_mass()

        if len(_shifted.full_geometries) > 0:
            for _g in _shifted.full_geometries:
                _g += vector

        return _shifted

    def set_center_of_mass(self, r0_new: torch.Tensor):
        """move center of mass to new position `r0_new` (in-place)"""
        r0_new = torch.as_tensor(r0_new, device=self.device)
        r0_old = self.get_center_of_mass()

        if len(r0_new.shape) != 1:
            if len(r0_new) not in [2, 3]:
                raise ValueError("`r0_new` needs to be (X,Y) or (X,Y,Z) tuple.")

        # treat case r0_new is 2D (X,Y)
        if len(r0_new) == 2:
            r0_new = torch.as_tensor(
                [r0_new[0], r0_new[1], r0_old[2]], device=self.device
            )

        # move each dipole to origin, then to new location
        self.gpm_pos -= (r0_old - r0_new).unsqueeze(0).unsqueeze(1)

        if len(self.full_geometries) > 0:
            # move to origin, the to new pos.
            self.full_geometries = [
                _g - (r0_old - r0_new) for _g in self.full_geometries
            ]

        self.r0 = self.get_center_of_mass()

    # --- plotting
    def plot(
        self,
        projection="auto",
        scale=1.0,
        color="auto",
        linestyle_circle=(0, (2, 2)),
        color_circle="auto",
        color_circle_fill=None,
        alpha=1,
        show_grid=True,
        color_grid="auto",
        alpha_grid=0.25,
        legend=True,
        set_ax_aspect=True,
        reset_color_cycle=True,
        **kwargs,
    ):
        """plot the point polarizability structure (2D)

        Args:
            projection (str, optional): Cartesian projection. Default: "XY" or plane in which all dipoles lie. Defaults to "auto".
            scale (float, optional): scaling factor of the grid cells, if shown. Defaults to 1.0.
            color (str, optional): plot color. Defaults to "auto".
            linestyle_circle (tuple, optional): optional line style for enclosing circle. Defaults to (0, (2, 2)).
            color_circle (str, optional): optional alternative color for enclosing circle. Defaults to "auto".
            color_circle_fill (_type_, optional): optional alternative fill color for enclosing circle. Defaults to None.
            alpha (int, optional): optional transparency. Defaults to 1.
            show_grid (bool, optional): whether to show mesh grid (if available in structure). Defaults to True.
            color_grid (str, optional): optional alternative color for the mesh grid. Defaults to "auto".
            alpha_grid (float, optional): optional alternative transparency for the mesh grid. Defaults to 0.25.
            legend (bool, optional): show legend. Defaults to True.
            set_ax_aspect (bool, optional): automatically set aspect ratio to equal. Defaults to True.
            reset_color_cycle (bool, optional): reset color cycle after finishing the plot. Defaults to True.

        Returns:
            matplotlib axes
        """
        from torchgdm.visu import visu2d

        im = visu2d.geo2d._plot_structure_eff_pola(
            self,
            projection=projection,
            scale=scale,
            color=color,
            linestyle_circle=linestyle_circle,
            color_circle=color_circle,
            color_circle_fill=color_circle_fill,
            alpha=alpha,
            show_grid=show_grid,
            color_grid=color_grid,
            alpha_grid=alpha_grid,
            legend=legend,
            set_ax_aspect=set_ax_aspect,
            reset_color_cycle=reset_color_cycle,
            **kwargs,
        )
        return im

    def plot_contour(
        self,
        projection="auto",
        color="auto",
        set_ax_aspect=True,
        alpha=1.0,
        alpha_value=None,
        reset_color_cycle=True,
        **kwargs,
    ):
        """plot the contour of the underlying mesh (2D)

        Args:
            projection (str, optional): which cartesian plane to project onto. Defaults to "auto".
            color (str, optional): optional matplotlib compatible color. Defaults to "auto".
            set_ax_aspect (bool, optional): If True, will set aspect of plot to equal. Defaults to True.
            alpha (float, optional): matplotlib transparency value. Defaults to 1.0.
            alpha_value (float, optional): alphashape value. If `None`, try to automatically optimize for best enclosing of structure. Defaults to None.
            reset_color_cycle (bool, optional): reset color cycle after finishing the plot. Defaults to True.

        Returns:
            matplotlib line: matplotlib's `scatter` output
        """
        from torchgdm.visu.visu2d._tools import _get_axis_existing_or_new
        from torchgdm.visu.visu2d.geo2d import _plot_contour_discretized
        from torchgdm.visu.visu2d.geo2d import _reset_color_iterator

        if reset_color_cycle:
            _reset_color_iterator()

        if len(self.full_geometries) == 0:
            warnings.warn("No mesh grid data available. Skipping.")
            return None
        ax, show = _get_axis_existing_or_new()
        for subgeo in self.full_geometries:
            im = _plot_contour_discretized(
                subgeo,
                projection=projection,
                color=color,
                alpha=alpha,
                alpha_value=alpha_value,
                set_ax_aspect=set_ax_aspect,
                **kwargs,
            )
        return im

    def plot3d(self, **kwargs):
        """plot the point polarizability structure (3D)"""
        from torchgdm.visu import visu3d

        return visu3d.geo3d._plot_structure_eff_3dpola(self, **kwargs)

    # --- geometry operations
    def rotate(self, alpha, center=torch.as_tensor([0.0, 0.0, 0.0]), axis="z"):
        """rotate the structure

        Args:
            alpha (float): rotation angle (in rad)
            center (torch.Tensor, optional): center of rotation axis. Defaults to torch.as_tensor([0.0, 0.0, 0.0]).
            axis (str, optional): rotation axis, one of ['x', 'y', 'z']. Defaults to 'z'.

        Raises:
            ValueError: unknown rotation axis

        Returns:
            :class:`StructEffPola3D`: copy of structure with rotated geometry
        """
        _s_rot = self.copy()
        center = center.to(dtype=DTYPE_FLOAT, device=self.device)

        if axis.lower() == "x":
            rot = rotation_x(alpha, device=self.device)
        elif axis.lower() == "y":
            rot = rotation_y(alpha, device=self.device)
        elif axis.lower() == "z":
            rot = rotation_z(alpha, device=self.device)
        else:
            raise ValueError("Unknown rotation axis ''.".format(axis))

        # rotate GPM positions around `center`
        for i in range(len(_s_rot.gpm_pos)):
            _s_rot.gpm_pos[i] = torch.matmul(
                _s_rot.gpm_pos[i] - (center + self.r0), rot
            ) + (center + self.r0)

        # rotate full discretizations (if available)
        for i_g, _geo in enumerate(_s_rot.full_geometries):
            if len(_geo) > 1:
                _s_rot.full_geometries[i_g] = torch.matmul(
                    _geo - (center + self.r0), rot
                ) + (center + self.r0)

        # rotate all local and non-local polarizability tensors
        rot = rot.to(DTYPE_COMPLEX).unsqueeze(0).unsqueeze(0)
        rotT = rot.transpose(-2, -1)
        N_dp = 2 * self.gpm_pos.shape[1]
        for i_m in range(N_dp):
            m = 3 * i_m
            for i_n in range(N_dp):
                n = 3 * i_n
                _s_rot.gpm_data[..., m : m + 3, n : n + 3] = torch.matmul(
                    torch.matmul(
                        rotT,
                        _s_rot.gpm_data[..., m : m + 3, n : n + 3],
                    ),
                    rot,
                )

        # update lookup tables
        _s_rot.create_lookup()

        return _s_rot

    def combine(
        self, other, inplace=False, refresh_lookup=True, on_distance_violation="warn"
    ):
        """combine with a second structure

        Structures must be of same coupling type (electric / magnetic)

        Args:
            other (_type_): _description_
            inplace (bool, optional): Don't copy original structure, just add other structure. Can be necessary e.g. when gradients are required. Defaults to False.
            refresh_lookup (bool, optional): refresh the polarizability lookup table. Defaults to True.
            on_distance_violation (str, optional): can be "error", "warn", None (do nothing). Defaults to "error".

        Returns:
            :class:`StructBase`: new structure
        """
        if inplace:
            new_struct = self
        else:
            new_struct = self.copy()

        assert torch.all(new_struct.wavelengths_data == other.wavelengths_data)
        assert type(self) == type(other)

        N_dist1, N_dist2 = test_structure_distances(self, other)
        if on_distance_violation == "error" and (N_dist1 + N_dist2 > 0):
            raise ValueError(
                "Several meshpoints in structures are too close (struct1: {}, structu2: {})!".format(
                    N_dist1, N_dist2
                )
            )
        elif on_distance_violation == "warn" and (N_dist1 + N_dist2 > 0):
            warnings.warn(
                "Several meshpoints in structures are too close (struct1: {}, structu2: {})!".format(
                    N_dist1, N_dist2
                )
            )

        new_struct.gpm_pos = torch.concatenate([self.gpm_pos, other.gpm_pos], dim=0)
        new_struct.step = torch.concatenate([new_struct.step, other.step], dim=0)

        new_struct.gpm_data = torch.concatenate(
            [new_struct.gpm_data, other.gpm_data], dim=0
        )
        new_struct.selfterms_data = torch.concatenate(
            [new_struct.selfterms_data, other.selfterms_data], dim=0
        )

        # finally, add full geometries lists together
        new_struct.full_geometries = new_struct.full_geometries + other.full_geometries

        new_struct.r0 = new_struct.get_center_of_mass()
        # create lookup
        if refresh_lookup:
            new_struct.create_lookup()

        return new_struct


def get_gpm_positions_by_clustering_3d(
    struct, n_gpm_dp, skeletonize=True, status_plotting=False
):
    """get GPM dipole positions by sectioning the geometry via spectral clustering

    Geometry sectioning is done using scikit-learn's `SpectralClustering`.
    Optionally, as a pre-processing step, a simple skeletonization via thinning is performed.
    See: Lamprianidis et al. JQSRT 296, 108455 (2023)

    caution: doesn't support auto-diff

    Args:
        struct (`struct` instance): torchgdm structure instance
        n_gpm_dp (int): Number of GPM dipole positions to create
        skeletonize (bool, optional): If True, perform a skeletonization prior clustering. Defaults to True.
        status_plotting (bool, optional): If True, plot the structure and GPM positions. Defaults to False.

    Returns:
        torch.Tensor: List of 3D coordinates
    """
    import numpy as np
    import sklearn.cluster as skc
    from torchgdm import to_np
    from torchgdm.tools.geometry import get_step_from_geometry

    _struct = struct.copy()
    _struct.set_center_of_mass([0, 0, 0])

    if skeletonize:
        from torchgdm.tools.geometry import get_surface_meshpoints

        g_s = _struct.get_all_positions()
        step = get_step_from_geometry(g_s)
        while 1:  # iteratively remove surface-shells
            p_s, n_s = get_surface_meshpoints(g_s, NN_surface=100)
            # _sim_sf, _sim_inner = tools.split_simulation(_s, p_s)
            if len(p_s) == len(g_s):
                break

            idx_remain = []
            for i, pos in enumerate(g_s):
                ## test if 'pos' exists in geometry
                if torch.linalg.norm(p_s - pos, dim=1).min() > step / 4:
                    idx_remain.append(i)
            g_s = g_s[idx_remain]

        r_loc = to_np(g_s)
    else:
        r_loc = to_np(_struct.get_all_positions())

    # - cluster the regions
    clustering = skc.SpectralClustering(n_clusters=n_gpm_dp).fit(r_loc)
    labels = clustering.labels_

    r_effdp = []
    for l in np.unique(labels):
        ## ignore label '-1' which is noise in certain clustring algorithms
        if l >= 0:
            r_effdp.append(np.average(r_loc[labels == l], axis=0))
    r_effdp = np.array(r_effdp)

    if status_plotting:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 3))
        plt.subplot(131)
        _struct.plot_contour(projection="xy")
        plt.scatter(r_effdp[:, 0], r_effdp[:, 1])
        plt.subplot(132)
        _struct.plot_contour(projection="xz")
        plt.scatter(r_effdp[:, 0], r_effdp[:, 2])
        plt.subplot(133)
        _struct.plot_contour(projection="yz")
        plt.scatter(r_effdp[:, 1], r_effdp[:, 2])
        plt.show()

    return torch.as_tensor(r_effdp, dtype=DTYPE_FLOAT, device=struct.device)


# %%
# GPM extraction
# --------------
def extract_gpm_3d(
    struct,
    r_gpm,
    environment,
    wavelengths,
    probe_around_particle_surface=True,
    n_probe=500,
    distance_probe=3.0,
    n_dipole_sources=None,
    distance_dipoles=5000,
    verbose=True,
    progress_bar=True,
    device=None,
    residual_warning_threshold=1.0,
    batch_size=16,
):
    """Extract global polarizability matrix (GPM) of a volume discretized structure

    Extract the GPM for `struct` in a given `environement` at `wavelengths`.
    This is done in 3 steps:

        1) The effective dipole responses for each GPM dipole are obtained
           via matching at locations close to the structure surface.
        2) The second inverse problem of adjusting the GPM for different
           illuminations is solved via pseudoinverse.

    By default, use 14 plane waves (different incidence directions and polarizations).
    alternative: illumination with `n_dipole_sources` point-dipole sources if `n_dipole_sources` is an integer > 0.

    Args:
        struct (class:`StructDiscretized3D`): the discretized structure to extract the model for.
        r_gpm (int or torch.Tensor): Either int: number of positions or a torch.Tensor of shape (N, 3), giving the locations where to place effective dipole pairs.
        environment (environment class): 3D environement class.
        wavelengths (torch.Tensor): list of wavelengths to extract the model at. in nm.
        probe_around_particle_surface (bool, optional): Probe at fixed distance to particle surface. If False, probe on enclosing sphere surface. Defaults to True.
        n_probe (int, optional): number of probe positions on enclosing sphere. Defaults to 500.
        distance_probe (float, optional): additional distance to particle surface, in units of discretization step. Defaults to 3.0.
        n_dipole_sources (int, optional): If given, use `n` dipole sources as illumination instead of plane waves. Defaults to None.
        distance_dipoles (int, optional): if using dipole light sources, specify their distance to the surface (in nm). Defaults to 3.0.
        verbose (bool, optional): whether to sprint progess info. Defaults to True.
        progress_bar (bool, optional): whether to show a progress bar. Defaults to True.
        device (str, optional). Defaults to None, in which case the structure's device is used.
        residual_warning_threshold (float, optional). Maximum residual L2 norm before triggering a warning. Defaults to 0.25.

    Returns:
        dict: contains all informations about the effective dipole polarizability model
    """
    from torchgdm.env.freespace_3d.inc_fields import ElectricDipole, PlaneWave
    from torchgdm.simulation import Simulation
    from torchgdm.linearsystem import _reduce_dimensions
    from torchgdm.postproc.fields import nf
    from torchgdm.tools.geometry import get_enclosing_sphere_radius
    from torchgdm.tools.geometry import sample_random_spherical
    from torchgdm.tools.misc import tqdm
    from torchgdm.constants import DTYPE_COMPLEX, DTYPE_FLOAT

    _struct = struct.copy()
    _struct.set_center_of_mass([0, 0, 0])

    if device is None:
        device = _struct.device
    else:
        struct.set_device(device)

    # convert single wavelength to list
    wavelengths = torch.as_tensor(wavelengths, dtype=DTYPE_FLOAT, device=device)
    wavelengths = torch.atleast_1d(wavelengths)

    if verbose:
        import time

        print(
            "--- extracting GPM model (3D, {} wavelengths) ---".format(len(wavelengths))
        )
        t_start = time.time()

    # use first order multipole moments (propto local field)
    step_max = torch.max(_struct.step)
    enclosing_radius = get_enclosing_sphere_radius(_struct.get_all_positions())
    illumination_radius = enclosing_radius + distance_dipoles
    probe_radius = enclosing_radius + distance_probe * step_max

    if type(r_gpm) == int:
        r_gpm = get_gpm_positions_by_clustering_3d(_struct, r_gpm)
    else:
        r_gpm = torch.as_tensor(r_gpm, dtype=DTYPE_FLOAT, device=device)
        r_gpm = torch.atleast_2d(r_gpm)
    n_gpm_dp = len(r_gpm)

    # setup perpendicular plane waves illuminations
    if n_dipole_sources is None:
        pw_conf_list = [
            [0.0, 1.0, 0, "xz"],  # E-x, H-y, k-z
            [1.0, 0.0, 0, "xz"],  # E-y, H-x, k-z
            #
            [1.0, 0.0, torch.pi / 2.0, "xz"],  # E-x, H-z, k-y
            [0.0, 1.0, torch.pi / 2.0, "xz"],  # E-z, H-x, k-y
            #
            [1.0, 0.0, torch.pi / 2.0, "yz"],  # E-y, H-z, k-x
            [0.0, 1.0, torch.pi / 2.0, "yz"],  # E-z, H-y, k-x
            #
            [1.0, 0.0, -torch.pi / 2.0, "xz"],  # E-x, H-z, -k-y
            [0.0, 1.0, -torch.pi / 2.0, "xz"],  # E-z, H-x, -k-y
            #
            [1.0, 0.0, -torch.pi / 2.0, "yz"],  # E-y, H-z, -k-x
            [0.0, 1.0, -torch.pi / 2.0, "yz"],  # E-z, H-y, -k-x
            #
            [1.0, 0.0, torch.pi / 4.0, "xz"],  # oblique
            [0.0, 1.0, torch.pi / 4.0, "yz"],  # oblique
            #
            [0.0, 1.0, -torch.pi / 4.0, "xz"],  # oblique, opposite
            [1.0, 0.0, -torch.pi / 4.0, "yz"],  # oblique, opposite
        ]
        e_inc_extract = [
            PlaneWave(e0s=a, e0p=b, inc_angle=c, inc_plane=d, device=device)
            for [a, b, c, d] in pw_conf_list
        ]
    # optional: multiple dipole illuminations
    else:
        if n_dipole_sources <= 0 or type(n_dipole_sources) != int:
            raise ValueError(
                "dipole illumination mode: `n_dipoles` needs to be a positive integer."
            )

        # setup dipoles of random position and random orientation
        rnd_pos_dp = (
            sample_random_spherical(n_dipole_sources, device) * illumination_radius
        )
        e_inc_extract = [
            ElectricDipole(
                r_source=r_dp,
                p_source=torch.rand(3, device=device) * illumination_radius,
                device=device,
            )
            for r_dp in rnd_pos_dp
        ]

    # setup probe positions
    if probe_around_particle_surface:
        # - outside particle surface
        from torchgdm.tools.geometry import get_surface_meshpoints

        sf_pos, sf_vec = get_surface_meshpoints(_struct.get_all_positions())
        r_probe = sf_pos + step_max * sf_vec * distance_probe
        if len(r_probe) > n_probe:
            perm = torch.randperm(r_probe.size(0))
            idx = perm[:n_probe]
            r_probe = r_probe[idx]
    else:
        # - on circumscribing sphere
        r_probe = sample_random_spherical(n_probe, device) * probe_radius

    # replace illumination
    _sim = Simulation(
        structures=[_struct],
        environment=environment,
        illumination_fields=e_inc_extract,
        wavelengths=wavelengths,
        device=device,
    )

    if verbose:
        t0 = time.time()
        _pos_p, _pos_m = _sim._get_polarizable_positions_p_m()
        n_dp = len(_pos_p) + len(_pos_m)
        n_wl = len(wavelengths)
        print("Running simulation ({} dipoles, {} wls)... ".format(n_dp, n_wl), end="")
    _sim.run(verbose=False, progress_bar=progress_bar, batch_size=batch_size)

    if verbose and not progress_bar:
        print("Done in {:.2f}s.".format(time.time() - t0))

    # solve the optimization problem
    GPM_N6xN6 = torch.zeros(
        (len(wavelengths), n_gpm_dp * 6, n_gpm_dp * 6),
        dtype=DTYPE_COMPLEX,
        device=device,
    )
    if verbose:
        t0 = time.time()
        print("Running GPM optimization (GPM size {})... ".format(n_gpm_dp), end="")

    for i_wl in tqdm(range(len(wavelengths)), progress_bar, title=""):
        wl = wavelengths[i_wl]

        # calculate fields at probe locations for all illuminations
        # shape: (n_illumination, n_probe*6)
        nf_probe = nf(_sim, wl, r_probe=r_probe, progress_bar=False)
        f_eval = torch.cat([nf_probe["sca"].efield, nf_probe["sca"].hfield], dim=-1)
        f_eval = f_eval.reshape(len(e_inc_extract), -1)

        # illuminating fields at expansion locations
        # shape: (n_illumination, 6 * n_gpm_dp)
        f0_eval = torch.zeros(
            (len(e_inc_extract), 6 * n_gpm_dp), dtype=DTYPE_COMPLEX, device=device
        )
        for i_field, e_inc in enumerate(e_inc_extract):
            inc_f = e_inc.get_field(r_gpm, wl, environment)
            _f0 = torch.cat([inc_f.efield, inc_f.hfield], dim=-1)[0]
            f0_eval[i_field] = torch.flatten(_f0)

        # --- full 6x6 polarizability
        # calculate Green's tensors between all r_gpm and r_probe
        # shape: (n_probe, n_gpm, 6, 6)
        G_6x6 = environment.get_G_6x6(
            r_probe=r_probe.unsqueeze(1), r_source=r_gpm.unsqueeze(0), wavelength=wl
        )
        # reshape to (n_probe*6, n_gpm*6)
        G_all = _reduce_dimensions(G_6x6)

        # inv. problem #1: probe fields + Green's tensors --> dipole moments
        Gi = torch.linalg.pinv(G_all)
        pm_eff = torch.matmul(Gi.unsqueeze(0), f_eval.unsqueeze(-1))[..., 0]

        # inv. problem #2: dipole moments + illumination --> effective pola
        pinv_f0 = torch.linalg.pinv(f0_eval)
        alpha_6x6_inv = torch.matmul(pinv_f0, pm_eff).T

        # optimum alphas to obtain dipole moments for each illumination
        GPM_N6xN6[i_wl] = alpha_6x6_inv

    if verbose:
        print("Done in {:.2f}s.".format(time.time() - t_start))
        print("---------------------------------------------")

    dict_gpm = dict(
        r_gpm=r_gpm,
        GPM_N6xN6=GPM_N6xN6,
        wavelengths=wavelengths,
        # additional metadata
        full_geometry=_struct.get_all_positions(),
        n_gpm_dp=n_gpm_dp,
        r0=_struct.get_center_of_mass(),
        enclosing_radius=enclosing_radius,
        k0_spectrum=2 * torch.pi / wavelengths,
        extraction_r_probe=r_probe,
        extraction_illuminations=e_inc_extract,
        environment=environment,
    )
    if probe_around_particle_surface:
        dict_gpm["surface_vec_normal"] = sf_vec

    return dict_gpm
