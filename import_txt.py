def import_txt():
    with open('data.txt', 'r', encoding = 'utf-8') as data:
        exist_data = data.read()
        print(exist_data)
        data.close()