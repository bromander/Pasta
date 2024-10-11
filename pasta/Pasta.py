import json
import os
from datetime import datetime

class Pasta:
    def __init__(self, type_of_pasta, sauce, cheese, *additional_ingredients):
        self._type_of_pasta = type_of_pasta
        self._sauce = sauce
        self._cheese = cheese
        self._additional_ingredients = list(additional_ingredients)

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

    def save_to_json(self, order_name, pasta):
        # Создаем директорию "orders", если она не существует
        directory = "orders"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Сохраняем файл в директорию "orders"
        file_path = os.path.join(directory, f"{order_name}.json")
        with open(file_path, "w") as json_file:
            json.dump(pasta.to_dict(), json_file)

    @staticmethod
    def load_from_json(order_name):
        # Загружаем файл из директории "orders"
        file_path = os.path.join("orders", f"{order_name}.json")
        with open(file_path, "r") as json_file:
            return json.load(json_file)
