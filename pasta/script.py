import json
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

    def update_pasta(self, order_name, pasta, user_access_level):
        if user_access_level == "admin":
            Pasta.save_to_json(order_name, pasta)
            return f"Заказ '{order_name}' успешно обновлен."
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

    @staticmethod
    def update_pasta_view(order_name, pasta, user_access_level):
        if user_access_level == "admin":
            Pasta.save_to_json(order_name, pasta)
            print(f"Заказ '{order_name}' обновлен.")
        else:
            print("У вас недостаточно прав.")

if __name__ == "__main__":
    while True:
        action = input("Выберите действие: (1) Создать пасту, (2) Обновить пасту, (3) Выход: ")

        if action == "1":
            custom_pasta = Pasta.create_custom_pasta()
            order_name = input("Введите имя заказа: ")
            controller = PastaController()
            view = PastaView()
            controller.save_order_to_json(order_name, custom_pasta)
            view.save_order_to_json(order_name, custom_pasta)

        elif action == "2":
            order_name = input("Введите имя заказа для обновления: ")
            user_access_level = input("Введите уровень доступа (admin/user): ")
            if user_access_level == "admin":
                updated_pasta = Pasta.create_custom_pasta()  # Создаем новую пасту для обновления
                controller = PastaController()
                view = PastaView()
                result = controller.update_pasta(order_name, updated_pasta, user_access_level)
                view.update_pasta_view(order_name, updated_pasta, user_access_level)
                print(result)
            else:
                print("У вас недостаточно прав.")

        elif action == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
