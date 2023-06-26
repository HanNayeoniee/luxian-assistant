import streamlit as st
import streamlit_ext as ste
from get_response import keyword_extraction as keyword


def main():
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Keyword Extraction",  # String or None. Strings get appended with "• Streamlit".
        page_icon="🗣️",  # String, anything supported by st.image, or None.
    )

    st.header("Keyword Extraction")
    # st.sidebar.header("페르소나에 따라 발화 변환하기")
    st.write(
        """💡문장에서 핵심이 되는 키워드를 추출해줄 수 있는 학습데이터를 자동으로 생성하는 기능입니다."""
    )
    st.text("\n")

    iter_, key_ = st.columns([1, 3])
    sent_, keyword_ = st.columns([3, 1])

    with iter_:
        k_iter = st.number_input(label="생성 할 데이터 개수", value=10)
    with key_:
        api_key_ = st.text_input(label="OpenAI API key", value="", help="OpenAI에서 발급받은 key를 입력해주세요.")
    with sent_:
        k_sent1 = st.text_input(label="예시 문장1", value="오늘 점심으로 햄버거와 피자를 먹었습니다")
        k_sent2 = st.text_input(label="예시 문장2", value="저는 주말에 이마트를 다녀올 예정입니다.")
        k_sent3 = st.text_input(label="예시 문장3", value="안녕하세요.")
    with keyword_:
        keyword1 = st.text_input(label="예시 키워드1", value="[\"햄버거\",\"피자\"]", help="리스트로 입력해주세요.")
        keyword2 = st.text_input(label="예시 키워드2", value="[\"이마트\"]", help="리스트로 입력해주세요.")
        keyword3 = st.text_input(label="예시 키워드3", value="[]", help="리스트로 입력해주세요.")

    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="생성하기")

    if submit_button:
        key_result = keyword(k_sent1, keyword1, k_sent2, keyword2, k_sent3, keyword3, k_iter, api_key="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")
        key_code = key_result["code"]
        key_result_ = key_result["result"]["answer"]

        if key_code == 1:
            st.success("데이터 생성 성공!", icon="✅")
            # st.markdown(cls_result_)
        else:
            st.error('데이터 생성 실패!', icon="🚨")
            # st.markdown(cls_result_)

        new_dir = '.'+key_result_
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