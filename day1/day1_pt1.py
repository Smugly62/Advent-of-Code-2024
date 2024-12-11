def total_distance() -> int:
    f = open("day1_input.txt", "r")
    l = f.readlines()
    distance_dict = {}
    for i in l:
        pair = i.split('   ')
        distance_dict[int(pair[0])] = int(pair[1].strip('\n'))
    key = sorted(distance_dict.keys())
    values = sorted(distance_dict.values())
    print(key)
    print(values)
    n = 0
    distance = 0
    while n < len(key):
        x = abs(key[n] - values[n])
        distance += x
        n += 1
    return distance
print(total_distance())