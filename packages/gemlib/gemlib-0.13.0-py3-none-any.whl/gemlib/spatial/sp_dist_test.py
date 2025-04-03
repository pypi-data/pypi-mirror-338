"""Test sparse distance"""

from .sp_dist import sparse_pdist


def test_sparse_pdist(coords):
    N = coords.shape[-2]
    BATCH_SIZE = 32
    sparse_coords = sparse_pdist(coords, 0.1, BATCH_SIZE)

    EXPECTED_NNZ = 412

    assert sparse_coords.shape == [N, N]
    assert sparse_coords.values.shape[-1] == EXPECTED_NNZ
