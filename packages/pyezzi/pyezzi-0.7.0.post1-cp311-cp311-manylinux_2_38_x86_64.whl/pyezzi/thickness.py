import logging
from dataclasses import dataclass
from typing import Collection

import numpy as np

from .flatten import flatten_domain, unflatten  # type:ignore
from .grad import gradient_3d_flat  # type:ignore
from .laplace import solve_3D as laplace_solver  # type:ignore
from .misc import keep_biggest_cc, timeit
from .yezzi import iterative_relaxation_3D  # type:ignore


@dataclass
class Domain:
    """
    This class handles going from a "full" (3D) to a "flat" (1D) representation
    of the domain.
    """

    endo: np.typing.NDArray[np.bool]
    r"""
    3D boolean mask representing the inner boundary of the domain: $\partial_0 R$

    All voxels "inside" must be set to `True`.
    """
    epi: np.typing.NDArray[np.bool]
    r"""
    3D boolean mask representing the outer boundary of the domain: $\partial_1 R$

    All voxels "inside" must be set to `True`, such that `endo` $\subset$ `epi`
    """
    spacing: Collection[float]
    """
    3 values representing the voxel spacing along the 3 axis of the domain.

    NB: anisotropic voxels are supported, but lead to very approximate results,
    consider resampling your domain to a uniform spacing beforehand.
    """

    weights: np.typing.NDArray[np.float64] | None = None
    r"""
    Float 3D array representing the "thickness weights", i.e. $f(x)$ in
    [the article](https://nicoco.fr/weighted-thickness/).

    Passing `None` is equivalent to passing an 3D array filled with `1`.
    """

    def __post_init__(self) -> None:
        self.epi = self.epi.astype(bool)
        self.endo = self.endo.astype(bool)

        if self.weights is not None:
            self.weights = self.weights.astype(np.float64)

        labeled_image = np.zeros_like(self.epi, dtype=int)
        labeled_image[self.epi] = 1
        labeled_image[self.endo] = 2

        self.wall = self.endo ^ self.epi
        self.wall[~self.epi] = False

        self.spacing = np.asarray(self.spacing, np.float64)

        self.indices, self.neighbours = flatten_domain(self.epi, self.endo)
        self.n = len(self.indices) // 3

    def restore_flat(
        self,
        flat_values: np.typing.NDArray[np.float64],
        outside: float = 0,
        inside: float = 0,
    ) -> np.typing.NDArray[np.float64]:
        """
        Go back from a "flat" (1)to a "full"

        :param flat_values: flat (1D) representation of the values on the domain
        :param outside: value to be set outside the outer boundary of the domain
        :param inside: value to be set inside the inner boundary of the domain
        :return: A 3D array where domain voxels are filled with `flat_values`
        """
        out = np.empty_like(self.wall, np.float64)
        out[self.endo] = inside
        out[~self.epi] = outside
        unflatten(flat_values, self.indices, out)
        return out


class ThicknessSolver:
    """
    Main class implementing the computation of weighted tissue thickness.

    Refer to `compute_thickness` and `compute_thickness_cardiac` for
    functional interfaces.
    """

    DEFAULT_TOLERANCE = 1e-6
    """Default relative tolerance convergence criterion."""
    DEFAULT_MAX_ITER = 5000
    """Default maximum iterations before giving up reaching the tolerance criterion."""

    def __init__(self, domain: Domain):
        """
        :param domain: The domain over which the thickness should be computed
        """
        self.domain = domain
        self.flat_laplace: np.typing.NDArray[np.float64] | None = None
        """Flat (1D) representation of the output of the heat equation solving"""
        self.flat_l0: np.typing.NDArray[np.float64] | None = None
        """Flat (1D) representation of $L_0$"""
        self.flat_l1: np.typing.NDArray[np.float64] | None = None
        """Flat (1D) representation of $L_1$"""
        self.flat_thickness: np.typing.NDArray[np.float64] | None = None
        """Flat (1D) representation of the thickness $W(x)$"""

    @timeit
    def solve_laplacian(
        self, tol: float | None = None, max_iter: int | None = None
    ) -> None:
        r"""
        Solve the heat equation over the domain.

        $\Delta u = 0$ with $u(\partial_0 R) = 0$ and $u(\partial_1 R) = 1$

        This is then used to compute the "tangent vector field":
        $\overrightarrow{T} = \frac{\nabla u}{|| \nabla u ||}$

        :param tol: relative error convergence criterion
        :param max_iter: maximum iterations
        """
        log.info("Solving Laplacian...")
        laplace_flat, iterations, max_error = laplace_solver(
            self.domain.neighbours,
            self.DEFAULT_TOLERANCE if tol is None else tol,
            self.DEFAULT_MAX_ITER if max_iter is None else max_iter,
            self.domain.spacing,
        )
        self.flat_laplace = laplace_flat

        log.debug(f"Laplacian: {iterations} iterations, max_error = {max_error}")
        self._get_gradients()

    @timeit
    def _get_gradients(self) -> None:
        log.debug("Computing tangent vector field")
        self.flat_gradients = gradient_3d_flat(
            self.flat_laplace, self.domain.neighbours, self.domain.spacing
        )

    @timeit
    def solve_thickness(
        self, tol: float | None = None, max_iter: int | None = None
    ) -> None:
        r"""
        Compute the thickness over the domain.

        $\nabla L_0 \cdot \overrightarrow{T} = 1$ with $L_0(\partial_0 R) = 0$

        $-\nabla L_1 \cdot \overrightarrow{T} = 1$ with $L_1(\partial_1 R) = 0$

        $W(x) = L_0(x) + L_1(x)$

        :param tol: relative error convergence criterion
        :param max_iter: maximum iterations
        """
        if self.flat_laplace is None:
            self.solve_laplacian()

        log.info("Computing L0 and L1...")

        if self.domain.weights is None:
            weights: np.typing.NDArray[np.float64] = np.full(
                self.domain.n, 1, dtype=np.float64
            )
        else:
            weights = self.domain.weights[self.domain.wall]

        l0_flat, l1_flat, iterations, max_error = iterative_relaxation_3D(
            self.domain.neighbours,
            self.flat_gradients,
            self.DEFAULT_TOLERANCE if tol is None else tol,
            self.DEFAULT_MAX_ITER if max_iter is None else max_iter,
            self.domain.spacing,
            weights,
        )
        log.debug(
            f"Thickness computation: {iterations} iterations, max_error = {max_error}"
        )

        self.flat_l0 = l0_flat
        self.flat_l1 = l1_flat
        self.flat_thickness = l0_flat + l1_flat

        if self.domain.weights is not None:
            # compensate for smaller values where weights < 1
            mean_spacing = np.mean(self.domain.spacing)  # type: ignore
            self.flat_thickness += mean_spacing - weights * mean_spacing

    @property
    def result(self) -> np.typing.NDArray[np.float64]:
        """
        3D representation of the thickness of the domain $W$
        """
        if self.flat_thickness is None:
            self.solve_thickness()
        assert self.flat_thickness is not None
        return self.domain.restore_flat(self.flat_thickness)

    @property
    def L0(self) -> np.typing.NDArray[np.float64]:
        r"""
        3D representation of distance $L_0$, from inner boundary $\partial_0 R$
        to a given voxel of the domain.
        """
        if self.flat_l0 is None:
            self.solve_thickness()
        assert self.flat_l0 is not None
        return self.domain.restore_flat(self.flat_l0)

    @property
    def L1(self) -> np.typing.NDArray[np.float64]:
        r"""
        3D representation of distance $L_1$, from outer boundary $\partial_1 R$
        to a given voxel of the domain.
        """
        if self.flat_l1 is None:
            self.solve_thickness()
        assert self.flat_l1 is not None
        return self.domain.restore_flat(self.flat_l1)

    @property
    def laplace_grid(self) -> np.typing.NDArray[np.float64]:
        """
        3D representation of $u$ (heat equation over the domain).
        """
        if self.flat_laplace is None:
            self.solve_laplacian()
        assert self.flat_laplace is not None
        return self.domain.restore_flat(self.flat_laplace, outside=1)


