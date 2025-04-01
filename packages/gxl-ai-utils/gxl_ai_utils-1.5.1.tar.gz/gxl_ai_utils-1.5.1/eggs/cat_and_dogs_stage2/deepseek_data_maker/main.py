# Please install OpenAI SDK first: `pip3 install openai`
import json

from openai import OpenAI

client = OpenAI(api_key="sk-d03313dd7c3a44a281187749c4203dda", base_url="https://api.deepseek.com")
print("Deepseek API client created successfully.")
# prompt = '我希望构造$询问输入语音的说话人的情感信息$的句子，具体情况是一个人为另一个人播放了一段音频，并询问音频中说话人的情感。我将为你提供一些具体的限制，你来为我生成多样的句子。句式:祈使句。 情感一词的表述： "情愫",具体场景为:$"写字楼茶水间"$, 代词为"她"（音频中的说话人的代词），询问两者的关系为: $"邻居关系"$，音频的同义词为：" "录音",说话人的同义词："谈话者". 请结合对话发生的场景和双方关系开始构造对音频中说话人的情感的询问的句子。直接返回构造的句子，以json list的形式返回'
# prompt = '我希望构造$询问输入语音的说话人的情感信息$的句子，具体情况是一个人为另一个人播放了一段音频，并询问音频中说话人的情感。我将为你提供一些具体的限制，你来为我生成多样的句子。句式:祈使句 。 情感一词的表述： "情愫",具体场景为:"写字楼茶水间", 代词为：不使用（音频中的说话人的代词），询问两者的关系为: "邻居关系"，音频的同义词为：" "录音",说话人的同义词："谈话者"。 我希望你先根据关系和场景构造核实的上文背景并直接输出，然后再构造符合改场景的句子，并以json list的形式只返回构造的句子（不包括上文）。'
prompt = '我希望构造$询问输入语音的说话人的情感信息$的句子，具体情况是一个人为另一个人播放了一段音频，并询问音频中说话人的情感。我将为你提供一些具体的限制，你来为我生成多样的句子。句式:询问句 。 情感一词的表述： "情愫", 代词为"她"（音频中的说话人的代词），音频的同义词为：" "录音",说话人的同义词："谈话者".请结合上述内容造对音频中说话人的情感的询问的句子。直接返回构造的句子，以json list的形式返回'
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
print(res)
start_index = res.find("[")
end_index = res.find("]")+1
res = res[start_index:end_index]
str_list = json.loads(res)
print(str_list)
res_file = 'res.txt'
with open(res_file, 'a', encoding='utf8') as f:
    for s in str_list:
        f.write(s+'\n')