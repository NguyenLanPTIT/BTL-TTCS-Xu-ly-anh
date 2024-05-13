import cv2
import numpy as np
# 1. Gau
# Đọc ảnh từ file

image = cv2.imread('Mo_anh_do_chuyen_dong.jpg')
if image is None:
    print("Không thể đọc được ảnh")
else:
    blurred_image = cv2.GaussianBlur(image, (35, 35), 25)  
    sharpened_image = cv2.addWeighted(image, 1.5, blurred_image, -0.5, 0)

    # Hiển thị ảnh gốc và ảnh đã làm nét
    cv2.imshow('Original Image', image)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Đọc ảnh từ file
image = cv2.imread('sharpen.png')

# Kiểm tra xem ảnh có được đọc thành công hay không
if image is None:
    print("Không thể đọc được ảnh")
else:
    # Tạo bộ lọc sharpening kernel
    sharpening_kernel = np.array([[-1, -1, -1],
                                   [-1, 9, -1],
                                   [-1, -1, -1]])

    # Áp dụng bộ lọc sharpening kernel để làm nét ảnh
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    # Hiển thị ảnh gốc và ảnh đã làm nét
    cv2.imshow('Original Image', image)
    cv2.imshow('Sharpened Image', sharpened_image)

    # Chờ bất kỳ phím nào được nhấn và sau đó đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()
