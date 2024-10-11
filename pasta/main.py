# Импортируем необходимые классы
from Pasta import Pasta  # Импортируем класс Pasta из файла pasta
from PastaController import PastaController
from PastaView import PastaView

if __name__ == "__main__":
    while True:
        action = input("Выберите действие: (1) Создать пасту, (2) Обновить пасту, (3) Выход: ")

        if action == "1":
            custom_pasta = Pasta.create_custom_pasta()  # Создаем заказ пасты
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
