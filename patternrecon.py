def is_sublist(sublist, main_list, position):
    return main_list[position:position + len(sublist)] == sublist


def find_reel(start_look_index = 0, array_look_limit = 3):
    data = []

    with open(r'C:\Users\sarantis\PycharmProjects\crashGameDistribution\reels\reel1_6.txt', 'r') as file:
        for line in file:
            number_list = [int(num) for num in line.strip().split(', ')]
            data.append(number_list)

    data = list(map(list, {tuple(lst): None for lst in data}))

    reel = [i for i in data[start_look_index]]
    data.pop(start_look_index)

    list_of_data = data


    for i in range(200):
        sublist_part = reel[len(reel) - 4: len(reel)]
        found = False
        array_look_len = 4
        while not found:

            sublist_part = reel[len(reel) - array_look_len: len(reel)]
            for index,  sub in enumerate(list_of_data):
                exists = is_sublist(sublist_part, sub, 0)
                if exists:
                    # print(sub , exists, sublist_part)
                    for found_value in sub[array_look_len - 5:]:
                        reel.append(found_value)

                    list_of_data.pop(index)

                    found = True
                    break


            array_look_len -= 1

            if array_look_len < array_look_limit:
                break

    print(len(reel))
    return reel
for i in range(40):

    array = find_reel(i ,3)
    print(f"Index: {i} Len: {len(array)}")

x = find_reel(0 ,3)
print(x, len(x))
