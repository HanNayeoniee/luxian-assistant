import streamlit as st
import streamlit_ext as ste
from get_response import knowledge_prompt as prompt

def main():
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Knowledge Prompt",  # String or None. Strings get appended with "• Streamlit".
        page_icon="🗣️",  # String, anything supported by st.image, or None.
    )

    st.header("Knowledge Prompt")
    # st.sidebar.header("페르소나에 따라 발화 변환하기")
    st.write(
        """💡특정 문서를 바탕으로 생성 가능한 다양한 프롬프트 데이터를 자동으로 구축합니다."""
    )
    st.text("\n")

    doc_sample = """특히 이번 채용은 일반 개발자가 인공지능(AI) 개발자로서 커리어를 시작할 수 있는 기회가 될 것으로 보인다.
솔트룩스 관계자는 "AI 관련 경력 보유 관계없이 우수한 역량을 지닌 개발자를 채용한다"며 "자체 프로그램을 통해 AI 전문가로 성장할 수 있도록 교육할 예정이라고 밝혔다.
프롬프트 엔지니어의 경우 글쓰기 등 작문과 IT 기술에 관심이 많은 사람이라면 전공과 무관하게 누구나 지원할 수 있다.
솔트룩스 관계자는 "AI와 빅데이터 원천 기술을 보유한 솔트룩스와 함께 성장할 창의적이고 도전적인 인재들의 많은 관심과 지원 바란다"고 말했다.
"""

    iter_, key_ = st.columns([1, 3])

    with iter_:
        c_iter = st.number_input(label="생성 할 데이터 개수", value=10)
    with key_:
        api_key_ = st.text_input(label="OpenAI API key", value="", help="OpenAI에서 발급받은 key를 입력해주세요.")
    
    content = st.text_area(
        "프롬프트 데이터를 구축하고 싶은 컨텐츠를 입력해주세요", doc_sample, max_chars=2000, height=400
    )

    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="생성하기")

    if submit_button:
        if len(content) <= 0:
            st.error('컨텐츠를 입력해주세요!', icon="🚨")

        else:
            content_result = prompt(content, c_iter, api_key="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") 
            content_code = content_result["code"]
            content_result_ = content_result["result"]["answer"]

            if content_code == 1:
                st.success("데이터 생성 성공!", icon="✅")
            else:
                st.error('데이터 생성 실패!', icon="🚨")

            new_dir = '.'+content_result_
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