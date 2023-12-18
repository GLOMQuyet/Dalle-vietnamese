import os
import glob
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm

model_name = "vinai/vinai-translate-en2vi-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name, src_lang="en_XX")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

input_folder = "data/text_img"
output_folder = "data/yu"

def translate_en2vi(en_texts: str) -> str:
    input_ids = tokenizer(en_texts, padding=True, return_tensors="pt").to(device)
    output_ids = model.generate(
        **input_ids,
        decoder_start_token_id=tokenizer.lang_code_to_id["vi_VN"],
        num_return_sequences=1,
        num_beams=5,
        early_stopping=True
    )
    vi_texts = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    return vi_texts

processed_files = set(os.listdir(output_folder))
for input_file in tqdm(glob.glob(os.path.join(input_folder, "*.txt"))):
    if os.path.basename(input_file) in processed_files:
        continue
    with open(input_file, "r", encoding="utf-8") as f:
        inputs = f.readlines()

    translations = translate_en2vi(inputs)

    output_file = os.path.join(output_folder, os.path.basename(input_file))
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(translations))
    
    torch.cuda.empty_cache()