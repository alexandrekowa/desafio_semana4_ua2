with open("filmesranking.txt", "r") as file:
    lines = file.readlines()

formatted_lines = [",".join(line.split()) for line in lines]

with open("filmesranking.csv", "w") as file:
    file.write("\n".join(formatted_lines))
