from src.ocr.handwriting_recognizer import HandwritingRecognizer
from src.grammar.grammar_corrector import GrammarCorrector
from src.tts.tts_engine import TextToSpeech
from src.stt.speech_to_text import SpeechToText

def main():
    # 1. 손글씨 추출
    image_path = "data/input/sample_data.jpg"
    ocr = HandwritingRecognizer()
    extracted_text = ocr.extract_text(image_path)
    print("추출된 텍스트:", extracted_text)

    # 2. 문법 교정
    corrector = GrammarCorrector(model_name="t5-small")
    corrected_text = corrector.correct(extracted_text)
    print("교정된 텍스트:", corrected_text)

    # 3. 텍스트를 음성으로 변환
    tts = TextToSpeech(language="en")
    tts.speak(corrected_text)
    tts.save_audio(corrected_text, "output_audio.mp3")

    # 4. 음성 인식 예시 (음성 파일을 텍스트로 변환)
    stt = SpeechToText()
    recognized_text = stt.recognize_from_audio("data/input/sample_audio.wav")
    print("음성 인식 결과:", recognized_text)

if __name__ == "__main__":
    main()
