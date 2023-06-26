import streamlit as st
import streamlit_ext as ste
from get_response import intent_sentence as intent


def main():
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Intent Sentence",  # String or None. Strings get appended with "• Streamlit".
        page_icon="🗣️",  # String, anything supported by st.image, or None.
    )

    st.header("Intent Sentence")
    # st.sidebar.header("페르소나에 따라 발화 변환하기")
    st.write(
        """💡인텐트 문장을 주제와 목적에 알맞게 자동 생성하는 기능입니다."""
    )
    st.text("\n")

    left, right = st.columns([2, 2])
    iter_, key_ = st.columns([1, 3])

    with left:
        topic = left.text_input(label="인텐트를 위한 주제를 입력해주세요", value="자동차")
    with right:
        intent_ = right.text_input(label="주제에 대한 인텐트의 목적을 입력해주세요", value="보험")
    with iter_:
        i_iter = st.number_input(label="생성 할 데이터 개수", value=10)
    with key_:
        api_key_ = st.text_input(label="OpenAI API key", value="", help="OpenAI에서 발급받은 key를 입력해주세요.")
    sample1 = st.text_input(label="예시 문장1", value="자동차 보험은 언제 갱신해야되나요?")
    sample2 = st.text_input(label="예시 문장2", value="자동차 보험을 변경하고 싶습니다.")
    sample3 = st.text_input(label="예시 문장3", value="자동차 보험 보장 범위가 어떻게 되나요?")

    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="생성하기")

    if submit_button:
        int_result = intent(topic, intent_, sample1, sample2, sample3, i_iter, api_key="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")
        # print(int_result)
        int_code = int_result["code"]
        int_result_ = int_result["result"]["answer"]

        if int_code == 1:
            st.success("데이터 생성 완료!", icon="✅")
        else:
            st.error('데이터 생성 실패!', icon="🚨")

        int_dir = '.'+int_result_
        file_name_ = int_dir.split("/")[2]

        print(file_name_)
        file_bytes = open(int_dir, 'rb')
        file_save = ste.download_button(
            label='다운로드', 
            data=file_bytes, 
            file_name=file_name_
        )
        
    st.text("by @Saltlux AI Labs 박상민, 손유리, 한나연")


if __name__ == "__main__":
    main()