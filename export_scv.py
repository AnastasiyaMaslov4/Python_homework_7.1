from new_member import new_member

def export_scv(new_member):
    with open ('data.scv', 'a', encoding = 'utf-8') as data:
        data.write(f'{new_member[0]} \n{new_member[1]} \n{new_member[2]} \n{new_member[3]} \n \n')
        data.close()