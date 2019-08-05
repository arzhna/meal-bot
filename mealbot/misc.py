import json
import random


def pretty_dump(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


def pick_number(max):
    return random.randint(0, max - 1)
