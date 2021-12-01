
def calc_sum_of_three(index, array):
    return int(array[index]) + int(array[index + 1]) + int(array[index + 2])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("text.txt", "r")
    values = f.readlines()
    count = 0
    last_value = calc_sum_of_three(0, values)
    for i in range(len(values) - 2):
        new_val = calc_sum_of_three(i, values)
        if new_val > last_value:
            count = count + 1
        last_value = new_val

    print(count)
