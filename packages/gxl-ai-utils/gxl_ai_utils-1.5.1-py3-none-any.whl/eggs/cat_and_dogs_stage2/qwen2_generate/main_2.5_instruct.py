import torch
from gxl_ai_utils.utils import utils_file
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2.5-7B-Instruct-1M"
model_name = "/mnt/sfs/asr/env/.cache/transformers/models--Qwen--Qwen2.5-7B-Instruct-1M/models--Qwen--Qwen2.5-7B-Instruct-1M/snapshots/e28526f7bb80e2a9c8af03b831a9af3812f18fba"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "中国的首都和美国的首都分别在哪里，他们的距离是多少"
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)

qwen_instruct_prompt_pattern_1 = "<|im_start|>system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant.<|im_end|>\n<|im_start|>user"
prompt_pattern1 = tokenizer([qwen_instruct_prompt_pattern_1], return_tensors="pt"
                                 )['input_ids'].to(model.device)
prompt_pattern1_embeds = model.model.embed_tokens(prompt_pattern1)
prompt_pattern1_lens = torch.tensor([len(i) for i in prompt_pattern1]).to(model.device)

qwen_instruct_prompt_pattern_2 = "<|im_end|>\n<|im_start|>assistant"
prompt_pattern2 = tokenizer([qwen_instruct_prompt_pattern_2] * 1, return_tensors="pt"
                                 )['input_ids'].to(model.device)
prompt_pattern2_embeds = model.model.embed_tokens(prompt_pattern2)
prompt_pattern2_lens = torch.tensor([len(i) for i in prompt_pattern2]).to(model.device)

prompt_ask = prompt
prompt_ask_label = tokenizer([prompt_ask] * 1, return_tensors="pt"
                                 )['input_ids'].to(model.device)
prompt_ask_embeds = model.model.embed_tokens(prompt_ask_label)
prompt_ask_lens = torch.tensor([len(i) for i in prompt_ask_label]).to(model.device)

embeds = torch.cat([prompt_pattern1_embeds, prompt_ask_embeds, prompt_pattern2_embeds], dim=1)

atts = torch.ones(embeds.size()[:-1], dtype=torch.long).to(embeds.device)

if model.model.embed_tokens.weight.dtype == torch.float16 or model.model.embed_tokens.weight.dtype == torch.bfloat16:
    utils_file.logging_limit_print('generate(): self.embed_tokens.weight.dtype == torch.float16')
    # embeds = embeds.to(torch.float16)
    embeds = embeds.to(torch.bfloat16)
    atts = atts.to(torch.bfloat16)
outputs = model.generate(
    inputs_embeds=embeds,
    attention_mask=atts,
    eos_token_id=151643,
    pad_token_id=-100,
    max_new_tokens=512
)
output_text = tokenizer.batch_decode(outputs, add_special_tokens=False, skip_special_tokens=True)
print(output_text)