full_name = input("ФИО: ")
counter = 0
i = 0
print('Инициалы: ', end='')
while (i < len(full_name)):
    while (i < len(full_name) and full_name[i] == ' '):
        i += 1
    if (i < len(full_name)):
        print(full_name[i], end='')
        while (i < len(full_name) and full_name[i] != ' '):
            i += 1
            counter += 1
    i += 1
print('.')
print(f"Длина (символов): {counter + 2}")


