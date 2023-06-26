import utils
import json
import jsonlines
import sys
import os
import re
from datetime import datetime

def class_prompt(theme=str, class_list=str, sent1=str, class1=str, sent2=str, class2=str, sent3=str, class3=str):
    prompt_path = './properties/prompt.json'
    hidden_instruct = 'classification_generation'
    with open(prompt_path, 'r', encoding='utf8') as fr:
        items = json.load(fr)
                
    prompt_form = items[hidden_instruct]
    prompt_input = prompt_form.format(theme=theme, class_list=class_list, sent1=sent1, class1=class1, sent2=sent2, class2=class2, sent3=sent3, class3=class3)
    
    return prompt_input

def make_data(prompt_input, api_key=str):
    response, _ = utils.run_openai(prompt_input, api_key)
    
    return response

def save_data(prompt_input, api_key, iter=10):
    save_list = []
    now_date = str(datetime.now())
    status = True

    while(status):
        result = make_data(prompt_input, api_key)
        items = result.split('\n')

        for item in items:
            item_ = re.split('1: |2: |3: |4: |5: |6: |7: |8: |9: |10: |1. |2. |3. |4. |5. |6. |7. |8. |9. |10. ', item)
            try:
                if len(item_) > 1:
                    item = item_[1]
                # print(item)
                if len(save_list) != iter:
                    item = item.replace("'","\"")
                    items_ = json.loads(str(item.strip()))
                    save_list.append(items_)
                elif len(save_list) == iter:
                    status = False
                    break
            except:
                pass
    
    save_path = os.path.join('./class_db/','classification_generation_'+now_date+'.jsonl')
    with open(save_path, 'w', encoding='utf8') as fw:
        for data in save_list:
            fw.write(json.dumps(data, ensure_ascii=False)+'\n')

    return save_path

if __name__ == "__main__":
    api_key = "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"
    theme = "뉴스제목 분류"
    class_list = ["경제", "스포츠", "사회"]
    sent1 = "손흥민, 3경기 득점포 가동, 토트넘 순위 훌쩍"
    class1 = "스포츠"
    sent2 = "코스닥지수 사상 최대로 떨어져.. 충격"
    class2 = "경제"
    sent3 = "아파트 분양사기, 극정.. 분양률 역대 최저"
    class3 = "사회"

    prompt_ = class_prompt(theme, str(class_list), sent1, class1, sent2, class2, sent3, class3)
    # result = make_data(class_prompt, api_key)
    save_path = save_data(prompt_, api_key, 10)
    print(save_path)
    # print(result)