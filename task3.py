def main():
    subjects = {}
    with open("Занятия.txt", "r", encoding="utf-8") as f:
        for line in f:
            subject, lectures, practices, labs = line.split()
            subjects[subject] = int(lectures) + int(practices) + int(labs)

    print(subjects)

if __name__ == "__main__":
    main()