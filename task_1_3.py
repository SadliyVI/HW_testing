documents = [
        {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
        {'type': 'driver license', 'number': '5455 028765', 'name': 'Василий Иванов'},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name (doc_number):
    name = 'Документ не найден'
    for document in documents:
        if document['number'] == doc_number:
            name = document['name']
    return name

def get_directory(doc_number):
    result = 'Полки с таким документом не найдено'
    for directory, numbers in directories.items():
        if doc_number in numbers:
            result = directory
    return result

def add(document_type, number, name, shelf_number):
    check_1 = False
    check_2 = False
    for dir in directories.values():
        if shelf_number not in dir:
            check_1 = True
    for document in documents:
        if number not in document['number']:
            check_2 = True
    if check_1:
        documents.append({'type': document_type, 'number': number, 'name': name})
    if check_2:
        directories[str(shelf_number)].append(number)
    else: directories[shelf_number] =[number]

if __name__ == '__main__':
    print(get_name('10006'))
    print(get_directory('11-2'))
    print(get_name('101'))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory('311 020203'))
    print(get_name('311 020203'))
    print(get_directory('311 020204'))