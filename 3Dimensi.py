import numpy as np

# Menggunakna matriks 4x4 untuk 3 Dimensi
def create_rotation(sudut: int, tipe: str = "yaw"): # Rotasi 3D terhadap Z-Axis
    rad = np.deg2rad(sudut)
    cos = np.cos(rad)
    sin = np.sin(rad)
    list_tipe = ["yaw", "pitch", "roll"]
    if tipe not in list_tipe:
        print("Tipe yang dimasukkan salah!")
        raise ValueError("Masukkan tipe yang benar!") # Akan mengembalikan error jika input tipe salah
    
    return np.array([ # Ini matriks yang merotasi terhadap Sumbu-Z
        [cos, -sin, 0, 0],
        [sin, cos,  0, 0],
        [0  , 0  ,  1, 0],
        [0  , 0  ,  0, 1]
    ]) if tipe == 'yaw' else np.array([
        [ cos, 0, sin, 0], # ini matriks rotasi terhadap Sumbu-Y
        [ 0  , 1, 0  , 0],
        [-sin, 0, cos, 0],
        [ 0  , 0, 0  , 1]
    ]) if tipe == 'pitch' else np.array([
        [1, 0   , 0  , 0], # Ini matriks rotasi terhadap Sumbu-X
        [0, cos , -sin, 0],
        [0, sin, cos, 0],
        [0, 0   , 0  , 1]
    ])

def create_translation(panjang, y=0, z=0): # Translasi matriks di 3D
    return np.array([
        [1, 0, 0, panjang],
        [0, 1, 0, y      ], # y dan z = 0, standar untuk robotika sederhana
        [0, 0, 1, z      ],
        [0, 0, 0, 1      ]
    ])

# Fungsi transformasi matrix dengan mengalikan matriks rotasi dengan translasi
def create_transform(panjang:int, sudut: int, tipe: str = 'yaw'): 
    rotation = create_rotation(sudut, tipe)
    translation = create_translation(panjang)
    return rotation @ translation

# Inisialisasi angka
a1 = 56; a2 = 65 # Panjang lengan
q1 = 40; q2 = 30 # Besar sudut (dalam derajat)

# Ini tambahan DoF
a3 = 20; q3 = -15 # Penambahan DoF ketiga
a4 = 400; q4 = -55 # Penambahan DoF keempat

T0_1 = create_transform(a1, q1) # Melakukan transformasi matriks pada lengan 1
T1_2 = create_transform(a2, q2) # Melakukan transformasi matriks pada lengan 2
T2_3 = create_transform(a3, q3, 'pitch') # Melakukan transformasi matriks pada lengan 3 terhadap Sumbu-Y
T3_4 = create_transform(a4, q4, 'roll') # Melakukan transformasi matriks pada lengan 4 terhadap Sumbu-X

T0_4 = T0_1 @ T1_2 @ T2_3 @ T3_4
x_akhir = T0_4[0, 3]
y_akhir = T0_4[1, 3]
z_akhir = T0_4[2, 3]

print(f"Matriks total: \n{T0_4}\n")
print(f"Koordinat lengan terakhir: \nX = {x_akhir}\nY = {y_akhir}\nZ = {z_akhir}")
