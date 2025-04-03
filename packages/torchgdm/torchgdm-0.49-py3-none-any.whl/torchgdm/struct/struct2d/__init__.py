# -*- coding: utf-8 -*-
"""2D surface discretizations

.. currentmodule:: torchgdm.struct.struct2d

Classes
-------

.. autosummary::
   :toctree: generated/

   StructDiscretized2D
   StructDiscretizedSquare2D
   StructEffPola2D
   StructMieCylinderEffPola2D


Functions
---------

.. autosummary::
   :toctree: generated/

   extract_eff_pola_2d


Geometries
----------

.. autosummary::
   :toctree: generated/

   square
   rectangle
   circle
   split_ring
   triangle_equilateral


Discretizer functions
---------------------

.. autosummary::
   :toctree: generated/

   discretizer_square

"""
from . import surface
from . import line
from . import gpm
from . import geometries

from .surface import StructDiscretized2D
from .surface import StructDiscretizedSquare2D
from .line import StructEffPola2D
from .line import StructMieCylinderEffPola2D
from .line import extract_eff_pola_2d

from .geometries import discretizer_square

from .geometries import square
from .geometries import rectangle
from .geometries import circle
from .geometries import split_ring
from .geometries import triangle_equilateral
