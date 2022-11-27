
import csv




employees = [
    {"id": 1, "fio": "ivan petrov", "salary": 40},
    {"id": 2, "fio": "bob ivanov", "salary": 50},
    {"id": 3, "fio": "john don", "salary": 100}
]
field_name_e = ["id", "fio", "salary"]

departments = [
    {"id": 10, "name": "accounting", "employees": [2, 1]},
    {"id": 11, "name": "marketing", "employees": [3]}
]
field_name = ["id", "name", "employees"]

def add_department(name):
    # TODO: найти максимальный номер отдела и увеличить на 1
    departments.append({
        "id": departments[-1]["id"] + 1,
        "name": name,
        "employees": []
    })


def add_employees(fio):
    employees.append(dict(id=employees[-1]["id"] + 1, fio=fio, salary=100))

def export_deparments_to_csv():
    filename = "dept.csv"
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=field_name)
        writer.writeheader()
        for row in departments:
            writer.writerow(row)

def export_employees_to_csv():
    filename = "empl.csv"
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=field_name_e)
        writer.writeheader()
        for row in employees:
            writer.writerow(row)


def del_emp_id():
    del_id = input("Введите id увольняемого сотрудника: ")
    d_id = int(del_id)
    employees[:] = [d for d in employees if d.get('id') != d_id]
    print(employees)

def dell_all_emp():
    del_all = input("Уволить всех? если да нажмите любую цифру: ")
    d_all = int(del_all)
    employees.clear()
    print(employees)