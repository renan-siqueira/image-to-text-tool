'''
    Execution project file
'''
import os
import json
from src.modules import blip_model
from src.settings import config


def process_images(model, processor, device, input_folder):
    descriptions = {}
    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)
        if os.path.isfile(image_path):
            description = blip_model.describe_image(model, processor, device, image_path)
            descriptions[image_name] = description
    return descriptions


def main():
    input_folder = config.APP_PATH_INPUT_FOLDER
    blip_output_file = config.APP_PATH_OUTPUT_JSON_FILE

    model, processor, device = blip_model.load_model()
    image_descriptions = process_images(model, processor, device, input_folder)

    with open(blip_output_file, "w", encoding='utf-8') as file:
        json.dump(image_descriptions, file, indent=4)


if __name__ == "__main__":
    main()
