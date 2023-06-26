import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from persona_data import create, delete, transfer
from closedqa_data_generation import closedqaGeneration
from classification_data_generation import class_prompt, save_data
from keyword_data_generation import keywordGeneration
from intent_data_generation import intentGeneration
from openqaprompt_data_generation import openqaPromoptGeneration
from closedqa_data_generation import closedqaGeneration

server_description = "Make your own character"

tags_metadata = [
    {
        "name": "0. Inference",
        "descrption": "Make your own character",
    }
]

app = FastAPI(
    title = "Persona Chat API SERVER",
    description = server_description,
    version = "0.0.1",
    openapi_tags = tags_metadata
)

    
class CreatePersona(BaseModel):
    employee_id: str
    name: str
    age: Optional[str] = "20"
    sex: Optional[str] = "여성"
    occupation: Optional[str] = "가수"
    personality: Optional[str] = "덤벙거리지만 쾌활함"
    likes: Optional[str] = "스타벅스 커피"
    
    
class DeletePersona(BaseModel):
    employee_id: str
    name: str
    
    
class Utterance(BaseModel):
    employee_id: str
    persona_name: str
    utterance: str
    api_key: str = "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"
    
    
class closedqaItems(BaseModel):
    content: str = "엘링 홀란(23, 맨체스터 시티)을 의심했던 이들을 향해 펩 과르디올라 감독이 뼈있는 말을 던졌다. 홀란은 4일(한국시간) 웨스트햄과 2022-2023 잉글리시 프리미어리그(EPL) 28라운드 홈경기에 선발 출장, 후반 25분 2-0으로 달아나는 골을 터뜨렸다. 홀란의 이 골은 EPL의 새로운 이정표였다. '전설' 앨런 시어러와 앤디 콜이 보유했던 34골을 넘어 EPL 단일 시즌 최다 득점자가 된 것이다. 시어러와 콜이 세운 34골은 당시 42경기 체제였다. 그런 반면 홀란은 현재 38경기 체제인 리그에서 단 31경기 만에 이 고지를 넘어선 것이었다. 홀란은 경기 후 팀 동료들로부터 '가드 오브 아너'를 받았다. 원래 '가드 오브 아너'는 축구계에서 우승팀을 향한 축하 행위다. 선수들이 양쪽에 도열, 박수로 축하해주는 것이다. 홀란은 맨시티 선수들의 축하 속에 이 영광을 누렸다."
    iter: int = 5
    api_key: str = "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"
    

class ClassicationGeneration(BaseModel):
    theme: str
    class_list: str
    sent1: str
    class1: str
    sent2: str
    class2: str
    sent3: str
    class3: str
    iter: int
    api_key: str = "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"
    
    
class keywordGenerationItems(BaseModel):
    sent1: str = "오늘 점심으로 햄버거와 피자를 먹었습니다"
    keyword1: str = "[\"햄버거\",\"피자\"]"
    sent2: str = "저는 주말에 이마트를 다녀올 예정입니다."
    keyword2: str = "[\"이마트\"]"
    sent3: str = "안녕하세요."
    keyword3: str = "[]"
    iter: int = 10
    api_key: str = "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"
    

class intentGenerationItems(BaseModel):
    topic: str = "자동차"
    intent: str = "보험"
    sample1: str = "자동차 보험은 언제 갱신해야되나요?"
    sample2: str = "자동차 보험을 변경하고 싶습니다."
    sample3: str = "자동차 보험 보장 범위가 어떻게 되나요?"
    iter: int = 10
    api_key: str = "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"
 
    
class openpromptItems(BaseModel):
    content: str = "엘링 홀란(23, 맨체스터 시티)을 의심했던 이들을 향해 펩 과르디올라 감독이 뼈있는 말을 던졌다. 홀란은 4일(한국시간) 웨스트햄과 2022-2023 잉글리시 프리미어리그(EPL) 28라운드 홈경기에 선발 출장, 후반 25분 2-0으로 달아나는 골을 터뜨렸다. 홀란의 이 골은 EPL의 새로운 이정표였다. '전설' 앨런 시어러와 앤디 콜이 보유했던 34골을 넘어 EPL 단일 시즌 최다 득점자가 된 것이다. 시어러와 콜이 세운 34골은 당시 42경기 체제였다. 그런 반면 홀란은 현재 38경기 체제인 리그에서 단 31경기 만에 이 고지를 넘어선 것이었다. 홀란은 경기 후 팀 동료들로부터 '가드 오브 아너'를 받았다. 원래 '가드 오브 아너'는 축구계에서 우승팀을 향한 축하 행위다. 선수들이 양쪽에 도열, 박수로 축하해주는 것이다. 홀란은 맨시티 선수들의 축하 속에 이 영광을 누렸다."
    iter: int = 5
    api_key: str = "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"
    
     
