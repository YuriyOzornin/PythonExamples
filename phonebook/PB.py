# приветственное слово 
print( "WELCOME TO THE PHONEBOOK DIRECTORY") 
 
# создание .txt file  
filename = "myphonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 
 
# главное меню 
def main_menu(): 
    print( "\nГЛАВНОЕ МЕНЮ\n") 
    print( "1. Показать все существующие контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Найти существующий контакт") 
    print( "4. Выход") 
    choice = input("Выберите пункт меню: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "Этого контакта нет в телефонной книге") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter для продолжения ...") 
        main_menu() 
    elif choice == "4": 
        print("Спасибо за использование телефонной книги!") 
    else: 
        print( "Пожалуйста, введите существующие данные!\n") 
        enter = input( "Нажмите Enter для продолжения ...") 
        main_menu() 
 
# defining search function         
def searchcontact(): 
    searchname = input( "Введите фамилию для поиска контактных данных: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Ваш запрос по контакту:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "Такого контакта несуществует", searchname) 
 
# first name 
def input_firstname(): 
    first = input( "Введите фамилию: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# last name 
def input_lastname(): 
    last = input( "Введите имя: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# storing the new contact details 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    emailID = input( "Введите E-mail Address: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Контактные данные:\n " + contactDetails + "\nбыли успешно сохранены!") 
 
main_menu() 
