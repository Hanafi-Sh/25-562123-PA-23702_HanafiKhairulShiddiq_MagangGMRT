import numpy as np

# Fungsi transformasi matrix
def create_transform(panjang: int, sudut: int):
    radian = np.deg2rad(sudut) # Mengubah sudut dalam derajat ke radian agar bisa dioperasikan oleh library numpy
    cos = np.cos(radian) # Inisialisasi cos theta
    sin = np.sin(radian) # Inisialisasi sin theta

    matrix = np.array([ # Ini adalah matrix transformasi T(theta, a) = H rotasi * H translasi, seperti yang dijelaskan dalam pdf
        [cos, -sin, panjang * cos],
        [sin,  cos, panjang * sin],
        [  0,    0,         1    ]
    ])
    return matrix # Mengembalikan matrix ketika pemanggilan fungsi

# Inisialisasi angka
a1 = 56; a2 = 65 # Panjang lengan
q1 = 40; q2 = 30 # Besar sudut (dalam derajat)

# Ini tambahan DoF
a3 = 20; q3 = -15 # Penambahan DoF ketiga
a4 = 400; q4 = -55 # Penambahan DoF keempat

T0_1 = create_transform(a1, q1) # Melakukan fungsi transformasi untuk mendapatkan matrix T0_1
T1_2 = create_transform(a2, q2) # Melakukan fungsi transformasi untuk mendapatkan matrix T1_2

T0_2 = T0_1 @ T1_2 # Perkalian matrix untuk mendapatkan matrix akhir T0_2 atau sama dengan H0_4

x_akhir2 = T0_2[0, 2] # Mengambil koordinat x yang berada di baris 0 kolom 2
y_akhir2 = T0_2[1, 2] # Mengambil koordinat y yang berada di baris 1 kolom 2
print(f"Matriks akhir T0_2: \n{T0_2}\n") # Siapa sih yang ga paham baris ini
print(f"Titik akhir lengan kedua berada di koordinat: \nx = {x_akhir2} \ny = {y_akhir2}\n\n") # Yang ini juga

# ------------ Tambahan DoF ----------------
T2_3 = create_transform(a3, q3)
T3_4 = create_transform(a4, q4)
T0_4 = T0_2 @ T2_3 @ T3_4

x_akhir4 = T0_4[0, 2] # Mengambil koordinat x yang berada di baris 0 kolom 2
y_akhir4 = T0_4[1, 2] # Mengambil koordinat y yang berada di baris 1 kolom 2
print(f"Matriks akhir T0_2: \n{T0_4}\n") 
print(f"Titik akhir lengan keempat berada di koordinat: \nx = {x_akhir4} \ny = {y_akhir4}")
