import os
import sys
import json
import requests


def create_persona(employee_id, name, age, sex, occupation, personality, likes):
    datas = {
        "employee_id": employee_id,
        "name": name,
        "age": age,
        "sex": sex,
        "occupation": occupation,
        "personality": personality,
        "likes": likes        
    }

    url = "http://211.109.9.144:8001/api/v1/create_persona"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    try:
        result = json.loads(response.text)['result']
        return {'code': 1, 'result': result, 'message': "Persona Creation Successful!"}

    except Exception as e:
        print('Error:', e)
        return {'code': 0, 'result': None, 'message': "Persona Creation Failed!"}
    

def delete_persona(employee_id, name):
    datas = {
        "employee_id": employee_id,
        "name": name,    
    }
    
    url = "http://211.109.9.144:8001/api/v1/delete_persona"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    try:
        result = json.loads(response.text)['result']
        if result:
            return {'code': 1, 'result': result, 'message': "Persona Deletion Successful!"}
        else:
            return {'code': 0, 'result': None, 'message': "Persona Deletion Failed!"}
    except:
        pass
    # except Exception as e:
    #     print('Error:', e)
    #     return {'code': 0, 'result': None, 'message': "Persona Deletion Failed!"}


def style_transfer(employee_id, name, utterance, api_key="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"):
    datas = {
        "employee_id": employee_id,
        "persona_name": name,
        "utterance": utterance,
        "api_key": api_key
    }
    
    url = "http://211.109.9.144:8001/api/v1/style_inference"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    try:
        result = json.loads(response.text)['result']
        print(type(result))
        print(result)
        if result:
            return {'code': 1, 'result': result, 'message': "Style Transfered Successful!"}
        else:
            return {'code': 0, 'result': None, 'message': "Style Transfered Failed!"}
    except:
        pass
    
    # except Exception as e:
    #     print('Error:', e)
    #     return {'code': 0, 'result': None, 'message': "Style Transfered Failed!"}


def text_classification(theme, class_list, sent1, class1, sent2, class2, sent3, class3, iter, api_key="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"):
    datas = {
        "theme": theme,
        "class_list": class_list,
        "sent1": sent1,
        "class1": class1,
        "sent2": sent2,
        "class2": class2,
        "sent3": sent3,
        "class3": class3,
        "iter": iter,
        "api_key": api_key
    }
    
    url = "http://211.109.9.144:8001/api/v1/classification_generation"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    
    try:
        result = json.loads(response.text)['result']

        if result:
            return {'code': 1, 'result': result, 'message': "Creating Classification data Successful!"}
        else:
            return {'code': 0, 'result': None, 'message': "Creating Classification data Failed!"}
    except:
        pass
    
    
# def knowledge_qa(doc, api_key):
#     datas = {
#         "doc": doc,
#         "api_key": api_key
#     }
    
#     url = "http://211.109.9.144:8001/api/v1/closed_qa"
#     response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

#     try:
#         result = json.loads(response.text)['result']
#         print(result)
#         if result:
#             return {'code': 1, 'result': result, 'message': "Knowledge QA data Generation Successful!"}
#         else:
#             return {'code': 0, 'result': None, 'message': "Knowledge QA data Generation Failed!"}
#     except:
#         pass


def knowledge_qa(content, c_iter, api_key):
    datas = {
        "content": content,
        "iter": c_iter,
        "api_key": api_key
    }
    
    url = "http://211.109.9.144:8001/api/v1/closed_qa"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    try:
        result = json.loads(response.text)['result']

        if result:
            return {'code': 1, 'result': result, 'message': "Knowledge QA data Generation Successful!"}
        else:
            return {'code': 0, 'result': None, 'message': "Knowledge QA data Generation Failed!"}
    except:
        pass


def intent_sentence(topic, intent, sample1, sample2, sample3, iter, api_key="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"):
    datas = {
        "topic": topic,
        "intent": intent,
        "sample1": sample1,
        "sample2": sample2,
        "sample3": sample3,
        "iter": iter,
        "api_key": api_key
    }
    
    url = "http://211.109.9.144:8001/api/v1/intent_generation"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    
    try:
        result = json.loads(response.text)['result']

        if result:
            return {'code': 1, 'result': result, 'message': "Creating Intent data Successful!"}
        else:
            return {'code': 0, 'result': None, 'message': "Creating Intent data Failed!"}
    except:
        pass


def keyword_extraction(k_sent1, keyword1, k_sent2, keyword2, k_sent3, keyword3, iter, api_key="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"):
    datas = {
        "sent1": k_sent1,
        "keyword1": keyword1,
        "sent2": k_sent2,
        "keyword2": keyword2,
        "sent3": k_sent3,
        "keyword3": keyword3,
        "iter": iter,
        "api_key": api_key
    }
    
    url = "http://211.109.9.144:8001/api/v1/keyword_generation"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    
    try:
        result = json.loads(response.text)['result']

        if result:
            return {'code': 1, 'result': result, 'message': "Creating KeywordExtraction data Successful!"}
        else:
            return {'code': 0, 'result': None, 'message': "Creating KeywordExtraction data Failed!"}
    except:
        pass


def knowledge_prompt(content, iter, api_key="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"):
    datas = {
        "content": content,
        "iter": iter,
        "api_key": api_key
    }
    
    url = "http://211.109.9.144:8001/api/v1/openprompt_generation"
    response = requests.post(url, data=json.dumps(datas), headers={"Content-Type" : "application/json;charset=UTF-8", "Accept" : "*/*"})

    
    try:
        result = json.loads(response.text)['result']

        if result:
            return {'code': 1, 'result': result, 'message': "Creating prompt data Successful!"}
        else:
            return {'code': 0, 'result': None, 'message': "Creating prompt data Failed!"}
    except:
        pass