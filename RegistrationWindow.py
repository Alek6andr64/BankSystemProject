from Window import *
from tkinter import *


class RegistrationWindow(Window):
    _instance = None

    def __new__(cls, *args, **kwargs):  # Реализация Singletone
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):  # Конструктор
        self.root = Tk()
        self.root.geometry("500x580")
        self.root.title("BankSystemRegistration")
        self.root.configure(bg='black')
        self.__accounts = {
            "adm69": "6969"
        }

    def __registration(self):  # Регистрация нового пользователя
        login = self.login_input.get()
        password = self.password_input.get()

        if not login or not password:
            self.alert_label.config(text="Заполните все поля!")
            return

        if login not in self.__accounts:
            self.root.destroy()
            from LoginWindow import LoginWindow
            login_window = LoginWindow()
            login_window.main()

        else:
            self.alert_label.config(text="Аккаунт уже существует!")
            self.password_input.delete(0, END)

    def __open_login(self):
        self.root.destroy()
        from LoginWindow import LoginWindow
        login_window = LoginWindow()
        login_window.main()

    def _create_widgets(self):  # Создание виджетов
        self.login_label = Label(
            self.root,
            text="Введите логин:",
            font=("Times New Roman", 40),
            bg='black',
            fg='white'
        )

        self.login_input = Entry(
            self.root,
            justify=LEFT,
            font=("Times New Roman", 20),
            bg='white',
            fg='black'
        )

        self.password_label = Label(
            self.root,
            text="Введите пароль:",
            font=("Times New Roman", 40),
            bg='black',
            fg='white'
        )

        self.password_input = Entry(
            self.root,
            justify=LEFT,
            show="*",
            font=("Times New Roman", 20),
            bg='white',
            fg='black'
        )

        self.alert_label = Label(
            self.root,
            text="",
            font=("Times New Roman", 14),
            bg='black',
            fg='white'
        )

        self.enter_button = Button(
            self.root,
            text="Зарегистрироваться",
            font=("Times New Roman", 20),
            command=self.__registration,
            bg='#ef4b3f',
            fg='black',
            activebackground='#ef4b3f',
            activeforeground='black',
            relief=FLAT
        )

        self.return_to_login_label = Label(
            self.root,
            text="Уже есть аккаунт?",
            font=("Times New Roman", 14),
            bg='black',
            fg='white'
        )

        self.return_to_login_button = Button(
            self.root,
            text="Войти",
            font=("Times New Roman", 20),
            command=self.__open_login,
            bg='#ef4b3f',
            fg='black',
            activebackground='#ef4b3f',
            activeforeground='black',
            relief=FLAT
        )

    def _pack_widgets(self):  # Размещение виджетов
        self.login_label.place(x=20, y=20, width=460, height=60)
        self.login_input.place(x=20, y=80, width=460, height=60)
        self.password_label.place(x=20, y=160, width=460, height=60)
        self.password_input.place(x=20, y=220, width=460, height=60)
        self.alert_label.place(x=20, y=280, width=460, height=60)
        self.enter_button.place(x=20, y=340, width=460, height=60)
        self.return_to_login_label.place(x=20, y=430, width=460, height=60)
        self.return_to_login_button.place(x=20, y=480, width=460, height=60)