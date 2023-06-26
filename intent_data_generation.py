import utils
import json
import datetime
import os
import re

class intentGeneration():
    def __init__(self, api_key):
        self.api_key = api_key
        self.hidden_instruct = 'intent_generation'
        self.prompt_form_path = './properties/prompt.json'
        
        self.prompt_form = {}
        with open(self.prompt_form_path, 'r', encoding='utf8') as fr:
            items = json.load(fr)
            
        self.prompt_form = items[self.hidden_instruct]

        
    def make_prompt(self, topic,intent,sample1,sample2,sample3):
        
        #print(self.prompt_form)
        self.prompt_input = self.prompt_form.format(topic=topic, intent=intent, sample1=sample1, sample2=sample2, sample3=sample3)
        #print(self.prompt_input)
        
        return self.prompt_input
    
    def requests_to_chat(self, prompt_input, iter=10):
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
        with open(os.path.join('./intent_db/','intent_generation_'+now_str+'.jsonl'), 'w', encoding='utf8') as fw:
            for data in data_sets:
                fw.write(json.dumps(data, ensure_ascii=False)+'\n')
                
        return {'save_path': os.path.join('./intent_db/','intent_generation_'+now_str+'.jsonl')}
        
    def run(self, topic,intent,sample1,sample2,sample3,iter=10):
        prompt_input = self.make_prompt(topic,intent,sample1,sample2,sample3,)
        return self.requests_to_chat(prompt_input, iter)

#api_key = "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"


#ig = intentGeneration(api_key)

#topic = "자동차"
#intent = '보험'
#sample1 = "자동차 보험은 언제 갱신해야되나요?"
#sample2 =  "자동차 보험을 변경하고 싶습니다."
#sample3 = "자동차 보험 보장 범위가 어떻게 되나요?"




#ig.run(topic,intent,sample1,sample2,sample3)