'''
@misc{https://doi.org/10.48550/arxiv.2201.12086,
  doi = {10.48550/ARXIV.2201.12086},
  url = {https://arxiv.org/abs/2201.12086},
  author = {Li, Junnan and Li, Dongxu and Xiong, Caiming and Hoi, Steven},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation},
  publisher = {arXiv},
  year = {2022},  
  copyright = {Creative Commons Attribution 4.0 International}
}
'''

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to(device)
    return model, processor, device


def describe_image(model, processor, device, image_path):
    with Image.open(image_path) as img:
        image = img.convert('RGB')
        inputs = processor(image, return_tensors="pt").to(device)
        outputs = model.generate(**inputs)
        return processor.decode(outputs[0], skip_special_tokens=True)
