import requests


class ChukJoke:
    """создание класса для полуения шуток Чака"""

    def __init__(self, category):
        """инициализация класса с дефортным значением категории шуток (для получения спика категорий шуток), аргументом
        вводимой пользователем категории и "флагом" при отсутствии которого шутка метод вызова шутки не вызывается"""
        self.category = category
        self.category_joke = []
        self.flag = True

    def get_category_list(self):
        """метод получения категорий шуток Чака"""
        base_url = "https://api.chucknorris.io/jokes/categories"
        res = requests.get(base_url)
        assert 200 == res.status_code  # Проверям статус код ответа, если успешно выводим соответствующее сообщение
        print(f"{res.status_code} код ответа - Успешно, мы получили список категорий шуток Чака!!!")
        self.category_joke = res.json()
        print("Список категорий шуток Чака:")
        print(*self.category_joke, sep=', ')
        print('---' * 20)

    def check_input_in_category(self):
        """медод валидации вводимой пользоватклкм категории шуток"""
        if self.category in self.category_joke:
            print("Ура, такая шутка есть у Чака!")
            print('---' * 20)
        else:
            print("Увы, на такую тему у Чака шуток нет(")
            print('---' * 20)
            self.flag = False  # Если введеной пользователем категории нет в списке шуток Чака, флаг переключается на False

    def get_joke_from_category(self):
        """метод получения рандомных шуток Чака из выбранной категорий"""
        if self.flag:  # если True то вызывается метод запроса шутки, иначе ничего не происходит
            base_url = "https://api.chucknorris.io/jokes/random?category=" + self.category
            res = requests.get(base_url)
            print(res.status_code)
            assert 200 == res.status_code  # Проверям статус код ответа, если успешно выводим соответствующее сообщение
            print(f"{res.status_code} код ответа - Успешно, мы получили шутку Чака из категории: {self.category}!!!")
            response = res.json()
            assert self.category.split() == response["categories"]  # проводим проверку соответствия категорий
            print(f'категория соответствует! {response["categories"]}')
            print('---' * 20)
            value = response["value"]
            name = "Chuck"
            if name in value:  # Проверям есть ли в шутке имя Чака
                print("Шутка: " + value)
                print('---' * 20)
                print("Отлично, с нами Чак\n")
            else:
                print("Что-то пошло не так, имя Чак отсутствует в шутке...")
                print('---' * 20)


print("На какую тему будет шутить Чак?")
category = input().lower()

joke = ChukJoke(category)
joke.get_category_list()
joke.check_input_in_category()
joke.get_joke_from_category()
