
import requests
import openai

import os
import re
import json
import copy


def get_post_openai(message):
    openai.api_key = ""

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    print(completion.choices[0].message)
    return completion.choices[0].message


def get_words(text):
    prompt = """
你是一个小说家，熟读三国演义，知道三国演义里面任何一个故事情节，任何一个人物，任何一个事件，尤其是对诸葛亮（孔明）非常熟悉。下面给你一段文本，你需要从文本中进行事件抽取，抽取出事件发生的时间、地点、人物，给出事件大纲；并且判断出该事件是否涉及到诸葛亮，如果涉及请说明，诸葛亮在该事件的位置和所起的作用。如果不涉及事件，请回答“无”。一定要按照格式回答，用中文简要作答。

输入文本：
{}

以下是需要的输出:
输出事件：
时间：
<>

地点:
<>

人物:
<>

事件大纲:
<>

是否涉及诸葛亮:
<是|否>

诸葛亮在该事件中的位置:
<>

所起作用:
<>


注意：
一定要按照格式回答，用中文回答。

    """
    query = prompt.format(text)
    res = get_post_openai(query)
    return res


file = "o_data.json"
data = json.load(open(file, 'r'))


def get(data, i):
    o_path = f'./o_data/{i}'
    if not os.path.exists(o_path):
        os.makedirs(o_path, exist_ok=True)

    for j, t in enumerate(data):
        try:
            r = get_words(t)
            t1 = {"text": t, "words": r}
            o_file = os.path.join(o_path, f"{j}.json")
            f = open(o_file, 'w', encoding="utf-8")
            json.dump(t1, f, ensure_ascii=False)
            f.close()
        except:
            print(f"error  ... {i} {j}.json ...")


if __name__ == '__main__':
    for i, d in enumerate(data):
        get(d, i)

    # nohup python3 -u t1.py > log_train_0312_4.log 2>&1 &
            