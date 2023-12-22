import pyperclip
import time

copied_items = []
zero_all_list = []
one_all_list = []

previous_clipboard = None
while True:
    current_clipboard = pyperclip.paste()
    if current_clipboard != previous_clipboard:
        copied_items.append(current_clipboard)
        previous_clipboard = current_clipboard

        reel_value = current_clipboard.split("reel_set=")[1].split()[0][0]
        values = current_clipboard.split("&s=")[1].split()[0][:-7].split(",")

        a = previous_clipboard.split(",")
        larger_list = []
        for i in range(6):
            mini_list = []
            for k in range(5):
                mini_list.append(values[i + (k*6)])

            larger_list.append(mini_list)

        files = [["reel0_1.txt","reel0_2.txt","reel0_3.txt","reel0_4.txt","reel0_5.txt","reel0_6.txt",],
                 ["reel1_1.txt","reel1_2.txt","reel1_3.txt","reel1_4.txt","reel1_5.txt","reel1_6.txt",]]

        with open(rf'C:\Users\sarantis\PycharmProjects\crashGameDistribution\reels\responses.txt',
                  'a') as file:
            file.write(current_clipboard + ',\n')


        for i, sub_list in enumerate(larger_list):
            with open(rf'C:\Users\sarantis\PycharmProjects\crashGameDistribution\reels\reel{reel_value}_{i+1}.txt', 'a') as file:
                    file.write(', '.join(map(str, larger_list[i])) + '\n')


        print("Items added to: File ", reel_value )
        print(f"New item added: {current_clipboard} \n\n")






    time.sleep(1)  # Check clipboard every 1 second


#
# a = {}
# x = 0
# for i in base_game:
#     if i not in a.keys():
#         a[i] = 1
#     else:
#         a[i] += 1
#
#     if i != 0 and i != 1:
#         x += 1
#
# for v in sorted(a.keys()):
#      if v != 0 and v != 1:
#
#           print(v, " ",a[v], a[v]/x)
#
# print(a)
# print(x)