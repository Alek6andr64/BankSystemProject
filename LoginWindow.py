from MainWindow import *
from Window import *
from tkinter import *


class LoginWindow(Window):
    _instance = None

    def __new__(cls, *args, **kwargs): #Реализация Singletone
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self): #Конструктор
        self.root = Tk()
        self.root.geometry("400x450")
        self.root.title("BankSystemLogin")
        self.__accounts = {
            "adm69": "6969"
        }

    def __enter(self): #Вход в систему
        login = self.login_input.get()
        password = self.password_input.get()

        if not login or not password:
            self.alert_label.config(text="Заполните все поля!")
            return

        if login in self.__accounts and self.__accounts[login] == password:
            main_window = MainWindow(login)
            main_window.main()
            # self.root.withdraw()
        else:
            self.alert_label.config(text="Неверный логин или пароль!")
            self.password_input.delete(0, END)

    def _create_widgets(self): #Создание виджетов
        self.login_label = Label(
            self.root,
            text=f"Введите логин:",
            font=("Times New Roman", 40)
        )

        self.login_input = Entry(
            self.root,
            justify=LEFT,
            font=("Times New Roman", 20)
        )

        self.password_label = Label(
            self.root,
            text="Введите пароль:",
            font=("Times New Roman", 40)
        )

        self.password_input = Entry(
            self.root,
            justify=LEFT,
            show="*",
            font=("Times New Roman", 20)
        )

        self.alert_label = Label(
            self.root,
            text="",
            font=("Times New Roman", 20)
        )

        self.enter_button = Button(
            self.root,
            text="Войти",
            font=("Times New Roman", 20),
            command=self.__enter
        )

    def _pack_widgets(self): #Размещение виджетов
        self.login_label.place(x=20, y=20, width=360, height=60)
        self.login_input.place(x=20, y=80, width=360, height=60)
        self.password_label.place(x=20, y=160, width=360, height=60)
        self.password_input.place(x=20, y=220, width=360, height=60)
        self.alert_label.place(x=20, y=280, width=360, height=60)
        self.enter_button.place(x=20, y=340, width=360, height=60)