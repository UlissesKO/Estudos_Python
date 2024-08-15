with open("Dados\Arquivos\salary.csv", "r") as arq:
    data = arq.read()
    data = data.split("\n")
    final_data = []

    for i in data:
        split_row = i.split(",")
        final_data.append(split_row)

print(final_data[0])