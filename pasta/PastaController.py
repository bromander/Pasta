from pasta import Pasta

class PastaController:
    def save_order_to_json(self, order_name, pasta):
        # Правильный вызов статического метода
        pasta.save_to_json(order_name, pasta)

    def get_data_from_json(self, order_name, user_access_level):
        if user_access_level == "admin":
            return Pasta.load_from_json(order_name)
        else:
            return "Доступ запрещен"

    def update_pasta(self, order_name, pasta, user_access_level):
        if user_access_level == "admin":
            pasta.save_to_json(order_name, pasta)
            return f"Заказ '{order_name}' успешно обновлен."
        else:
            return "Доступ запрещен"
