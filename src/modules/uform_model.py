from uform.gen_model import VLMForCausalLM, VLMProcessor
from PIL import Image
import torch


def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = VLMForCausalLM.from_pretrained("unum-cloud/uform-gen").to(device)
    processor = VLMProcessor.from_pretrained("unum-cloud/uform-gen")
    return model, processor, device


def describe_image(model, processor, device, image_path, max_tokens=128):
    with Image.open(image_path) as img:
        image = img.convert('RGB')
        prompt = "[cap] Summarize the visual content of the image."
        inputs = processor(texts=[prompt], images=[image], return_tensors="pt").to(device)
        with torch.inference_mode():
            output = model.generate(
                **inputs,
                do_sample=False,
                use_cache=True,
                max_new_tokens=max_tokens,
                eos_token_id=32001,
                pad_token_id=processor.tokenizer.pad_token_id
            )
        prompt_len = inputs["input_ids"].shape[1]
        return processor.batch_decode(output[:, prompt_len:])[0]
