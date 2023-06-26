import streamlit as st
import time
from get_response import create_persona, delete_persona, style_transfer


def main():
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Style Transfer",  # String or None. Strings get appended with "• Streamlit".
        page_icon="🗣️",  # String, anything supported by st.image, or None.
    )

    st.header("Style Transfer")
    # st.sidebar.header("페르소나에 따라 발화 변환하기")
    st.write(
        """💡특정 캐릭터와 페르소나를 갖는 발화 스타일을 변환하고, 학습데이터화 할 수 있는 기능입니다."""
    )
    st.text("\n")
    
    job = st.radio(
        label="기능을 선택해주세요",
        options=("페르소나 생성", "페르소나 삭제", "발화 스타일 변환"),
        horizontal=True
    )
    
    if job == "페르소나 생성":        
        col1, col2 = st.columns([1, 3])
        with col1:
            employee_id = st.text_input(label="사번", value="230505")
            
        with col2:
            name = st.text_input(label="페르소나 이름", value="뽀로로")
            age = st.text_input(label="페르소나 나이", value="5살")
            sex = st.text_input(label="페르소나 성별", value="남자")
            occupation = st.text_input(label="페르소나 직업", value="유치원생")
            personality = st.text_input(label="페르소나 성격", value="쾌활하고 수다스러움")
            likes = st.text_input(label="페르소나가 좋아하는 것", value="밖에서 친구들과 뛰어노는 것")
            # create_persona_button = st.form_submit_button(label="페르소나 생성")
            
        
        with st.form(key="inputs"):
            create_persona_button = st.form_submit_button(label="페르소나 생성")
            
            ## 페르소나 생성
            if create_persona_button:
                response = create_persona(employee_id, name, age, sex, occupation, personality, likes)
                print(response)    

                
                status_code = response['code']
                if status_code == 1:
                    st.success("페르소나 생성 성공!", icon="✅")
                    created_persona = list(response["result"]['answer'].keys())[0]
                    created_persona_context = list(response["result"]['answer'].values())[0]
                    st.markdown(created_persona)
                    st.markdown(created_persona_context)
                    
                else:
                    st.error('페르소나 생성 실패!', icon="🚨")
                
        
    elif job == "페르소나 삭제":
        col1, col2 = st.columns([1, 3])
        with col1:
            employee_id = st.text_input(label="사번", value="230505")
            
        with col2:
            name = st.text_input(label="페르소나 이름", value="뽀로로")
        
        with st.form(key="inputs"):
            delete_persona_button = st.form_submit_button(label="페르소나 삭제")
            
            ## 페르소나 삭제
            if delete_persona_button:
                response = delete_persona(employee_id, name)
                print(response)
                
                status_code = response['code']
                if status_code == 1:
                    st.success("페르소나 삭제 성공!", icon="✅")
                else:
                    st.error('페르소나 삭제 실패!', icon="🚨")
                
    else:
        col1, col2 = st.columns([1, 3])
        
        with col1:
            employee_id = st.text_input(label="사번", value="230505")
        with col2:
            name = st.text_input(label="페르소나 이름", value="뽀로로")
            utterance = st.text_input(label="변환할 발화", value="나 배고파")
            _api_key = st.text_input(label="OpenAI API key", value="", help="OpenAI에서 발급받은 key를 입력해주세요.")
            
        with st.form(key="inputs"):
            transfer_button = st.form_submit_button(label="발화 스타일 변환")
            
            ## 발화 스타일 변환
            if transfer_button:
                # if _api_key is not None:
                #     api_key = _api_key
                # else:                  
                #     api_key = "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"
                    
                api_key = "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"
                response = style_transfer(employee_id, name, utterance, api_key)
                print(response)
                
                status_code = response['code']
                print('status_code:', status_code)
                
                if status_code == 1:
                    st.success("발화 스타일 변환 성공!", icon="✅")
                    transfered_utt = response["result"]['answer']
                    inference_time = response["result"]['inference_time']
                    st.markdown(transfered_utt)
                else:
                    st.error('발화 스타일 변환 실패!', icon="🚨")
                    
    st.text("by @Saltlux AI Labs 박상민, 손유리, 한나연")

if __name__ == "__main__":
    main()