'''
    Execution project file
'''
import os
from src.settings import config
from src.modules import blip_model
from src.utils import utils


def process_images(model, processor, device, input_folder):
    descriptions = {}
    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)
        if os.path.isfile(image_path):
            description = blip_model.describe_image(model, processor, device, image_path, max_tokens=100)
            descriptions[image_name] = description
    return descriptions


def main():
    model, processor, device = blip_model.load_model()
    image_descriptions = process_images(model, processor, device, config.APP_PATH_INPUT_FOLDER)
    utils.write_json_file(config.APP_PATH_OUTPUT_JSON_FILE, image_descriptions)


if __name__ == "__main__":
    main()
