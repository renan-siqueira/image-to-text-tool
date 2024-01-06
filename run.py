# run.py

import argparse
import os
from src.settings import config
from src.modules import blip_model, uform_model
from src.utils import utils


def process_images(model, processor, device, input_folder, describe_function):
    descriptions = {}
    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)
        if os.path.isfile(image_path):
            description = describe_function(model, processor, device, image_path)
            descriptions[image_name] = description
    return descriptions


def main():
    parser = argparse.ArgumentParser(description="Process images using different models.")
    parser.add_argument(
        "models",
        nargs='*',
        default=config.APP_AVAILABLE_MODELS,
        help="List of models to use. Available: " + ", ".join(config.APP_AVAILABLE_MODELS)
    )

    args = parser.parse_args()

    if "blip" in args.models:
        blip_model_obj, blip_processor, blip_device = blip_model.load_model()
        blip_descriptions = process_images(blip_model_obj, blip_processor, blip_device, config.APP_PATH_INPUT_FOLDER, blip_model.describe_image)
        utils.write_json_file(config.APP_PATH_BLIP_OUTPUT_JSON_FILE, blip_descriptions)

    if "uform" in args.models:
        uform_model_obj, uform_processor, uform_device = uform_model.load_model()
        uform_descriptions = process_images(uform_model_obj, uform_processor, uform_device, config.APP_PATH_INPUT_FOLDER, uform_model.describe_image)
        utils.write_json_file(config.APP_PATH_UFORM_OUTPUT_JSON_FILE, uform_descriptions)


if __name__ == "__main__":
    main()
