
if __name__ == '__main__':
    f = open("text.txt", "r")
    values = f.readlines()
    count = 0
    last_value = int(values[0])
    for val in values:
        if int(val) > last_value:
            count = count + 1
        last_value = int(val)

    print(count)
