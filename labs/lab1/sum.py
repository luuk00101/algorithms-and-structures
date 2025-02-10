sum_count = int(input())

number_pairs = []
for i in range(sum_count):
    line = input().split(" ")
    number_pairs.append((int(line[0]), int(line[1])))

for number_pair in number_pairs:
    print(number_pair[0] + number_pair[1])
