import math

table = {}

input_filename = input("input.csv")

with open(input_filename, encoding="utf8") as file:
    lines = file.readlines()[1:]
    for line in lines:
        data = line.strip().split(",")

        frequency = data[0]
        reactance = math.fabs(float(data[2]))

        if reactance not in table:
            table[reactance] = []

        table[reactance].append(frequency)

for index, value in enumerate(table[min(table)]):
    print(f"Resonance #{index+1}: {value}")
