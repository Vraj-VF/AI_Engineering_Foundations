def benchmark(token_count):
    no_cache_total = 0
    cache_total = 0
    rows = []

    for step in range(1, token_count + 1):
        no_cache = step
        with_cache = 1
        no_cache_total += no_cache
        cache_total += with_cache
        rows.append((step, no_cache, with_cache, no_cache_total, cache_total))

    return rows


def main():
    rows = benchmark(100)
    print(" step  no-cache  cache  cumulative no-cache  cumulative cache")
    for row in rows:
        step, no_cache, cached, total_no_cache, total_cache = row
        if step in [1, 2, 3, 5, 10, 25, 50, 75, 100]:
            print(
                f"{step:5} {no_cache:9} {cached:6} "
                f"{total_no_cache:19} {total_cache:17}"
            )

    total_no_cache = rows[-1][3]
    total_cache = rows[-1][4]
    print(f"\nTotal K/V computations, no cache: {total_no_cache}")
    print(f"Total K/V computations, cache: {total_cache}")
    print(f"Speedup: {total_no_cache / total_cache:.1f}x")

    tokens = 4096
    d_model = 4096
    layers = 32
    bytes_per_value = 2
    memory_bytes = tokens * d_model * 2 * layers * bytes_per_value
    gib = memory_bytes / (1024**3)
    per_token_kib = memory_bytes / tokens / 1024
    print("\nKV cache estimate")
    print(f"Tokens: {tokens}, d_model: {d_model}, layers: {layers}")
    print(f"Float16 memory: {memory_bytes:,} bytes = {gib:.2f} GiB")
    print(f"Per-token memory: {per_token_kib:.0f} KiB")


if __name__ == "__main__":
    main()
