import streamlit as st
from PIL import Image
import io

# Judul aplikasi
st.title("Rotating Picture with Download Options")

# Upload gambar
uploaded_image = st.file_uploader("Upload gambar (PNG atau JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Membaca gambar yang diunggah
    image = Image.open(uploaded_image)

    # Slider untuk mengatur rotasi gambar
    angle = st.slider("Rotasi gambar (derajat)", 0, 360, 0)

    # Melakukan rotasi gambar
    rotated_image = image.rotate(angle)

    # Menampilkan gambar asli
    st.subheader("Gambar Asli")
    st.image(image, caption="Gambar Asli", use_column_width=True)

    # Menampilkan gambar setelah rotasi
    st.subheader("Gambar Setelah Rotasi")
    st.image(rotated_image, caption="Gambar Setelah Rotasi", use_column_width=True)

    # Menyiapkan file untuk diunduh
    st.subheader("Unduh Gambar Hasil Rotasi")
    
    # Simpan sebagai JPG
    buffer_jpg = io.BytesIO()
    rotated_image.convert("RGB").save(buffer_jpg, format="JPEG")
    buffer_jpg.seek(0)
    st.download_button(
        label="Download sebagai JPG",
        data=buffer_jpg,
        file_name="rotated_image.jpg",
        mime="image/jpeg",
    )

    # Simpan sebagai PNG
    buffer_png = io.BytesIO()
    rotated_image.save(buffer_png, format="PNG")
    buffer_png.seek(0)
    st.download_button(
        label="Download sebagai PNG",
        data=buffer_png,
        file_name="rotated_image.png",
        mime="image/png",
    )

    # Simpan sebagai PDF
    buffer_pdf = io.BytesIO()
    rotated_image.convert("RGB").save(buffer_pdf, format="PDF")
    buffer_pdf.seek(0)
    st.download_button(
        label="Download sebagai PDF",
        data=buffer_pdf,
        file_name="rotated_image.pdf",
        mime="application/pdf",
    )
