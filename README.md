# QUẢN LÝ ĐIỂM SINH VIÊN

Ứng dụng Streamlit hiển thị bảng điểm của 10 sinh viên, tính điểm tổng kết và xếp loại, thống kê điểm trung bình, sinh viên cao/thấp điểm nhất, số sinh viên đạt, tra cứu theo Selectbox và biểu đồ cột.

## Chạy ứng dụng trên máy tính

1. Cài Python nếu máy chưa có.
2. Mở Terminal/CMD trong thư mục dự án.
3. Cài thư viện:

   ```bash
   pip install -r requirements.txt
   ```

4. Chạy ứng dụng:

   ```bash
   streamlit run app.py
   ```

5. Trình duyệt sẽ mở ứng dụng; nếu không, mở địa chỉ local được hiển thị trong Terminal (thường là `http://localhost:8501`).

## Đưa lên GitHub và triển khai Streamlit Community Cloud

1. Tạo repository mới trên GitHub, ví dụ `quan-ly-diem-sinh-vien`.
2. Tải lên `app.py`, `requirements.txt` và `README.md` (không cần tải thư mục môi trường ảo).
3. Mở Streamlit Community Cloud, đăng nhập bằng GitHub và cấp quyền truy cập repository.
4. Chọn **Create app** / **Deploy an app**, chọn repository vừa tạo, nhánh `main`, file chính `app.py`.
5. Nhấn **Deploy** và chờ ứng dụng được triển khai. Sau đó bạn sẽ nhận được đường dẫn web để chia sẻ.

Lưu ý: Bạn cần tự đăng nhập và xác nhận thao tác trên GitHub/Streamlit; không nên chia sẻ mật khẩu hoặc mã xác thực với người khác.
