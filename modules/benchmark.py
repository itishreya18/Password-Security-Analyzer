import time
from modules.hashing import generate_hash


def benchmark_hashes(password):
    """
    Benchmark different hashing algorithms.
    Returns a dictionary with algorithm names and execution times.
    """

    algorithms = ["md5", "sha1", "sha256", "sha512"]

    results = {}

    for algorithm in algorithms:

        start = time.perf_counter()

        generate_hash(password, algorithm)

        end = time.perf_counter()

        results[algorithm.upper()] = end - start

    return results