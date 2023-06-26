import streamlit as st
import streamlit_ext as ste
from get_response import text_classification as text_cls


def main():
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Text Classification",  # String or None. Strings get appended with "• Streamlit".
        page_icon="🗣️",  # String, anything supported by st.image, or None.
    )

    st.header("Text Classification")
    # st.sidebar.header("페르소나에 따라 발화 변환하기")
    
    st.write(
        """💡자연어 텍스트에 대한 다양한 분류데이터를 만들 수 있는 기능을 제공합니다."""
    )
    st.text("\n")

    left, right = st.columns([2, 2])
    iter_, key_ = st.columns([1, 3])
    sent_, class_ = st.columns([3, 1])

    with left:
        theme = left.text_input(label="분류 데이터의 주제를 입력해주세요", value="뉴스제목 분류")
    with right:
        class_list = right.text_input(label="분류 클래스를 입력해주세요", value="[\"경제\", \"스포츠\", \"사회\"]", help="리스트로 입력해주세요.")
    with iter_:
        d_iter = st.number_input(label="생성 할 데이터 개수", value=10)
    with key_:
        api_key = st.text_input(label="OpenAI API key", value="", help="OpenAI에서 발급받은 key를 입력해주세요.")
    with sent_:
        ex_sent1 = st.text_input(label="예시 문장1", value="손흥민, 3경기 득점포 가동, 토트넘 순위 훌쩍")
        ex_sent2 = st.text_input(label="예시 문장2", value="코스닥지수 사상 최대로 떨어져.. 충격")
        ex_sent3 = st.text_input(label="예시 문장3", value="아파트 분양사기, 극정.. 분양률 역대 최저")
    with class_:
        ex_class1 = st.text_input(label="예시 클래스1", value="스포츠")
        ex_class2 = st.text_input(label="예시 클래스2", value="경제")
        ex_class3 = st.text_input(label="예시 클래스3", value="사회")

    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="생성하기")

    if submit_button:
        cls_result = text_cls(theme, class_list, ex_sent1, ex_class1, ex_sent2, ex_class2, ex_sent3, ex_class3, d_iter, api_key="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")
        cls_code = cls_result["code"]
        cls_result_ = cls_result["result"]["answer"]

        if cls_code == 1:
            st.success("데이터 생성 성공!", icon="✅")
            # st.markdown(cls_result_)
        else:
            st.error('데이터 생성 실패!', icon="🚨")
            # st.markdown(cls_result_)

        new_dir = '.'+cls_result_
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