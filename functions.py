# Каталог документов хранится в следующем виде:
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def options():
    return '''    Пользовательские команды:
        h - Список пользовательских команд
        p - people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
        s - shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
        l - list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
        a - add – команда, которая добавит новый документ в каталог и в перечень полок
        d - delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
        m - move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
        as - add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
        ls - list shelf – команда выведет список полок места хранения документов.
        q - Выход
        '''
def owner_by_document(document_number, documents):

    found = False
    res = ""
    for document in documents:
        if document['number'] == document_number:
            res = f"    Документ № {document['number']} принадлежит {document['name']}"
            found = True
    if found == False:
        res = f"    Указанный документ № {document_number} не найден в системе, попробуйте повторить поиск."
    return res

def search_document(document_number,directories):
    for i in directories:
        if document_number in directories[i]:
            return i
    return False

def search_by_storage(document_number,directories):
    key = search_document(document_number,directories)
    if  key != False:
        return f"    Документ № {document_number} хранится на полке №-{key}"
    else:
        return f"    Указанный документ № {document_number} не найден на полках."

def documents_list(documents):
    res = ""
    if len(documents) == 0:
        res = "   В системе нет сохраненных документов."
    for document in documents:
        res += f"    Документ {document['type']} № \"{document['number']}\" принадлежит \"{document['name']}\"\n"
    return res

def document_add(document_number,document_type,document_owner,document_storage):
    if document_storage in directories:
        documents.append({"type":document_type, "number":document_number, "name":document_owner})
        directories[document_storage].append(document_number)
        return f"    Документ {document_type} № \"{document_number}\" принадлежит \"{document_owner}\" Сохранет на {document_storage} полке."
    else:
        return "    Указана не существующая полка."

def document_del(document_number):
    res = ""
    found = False
    key_pop = 0
    for document in documents:
        if document['number'] == document_number:
            # print(f"    Документ № {document['number']} принадлежит {document['name']}")
            found = True
            break
        key_pop += 1
    documents.pop(key_pop)
    storage = 0
    for storage, catalog in directories.items():
        #print(key, catalog)
        for num_doc in catalog:
            if num_doc == document_number:
                catalog.remove(document_number)
                res = f"    Документ №{document_number} удален с полки №-{storage}/n"
                break
    if found == True:
        res += f"    Документ с номером № {document_number} удален из системы."
    else:
        res = f"    Документ с номером № {document_number} не найден."
    return res

def move_document(document_number,document_storage):
    found = False
    res = ""
    for document in documents:
        if document['number'] == document_number:
            found = True
            break
    if found == False:
        return f"    Документ с указанным номером № {document_number}не найден."
    document_storage_remove = search_document(document_number,directories)
    if document_storage in directories: # добаляем в новую полку
        if document_storage_remove != False: # ищем и удаляем с прошлой полки
            directories[document_storage_remove].remove(document_number)
        directories[document_storage].append(document_number)
        res = f"    Документ {document['type']} № \"{document['number']}\" принадлежит \"{document['name']}\" Сохранет на {document_storage} полке."
    else:
        res = "    Указана не существующая полка."
    return res

def storage_add(storage_new):
    if storage_new in directories: # проверяем наличие полки в месте хранения
        return f"    Полка {storage_new} уже была ранее создана."

    directories[storage_new] = []
    # print(directories)

def main(documents, directories):
    while True:
        user_input = input("->    Введите команду: ")
        if user_input == "h":
            res = options()
            print(res)
        elif user_input == "p":
            document_number = input("->    Для поиска владельца необходимо указать номер документа: ")
            res = owner_by_document(document_number,documents)
            print(res)
        elif user_input == "s":
            document_number = input("->    Для поиска места хранения необходимо указать номер документа: ")
            res = search_by_storage(document_number,directories)
            print(res)
        elif user_input == "l":
            res = documents_list(documents)
            print(res)
        elif user_input == "a":
            document_number = input("->    Укажите номер документа: ")
            document_type = input("->    Укажите тип документа: ")
            document_owner = input("->    Укажите Имя владельца документа: ")
            document_storage = input("->    Укажите полку хранения документа: ")
            res = document_add(document_number,document_type,document_owner,document_storage)
            print(res)
        elif user_input == "d":
            document_number = input("->    Для удаления необходимо указать номер документа: ")
            res = document_del(document_number)
            print(res)
        elif user_input == "m":
            document_number = input("->    Укажите номер перемещаемого документа: ")
            document_storage = input("->    Укажите полку на которую перемещается документ: ")
            res = move_document(document_number,document_storage)
            print(res)
        elif user_input == "as":
            storage_new = input("->    Укажите номер добавляемой полки: ")
            res = storage_add(storage_new)
            print(res)
        elif user_input == "ls":
            print(directories)
        elif user_input == "q":
            break
        else:
            print("   Команда не доступна, воспользуйтесь помощью, команда Help - h")

def sum_x(a,b):
    return a + b

if __name__ == '__main__':
    main(documents, directories)
