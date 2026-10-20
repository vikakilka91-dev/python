
import os
import sys
import platform


def main():
    # Сохраняем результаты работы системных библиотек
    results = []

    results.append(("Операционная система", os.name))
    results.append(("Платформа", platform.platform()))
    results.append(("Имя ОС", platform.system()))
    results.append(("Версия ОС", platform.version()))
    results.append(("Архитектура", platform.architecture()[0]))
    results.append(("Версия Python", sys.version))
    results.append(("Количество процессоров", os.cpu_count()))
    results.append(("Текущая папка", os.getcwd()))
    results.append(("Путь к Python", sys.executable))
    results.append(("Имя компьютера", platform.node()))

    while True:
        # Меню программы
        print("\n===== ДИАГНОСТИКА СИСТЕМЫ =====")
        print("1. Показать все характеристики")
        print("2. Показать одну характеристику")
        print("3. Показать список характеристик")
        print("4. Выход")

        sys.stdout.write("Выберите пункт меню: ")
        sys.stdout.flush()

        choice = sys.stdin.readline().strip()

        if choice == "1":
            for index, item in enumerate(results):
                print(f"{index}. {item[0]}: {item[1]}")

        elif choice == "2":
            print("\nСписок характеристик:")
            for index, item in enumerate(results):
                print(f"{index}. {item[0]}")

            sys.stdout.write("Введите индекс характеристики: ")
            sys.stdout.flush()
            value = sys.stdin.readline().strip()

            if value.isdigit():
                index = int(value)
                if 0 <= index < len(results):
                    print(f"{results[index][0]}: {results[index][1]}")
                else:
                    print("Ошибка: такого индекса нет.")
            else:
                print("Ошибка: введите целое число.")

        elif choice == "3":
            print("\nСписок сохранённых характеристик:")
            for index, item in enumerate(results):
                print(f"{index}. {item[0]}")

        elif choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Неверный пункт меню. Попробуйте снова.")


if __name__ == "__main__":
    main()
