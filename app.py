import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cấu hình trang
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Bảng điểm, thống kê kết quả học tập và tra cứu điểm từng sinh viên.")

# 1. Tạo dữ liệu
data = {
    "Ho_ten": [
        "Mai Thùy Trang",
        "Bùi Hữu Học",
        "Lê Nguyễn Lan Anh",
        "Trần Quang Thắng",
        "Vũ Viết Hoàng Dũng",
        "Phạm Hoàng Anh",
        "Lương Công Khánh",
        "Lê Ngọc Uyên",
        "Đinh Thị Ngọc Hân",
        "Ngô Gia Hân"
    ],
    "Chuyen_can": [10, 9.5, 9.0, 8.5, 8.0, 8.5, 9.0, 9.5, 9.0, 8.0],
    "Giua_ki": [10, 9.5, 6.0, 8.5, 8.0, 7.5, 8.0, 8.5, 9.0, 8.5],
    "Cuoi_ki": [9.5, 9.0, 5.5, 10, 7.5, 8.0, 9.0, 8.5, 9.0, 9.5],
}

df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)

# 2. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ki"]
    + 0.5 * df["Cuoi_ki"]
)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Tên cột hiển thị thân thiện
bang_diem = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ki": "Giữa kỳ",
    "Cuoi_ki": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại",
})

# 4. Bảng điểm
st.subheader("📋 Bảng điểm của 10 sinh viên")
st.dataframe(
    bang_diem[["Họ tên", "Chuyên cần", "Giữa kỳ", "Cuối kỳ", "Tổng kết", "Xếp loại"]]
    .round(2),
    use_container_width=True
)

# 5. Thống kê lớp
diem_trung_binh = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sinh_vien_dat = int((df["Tong_ket"] >= 5).sum())

st.subheader("📊 Thống kê kết quả học tập")
cot1, cot2, cot3 = st.columns(3)
cot1.metric("Điểm trung bình của lớp", f"{diem_trung_binh:.2f}")
cot2.metric("Số sinh viên đạt (từ 5 điểm)", f"{so_sinh_vien_dat}/{len(df)}")
cot3.metric("Tổng số sinh viên", len(df))

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 🏆 Sinh viên có điểm cao nhất")
    st.write(f"**Họ tên:** {sv_cao_nhat['Ho_ten']}")
    st.write(f"**Điểm tổng kết:** {sv_cao_nhat['Tong_ket']:.2f}")
    st.write(f"**Xếp loại:** {sv_cao_nhat['Xep_loai']}")

with col2:
    st.markdown("#### 📉 Sinh viên có điểm thấp nhất")
    st.write(f"**Họ tên:** {sv_thap_nhat['Ho_ten']}")
    st.write(f"**Điểm tổng kết:** {sv_thap_nhat['Tong_ket']:.2f}")
    st.write(f"**Xếp loại:** {sv_thap_nhat['Xep_loai']}")

# 6. Selectbox tra cứu sinh viên
st.subheader("🔎 Tra cứu điểm theo sinh viên")
ten_sinh_vien = st.selectbox(
    "Chọn một sinh viên:",
    options=df["Ho_ten"].tolist()
)
sinh_vien = df.loc[df["Ho_ten"] == ten_sinh_vien].iloc[0]

d1, d2, d3, d4, d5 = st.columns(5)
d1.metric("Chuyên cần", f"{sinh_vien['Chuyen_can']:.1f}")
d2.metric("Giữa kỳ", f"{sinh_vien['Giua_ki']:.1f}")
d3.metric("Cuối kỳ", f"{sinh_vien['Cuoi_ki']:.1f}")
d4.metric("Điểm tổng kết", f"{sinh_vien['Tong_ket']:.2f}")
d5.metric("Xếp loại", sinh_vien["Xep_loai"])

# 7. Biểu đồ cột điểm tổng kết
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", labelrotation=45)
for label in ax.get_xticklabels():
    label.set_horizontalalignment("right")
ax.bar_label(bars, fmt="%.2f", padding=3, fontsize=8)
fig.tight_layout()
st.pyplot(fig, use_container_width=True)
plt.close(fig)

# 8. Thông tin người tạo ứng dụng ở cuối trang
st.markdown(
    """
    <hr>
    <div style="text-align:center; color:gray; font-size:12px;">
        Người tạo ứng dụng: Mai Thùy Trang | MSSV: 034308004826
    </div>
    """,
    unsafe_allow_html=True
)
