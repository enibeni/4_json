import json
import sys


def load_data(json_filepath):
    print(json_filepath + "!!!")
    json_data = ""
    with open(json_filepath, "r", encoding="utf-8") as file:
        for line in file:
            json_data += line
    return json_data


def pretty_print_json(json_data):
    print(json.dumps(json.loads(json_data, encoding="utf-8"), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
