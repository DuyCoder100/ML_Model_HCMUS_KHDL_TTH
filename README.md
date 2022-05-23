# SỬ DỤNG MÔ HÌNH HỒI QUY RIDGE THÔNG QUA MỘT BÀI TOÁN HỒI QUY

## 1. Dataset.

- Nguồn dataset: Kaggle: (link lát quăng)
- Mục tiêu: dự đoán viện phí dựa trên các yếu tố về giới tính, chỉ số BMI, độ tuổi, số lượng con, độ nghiện hút thuốc (1 là có, 0 là không).
- Giải pháp: dựa vào mô hình hồi quy Ridge.

## 2. Data visualization.

## 3. Mô hình hồi quy Ridge.

### 3.1. Lý thuyết.

- Về cơ bản, mô hình hồi quy Ridge cũng có dạng $y = wx + b$.

- Tuy nhiên, khác với Linear Regression, để tránh xảy ra hiện tượng overfitting, hàm mất mát của mô hình hồi quy Ridge thêm hệ số l2-regularization vào hàm mất mát