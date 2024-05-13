import cv2
import numpy as np

# Đọc ảnh mo do nhieu hat
img = cv2.imread('Mo_anh_do_nhieu_hat.jpg')

# Áp dụng Non-local Means Denoising để giảm độ nhiễu
denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# Kích thước mới cho ảnh (ở đây là 1/2 kích thước gốc)
new_width = img.shape[1] // 4
new_height = img.shape[0] // 4
new_size = (new_width, new_height)

# Thay đổi kích thước của ảnh gốc và ảnh đã giảm độ nhiễu
resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
resized_denoised = cv2.resize(denoised, new_size, interpolation=cv2.INTER_LINEAR)

# Hiển thị ảnh gốc và ảnh đã giảm độ nhiễu
cv2.imshow('Original Image', resized_img)
cv2.imshow('Denoised Image', resized_denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Đọc ảnh
#mo do thieu sang
img = cv2.imread('Mo_anh_do_thieu_anh_sang.jpg')

# Áp dụng phương pháp làm rõ ảnh (ví dụ: sử dụng phương pháp làm nét thông minh)
new_width = img.shape[1] // 4
new_height = img.shape[0] // 4
new_size = (new_width, new_height)
enhanced = cv2.detailEnhance(img)
resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
resized_denoised = cv2.resize(enhanced, new_size, interpolation=cv2.INTER_LINEAR)

# Hiển thị ảnh gốc và ảnh đã giảm độ nhiễu
cv2.imshow('Original Image', resized_img)
cv2.imshow('Denoised Image', resized_denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()



#mo do suong

# Đọc ảnh
img = cv2.imread('Mo_anh_do_moi_truong.jpg')

# Áp dụng bộ lọc Gaussian để làm mờ ảnh
blurred = cv2.GaussianBlur(img, (0, 0), 3)
edge_mask = cv2.subtract(img, blurred)
unsharp_masked = cv2.addWeighted(img, 1.5, edge_mask, -0.5, 0)

# Hiển thị ảnh gốc và ảnh đã làm rõ
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', unsharp_masked)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Đọc ảnh mo do sai tieu diem
image = cv2.imread('Mo_anh_do_ngoai_tieu_diem.jpg')

# Điều chỉnh kích thước của ảnh
scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5)  

# Tạo bản sao của ảnh
sharpened_image = scaled_image.copy()

# Áp dụng Median Blur
blurred_image = cv2.medianBlur(scaled_image, 27)  

# Tính toán hiệu ứng Unsharp Masking
sharpened_image = cv2.addWeighted(scaled_image, 1.5, blurred_image, -0.5, 0)

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow('Original Image', scaled_image)
cv2.imshow('Sharpened Image',sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#########


