import requests


class ChukJoke:
    """создание класса для полуения шуток Чака"""

    def __init__(self):
        """инициализация класса с дефортным значением категории шуток, для получения спика категорий шуток"""
        self.category = []

    def get_category_list(self):
        """метод получения категорий шуток Чака"""
        base_url = "https://api.chucknorris.io/jokes/categories"
        res = requests.get(base_url)
        assert 200 == res.status_code    # Проверям статус код ответа, если успешно выводим соответствующее сообщение
        print(f"{res.status_code} код ответа - Успешно, мы получили список категорий шуток Чака!!!")
        self.category = res.json()
        print("Список категорий шуток Чака:")
        print(*self.category, sep=', ')
        print('---' * 20)

    def get_joke_from_category(self):
        """метод получения рандомных шуток Чака из соответствующих категорий"""
        count = 0
        for category in self.category:
            base_url = "https://api.chucknorris.io/jokes/random?category=" + category
            res = requests.get(base_url)
            count += 1
            assert 200 == res.status_code  # Проверям статус код ответа, если успешно выводим соответствующее сообщение
            print(f"{count}) {res.status_code} код ответа - Успешно, мы получили шутку Чака из категории: {category}!!!")
            response = res.json()
            assert category.split() == response["categories"]  # проводим проверку соответствия категорий
            print(f'категория соответствует! {response["categories"]}')
            value = response["value"]
            name = "Chuck"
            if name in value:  # Проверям есть ли в шутке имя Чака
                print(value)
                print("Отлично, с нами Чак\n")
            else:
                print("Что-то пошло не так, имя Чак отсутствует в шутке...")


joke = ChukJoke()
joke.get_category_list()
joke.get_joke_from_category()
