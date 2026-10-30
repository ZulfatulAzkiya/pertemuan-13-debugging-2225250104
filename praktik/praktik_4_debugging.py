def status_lulus(nilai, batas=60):
    if not 0 <= nilai <= 100:
        return "Nilai tidak valid"

    return "Lulus" if nilai >= batas else "Belum lulus"


def jalankan_test():
    kasus = [
        (85, "Lulus"),
        (60, "Lulus"),
        (59, "Belum lulus"),
        (0, "Belum lulus"),
        (101, "Nilai tidak valid"),
    ]

    semua_lulus = True

    for nilai, expected in kasus:
        actual = status_lulus(nilai)
        ok = actual == expected
        semua_lulus = semua_lulus and ok

        hasil = "PASS" if ok else "FAIL"

        print(
            f"{nilai}: expected={expected}; "
            f"actual={actual}; {hasil}"
        )

    if semua_lulus:
        print("Semua test PASS.")
    else:
        print("Ada test yang gagal.")


if __name__ == "__main__":
    jalankan_test()