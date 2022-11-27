
from models import add_department, add_employees, del_emp_id, dell_all_emp, export_deparments_to_csv, export_employees_to_csv
from .ui_view import show_departments, show_employees, menu, show_employees_in_department, input_department, \
    input_emoployees

def exitProgram(_=None):
    exit()

MENU_ACTIONS = {
    1: ["Вывести список отделов", show_departments],
    2: ["Вывести список всех сотрудников", show_employees],
    3: ["Вывести список сотрудниеков отдела (по номеру)", show_employees_in_department],
    4: ["Добавить отдел", input_department, add_department],
    5: ["Добавить сотрудника", input_emoployees, add_employees],
    6: ["Уволить всех сотрудников?", dell_all_emp],
    7: ["Уволить сотрудника", del_emp_id],
    8: ["Экспорт отделов в csv", export_deparments_to_csv],
    9: ["Экспорт сотрудников в csv", export_employees_to_csv],
    0: ["Выход", exitProgram]
}


def main():
    menu_number = 1000000

    while menu_number:
        menu_number = menu()
        input_data = MENU_ACTIONS[menu_number][1]()
        if input_data:
            MENU_ACTIONS[menu_number][2](input_data)

