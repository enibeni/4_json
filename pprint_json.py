import json
import sys


def load_data(filepath):
    print(filepath + "!!!")
    data = ""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            data += line
    return data


def pretty_print_json(data):
    print(json.dumps(json.loads(data, encoding="utf-8"), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))