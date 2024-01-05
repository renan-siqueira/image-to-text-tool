'''
    Generic and Aux functions
'''
import os
import json
import datetime


def read_json_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding='utf-8') as file:
            return json.load(file)
    return []


def write_json_file(filepath, image_descriptions):
    data = read_json_file(filepath)
    new_execution = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "descriptions": image_descriptions
    }
    data.append(new_execution)
    with open(filepath, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)
