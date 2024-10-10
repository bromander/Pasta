import json
from datetime import datetime


class Pasta:
    def __init__(self, type_of_pasta, sauce, cheese, *additional_ingredients):
        self._type_of_pasta = type_of_pasta
        self._sauce = sauce
        self._cheese = cheese
        self._additional_ingredients = list(additional_ingredients)

    # Геттеры и сеттеры (не изменились)

    def __str__(self):
        return f"Паста: {self._type_of_pasta}, Соус: {self._sauce}, Сыр: {self._cheese}, Дополнительные ингредиенты: {', '.join(self._additional_ingredients)}"

    def to_dict(self):
        return {
            "type_of_pasta": self._type_of_pasta,
            "sauce": self._sauce,
            "cheese": self._cheese,
            "additional_ingredients": self._additional_ingredients,
            "order_time": datetime.now().isoformat()
        }

    @classmethod
    def create_custom_pasta(cls):
        type_of_pasta = input("Введите тип пасты: ")
        sauce = input("Введите соус: ")
        cheese = input("Введите сыр: ")
        additional_ingredients = input("Введите дополнительные ингредиенты (через запятую): ").split(",")
        return cls(type_of_pasta, sauce, cheese, *additional_ingredients)

    @staticmethod
    def save_to_json(order_name, pasta):
        with open(f"{order_name}.json", "w") as json_file:
            json.dump(pasta.to_dict(), json_file)

    @staticmethod
    def load_from_json(order_name):
        with open(order_name, "r") as json_file:
            return json.load(json_file)

class PastaController:
    def save_order_to_json(self, order_name, pasta):
        Pasta.save_to_json(order_name, pasta)

    def get_data_from_json(self, order_name, user_access_level):
        if user_access_level == "admin":
            return Pasta.load_from_json(order_name)
        else:
            return "Доступ запрещен"
class PastaView:
    @staticmethod
    def save_order_to_json(order_name, pasta):
        Pasta.save_to_json(order_name, pasta)
        print(f"Файл '{order_name}.json' успешно сохранен.")

    @staticmethod
    def get_data_from_json(order_name, user_access_level):
        if user_access_level == "admin":
            data = Pasta.load_from_json(order_name)
            print(f"Данные из файла '{order_name}.json': {data}")
        else:
            print("У вас недостаточно прав.")


if __name__ == "__main__":
    custom_pasta = Pasta.create_custom_pasta()
    order_name = input("Введите имя заказа: ")

    # Сохранение заказа в JSON
    controller = PastaController()
    view = PastaView()
    controller.save_order_to_json(order_name, custom_pasta)
    view.save_order_to_json(order_name, custom_pasta)

    # Чтение данных из JSON
    user_access_level = input("Введите уровень доступа (admin/user): ")
    view.get_data_from_json(order_name, user_access_level)

