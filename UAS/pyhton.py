import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path ke file gambar lokal
file_path = 'C:/Users/sabin/Downloads/New folder/image.jpeg'

# Membaca gambar dari file
image = cv2.imread(file_path)

# Periksa apakah gambar berhasil dibaca
if image is None:
    print("Gagal membaca gambar. Pastikan path gambar benar.")
else:
    # Mengubah gambar ke grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Menghitung Singular Value Decomposition (SVD)
    U, S, Vt = np.linalg.svd(gray_image, full_matrices=False)

    # Variance explained
    singular_values = S
    variance_explained = (singular_values ** 2) / np.sum(singular_values ** 2)

    # Cumulative variance explained
    cumulative_variance_explained = np.cumsum(variance_explained)

    # Rekonstruksi gambar dengan jumlah komponen yang berbeda
    def reconstruct_image(U, S, Vt, num_components):
        S_reduced = np.zeros_like(S)
        S_reduced[:num_components] = S[:num_components]
        return np.dot(U[:, :num_components] * S_reduced[:num_components], Vt[:num_components, :])

    # Jumlah komponen yang ingin ditampilkan
    num_components_list = [
3648, 1, 5, 10, 15, 20]

    # Menampilkan gambar asli, gambar rekonstruksi, dan variance explained
    plt.figure(figsize=(12, 6))

    # Menampilkan gambar asli
    plt.subplot(len(num_components_list) + 1, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Gambar Asli')
    plt.axis('off')

    for i, num_components in enumerate(num_components_list):
        # Rekonstruksi gambar
        reconstructed_image = reconstruct_image(U, S, Vt, num_components)
        
        # Variance explained untuk jumlah komponen yang digunakan
        variance_explained_by_components = np.sum(variance_explained[:num_components])
        
        # Menampilkan gambar rekonstruksi
        plt.subplot(len(num_components_list) + 1, 2, 2 * i + 3)
        plt.imshow(reconstructed_image, cmap='gray')
        plt.title(f'{num_components} Komponen\nVariance Explained: {variance_explained_by_components:.2f}')
        plt.axis('off')
        
        # Menampilkan grafik cumulative variance explained
        plt.subplot(len(num_components_list) + 1, 2, 2 * i + 4)
        plt.plot(cumulative_variance_explained, marker='o')
        plt.axvline(x=num_components-1, color='r', linestyle='--')
        plt.title(f'Variance Explained\nUp to {num_components} Components')
        plt.xlabel('Jumlah Singular Vectors')
        plt.ylabel('Variance Explained')
        plt.grid(True)

    plt.tight_layout()
    plt.show()
