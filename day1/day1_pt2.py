def part_2() -> int:
    f = open("day1_input.txt", "r")
    l = f.readlines()
    distance_dict = {}
    for i in l:
        pair = i.split('   ')
        distance_dict[int(pair[0])] = int(pair[1].strip('\n'))
    key = distance_dict.keys()
    values = distance_dict.values()
    total = 0
    for i in key:
        count = 0
        for j in values:
            if i == j:
                count += 1
        x = i * count
        total += x
    return total
print(part_2())