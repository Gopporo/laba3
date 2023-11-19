subjects = {}


def count(str):
    sum = 0
    number = ""
    c = 0
    for i in range(len(str) - 1):
        number = ""
        if (str[c].isdigit()):
            number += str[c]
            cou = c + 1
            while (str[cou].isdigit()):
                number += str[cou]
                cou += 1

            sum += int(number)
        if (len(number) == 0):
            c += 1
        else:
            c += len(number)

        if (c >= len(str)):
            break
        print(number)

    return sum


with open("Занятия.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.split(":")

        subject = parts[0].strip()

        summa = count(parts[1])

        subjects[subject] = summa

print(subjects)