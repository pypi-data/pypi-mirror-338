# -*- coding: utf-8 -*-
"""package for torchgdm structures

Contains Classes for 3D and 2D discretized structures and point (3D) and line (2D) effective polarizability structures:

.. currentmodule:: torchgdm.struct

3D
--

.. autosummary::
   :toctree: generated/
   
   StructDiscretizedCubic3D
   StructDiscretizedHexagonal3D
   StructMieSphereEffPola3D
   StructEffPola3D
   StructGPM3D


3D discretization
-----------------

.. autosummary::
   :toctree: generated/
   
   struct3d


2D
--

.. autosummary::
   :toctree: generated/
   
   StructDiscretizedSquare2D
   StructMieCylinderEffPola2D
   StructEffPola2D


2D discretization
-----------------

.. autosummary::
   :toctree: generated/
   
   struct2d

base class
----------

.. autosummary::
   :toctree: generated/
   
   StructBase

"""
from . import struct2d
from . import struct3d

# - 3D
from .struct3d.volume import StructDiscretized3D
from .struct3d.volume import StructDiscretizedCubic3D
from .struct3d.volume import StructDiscretizedHexagonal3D

from .struct3d.point import StructMieSphereEffPola3D  # Mie core-shell sphere
from .struct3d.point import StructEffPola3D

from .struct3d.gpm import StructGPM3D

# - 2D
from .struct2d.surface import StructDiscretized2D
from .struct2d.surface import StructDiscretizedSquare2D

from .struct2d.line import StructMieCylinderEffPola2D  # Mie core-shell cylinder
from .struct2d.line import StructEffPola2D

# - base class
from .base_classes import StructBase