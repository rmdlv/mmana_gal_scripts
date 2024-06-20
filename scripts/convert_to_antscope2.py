input_filename = "input.csv"
output_filename = "output.csv"

with open(input_filename, encoding="utf8") as input_file:
    lines = input_file.readlines()[1:]

    with open(output_filename, "w+", encoding="utf8") as output_file:
        output_file.write("#Frequency(MHz);R;X\n")

        for line in lines:
            data = line.strip().split(",")

            output_file.write(f"{float(data[0]):.6f},{data[1]},{data[2]}\n")
