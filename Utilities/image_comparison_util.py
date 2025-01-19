from skimage.metrics import structural_similarity as compare_ssim
import cv2
import os

def assert_images(expected_image_path,actual_image_path):
    image1 = cv2.imread(os.path.join(expected_image_path) ,cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(os.path.join(actual_image_path),cv2.IMREAD_GRAYSCALE)
    similarity_score, diff = compare_ssim(image1, image2, full=True)
    return similarity_score