from transformers import pipeline

class GrammarCorrector:
    def __init__(self, model_name="t5-base"):
        """
        문법 교정기를 초기화합니다.
        Args:
            model_name (str): 사전 학습된 모델 이름 (기본값: "t5-base")
        """
        self.corrector = pipeline("text2text-generation", model=model_name)

    def correct(self, text):
        """
        입력 텍스트의 문법을 교정합니다.
        Args:
            text (str): 입력 텍스트
        Returns:
            corrected_text (str): 교정된 텍스트
        """
        # T5 모델은 "문법 교정"을 명시적으로 지정
        input_text = f"grammar: {text}"
        result = self.corrector(input_text, max_length=512, truncation=True)
        corrected_text = result[0]["generated_text"]
        return corrected_text

# 테스트 코드
if __name__ == "__main__":
    input_text = """This is a sample txt with som grammar mistakes."""
    
    # GrammarCorrector 인스턴스 생성
    corrector = GrammarCorrector(model_name="t5-small")  # 경량 모델로 테스트
    corrected_text = corrector.correct(input_text)
    
    print("입력 텍스트:")
    print(input_text)
    print("\n교정된 텍스트:")
    print(corrected_text)
