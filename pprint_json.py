import json
import sys
import os


def load_data(json_filepath):
    if not os.path.exists(json_filepath):
        return None
    with open(json_filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def pretty_print_json(json_data):
    print(json.dumps(
        json_data,
        indent=4,
        ensure_ascii=False)
    )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        json_data = load_data(sys.argv[1])
        pretty_print_json(json_data)
