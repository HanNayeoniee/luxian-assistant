import utils
import json
import datetime
import os
import re

class keywordGeneration():
    def __init__(self, api_key):
        self.api_key = api_key
        self.hidden_instruct = 'keyword_generation'
        self.prompt_form_path = './properties/prompt.json'
        
        self.prompt_form = {}
        with open(self.prompt_form_path, 'r', encoding='utf8') as fr:
            items = json.load(fr)
            
        self.prompt_form = items[self.hidden_instruct]

        
    def make_prompt(self, sent1, keyword1, sent2, keyword2, sent3, keyword3):
        
        #print(self.prompt_form)
        self.prompt_input = self.prompt_form.format(sent1=sent1, keywords1=keyword1, sent2=sent2, keywords2=keyword2, sent3=sent3, keywords3=keyword3)
        #print(self.prompt_input)
        
        return self.prompt_input
    
    def requests_to_chat(self, prompt_input, iter):
        now_str = str(datetime.datetime.now())
        data_sets = []
        condition=True
        while(condition):
            result, _ = utils.run_openai(prompt_input, self.api_key)
            items_tokens = result.split('\n')
            
            for token in items_tokens:
                token_tokens = re.split('1: |2: |3: |4: |5: |6: |7: |8: |9: |10: |1. |2. |3. |4. |5. |6. |7. |8. |9. |10. ', token)
                if len(token_tokens) > 1:
                    token = token_tokens[1]
                try:
                    print(token)
                    if len(data_sets) != iter:
                        token = token.replace("'","\"")
                        element = json.loads(str(token.strip()))
                        data_sets.append(element)
                    elif len(data_sets) == iter:
                        condition=False
                        break
                except:
                    pass
    
        print(data_sets)       
        with open(os.path.join('./keyword_db/','keyword_generation_'+now_str+'.jsonl'), 'w', encoding='utf8') as fw:
            for data in data_sets:
                fw.write(json.dumps(data, ensure_ascii=False)+'\n')
        
        return {'save_path': os.path.join('./keyword_db/','keyword_generation_'+now_str+'.jsonl')}
        
    def run(self, sent1, keyword1, sent2, keyword2, sent3, keyword3, iter=10):
        prompt_input = self.make_prompt(sent1, keyword1, sent2, keyword2, sent3, keyword3)
        return self.requests_to_chat(prompt_input,iter)

#api_key = "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"


#kg = keywordGeneration(api_key)

#s1 = "오늘 점심으로 햄버거와 피자를 먹었습니다"
#k1 = ["햄버거","피자"]
#s2 = "저는 주말에 이마트를 다녀올 예정입니다."
#k2 =  ["이마트"]
#s3 = "안녕하세요."
#k3 =  []



#kg.run(s1,k1,s2,k2,s3,k3)