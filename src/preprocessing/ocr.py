import pytesseract
from preprocess import preprocess_image

# Tesseract-OCR 경로 설정 (Windows 사용자라면 경로를 직접 지정)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    """
    이미지를 읽어 텍스트를 추출
    Args:
        image_path (str): 입력 이미지 경로
    Returns:
        extracted_text (str): 추출된 텍스트
    """
    # 전처리된 이미지 가져오기
    processed_image = preprocess_image(image_path)

    # Tesseract를 사용하여 텍스트 추출
    extracted_text = pytesseract.image_to_string(processed_image, lang="eng")  # 언어 설정 가능 (e.g., 'kor' for Korean)

    return extracted_text

# 테스트 코드
if __name__ == "__main__":
    image_path = "data/input/sample_handwriting.jpg"  # 샘플 이미지 경로
    try:
        text = extract_text(image_path)
        print("추출된 텍스트:")
        print(text)
    except FileNotFoundError as e:
        print(e)
