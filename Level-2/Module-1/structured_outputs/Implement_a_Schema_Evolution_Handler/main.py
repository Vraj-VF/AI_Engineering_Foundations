def to_v2(product):
    result = dict(product)
    result["version"] = 2
    result.setdefault("confidence", 0.0)
    return result


def to_v3(product):
    result = to_v2(product)
    result["version"] = 3
    result.setdefault("risks", [])
    return result


def main():
    old = {"version": 1, "product": "router", "summary": "reliable"}
    migrated = to_v3(old)
    assert migrated["confidence"] == 0.0
    assert migrated["risks"] == []
    print("V1:", old)
    print("V2:", to_v2(old))
    print("V3:", migrated)
    print("backward_compatibility: passed")


if __name__ == "__main__":
    main()
