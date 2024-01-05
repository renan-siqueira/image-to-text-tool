'''
    Execution project file
'''
import os
import json
import datetime

from src.modules import blip_model
from src.settings import config


def process_images(model, processor, device, input_folder):
    descriptions = {}
    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)
        if os.path.isfile(image_path):
            description = blip_model.describe_image(model, processor, device, image_path, max_tokens=100)
            descriptions[image_name] = description
    return descriptions


def read_json_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding='utf-8') as file:
            return json.load(file)
    return []


def write_json_file(filepath, new_data):
    data = read_json_file(filepath)
    data.append(new_data)
    with open(filepath, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def main():
    model, processor, device = blip_model.load_model()
    image_descriptions = process_images(model, processor, device, config.APP_PATH_INPUT_FOLDER)
    
    new_execution = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "descriptions": image_descriptions
    }

    write_json_file(config.APP_PATH_OUTPUT_JSON_FILE, new_execution)


if __name__ == "__main__":
    main()