@app.post("/api/v1/create_persona")
def create_persona(persona: CreatePersona):
    try:
        file_path = os.path.join("/workspace/persona_db", persona.employee_id + ".json")
        new_persona = create(persona.name, persona.age, persona.sex, persona.occupation, persona.personality, persona.likes, file_path)
        
        results = {
            "code": 1,
            "result": {
                "answer": new_persona
            },
            "message": "Persona Creation Successful!"
        }
        return results
    except:
        return {"code": 0, "result": None, "message": "Persona Creation Failed!"}


@app.post("/api/v1/delete_persona")
def delete_persona(persona: DeletePersona):
    try:
        file_path = os.path.join("/workspace/persona_db", persona.employee_id + ".json")
        deleted_persona = delete(persona.name, file_path)
        results = {
            "code": 1,
            "result": {
                "answer": deleted_persona
            },
            "message": "Persona Deletion Successful!"
        }
        return results
    except:
        return {"code": 0, "result": None, "message": "Persona Deletion Failed!"}


@app.post("/api/v1/style_inference")
def style_transfer(utt: Utterance):
    try:
        file_path = os.path.join("./persona_db", utt.employee_id + ".json")
        out_utt, inference_time = transfer(utt.persona_name, utt.utterance, utt.api_key, file_path)
        results = {
            "code" : 1,
            "result" : {
                "answer" : out_utt,
                "inference_time": inference_time
        },
        "message": "Style Transfered Successful!"
        }
        return results
    except:
        return {"code": 0, "result": None, "message": "Style Transfered Failed!"}

 
@app.post("/api/v1/closed_qa")
def make_closedqa_data(closedqa: closedqaItems):
    content = closedqa.content
    iters = closedqa.iter
    api = closedqa.api_key
    
    try:
        opg = closedqaGeneration(api)
        result  = opg.run(content, iters)
        results = {
                "code" : 1,
                "result" : {
                    "answer" : result['save_path']
            },
            "message": "Creating ClosedQA data Successful!"
        }
    
        return results
    except:
        return {"code": 0, "result": None, "message": "Creating ClosedQA data Failed!"}
 
    
@app.post("/api/v1/classification_generation")
def make_classification(item: ClassicationGeneration):
    try:
        prompt_ = class_prompt(theme=item.theme, class_list=item.class_list, sent1=item.sent1, class1=item.class1, sent2=item.sent2, class2=item.class2, sent3=item.sent3, class3=item.class3)
        save_path = save_data(prompt_, api_key=item.api_key, iter=item.iter)
        
        results = {
                "code" : 1,
                "result" : {
                    "answer" : save_path
            },
            "message": "Creating Classification data Successful!"
        }
    
        return results
    except:
        return {"code": 0, "result": None, "message": "Creating Classification data Failed!"}
        

@app.post("/api/v1/keyword_generation")
def make_keyword(keywords: keywordGenerationItems):
    
    s1=keywords.sent1
    k1=keywords.keyword1
    s2=keywords.sent2
    k2=keywords.keyword2
    s3=keywords.sent3
    k3=keywords.keyword3
    iters = keywords.iter
    api = keywords.api_key
    
    try:
        kg = keywordGeneration(api)
        result  = kg.run(s1,k1,s2,k2,s3,k3,iters)
        results = {
                "code" : 1,
                "result" : {
                    "answer" : result['save_path']
            },
            "message": "Creating KeywordExtraction data Successful!"
        }
    
        return results
    except:
        return {"code": 0, "result": None, "message": "Creating KeywordExtraction data Failed!"}
  
  

@app.post("/api/v1/intent_generation")
def make_intent(intents: intentGenerationItems):
    
    topic=intents.topic
    intent=intents.intent
    s1=intents.sample1
    s2=intents.sample2
    s3=intents.sample3
    iters = intents.iter
    api = intents.api_key
    
    try:
        ig = intentGeneration(api)
        result  = ig.run(topic,intent,s1,s2,s3,iters)
        results = {
                "code" : 1,
                "result" : {
                    "answer" : result['save_path']
            },
            "message": "Creating intent data Successful!"
        }
    
        return results
    except:
        return {"code": 0, "result": None, "message": "Creating intent data Failed!"}
  

@app.post("/api/v1/openprompt_generation")
def make_prompt(openprompt: openpromptItems):
    
    content = openprompt.content
    iters = openprompt.iter
    api = openprompt.api_key
    
    try:
        opg = openqaPromoptGeneration(api)
        result  = opg.run(content,iters)
        results = {
                "code" : 1,
                "result" : {
                    "answer" : result['save_path']
            },
            "message": "Creating prompt data Successful!"
        }
    
        return results
    except:
        return {"code": 0, "result": None, "message": "Creating prompt data Failed!"} 
  

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001)