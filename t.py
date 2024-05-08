
import json

file = "三国演义.txt"

with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

res = []
r = []
i = 0
while i < len(lines)-1:

    if lines[i] == '\n' and lines[i+1] == '\n':

        res.append(r)
        r = []
        i += 2
    else:
        r.append(lines[i])
        i += 1

if len(r) > 0:
    res.append(r)
    
res1 = []
res2 = []
text_len1 = []
for x in res:
    x1 = []
    for c in x:
        c = c.replace('\n', '')
        if len(c) == 0:
            continue
        x1.append(c)
    if len(x1) > 0:
        res1.append('\n'.join(x1))
        res2.append(x1)
        text_len1 += [len(c1) for c1 in x1]

text_len = []
for x in res1:
    text_len.append(len(x))

otf = "o_data.json"
f = open(otf, 'w', encoding='utf-8')
json.dump(res2, f, ensure_ascii=False)
f.close()

# 事件大纲

