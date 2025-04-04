import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def piecewise_linear_transform(value, breakpoints):
    for i in range(len(breakpoints) - 1):
        x1, y1 = breakpoints[i]
        x2, y2 = breakpoints[i + 1]

        if x1 <= value <= x2:
            return y1 + (y2 - y1) * (value - x1) / (x2 - x1)
    return value

def apply_transform(image, breakpoints):
    vectorized_transform = np.vectorize(lambda x: piecewise_linear_transform(x, breakpoints))
    return vectorized_transform(image).astype(np.uint8)

def auto_breakpoints_histogram(image, num_segments=3):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0,256])
    cdf = hist.cumsum()
    
    total_pixels = cdf[-1]
    segment_size = total_pixels // num_segments
    breakpoints = [0]
    
    for i in range(1, num_segments):
        idx = np.searchsorted(cdf, i * segment_size)
        breakpoints.append(bins[idx])
    
    breakpoints.append(255)
    return [(int(b), int(b)) for b in breakpoints]

def auto_breakpoints_kmeans(image, num_clusters=3):
    pixels = image.flatten().reshape(-1, 1)
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(pixels)
    centroids = sorted(kmeans.cluster_centers_.flatten())
    
    return [(int(c), int(c)) for c in centroids] + [(255, 255)]

def process_gray_image(image_path, output_path, breakpoints=None, auto_mode=None):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if breakpoints is None:
        if auto_mode == "histogram":
            breakpoints = auto_breakpoints_histogram(image)
        elif auto_mode == "kmeans":
            breakpoints = auto_breakpoints_kmeans(image)
        else:
            raise ValueError("Cần nhập điểm biến đổi hoặc chọn chế độ tự động!")

    output_image = apply_transform(image, breakpoints)
    cv2.imwrite(output_path, output_image)  # ✅ Thêm lưu ảnh

    return output_image  # ✅ Trả về ảnh đã xử lý

def process_color_image(image_path, output_path, breakpoints=None, auto_mode=None):
    image = cv2.imread(image_path)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    if breakpoints is None:
        if auto_mode == "histogram":
            breakpoints = auto_breakpoints_histogram(image_hsv[:,:,2])
        elif auto_mode == "kmeans":
            breakpoints = auto_breakpoints_kmeans(image_hsv[:,:,2])
        else:
            raise ValueError("Cần nhập điểm biến đổi hoặc chọn chế độ tự động!")

    image_hsv[:,:,2] = apply_transform(image_hsv[:,:,2], breakpoints)
    output_image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
    
    cv2.imwrite(output_path, output_image)  # ✅ Thêm lưu ảnh

    return output_image  # ✅ Trả về ảnh đã xử lý

