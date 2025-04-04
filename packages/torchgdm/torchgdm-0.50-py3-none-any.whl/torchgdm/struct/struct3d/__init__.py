# -*- coding: utf-8 -*-
"""3D volume discretizations

.. currentmodule:: torchgdm.struct.struct3d

Classes
-------

.. autosummary::
   :toctree: generated/
   
   StructDiscretized3D
   StructDiscretizedCubic3D
   StructDiscretizedHexagonal3D
   StructMieSphereEffPola3D
   StructEffPola3D
   StructGPM3D


Functions
---------

.. autosummary::
   :toctree: generated/
   
   extract_eff_pola_3d
   extract_gpm_3d


Geometries
----------

.. autosummary::
   :toctree: generated/
   
   cube
   cuboid
   sphere
   spheroid
   disc
   ellipse
   split_ring
   prism_trigonal
   from_image


Discretizer functions
---------------------

.. autosummary::
   :toctree: generated/
   
   discretizer_cubic
   discretizer_hexagonalcompact


"""
from . import volume
from . import point
from . import gpm
from . import geometries

from .volume import StructDiscretizedCubic3D
from .volume import StructDiscretizedHexagonal3D
from .volume import StructDiscretized3D
from .point import StructEffPola3D
from .point import StructMieSphereEffPola3D
from .gpm import StructGPM3D

from .point import extract_eff_pola_3d
from .gpm import extract_gpm_3d

from .geometries import discretizer_cubic
from .geometries import discretizer_hexagonalcompact

from .geometries import cube
from .geometries import cuboid
from .geometries import sphere
from .geometries import spheroid
from .geometries import disc
from .geometries import ellipse
from .geometries import split_ring
from .geometries import prism_trigonal

from .geometries import from_image
