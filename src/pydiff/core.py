def diff_dicts(left, right):
    """Return added, removed, and changed keys between two mappings."""
    if not isinstance(left, dict) or not isinstance(right, dict):
        raise TypeError("left and right must be dictionaries")

    added = {key: right[key] for key in right.keys() - left.keys()}
    removed = {key: left[key] for key in left.keys() - right.keys()}
    changed = {
        key: {"from": left[key], "to": right[key]}
        for key in left.keys() & right.keys()
        if left[key] != right[key]
    }
    return {"added": added, "removed": removed, "changed": changed}
