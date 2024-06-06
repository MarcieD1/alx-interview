#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set([0])
    new_keys = set([0])

    while new_keys:
        box_keys = set()
        for key in new_keys:
            box_keys.update(boxes[key])

        new_keys = box_keys - keys
        keys.update(new_keys)

    return len(keys) == len(boxes)
