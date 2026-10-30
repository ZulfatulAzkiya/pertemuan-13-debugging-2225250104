try:
    with open("data/nilai.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("File nilai.txt tidak ditemukan.")