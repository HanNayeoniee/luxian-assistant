import streamlit as st
import streamlit_ext as ste
from get_response import knowledge_qa

def main():
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Knowledge QA",  # String or None. Strings get appended with "• Streamlit".
        page_icon="🗣️",  # String, anything supported by st.image, or None.
    )

    st.header("Knowledge QA")
    # st.sidebar.header("페르소나에 따라 발화 변환하기")
    st.write(
        """💡특정 문서를 기반으로 한 다양한 QA 학습 데이터를 구축할 수 있습니다."""
    )
    st.text("\n")

    
    sample_doc = """특히 이번 채용은 일반 개발자가 인공지능(AI) 개발자로서 커리어를 시작할 수 있는 기회가 될 것으로 보인다.
솔트룩스 관계자는 "AI 관련 경력 보유 관계없이 우수한 역량을 지닌 개발자를 채용한다"며 "자체 프로그램을 통해 AI 전문가로 성장할 수 있도록 교육할 예정이라고 밝혔다.
프롬프트 엔지니어의 경우 글쓰기 등 작문과 IT 기술에 관심이 많은 사람이라면 전공과 무관하게 누구나 지원할 수 있다.
솔트룩스 관계자는 "AI와 빅데이터 원천 기술을 보유한 솔트룩스와 함께 성장할 창의적이고 도전적인 인재들의 많은 관심과 지원 바란다"고 말했다.
"""
    col1, col2 = st.columns([1, 3])
    with col1:
        c_iter = st.number_input(label="생성 할 데이터 개수", value=10)
    with col2:
        api_key_ = st.text_input(label="OpenAI API key", value="", help="OpenAI에서 발급받은 key를 입력해주세요.")
    
    content = st.text_area(
        "질의응답 데이터를 생성하고 싶은 문서를 입력해주세요", sample_doc, max_chars=2000, height=400
    )
    
    with st.form(key="inputs"):
        knowledge_qa_button = st.form_submit_button(label="생성하기")
        
        ## 문서기반 질의응답 데이터 생성
        if knowledge_qa_button:
            api_key = "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"
            print(content, c_iter, api_key)
            
            
            if len(content) <= 0:
                st.error('문서를 입력해주세요!', icon="🚨")
            else:
                response = knowledge_qa(content, c_iter, api_key)
                print('response')
                print(response)    

                
                status_code = response['code']
                out_path = response['result']['answer']
                if status_code == 1 and len(content) > 0:
                    st.success("데이터 생성 성공!", icon="✅")
                else:
                    st.error('데이터 생성 실패!', icon="🚨")
                    
                new_dir = '.' + out_path
                file_name_ = new_dir.split("/")[2]
                print(file_name_)
                
                file_bytes = open(new_dir, 'rb')
                file_save = ste.download_button(
                    label='다운로드', 
                    data=file_bytes, 
                    file_name=file_name_
                )
                    
    st.text("by @Saltlux AI Labs 박상민, 손유리, 한나연") 

if __name__ == "__main__":
    main()