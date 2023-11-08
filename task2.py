def main():

    movies = {}

    with open("Кинотеатр.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, date, price, viewers = line.split('  ')
            movies[date] = movies.get(date, []) + [(name, int(price), int(viewers))]

    date = input("Введите дату: ")

    if date in movies:
        for name, price, viewers in movies[date]:
            print(f"{name} ({date}): {price} руб., {viewers} зрителей")
    else:
        print(f"В указанную дату нет сеансов.")

    most_visited_movie = max(movies.values(), key=lambda x: sum(x[2] for x in x))

    for name, price, viewers in most_visited_movie:
        print(f"Самый посещаемый фильм: {name} ({date}): {price} руб., {viewers} зрителей")

if __name__ == "__main__":
    main()