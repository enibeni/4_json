import json
import sys


def load_data(json_filepath):
    with open(json_filepath, "r", encoding="utf-8") as file:
        print(type(file))
        json_data = file.read()
    return json_data


def pretty_print_json(json_data):
    print(json.dumps(json.loads(json_data),
                     indent=4, ensure_ascii=False))


if __name__ == "__main__":
    pretty_print_json(load_data(sys.argv[1]))
