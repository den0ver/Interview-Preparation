#Задание:
#Написать функции, которые принимают параметры по которым мы сможем вернуть объекты JSON 
import json


filename = "JSON/Practice/data.json"

filename2 = "JSON/Practice/users.json"


def func_for_data(package, version):
    with open(filename) as file:
        datas = json.load(file)

        for data in datas['dependencies']:
            if data['package'] == package and data['version'] == version:
                return data
        return None
    

def func_for_users(username):
    with open(filename2) as file:
        objects = json.load(file)

        for data in objects['users']:
            if data['name'] == username:
                return data
        return None


print(func_for_data(package="package-sub-01", version="3.4.6"))
print(func_for_users(username="den0ver"))