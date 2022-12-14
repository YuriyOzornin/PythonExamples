import json

# Список словарей контактов. Каждый словарь содержит ключи, соответствующие полям контакта (name и phone) и соотв. значения
phonebookData = []

# Формирование списка строк для экспорта в текстовом формате
# indList - список индексов в phonebookData
def txtExp (indList):
    expList = []
    for cInd in indList:
        expList.append(phonebookData[cInd]["name"])
        expList.append(phonebookData[cInd]["phone"])
        expList.append("")
    return expList


def csvExp (indList):
    expList = []
    for cInd in indList:
        expList.append(phonebookData[cInd]["name"] + ";" + phonebookData[cInd]["phone"])
    return expList


def jsonExp (indList):
    return [json.dumps(getContList(indList), indent=4)]


# Импорт из списка строк в текстовом формате: имена и тел. на отдельных строках, между контактами пустая строка
# Функции импорта перезаписывают сущствующие контакты с такими же именами
def txtImp (sList):
    while len(sList) >= 3:
        if sList[0] != "":
            if not isPhone(sList[1]):
                return -1
            if len(cList := findContacts(sList[0], strong=True)) > 0:
                phonebookData[cList[0]]["name"] = sList[0]
                phonebookData[cList[0]]["phone"] = sList[1]
            else:
                phonebookData.append({"name": sList[0], "phone": sList[1]})
        sList = sList[3:]
    return 0


def csvImp (sList):
    for contStr in sList:
        if contStr != "":
            contact = contStr.split(";")
            if len(contact) <= 1 or not isPhone(contact[1]):
                return -1
            if len(cList := findContacts(contact[0], strong=True)) > 0:
                phonebookData[cList[0]]["name"] = contact[0]
                phonebookData[cList[0]]["phone"] = contact[1]
            else:
                phonebookData.append({"name": contact[0], "phone": contact[1]})
    return 0


def jsonImp (sList):
    contStr = "".join(sList)
    contList = json.loads(contStr)
    for contact in contList:
        if not isPhone(contact["phone"]):
                return -1
        if len(cList := findContacts(contact["name"], strong=True)) > 0:
            phonebookData[cList[0]] = contact
        else:
            phonebookData.append(contact)
    return 0


EXP_FUNCS = {
    "txt": txtExp,
    "csv": csvExp,
    "json": jsonExp,
}


IMP_FUNCS = {
    "txt": txtImp,
    "csv": csvImp,
    "json": jsonImp,
}


# Определяет, является ли строка номером телефона
def isPhone(phoneStr):
    return not bool(len(list(filter(lambda ch: ch not in "+() 0123456789", phoneStr))))


# Формирует список индексов контактов в phonebookData, на основе строки, в которой должно содержаться имя или часть имени контакта
# strong - булевый флаг, True - ищет только полное соответствие в именах, False - вхождение
def findContacts (nameStr, strong=False):
    resList = []
    for ind, contact in enumerate(phonebookData):
        if not strong and nameStr in contact["name"] or strong and nameStr == contact["name"]:
            resList.append(ind)

    return resList


# Возвращает список контактов по списку индексов из phonebookData
def getContList (indList):
    return [phonebookData[ind] for ind in indList]


# Добавляет пустой контакт перед заполнением нового контакта
def addContact ():
    global phonebookData
    phonebookData.append({"name": "", "phone": ""})


def delContacts (indList):
    global phonebookData
    for i in range(len(indList)):
        phonebookData.pop(indList[i] - i)


def sortContacts ():
    phonebookData.sort(key=lambda contact: contact["name"])