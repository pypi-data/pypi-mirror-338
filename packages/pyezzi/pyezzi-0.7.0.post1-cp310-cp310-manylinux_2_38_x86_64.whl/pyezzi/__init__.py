"""
Implementation of [weighted tissue thickness](https://nicoco.fr/weighted-thickness/).

Homepage: [gitlab.inria.fr](https://gitlab.inria.fr/ncedilni/pyezzi)

"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyezzi")
except PackageNotFoundError:
    __version__ = "DEV"

__doc__ = __doc__ + f"\nThis is the documentation for pyezzi version {__version__}"

from .thickness import (
    Domain,
    ThicknessSolver,
    compute_thickness,
    compute_thickness_cardiac,
)

__all__ = (
    "Domain",
    "ThicknessSolver",
    "compute_thickness",
    "compute_thickness_cardiac",
    "__version__",
)
