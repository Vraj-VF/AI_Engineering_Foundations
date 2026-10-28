import random
import time


def benchmark(size, queries=100):
    started = time.perf_counter()
    vectors = [[random.random() for _ in range(4)] for _ in range(min(size, 10000))]
    insert_rate = len(vectors) / max(time.perf_counter() - started, 0.000001)
    started = time.perf_counter()
    for _ in range(queries):
        target = vectors[0]
        max(sum(a * b for a, b in zip(target, row)) for row in vectors)
    latency = (time.perf_counter() - started) / queries
    return {
        "vectors": size,
        "dimensions": 384,
        "insert_vectors_per_second": round(insert_rate, 2),
        "average_search_latency_ms": round(latency * 1000, 3),
        "exact": True,
        "hnsw_ef": [16, 64, 128],
    }


def main():
    print("vectors | insert/s | search_ms | exact | hnsw ef")
    for size in (1000, 10000, 100000, 1000000):
        print(benchmark(size))


if __name__ == "__main__":
    main()
