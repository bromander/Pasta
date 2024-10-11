from pasta import Pasta

class PastaView:
    @staticmethod
    def save_order_to_json(order_name, pasta):
        # Вызов метода save_to_json через объект pasta
        pasta.save_to_json(order_name, pasta)
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
            pasta.save_to_json(order_name, pasta)
            print(f"Заказ '{order_name}' обновлен.")
        else:
            print("У вас недостаточно прав.")