@timeit
def compute_thickness(
    domain: Domain,
    laplace_tolerance: float = ThicknessSolver.DEFAULT_TOLERANCE,
    laplace_max_iter: int = ThicknessSolver.DEFAULT_MAX_ITER,
    yezzi_tolerance: float = ThicknessSolver.DEFAULT_TOLERANCE,
    yezzi_max_iter: int = ThicknessSolver.DEFAULT_MAX_ITER,
) -> np.typing.NDArray[np.float64]:
    """
    Returns wall thicknesses computed with Yezzi's method

    Easy-to-use, functional interface to the ThicknessSolver class.

    :param domain: The domain represented with the appropriate class.
    :param laplace_tolerance:float, optional
    Maximum error allowed for Laplacian resolution
    :param laplace_max_iter:int, optional
    Maximum iterations allowed for Laplacian resolution
    :param yezzi_tolerance:float, optional
    Maximum error allowed for thickness computation
    :param yezzi_max_iter:int, optional
    Maximum iterations allowed for thickness computation
    :return:np.ndarray
    3D array of floats, representing thickness at each wall point
    """

    solver = ThicknessSolver(domain)
    solver.solve_laplacian(laplace_tolerance, laplace_max_iter)
    solver.solve_thickness(yezzi_tolerance, yezzi_max_iter)
    return solver.result


def compute_thickness_cardiac(
    endo: np.typing.NDArray[np.bool],
    epi: np.typing.NDArray[np.bool],
    spacing: tuple[float, float, float] = (1, 1, 1),
    weights: np.typing.NDArray[np.float64] | None = None,
    laplace_tolerance: float = ThicknessSolver.DEFAULT_TOLERANCE,
    laplace_max_iter: int = ThicknessSolver.DEFAULT_MAX_ITER,
    yezzi_tolerance: float = ThicknessSolver.DEFAULT_TOLERANCE,
    yezzi_max_iter: int = ThicknessSolver.DEFAULT_MAX_ITER,
) -> np.typing.NDArray[np.float64]:
    r"""
    Similar to `compute_thickness` but fully functional, does not require
    instantiating a `Domain`.

    :param endo: The endocardial mask, representing $\partial_0 R$
    :param epi: The epicardial mask, representing $\partial_1 R$
    :param spacing: Spacing of the voxels in the domain. Should be homogeneous for
        better results
    :param weights: Thickness weights $f(x)$, cf [weighted tissue thickness](https://nicoco.fr/weighted-thickness/).
    :param laplace_tolerance:float, optional
    Maximum error allowed for Laplacian resolution
    :param laplace_max_iter:int, optional
    Maximum iterations allowed for Laplacian resolution
    :param yezzi_tolerance:float, optional
    Maximum error allowed for thickness computation
    :param yezzi_max_iter:int, optional
    Maximum iterations allowed for thickness computation
    :return:np.ndarray
    3D array of floats, representing thickness at each wall point
    """
    return compute_thickness(
        Domain(endo=keep_biggest_cc(endo), epi=epi, spacing=spacing, weights=weights),
        laplace_tolerance=laplace_tolerance,
        laplace_max_iter=laplace_max_iter,
        yezzi_tolerance=yezzi_tolerance,
        yezzi_max_iter=yezzi_max_iter,
    )


log = logging.getLogger(__name__)
