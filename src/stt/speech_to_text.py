import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        """
        음성 인식기 초기화
        """
        self.recognizer = sr.Recognizer()

    def recognize_from_audio(self, audio_path):
        """
        오디오 파일을 텍스트로 변환
        Args:
            audio_path (str): 오디오 파일 경로 (mp3, wav 등)
        Returns:
            str: 변환된 텍스트
        """
        # 오디오 파일을 읽기
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)  # 오디오 파일에서 음성 데이터 추출

            # 음성을 텍스트로 변환
            text = self.recognizer.recognize_google(audio, language="en-US")  # 영어로 변환
            return text
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
            return None
        except sr.RequestError as e:
            print(f"Google 음성 인식 서비스에 접근할 수 없습니다. 오류: {e}")
            return None

# 테스트 코드
if __name__ == "__main__":
    audio_path = "data/input/sample_audio.wav"  # 샘플 오디오 파일 경로
    stt = SpeechToText()
    text = stt.recognize_from_audio(audio_path)

    if text:
        print("변환된 텍스트:")
        print(text)
    else:
        print("음성 인식에 실패했습니다.")
