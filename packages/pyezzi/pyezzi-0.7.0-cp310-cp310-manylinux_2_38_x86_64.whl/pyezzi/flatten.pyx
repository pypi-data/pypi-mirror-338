import numpy as np

cimport numpy as cnp
cimport cython

from .common cimport OUTSIDE, INSIDE


@cython.boundscheck(False)
@cython.wraparound(False)
def flatten_domain(
    cnp.ndarray[cnp.npy_bool, ndim=3] epi,
    cnp.ndarray[cnp.npy_bool, ndim=3] endo,
) -> [np.typing.NDArray, np.typing.NDArray]:
    cdef unsigned int n = 0
    cdef unsigned int ii = 0
    cdef unsigned int i, j, k, c
    cdef cnp.ndarray[unsigned int, ndim=3] index_array = np.zeros_like(epi, dtype=np.uint32)

    for i in range(epi.shape[0]):
        for j in range(epi.shape[1]):
            for k in range(epi.shape[2]):
                if endo[i, j, k]:
                    index_array[i, j, k] = INSIDE
                    continue
                if not epi[i, j, k]:
                    index_array[i, j, k] = OUTSIDE
                    continue
                index_array[i, j, k] = n
                n += 1

    cdef cnp.ndarray[unsigned int, ndim=1] indices = np.empty(n * 3, dtype=np.uint32)

    for i in range(epi.shape[0]):
        for j in range(epi.shape[1]):
            for k in range(epi.shape[2]):
                if endo[i, j, k]:
                    continue
                if not epi[i, j, k]:
                    continue
                indices[ii] = i
                indices[ii + 1] = j
                indices[ii + 2] = k
                ii += 3

    cdef cnp.ndarray[unsigned int, ndim=1] neighbours = np.empty(n * 6, dtype=np.uint32)

    for c in range(0, n * 6, 6):
        i = indices[c // 2]
        j = indices[c // 2 + 1]
        k = indices[c // 2 + 2]

        if i + 1 == endo.shape[0]:
            neighbours[c] = OUTSIDE
        else:
            neighbours[c] = index_array[i + 1, j, k]

        if i == 0:
            neighbours[c + 1] = OUTSIDE
        else:
            neighbours[c + 1] = index_array[i - 1, j, k]

        if j + 1 == endo.shape[1]:
            neighbours[c + 2] = OUTSIDE
        else:
            neighbours[c + 2] = index_array[i, j + 1, k]

        if j == 0:
            neighbours[c + 3] = OUTSIDE
        else:
            neighbours[c + 3] = index_array[i, j - 1, k]

        if k + 1 == endo.shape[2]:
            neighbours[c + 4] = OUTSIDE
        else:
            neighbours[c + 4] = index_array[i, j, k + 1]

        if k == 0:
            neighbours[c + 5] = OUTSIDE
        else:
            neighbours[c + 5] = index_array[i, j, k - 1]

    return indices, neighbours


@cython.boundscheck(False)
@cython.wraparound(False)
def unflatten(
    double[:] flat_values,
    unsigned int[:] indices,
    cnp.ndarray[double, ndim=3] out,
) -> None:
    cdef unsigned int c, i, j, k
    for c in range(flat_values.shape[0]):
        i = indices[c * 3]
        j = indices[c * 3 + 1]
        k = indices[c * 3 + 2]
        out[i, j, k] = flat_values[c]
