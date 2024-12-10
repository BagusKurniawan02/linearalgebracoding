import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("Rotating Picture")

# Upload gambar
uploaded_image = st.file_uploader("Upload gambar (PNG atau JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Baca gambar
    image = Image.open(uploaded_image)

    # Slider untuk rotasi
    angle = st.slider("Rotasi gambar (derajat)", 0, 360, 0)

    # Rotasi gambar
    rotated_image = image.rotate(angle)

    # Tampilkan gambar asli dan gambar yang sudah dirotasi
    st.subheader("Gambar Asli")
    st.image(image, use_column_width=True)

    st.subheader("Gambar Setelah Rotasi")
    st.image(rotated_image, use_column_width=True)