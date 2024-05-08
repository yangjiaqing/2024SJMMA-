
import json
import os
import re


file = "o_data.json"
o_data = json.load(open(file, 'r'))


res = []
for i in range(120):
    a = f"./o_data/{i}/"
    r = []
    for c in os.listdir(a):
        if c.endswith('json'):
            c1 = os.path.join(a, c)
            r.append([c1, int(c[:-5])])
    r1 = sorted(r, key=lambda x: x[1])
    res.append(r1)

# i = 0
# for  a, b in zip(o_data, res):
#     if len(a) != len(b):
#         i += 1
#         print(i-1)


def get_content_between_a_b(a, b, text):
    return re.search(f"{a}(.*?)\n{b}", text, re.DOTALL).group(1).strip().replace('\n', "")


def read(file):
    
    data = json.load(open(file, 'r', encoding='utf-8'))
    
    res = {
        "时间": None,
        "地点": None,
        "人物": None,
        "事件大纲": None,
        "是否涉及诸葛亮": None,
        "诸葛亮在该事件中的位置": None,
        "所起作用": None
    }
    r = data['words']
    try:
        res["时间"] = get_content_between_a_b("时间", "地点", r)
        res["地点"] = get_content_between_a_b("地点", "人物", r)
        res["人物"] = get_content_between_a_b("人物", "事件大纲", r)
        res["事件大纲"] = get_content_between_a_b("事件大纲", "是否涉及诸葛亮", r)
        res["是否涉及诸葛亮"] = get_content_between_a_b("是否涉及诸葛亮", "诸葛亮在该事件中的位置", r)
        res["诸葛亮在该事件中的位置"] = get_content_between_a_b("诸葛亮在该事件中的位置", "所起作用", r)
        if "所起作用" in r:
            r1 = r[r.index("所起作用")+len("所起作用")+1:].replace('\n', "")
            res["所起作用"] = r1
    
    except:
        res['text'] = data['text']
        res['words'] = data['words']
        return res

    # r = data['words'].split("\n\n")
    # for a in r:
    #     if a.startswith("输出事件："):
    #         a = a[len("输出事件："):]
    #     if a.startswith("\n"):
    #         a = a[1:]
    #         
    #     a = a.split('\n')
    # 
    #     if len(a) == 2:
    #         for k, v in res.items():
    #             if a[0].startswith(k):
    #                 res[k] = a[1]
    #     elif len(a) == 3:
    #         for k, v in res.items():
    #             if a[1].startswith(k):
    #                 res[k] = a[2]
    #                 
    #     elif len(a) == 1:
    #         a = a[0]
    #         for k, v in res.items():
    #             if a.startswith(k):
    #                 res[k] = a[len(k)+1:]
    #     else:
    #         print(1)
    
    res['text'] = data['text']
    res['words'] = data['words']
    
    return res
    

result = []
for r in res:
    a = []
    for r1 in r:
        a.append(read(r1[0]))
        
    result.append(a)
    
otf = "o_res.json"
f = open(otf, 'w', encoding='utf-8')
json.dump(result, f, ensure_ascii=False)
f.close()
    
print(1)
