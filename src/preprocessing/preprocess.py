import cv2
import numpy as np

def preprocess_image(image_path):
    """
    이미지를 전처리하여 OCR에 적합한 상태로 변환
    Args:
        image_path (str): 입력 이미지 경로
    Returns:
        processed_image: 전처리된 이미지
    """
    # 이미지 읽기 (그레이스케일)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"이미지를 찾을 수 없습니다: {image_path}")

    # 노이즈 제거
    denoised = cv2.fastNlMeansDenoising(image, h=30)

    # 이진화 처리 (Thresholding)
    _, binary_image = cv2.threshold(denoised, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # 가장자리 검출 (선택 사항)
    edges = cv2.Canny(binary_image, 50, 150)

    return binary_image

