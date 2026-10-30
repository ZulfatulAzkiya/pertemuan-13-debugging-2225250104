def status_lulus(nilai, batas=60):
    if not 0 <= nilai <= 100:
        return "Nilai tidak valid"

    return "Lulus" if nilai >= batas else "Belum lulus"


test_cases = [
    (80, "Lulus"),
    (60, "Lulus"),
    (59, "Belum lulus"),
    (0, "Belum lulus"),
    (101, "Nilai tidak valid"),
]

for nilai, expected in test_cases:
    actual = status_lulus(nilai)

    status = "PASS" if actual == expected else "FAIL"

    print(
        f"nilai={nilai}: expected={expected}, "
        f"actual={actual} [{status}]"
    )