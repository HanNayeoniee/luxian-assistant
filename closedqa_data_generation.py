import utils
import json
import datetime
import os
import re


class closedqaGeneration():
    def __init__(self, api_key):
        self.api_key = api_key
        self.hidden_instruct = 'closedqa_generation'
        self.prompt_form_path = './properties/prompt.json'
        
        self.prompt_form = {}
        with open(self.prompt_form_path, 'r', encoding='utf8') as fr:
            items = json.load(fr)
            
        self.prompt_form = items[self.hidden_instruct]

        
    def make_prompt(self, text):
        
        print(self.prompt_form)
        self.prompt_input = self.prompt_form.format(text=text)
        print(self.prompt_input)
        
        return self.prompt_input
    
    def requests_to_chat(self, prompt_input, text, iter=5):
        now_str = str(datetime.datetime.now())
        data_sets = []
        condition=True
        while(condition):
            result, _ = utils.run_openai(prompt_input, self.api_key)
            print(result)
            items_tokens = result.split('\n')
            
            for token in items_tokens:
                token_tokens = re.split('1: |2: |3: |4: |5: |6: |7: |8: |9: |10: |1. |2. |3. |4. |5. |6. |7. |8. |9. |10. ', token)
                if len(token_tokens) > 1:
                    token = token_tokens[1]
                try:
                    token = token.strip('\n').strip()
                    if len(data_sets) != iter:
                        #token = token.replace("'","\"")
                        print('입력: ', token)
                        element = json.loads(token.strip())
                        data_sets.append(element)
                    elif len(data_sets) == iter:
                        condition=False
                        break
                except:
                    pass
    
        print(data_sets)       
        with open(os.path.join('./closedqa_db/','closedqa_generation_'+now_str+'.jsonl'), 'w', encoding='utf8') as fw:
            for data in data_sets:
                data['문서'] = text
                fw.write(json.dumps(data, ensure_ascii=False)+'\n')
                
        return {'save_path': os.path.join('./closedqa_db/','closedqa_generation_'+now_str+'.jsonl')}
        
    def run(self, text, iter=10):
        prompt_input = self.make_prompt(text)
        return self.requests_to_chat(prompt_input, text, iter)


if __name__ == "__main__":
    api_key = "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"
    opg = closedqaGeneration(api_key)

    text = """엘링 홀란(23, 맨체스터 시티)을 의심했던 이들을 향해 펩 과르디올라 감독이 뼈있는 말을 던졌다.
홀란은 4일(한국시간) 웨스트햄과 2022-2023 잉글리시 프리미어리그(EPL) 28라운드 홈경기에 선발 출장, 후반 25분 2-0으로 달아나는 골을 터뜨렸다.
홀란의 이 골은 EPL의 새로운 이정표였다.
'전설' 앨런 시어러와 앤디 콜이 보유했던 34골을 넘어 EPL 단일 시즌 최다 득점자가 된 것이다.
시어러와 콜이 세운 34골은 당시 42경기 체제였다.
그런 반면 홀란은 현재 38경기 체제인 리그에서 단 31경기 만에 이 고지를 넘어선 것이었다.
홀란은 경기 후 팀 동료들로부터 '가드 오브 아너'를 받았다.
원래 '가드 오브 아너'는 축구계에서 우승팀을 향한 축하 행위다.
선수들이 양쪽에 도열, 박수로 축하해주는 것이다.
홀란은 맨시티 선수들의 축하 속에 이 영광을 누렸다. 
"""
    opg.run(text)