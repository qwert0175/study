original_list = [1, 2, [100,200]]
copy_list = original_list[:]

copy_list[2][0] = 999
print(original_list)  # [1, 2, [999, 200]]