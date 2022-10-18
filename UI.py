from new_member import new_member_init
from new_member import new_member
from export_scv import export_scv
from export_txt import export_txt
from import_txt import import_txt

def user_interface_create(): # Добавление новой записи и экспорт ее в существующие справочники
    new_member_init()
    export_scv(new_member)
    export_txt(new_member)

def user_interface_import(): # Импорт(чтение) существующих записей
    import_txt()

user_interface_create()

user_interface_import()