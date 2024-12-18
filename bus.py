def greedy_rute(rute, biaya, awal, akhir):
    rute_terbaik = []
    waktu_tempuh = 0
    biaya_total = 0
    visited = [False] * len(rute)  # Menandai kota yang telah dikunjungi

    while awal != akhir:
        visited[awal] = True  # Tandai kota saat ini sebagai dikunjungi
        prioritas = []

        # Cari rute yang tersedia ke kota lain yang belum dikunjungi
        for i in range(len(rute)):
            if rute[awal][i] != 0 and not visited[i]:
                prioritas.append((rute[awal][i], biaya[awal][i], i))

        # Pilih rute dengan prioritas tertinggi (waktu minimum)
        prioritas.sort()
        waktu_tempuh += prioritas[0][0]
        biaya_total += prioritas[0][1]
        rute_terbaik.append((awal, prioritas[0][2]))
        awal = prioritas[0][2]  # Pindah ke kota berikutnya

    return rute_terbaik, waktu_tempuh, biaya_total

# Matriks Rute (A -> C -> B)
rute = [
    [0, 18, 12],  # Rute dari A ke C, B
    [18, 0, 15],  # Rute dari C ke A, B
    [12, 15, 0]   # Rute dari B ke A, C
]

# Matriks Biaya (A -> C -> B)
biaya = [
    [0, 6200, 4500],  # Biaya dari A ke C, B
    [6200, 0, 5200],  # Biaya dari C ke A, B
    [4500, 5200, 0]   # Biaya dari B ke A, C
]

awal = 0  # A
akhir = 2  # B

rute_terbaik, waktu_tempuh, biaya_total = greedy_rute(rute, biaya, awal, akhir)
print("Rute terbaik:", rute_terbaik)
print("Waktu tempuh:", waktu_tempuh)
print("Biaya total:", biaya_total)
