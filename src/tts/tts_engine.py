import pyttsx3

class TextToSpeech:
    def __init__(self, language="en"):
        """
        Text-to-Speech 엔진 초기화
        Args:
            language (str): 사용할 언어 코드 (예: 'en' 영어, 'ko' 한국어)
        """
        self.engine = pyttsx3.init()
        self.language = language
        self._configure_engine()

    def _configure_engine(self):
        """
        TTS 엔진 설정
        """
        # 속도, 음량, 목소리 설정
        self.engine.setProperty("rate", 150)  # 발음 속도
        self.engine.setProperty("volume", 1.0)  # 음량
        voices = self.engine.getProperty("voices")
        if self.language == "ko":
            # 한국어 음성을 지원하는 경우
            self.engine.setProperty("voice", voices[1].id)  # 1번 인덱스는 한국어
        else:
            # 기본 영어 목소리
            self.engine.setProperty("voice", voices[0].id)  # 0번 인덱스는 영어

    def speak(self, text):
        """
        텍스트를 음성으로 변환하여 출력
        Args:
            text (str): 입력 텍스트
        """
        print("텍스트를 음성으로 변환 중...")
        self.engine.say(text)
        self.engine.runAndWait()

    def save_audio(self, text, output_path="output_audio.mp3"):
        """
        텍스트를 음성으로 변환하여 파일로 저장
        Args:
            text (str): 입력 텍스트
            output_path (str): 저장할 파일 경로
        """
        self.engine.save_to_file(text, output_path)
        self.engine.runAndWait()
        print(f"오디오 파일이 저장되었습니다: {output_path}")


# 테스트 코드
if __name__ == "__main__":
    input_text = "Hello! This is a text-to-speech conversion example."
    tts = TextToSpeech(language="en")  # 영어
    tts.speak(input_text)
    tts.save_audio(input_text, "output_audio.mp3")
