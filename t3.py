import json


class ZhuGeLiangImp:
    def __init__(self):
        data = json.load(open("o_res.json", 'r', encoding='utf-8'))
        self.name = "诸葛亮"
        self.name1 = "孔明"
        start_time = [0, 0]
        for i, d in enumerate(data):
            flag = False
            for j, d1 in enumerate(d):
                if "诸葛亮" in d1['text']:
                    start_time = [i, j]
                    flag = True
                    break
            if flag:
                break
        
        self.data = data
        self.start_time = start_time
        
    def calculate_score(self):
        res_score = []
        res_text = []
        for i, d in enumerate(self.data):
            if i < self.start_time[0]:
                for j, d1 in enumerate(d):
                    res_score.append([d1, i, j, 0])
                    res_text.append(d1)
            else:
                for j, d1 in enumerate(d):
                    res_text.append(d1)
                    if j < self.start_time[1]:
                        res_score.append([d1, i, j, 0])

                    else:
                        s = 0
                        if self.name in d1['人物'] or self.name1 in d1['人物']:
                            s += 10
                            
                        t = d1['text']
                        t1 = d1['事件大纲']

                        s += len(t.split(self.name))-1
                        s += len(t.split(self.name1)) - 1
                        s += len(t1.split(self.name)) - 1
                        s += len(t1.split(self.name1)) - 1
                        res_score.append([d1, i, j, s])

        res_score1 = sorted(res_score, key=lambda x: x[-1], reverse=True)
        
        print(res_score1[:3])
        print(1)


if __name__ == '__main__':
    zgl = ZhuGeLiangImp()
    zgl.calculate_score()
