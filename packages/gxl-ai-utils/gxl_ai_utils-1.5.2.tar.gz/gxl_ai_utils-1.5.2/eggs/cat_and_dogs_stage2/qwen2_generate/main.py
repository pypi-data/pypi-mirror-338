from gxl_ai_utils.utils import utils_file


from transformers import AutoModelForCausalLM, AutoTokenizer


model_name = "/home/node54_tmpdata/xlgeng/ckpt/qwen-7B-instruct/qwen2_7b"
# gpu_id = 3
#
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
# from transformers import pipeline
#
# pipe = pipeline("text-generation", model=model_name)
# model = model.to(f"cuda:{gpu_id}")
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "中国和日本国之间的战争史有哪些？ "
def get_generate(prompt):
    messages = [
        # {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    print(text)
    # text = promp
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    print(model_inputs)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response
#
# a = get_generate(prompt)
# print(a)

def get_generate2(prompt):
    text = prompt
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    print(model_inputs)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response

a = get_generate2(prompt)
print(a)


# def get_generate3(prompt):
#
#     messages = [
#         {"role": "user", "content": "Who are you?"},
#     ]
#     res = pipe(messages)
#     return res
#
# a = get_generate3(prompt)
# print(a)

if __name__ == '__main__':
    while True:
        # 获取用户输入
        input_str = input("请输入想要告诉LLM的话（输入 'exit' 可退出程序）: ")
        # 若用户输入 'exit'，则退出循环
        if input_str == 'exit':
            break
        reversed_str = get_generate2(input_str)
        print("LLM: ",reversed_str)