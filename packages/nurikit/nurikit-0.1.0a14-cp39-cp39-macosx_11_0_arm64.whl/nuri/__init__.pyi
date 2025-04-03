"""

Project NuriKit: *the* fundamental software platform for chem- and
bio-informatics.
"""
from __future__ import annotations
from nuri.fmt import readfile
from nuri.fmt import readstring
from nuri.fmt import to_mol2
from nuri.fmt import to_pdb
from nuri.fmt import to_sdf
from nuri.fmt import to_smiles
from . import _log_adapter
from . import _log_interface
from . import _version
from . import core
from . import fmt
__all__: list = ['readfile', 'readstring', 'to_smiles', 'to_mol2', 'to_sdf', 'to_pdb', 'periodic_table', '__version__']
__full_version__: str = '0.1.0a14'
__version__: str = '0.1.0a14'
periodic_table: core._core.PeriodicTable  # value = <nuri.core._core.PeriodicTable object>
