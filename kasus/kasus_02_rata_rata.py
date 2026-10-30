def hitung_rata_rata(data):
    if not data:
        return None

    return sum(data) / len(data)


print(hitung_rata_rata([70, 80, 90]))
print(hitung_rata_rata([]))