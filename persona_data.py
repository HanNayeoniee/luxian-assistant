import os
import sys
import json
import time
import openai
from utils import run_openai


def make_prompt_ver1(name:str, age:str, sex:str, occupation:str, personality:str, likes:str) -> str:
    # base = "아래의 지시사항에 맞게 주어진 문장을 변환해주세요"
    # prompt = f"{age}살 {occupation} 직업을 가진 {sex}이며, {personality} 특징이 있고 {likes}를 좋아합니다."
    
    
    base = "다음 문장을 주어진 캐릭터의 특징을 반영한 스타일로 변환해주세요"
    prompt = f"<주어진 캐릭터>\n나이: {age}\n성별: {sex}\n직업: {occupation}\n성격: {personality}\n좋아하는 것: {likes}"
    
    return base + "\n\n" + prompt

def make_prompt(name:str, age:str, sex:str, occupation:str, personality:str, likes:str) -> str:
    base = "주어진 지시사항에 따라 문장의 말투를 포맷에 맞게 변환해주세요."
    prompt = f"지시사항:\n- 나이: {age}\n- 성별: {sex}\n- 직업: {occupation}\n- 성격: {personality}\n- 취미: {likes}"

    return base + "\n\n" + prompt



def create(name:str, age:str, sex:str, occupation:str, personality:str, likes:str, file_path="./persona_persona_db/sample2.json") -> dict:
    """
    name: 페르소나의 이름
    age: 페르소나의 연령대
    sex: 페르소나의 성별
    occupation: 페르소나의 직업
    personality: 페르소나의 성격/말투
    likes: 페르소나의 취미/좋아하는 것
    file_path: 페르소나 파일 저장 경로
    """
    name = name.strip()
    hidden_prompt = make_prompt(name, age, sex, occupation, personality, likes)
    new_persona = {name: hidden_prompt}
    
    # 기존에 저장된 페르소나가 있으면 불러오기
    if os.path.exists(file_path):
        with open(file_path) as fin:
            all_persona = json.load(fin)            
            all_persona.update(new_persona)
        with open(file_path, "w", encoding="UTF-8") as fout:
            fout.write(json.dumps(all_persona, ensure_ascii=False, indent="\t"))
            
    else:    
        with open(file_path, "w", encoding="UTF-8") as fout:
            fout.write(json.dumps(new_persona, ensure_ascii=False, indent="\t"))
        
    return new_persona


def delete(name:str, file_path="./persona_db/sample2.json") -> str:
    with open(file_path) as fin:
        all_persona = json.load(fin)
    del all_persona[name]
    with open(file_path, "w", encoding="UTF-8") as fout:
        fout.write(json.dumps(all_persona, ensure_ascii=False, indent="\t"))
        
    return name


def transfer(persona_name:str, utterance:str, api_key:str, file_path = './persona_db/sample2.json'):
    start_time = time.time()
    with open(file_path, 'r') as fw:
        persona_data = json.load(fw)
        for k, v in persona_data.items():
            if k == persona_name:
                prompt = v
                prompt_ = prompt + '\n\n문장: ' + utterance + '\n\n포맷: {"변환문장": ""}'
                response, _ = run_openai(prompt=prompt_, api_key=api_key)
                try:
                    response = json.loads(response)["변환문장"]
                except:
                    response = "생성 안됨"
                
    inference_time = time.time() - start_time
    
    return response, inference_time


    
def persona_sample():
    name = "샘플"
    age = "20"
    sex = "여성"
    occupation = "리셉셔니스트"
    personality = "차분하고 조용"
    likes = "패션"
    
    new_persona = create(name, age, sex, occupation, personality, likes, file_path = './persona_db/0504_sample.json')
    print("New persona:", new_persona)
    
    # deleted = delete(name="샘플3", file_path = './persona_db/0504_sample.json')
    # print("Deleted persona:", deleted)
    
    
    
def transfer_sample():
    api_key_ = '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'
    response, inference_time = transfer(persona_name='샘플', utterance='점심을 먹으셨나요?', api_key=api_key_, file_path = './persona_db/0504_sample.json')
    print(type(response))
    print(response)
    
    
    
if __name__ == "__main__":
    # deleted = delete(name="샘플3", file_path="jjj.json")
    # print("Deleted persona:", deleted)
    
    
    # persona_sample()
    
    transfer_sample()