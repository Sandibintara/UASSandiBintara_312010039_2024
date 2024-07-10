import streamlit as st
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import numpy as np
import colorsys


# Mengimpor gambar dari file lokal
from PIL import Image

# Judul halaman
st.title('UTS Pengolahan citra Streamlit dengan Gambar')
st.title('Universitas Pelitabangsa')

# Deskripsi
st.write('Ini adalah contoh aplikasi Streamlit yang menampilkan gambar')
st.write('Nama : Sandi Bintara')
st.write('NIM : 312010039')
st.write('Kelas : TI20B1 Universitas Pelitabangsa')


# Contoh Upload Gambar pada streamlit
# Mengimpor gambar dari file lokal
gambar = Image.open('C:/Users/sabin/Downloads/UTS CITRA/foto/fruit2.PNG') 

# Menampilkan gambar
st.image(gambar, caption='Gambar buah', use_column_width=True, channels="RGB")
#--------------------------------------------------------------------------------------

# Deskripsi tambahan
st.write('Gambar berikut merupakan kondisi citra normal')

st.write('------------------------------------------------------')
#--------------------------------------------------------------------------------------
st.write('------------------------------------------------------')
# Fungsi untuk mengubah gambar dari RGB ke HSV
def rgb_to_hsv(image):
    # Ubah gambar ke array numpy
    img_array = np.array(image)

    # Ambil ukuran gambar
    height, width, _ = img_array.shape

    # Buat array kosong untuk menyimpan nilai HSV
    hsv_image = np.zeros((height, width, 3))

    # Iterasi melalui setiap piksel gambar dan ubah ke ruang warna HSV
    for y in range(height):
        for x in range(width):
            # Dapatkan nilai RGB dari piksel
            r, g, b = img_array[y, x]

            # Konversi nilai RGB ke HSV menggunakan colorsys
            h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

            # Simpan nilai HSV ke dalam array
            hsv_image[y, x] = [h, s, v]

    return hsv_image

# Tampilkan judul aplikasi
st.title('Konversi Gambar dari RGB ke HSV')

# Pilih gambar default
default_image = Image.open("C:/Users/sabin/Downloads/UTS CITRA/foto/basketball.jpg")

# Tampilkan gambar default
st.image(default_image, caption='Gambar Default (RGB)', use_column_width=True)

# Tombol untuk konversi
if st.button('Konversi ke HSV'):
    # Konversi gambar default ke HSV
    hsv_image = rgb_to_hsv(default_image)

    # Tampilkan gambar yang telah dikonversi
    st.image(hsv_image, caption='Gambar dalam Format HSV', use_column_width=True)
    
st.write('------------------------------------------------------')    
#--------------------------------------------------------------------------------------
st.write('------------------------------------------------------')

# Fungsi untuk menghitung histogram gambar
def calculate_histogram(image):
    # Konversi gambar ke array numpy dan ubah menjadi grayscale jika perlu
    img_array = np.array(image)
    if len(img_array.shape) == 3:
        img_array = np.mean(img_array, axis=2).astype(np.uint8)

    # Hitung histogram menggunakan numpy
    histogram, bins = np.histogram(img_array.flatten(), bins=256, range=[0,256])

    return histogram

# Tampilkan judul aplikasi
st.title('Hitung Histogram Gambar Default')

# Pilih gambar default
default_image = Image.open("C:/Users/sabin/Downloads/UTS CITRA/foto/basketball.jpg")

# Tampilkan gambar default
st.image(default_image, caption='Gambar Default', use_column_width=True)

# Tombol untuk hitung histogram
if st.button('Hitung Histogram'):
    # Hitung histogram gambar
    histogram = calculate_histogram(default_image)
    
    # Tampilkan histogram
    st.write("Histogram:", histogram)
st.write('------------------------------------------------------')
#--------------------------------------------------------------------------------------
st.write('------------------------------------------------------')

# Fungsi untuk mengatur kecerahan dan kontras gambar
def adjust_brightness_contrast(image, brightness, contrast):
    # Konversi gambar ke mode 'RGB' jika tidak dalam mode tersebut
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Buat objek ImageEnhance untuk mengatur kecerahan dan kontras
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    return image

# Tampilkan judul aplikasi
st.title('Atur Kecerahan dan Kontras Gambar Default')

# Pilih gambar default
default_image = Image.open("C:/Users/sabin/Downloads/UTS CITRA/foto/basketball.jpg")

# Tampilkan gambar default
st.image(default_image, caption='Gambar Default', use_column_width=True)

# Tambahkan slider untuk kecerahan dan kontras
brightness = st.slider("Kecerahan", 0.0, 2.0, 1.0, 0.1)
contrast = st.slider("Kontras", 0.0, 2.0, 1.0, 0.1)

# Tombol untuk menerapkan penyesuaian
if st.button('Terapkan Penyesuaian'):
    # Terapkan penyesuaian ke gambar default
    adjusted_image = adjust_brightness_contrast(default_image, brightness, contrast)

    # Tampilkan gambar yang telah disesuaikan
    st.image(adjusted_image, caption='Gambar Dengan Penyesuaian', use_column_width=True)


# Fungsi untuk mengatur kontras gambar
def adjust_contrast(image, contrast):
    # Konversi gambar ke mode 'RGB' jika tidak dalam mode tersebut
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Buat objek ImageEnhance untuk mengatur kontras
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    return image

st.write('------------------------------------------------------')
#--------------------------------------------------------------------------------------
st.write('------------------------------------------------------')

# Fungsi untuk mengubah kontur gambar
def apply_contour(image, threshold):
    # Konversi gambar ke grayscale
    gray_image = ImageOps.grayscale(image)

    # Terapkan filter threshold
    binary_image = gray_image.point(lambda p: p > threshold and 255)

    # Dapatkan kontur menggunakan filter emboss
    contour_image = binary_image.filter(ImageFilter.FIND_EDGES)

    return contour_image

# Tampilkan judul aplikasi
st.title('Ubah Kontur Gambar Default')

# Pilih gambar default
default_image = Image.open("C:/Users/sabin/Downloads/UTS CITRA/foto/basketball.jpg")

# Tampilkan gambar default
st.image(default_image, caption='Gambar Default', use_column_width=True)

# Tambahkan slider untuk threshold
threshold = st.slider("Threshold", 0, 255, 100)

# Tombol untuk menerapkan perubahan kontur
if st.button('Terapkan Perubahan Kontur'):
    # Terapkan perubahan kontur ke gambar default
    contoured_image = apply_contour(default_image, threshold)

    # Tampilkan gambar yang telah diubah kontur
    st.image(contoured_image, caption='Gambar Dengan Kontur', use_column_width=True)

st.write('------------------------------------------------------')
#--------------------------------------------------------------------------------------