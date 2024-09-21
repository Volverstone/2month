movies = {
    "Jango Unchained": {
        "John": 10,
        "Jack":9
    },
    "Troy":{}
}
def add_film(add_mov = input("add the name of movie").lower().title()):
    if add_mov not in movies:
        print("Movie added sucessfully")
        movies.update({add_mov:None})
    else:
        print("Movie already exist")
def add_rate(add_rate = input("add film which you will rated:")):
    if add_rate in movies:
        name = input("add your name:")
        rate = int(input("add your rate for film:"))
        #дальше не получилось добавить ключ значение
    else:
        print("this movie already exist")