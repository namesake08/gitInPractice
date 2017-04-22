import requests
from tkinter import *
from tkinter import ttk


def login(email, password):
    login_dict = {"notify_method": "login", "email": email, "password": password}
    login_response = requests.post("http://rmnova.30meridian.com/API", json=login_dict)
    token = login_response.json()
    return token

root = Tk()#Создаем объект ТК- главное окно
root.title("Notifications")

