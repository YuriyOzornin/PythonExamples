import calc_model

MENU_ITEMS = {
   "E": "Выход",
   "+": "a + b",
   "-": "a - b",
   "*": "a * b",
   "/": "a / b",
   "M": "M+ "
}


def print_memory():

    print(f"Число в памяти: {calc_model.memory}")


def menu():
    for index, item in MENU_ITEMS.items():
        print(f"{index}. {item}")

    print("Выберите пункт меню: ", end="")


def print_char(ch):
    print(f"Введите {ch}: ", end="")