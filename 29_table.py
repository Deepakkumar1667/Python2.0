def genreateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/tabel_{n}.txt", "w") as f:
        f.write(table)


for i in range(1, 21):
    genreateTable(i)