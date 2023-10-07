# import disini
import os
import numpy as np
import math


# Buat function hitung Mean
def hitung_mean(data, jumlahData):
    os.system("clear")
    # Jumlah semua data
    total = sum(data)
    mean = total / jumlahData
    print("\n--------")
    print("| Mean |")
    print("--------")
    print(f"Rata-Ratanya adalah : {mean}")
    return mean  # Masukkan rumus menghitung Mean


# Buat function hitung Median
def hitung_median(data, jumlahData):
    os.system("clear")
    # Mengurutkan data
    data.sort()

    # Jika jumlah data genap
    if jumlahData % 2 == 0:
        # Mengambil dua nilai tengah
        median1 = data[jumlahData // 2]
        median2 = data[jumlahData // 2 - 1]
        # Menghitung rata-rata dari dua nilai tengah
        median = (median1 + median2) / 2
    else:
        # Jika jumlah data ganjil, ambil nilai tengah langsung
        median = data[jumlahData // 2]

    # Mencetak nilai median
    print("\n----------")
    print("| Median |")
    print("----------")
    print(f"Median dari data adalah : {median}")

    # Mengembalikan nilai median
    return median


# Buat function hitung Kuartil data tunggal
def hitung_kuartil(data, jumlahData):
    os.system("clear")
    # Mengurutkan data
    data.sort()

    # Menghitung posisi kuartil
    Q1_pos = 1 + (jumlahData - 1) * 0.25
    Q2_pos = 1 + (jumlahData - 1) * 0.5
    Q3_pos = 1 + (jumlahData - 1) * 0.75

    # Mengambil nilai kuartil
    Q1 = data[int(Q1_pos) - 1] + (Q1_pos - int(Q1_pos)) * (
        data[int(Q1_pos)] - data[int(Q1_pos) - 1]
    )
    Q2 = data[int(Q2_pos) - 1] + (Q2_pos - int(Q2_pos)) * (
        data[int(Q2_pos)] - data[int(Q2_pos) - 1]
    )
    Q3 = data[int(Q3_pos) - 1] + (Q3_pos - int(Q3_pos)) * (
        data[int(Q3_pos)] - data[int(Q3_pos) - 1]
    )

    # Mencetak nilai kuartil
    print("\n-----------")
    print("| Kuartil |")
    print("-----------")
    print("Kuartil pertama (Q1) dari data adalah : ", Q1)
    print("Kuartil kedua (Q2) atau median dari data adalah : ", Q2)
    print("Kuartil ketiga (Q3) dari data adalah : ", Q3)

    # Mengembalikan nilai kuartil
    return Q1, Q2, Q3


# Buat function hitung Modus data tunggal
def hitung_modus(data, jumlahData):
    os.system("clear")
    frekuensi = {}

    for elemen in data:
        if elemen in frekuensi:
            frekuensi[elemen] += 1
        else:
            frekuensi[elemen] = 1

    modus = []
    max_frekuensi = max(frekuensi.values())

    for k, v in frekuensi.items():
        if v == max_frekuensi:
            modus.append(k)

    # Mencetak nilai modus
    print("\n---------")
    print("| Modus |")
    print("---------")
    print("Modus dari data adalah : ", modus)

    return modus


# Buat function hitung Persentil data tunggal
def hitung_persentil(data, jumlahData):
    os.system("clear")
    print("\n------------")
    print("| Persentil |")
    print("------------")
    p = int(input("Masukkan nilai P untuk persentil yang ingin dihitung : "))
    data.sort()

    if 0 < p < 100:
        index = (p / 100) * (jumlahData - 1)
        if index.is_integer():
            persentil = data[int(index)]
        else:
            lower_index = int(index)
            upper_index = lower_index + 1
            lower_value = data[lower_index]
            upper_value = data[upper_index]
            persentil = lower_value + (index - lower_index) * (
                upper_value - lower_value
            )

        print(f"Persentil ke-{p}% adalah {persentil}")
    else:
        print(
            "Pilihan persentil tidak valid. Persentil harus berada dalam rentang 1 hingga 99."
        )


# Buat function hitung Desil data tunggal
def hitung_desil(data, jumlahData):
    os.system("clear")
    print("\n---------")
    print("| Desil |")
    print("---------")
    D = int(input("Masukkan nilai D untuk desil yang ingin dihitung : "))
    # Mengurutkan data
    data.sort()

    indeks_desil = (D / 10) * jumlahData
    if indeks_desil.is_integer():
        desil = (data[int(indeks_desil)] + data[int(indeks_desil) - 1]) / 2
    else:
        desil = data[int(indeks_desil)]

    # Mencetak nilai Desil

    print(f"Desil ke-{D} dari data adalah : {desil}")

    return desil


# Buat function hitung Jangkauan data tunggal
def hitung_jangkauan(data, jumlahData):
    os.system("clear")
    # Mengurutkan data
    data.sort()

    # Menghitung jangkauan
    jangkauan = data[-1] - data[0]

    # Mencetak nilai jangkauan
    print("\n-------------")
    print("| Jangkauan |")
    print("-------------")
    print("Jangkauan dari data adalah : ", jangkauan)

    return jangkauan


# Buat function Varian data tunggal
def hitung_varian(data, jumlahData):
    os.system("clear")
    # Menghitung rata-rata
    rata_rata = sum(data) / jumlahData
    # Menghitung varian
    varian = sum((x - rata_rata) ** 2 for x in data) / jumlahData

    # Mencetak varian
    print("Varian data tersebut adalah:", varian)


# Buat function Standar Deviasi
def hitung_standar_deviasi(data, jumlahData):
    os.system("clear")
    if jumlahData < 2:
        print(
            "Data harus memiliki setidaknya 2 angka untuk menghitung standar deviasi."
        )
        return None

    rata_rata = sum(data) / jumlahData
    selisih_kuadrat = [(x - rata_rata) ** 2 for x in data]
    varian = sum(selisih_kuadrat) / (jumlahData - 1)
    standar_deviasi = varian**0.5

    print("\n-------------------")
    print("| Standar Deviasi |")
    print("-------------------")
    print(f"Standar Deviasi: {standar_deviasi}")
    return standar_deviasi


# Buat function Box Plot Data Tunggal
def hitung_box_plot(data, jumlahData):
    os.system("clear")
    if jumlahData < 4:
        print("Data harus memiliki setidaknya 4 angka untuk menghitung box plot.")
        return None

    data.sort()  # Urutkan data terlebih dahulu

    # Hitung median
    if jumlahData % 2 == 0:
        median1 = data[jumlahData // 2 - 1]
        median2 = data[jumlahData // 2]
        median = (median1 + median2) / 2
    else:
        median = data[jumlahData // 2]

    # Hitung kuartil
    kuartil1 = data[jumlahData // 4]
    kuartil3 = data[3 * jumlahData // 4]

    # Hitung rentang interkuartil
    interkuartil_range = kuartil3 - kuartil1

    # Hitung batas outlier
    lower_bound = kuartil1 - 1.5 * interkuartil_range
    upper_bound = kuartil3 + 1.5 * interkuartil_range

    # Cetak hasil box plot
    print("\n------------")
    print("| Box Plot |")
    print("------------")
    print(f"Box Plot:")
    print(f"Q1 (Kuartil 1): {kuartil1}")
    print(f"Median: {median}")
    print(f"Q3 (Kuartil 3): {kuartil3}")
    print(f"Rentang Interkuartil: {interkuartil_range}")
    print(f"Lower Bound (Batas Bawah Outlier): {lower_bound}")
    print(f"Upper Bound (Batas Atas Outlier): {upper_bound}")

    # Cek dan cetak data outlier
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    if outliers:
        print(f"Data Outlier: {outliers}")

    return median, kuartil1, kuartil3, interkuartil_range, lower_bound, upper_bound


# Fungsi untuk menghitung skewness dari data
def hitung_skewness(data, jumlahData):
    os.system("clear")
    rata_rata = sum(data) / jumlahData

    jumlah_pangkat_tiga = sum([(x - rata_rata) ** 3 for x in data])
    standar_deviasi = math.sqrt(
        sum([(x - rata_rata) ** 2 for x in data]) / (jumlahData - 1)
    )

    skewness = jumlah_pangkat_tiga / (jumlahData * standar_deviasi**3)
    print("\n-------------")
    print("| Skewwness |")
    print("-------------")
    print(f"Skewness dari data adalah: {skewness}")
    return skewness


# Buat function Kurtosis data tunggal
def hitung_kurtosis(data, jumlahData):
    os.system("clear")
    if jumlahData < 4:
        return "Data tidak cukup untuk menghitung kurtosis"

    mean = sum(data) / jumlahData
    variance = sum((x - mean) ** 2 for x in data) / (jumlahData - 1)

    # Menambahkan pengecekan varians nol
    if variance == 0:
        return "Varians data adalah nol, tidak dapat menghitung kurtosis."

    kurtosis = sum((x - mean) ** 4 for x in data) / (jumlahData * variance**2)

    if kurtosis < 3:
        jenis_kurtosis = "platykurtik (datar)"
    elif kurtosis > 3:
        jenis_kurtosis = "leptokurtik (tajam)"
    else:
        jenis_kurtosis = "mesokurtik (normal)"

    # Menambahkan pernyataan print di dalam fungsi
    print("\n------------")
    print("| Kurtosis |")
    print("------------")
    print(f"Kurtosis data: {kurtosis}")
    print(f"Jenis kurtosis: {jenis_kurtosis}")


# Buat inputan jumlah data
print("\n---------------------------------------")
print("| Program Menghitung Rumus Statistika |")
print("---------------------------------------\n")
while True:
    jumlahData = int(input("Berapa jumlah data yang akan dimasukkan: "))
    deret = input("Masukkan deret bilangan (pisahkan dengan koma): ")
    data = deret.split(",")

    if len(data) != jumlahData:
        print(
            f"Panjang deret harus sama dengan jumlah data yang diminta ({jumlahData}). Coba lagi."
        )
    else:
        data = [int(x) for x in data]
        break  # Keluar dari loop jika input sesuai

while True:
    print(f"\nData :{data} \n")
    userInput = int(
        input(
            "\nDashboard : \n\n1. Menghitung Mean\n2. Mencari Median\n3. Menghitung Modus\n4. Menghitung Jangkauan\n"
            "5. Menghitung Kuartil\n6. Menghitung Varian\n7. Menghitung Deviasi Standar\n8. Menghitung skewness\n9. Menghitung Kurtosis\n"
            "10. Menghitung Persentil\n11. Menghitung Boxplot\n12. Menghitung Desil\n\n99. Exit\n\n Masukkan pilihan nomor : "
        )
    )

    match userInput:
        case 1:
            hitung_mean(data, jumlahData)
        case 2:
            hitung_median(data, jumlahData)
        case 3:
            hitung_modus(data, jumlahData)
        case 4:
            hitung_jangkauan(data, jumlahData)
        case 5:
            hitung_kuartil(data, jumlahData)
        case 6:
            hitung_varian(data, jumlahData)
        case 7:
            hitung_standar_deviasi(data, jumlahData)
        case 8:
            hitung_skewness(data, jumlahData)
        case 9:
            hitung_kurtosis(data, jumlahData)
        case 10:
            hitung_persentil(data, jumlahData)
        case 11:
            hitung_box_plot(data, jumlahData)
        case 12:
            hitung_desil(data, jumlahData)
        case 99:
            os.system("clear")
            print("Terima kasih")
            break
        case _:
            print("Menu tidak tersedia. silahkan masukan nomor yang tersedia!")
