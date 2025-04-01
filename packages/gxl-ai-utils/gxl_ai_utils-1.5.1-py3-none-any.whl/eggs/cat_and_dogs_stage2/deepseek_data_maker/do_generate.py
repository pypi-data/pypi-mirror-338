# Please install OpenAI SDK first: `pip3 install openai`
import json
import random

import tqdm

from gxl_ai_utils.utils import utils_file

from openai import OpenAI

client = OpenAI(api_key="sk-d03313dd7c3a44a281187749c4203dda", base_url="https://api.deepseek.com")
print("Deepseek API client created successfully.")

prompt_person2person = '我希望构造$询问输入语音的说话人的情感信息$的句子，具体情况是一个人为另一个人播放了一段音频，并询问音频中说话人的情感。我将为你提供一些具体的限制，你来为我生成多样的句子。句式:{}。 情感一词的表述:"{}", 代词为"{}"（音频中的说话人的代词），音频的同义词为：" "{}",说话人的同义词："{}".请结合上述内容造对音频中说话人的情感的询问的句子。直接返回构造的句子，以json list的形式返回'
prompt_person2robot = '我希望构造$对机器人询问输入语音的说话人的情感信息$的句子，具体情况是一个人给LLM输入了一段音频，并询问音频中说话人的情感。我将为你提供一些具体的限制，你来为我生成多样的句子。句式:{}。 情感一词的表述:"{}",代词为"{}"（音频中的说话人的代词），音频的同义词为："{}",说话人的同义词："{}"， 输入的同义词为："{}".结合上述内容造对音频中说话人的情感的询问的句子。直接返回构造的句子，以json list的形式返回'

with open("meta_data/sentence.json", "r", encoding="utf-8") as file:
    sentence_list = json.loads(file.read())
    print(f'len: {len(sentence_list)}, {sentence_list}')
with open("meta_data/emotion_list.json", "r", encoding="utf-8") as file:
    emotion_list = json.loads(file.read())
    print(f'len: {len(emotion_list)}, {emotion_list}')
with open("meta_data/person.json", "r", encoding="utf-8") as file:
    person_list = json.loads(file.read())
    print(f'len: {len(person_list)}, {person_list}')
with open("meta_data/wav.json", "r", encoding="utf-8") as file:
    wav_list = json.loads(file.read())
    print(f'len: {len(wav_list)}, {wav_list}')
with open("meta_data/talker.json", "r", encoding="utf-8") as file:
    talk_list = json.loads(file.read())
    print(f'len: {len(talk_list)}, {talk_list}')
with open("meta_data/input_word.json", "r", encoding="utf-8") as file:
    input_word_list = json.loads(file.read())
    print(f'len: {len(input_word_list)}, {input_word_list}')

prompt_num = 0
for sentence_i in sentence_list:
    for emotion_i in emotion_list:
        for person_i in person_list:
            for i in range(6):
                wav_i = random.choice(wav_list)
                talk_i = random.choice(talk_list)
                prompt_num += 1
                prompt = prompt_person2person.format(sentence_i, emotion_i, person_i, wav_i, talk_i)
print(f"Total prompt num: {prompt_num}")
tqdm_obj = tqdm.tqdm(total=prompt_num)
for sentence_i in sentence_list:
    for emotion_i in emotion_list:
        for person_i in person_list:
            for i in range(6):
                wav_i = random.choice(wav_list)
                talk_i = random.choice(talk_list)
                prompt_num += 1
                tqdm_obj.update(1)
                prompt = prompt_person2person.format(sentence_i, emotion_i, person_i, wav_i, talk_i)
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    temperature=1.5,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant"},
                        {"role": "user", "content": f"{prompt}"},
                    ],
                    stream=False
                )
                res = response.choices[0].message.content
                start_index = res.find("[")
                end_index = res.find("]") + 1
                res = res[start_index:end_index]
                str_list = json.loads(res)
                res_file = './output_data/res_emotion_p2p.txt'
                utils_file.makedir_for_file(res_file)
                with open(res_file, 'a', encoding='utf8') as f:
                    for s in str_list:
                        f.write(s + '\n')
tqdm_obj2 = tqdm.tqdm(total=prompt_num)
for sentence_i in sentence_list:
    for emotion_i in emotion_list:
        for person_i in person_list:
            for i in range(6):
                wav_i = random.choice(wav_list)
                talk_i = random.choice(talk_list)
                input_word_i = random.choice(input_word_list)
                prompt_num += 1
                tqdm_obj2.update(1)
                prompt = prompt_person2robot.format(sentence_i, emotion_i, person_i, wav_i, talk_i, input_word_i)
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    temperature=1.3,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant"},
                        {"role": "user", "content": f"{prompt}"},
                    ],
                    stream=False
                )
                res = response.choices[0].message.content
                start_index = res.find("[")
                end_index = res.find("]") + 1
                res = res[start_index:end_index]
                str_list = json.loads(res)
                res_file = './output_data/res_emotion_p2r.txt'
                utils_file.makedir_for_file(res_file)
                with open(res_file, 'a', encoding='utf8') as f:
                    for s in str_list:
                        f.write(s + '\n')





# response = client.chat.completions.create(
#     model="deepseek-chat",
#     temperature=1.5,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": f"{prompt}"},
#     ],
#     stream=False
# )
# res = response.choices[0].message.content
# print(res)
# start_index = res.find("[")
# end_index = res.find("]")+1
# res = res[start_index:end_index]
# str_list = json.loads(res)
# print(str_list)
# res_file = 'res.txt'
# with open(res_file, 'a', encoding='utf8') as f:
#     for s in str_list:
#         f.write(s+'\n')