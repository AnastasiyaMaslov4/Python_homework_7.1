from new_member import new_member

def export_txt(new_member):
    with open('data.txt', 'a', encoding = 'utf-8') as data:
        data.write(f"{new_member[0]}, {new_member[1]}, {new_member[2]}, {new_member[3]}; \n" )
        data.close()