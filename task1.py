def main():
    f1 = open("f1.txt", "w")
    f2 = open("f2.txt", "w")

    print("Введите данные, которые нужно записать в файл f1.")
    print("Для завершения ввода данных нажмите Enter дважды.")
    while True:
        data = input()
        if data == "":
            break
        f1.write(data + "\n")

    f1.close()
    f2.close()

    with open("f1.txt", "r") as f1:
        with open("f2.txt", "a") as f2:
            for line in f1:
                words = line.split()
                if len(words) == 1:
                    f2.write(words[0] + "\n")

    print("В файле два находятся строки: " + "\n")

    with open("f2.txt", "r") as f2:
        for line in f2:
            print(line)

    with open("f2.txt", "r") as f2:
        words = [word for line in f2 for word in line.split()]
        logest_word = max(words, key=len)

    print("Самое длинное слово в файле f2: ", logest_word)

if __name__ == "__main__":
    main()