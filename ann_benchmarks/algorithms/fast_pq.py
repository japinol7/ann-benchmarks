import fast_pq

from .base import BaseANN


class FastPQ(BaseANN):
    def __init__(self, metric, build_probes):
        self._build_probes = build_probes
        self._query_probes = None
        self._metric = metric

    def fit(self, X):
        n = X.shape[0]
        self._ivf = fast_pq.IVF(self._metric, cl=int(n**.5 + 1), pq=fast_pq.FastPQ(dims_per_block=2))
        self._ivf.fit(X).build(X, n_probes=self._build_probes)

    def set_query_arguments(self, query_probes):
        self._query_probes = query_probes

    def query(self, v, n):
        return self._ivf.query(v, k=n, n_probes=self._query_probes)

    def __str__(self):
        return f"FastPQ(build_probes={self._build_probes}, query_probes={self._query_probes})"
