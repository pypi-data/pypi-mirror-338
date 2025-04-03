"""Compute a sparse distance matrix given coordinates"""

import numpy as np
import tensorflow as tf
from tensorflow import sparse as ts
from tqdm import tqdm

__all__ = ["squared_distance", "sparse_pdist"]


def squared_distance(a, b):
    """Compute the squared Euclidean distance between a and b

    Args:
        a: a :code:`[N, D]` tensor of coordinates
        b: a :code:`[M, D]` tensor of coordinates

    Returns:
        A :code:`[N, M]` matrix of squared distances between
        coordinates.
    """
    ra = tf.reshape(tf.reduce_sum(a * a, 1), [-1, 1])
    rb = tf.reshape(tf.reduce_sum(b * b, 1), [1, -1])

    Dsq = ra - 2 * tf.matmul(a, b, transpose_b=True) + rb
    return Dsq


@tf.function(jit_compile=False, autograph=False)
def compress_distance(a, b, max_dist):
    """Return a sparse tensor containing all distances
    between :code:`a` and :code:`b` less than :code:`max_dist`.
    """
    d_slice = squared_distance(a, b)
    is_valid = tf.less(d_slice, max_dist * max_dist)
    return tf.where(is_valid), d_slice[is_valid]


def sparse_pdist(
    coords: np.array, max_dist: float = np.inf, batch_size: int = None
):
    """Compute a sparse distance matrix

    Compute a sparse Euclidean distance matrix between all pairs of
    :code:`coords` such that the distance is less than :code:`max_dist`.

    Args:
        coords: a :code:`[N, D]` array of coordinates
        max_dist: the maximum distance to return
        batch_size: If memory is limited, compute the distances in batches
                    of :code:`[batch_size, N]` stripes.

    Returns:
        A sparse tensor of Euclidean distances less than :code:`max_dist`.

    Example:

        >>> import numpy as np
        >>> from gemlib.spatial import sparse_pdist
        >>> coords = np.random.uniform(size=(1000, 2))
        >>> d_sparse = sparse_pdist(coords, max_dist=0.01, batch_size=200)
        >>> d_sparse
        SparseTensor(indices=tf.Tensor(
        [[  0   0]
         [  1   1]
         [  2   2]
         ...
         [997 997]
         [998 998]
         [999 999]], shape=(1316, 2), dtype=int64), values=tf.Tensor(
        [0.00000000e+00 2.22044605e-16 0.00000000e+00 ... 0.00000000e+00
         0.00000000e+00 0.00000000e+00], shape=(1316,), dtype=float64),
        dense_shape=tf.Tensor([1000 1000], shape=(2,), dtype=int64))

    """
    if batch_size is None:
        batch_size = coords.shape[0]

    batched_coords = tf.data.Dataset.from_tensor_slices(coords).batch(
        batch_size
    )

    dist_nz = []
    pbar = tqdm(total=coords.shape[-2])

    for batch in batched_coords.prefetch(tf.data.experimental.AUTOTUNE):
        indices, values = compress_distance(batch, coords, max_dist)
        with tf.device("CPU"):  # Force results into host mem
            dist_nz.append(
                tf.SparseTensor(
                    indices.numpy(),
                    values.numpy(),
                    [batch.shape[0], coords.shape[0]],
                )
            )
        pbar.update(batch_size)

    with tf.device("CPU"):  # Force concatenation in host mem
        res = ts.concat(-2, dist_nz)

    return res
