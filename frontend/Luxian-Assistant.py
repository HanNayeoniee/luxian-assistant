import streamlit as st

def main():
    st.set_page_config(
        page_title="LUXIAN-ASSISTANT",
        page_icon="👋",
        layout="centered"
    )
    
    st.title("LUXIAN-ASSISTANT ver 0.9")
    st.sidebar.info("6가지 기능 중 하나를 선택해주세요.")
    st.markdown(
        """
        Luxian-Assistant는 자연어처리 학습데이터 구축이 필요한 룩시안에게 도움을 줄 수 있습니다.
        
        제공되는 6가지의 학습데이터 구축 기능을 통해 인공지능 모델을 학습해보세요!



        ### Intent Sentence
        - 인텐트 문장을 주제와 목적에 알맞게 자동 생성하는 기능입니다.
        - 다양한 톡봇 서비스에 활용 가능합니다!


        ### Keyword Extraction
        - 문장에서 핵심이 되는 키워드를 추출해줄 수 있는 학습데이터를 자동으로 생성하는 기능입니다.
        - 키워드는 N개 이상 포함되어 있으며, 키워드가 추출되지 않아야할 케이스에 대해서도 생성 가능합니다.


        ### Knowledge Prompt
        - 특정 문서를 바탕으로 생성 가능한 다양한 프롬프트 데이터를 자동으로 구축합니다.
        - 다양한 루시아 기반 프로젝트에 활용 가능합니다.


        ### Knowledge QA
        - 특정 문서를 기반으로 한 다양한 QA 학습 데이터를 구축할 수 있습니다.
        - 룩시아 및 톡봇의 IRQA에 사용 가능합니다.


        ### Style Transfer
        - 특정 캐릭터와 페르소나를 갖는 발화 스타일을 변환하고, 학습데이터화 할 수 있는 기능입니다.
        - 손비서, 메타휴먼 등에 적용 가능합니다.

        
        ### Text Classification
        - 자연어 텍스트에 대한 다양한 분류데이터를 만들 수 있는 기능을 제공합니다.
        - 설정된 값에 따라 감성분석, 뉴스 주제 분류 등 다양한 태스크에 적용이 가능합니다.


        ### 추후에 다양한 기능들이 추가될 예정입니다.
        - 문서 생성 요약 학습데이터 구축 기능
        - 문서 제목 생성 학습데이터 구축 기능
        - 한국어 영어 번역 학습데이터 구축 기능
        - 문장 임베딩 학습데이터 구축 기능

        **ChatGPT 서비스이기 때문에 반드시 OpenAI API Key를 발급하신 후 이용해주세요.**
        """
    )
    
    st.text("by @Saltlux AI Labs 박상민, 손유리, 한나연")
    

if __name__ == "__main__":
    main()