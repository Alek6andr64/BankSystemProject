from tkinter import *
import sys
from tkinter import messagebox


class Window:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("BankSystem")

    def _create_widgets(self):
        pass

    def _pack_widgets(self):
        pass

    def main(self):
        self._create_widgets()
        self._pack_widgets()
        self.root.mainloop()


class MainWindow(Window):
    def __get_balance_message(self):
        return messagebox.showinfo("Баланс", f"Ваш баланс: {self._balance_user}")

    def __create_deposit_window(self):
        deposit_window = DepositWindow(self)
        deposit_window.main()

    def __init__(self, user_name):
        super().__init__()
        self.__accounts = {
            "adm69": 777.0
        }
        self._user_name = user_name
        if user_name in self.__accounts and self.__accounts[user_name]:
            self._balance_user = self.__accounts[user_name]
        else:
            self._balance_user = 0.0


    def update_balance(self, amount):
        self._balance_user += amount

    def _create_widgets(self):
        self.label_main_window = Label(
            self.root,
            text=f"Привет, {self._user_name}",
            font=("Times New Roman", 40)
        )

        self.button_get_balance = Button(
            self.root,
            text="Узнать баланс",
            font=("Times New Roman", 20),
            command=self.__get_balance_message
        )

        self.button_deposit = Button(
            self.root,
            text="Пополнить баланс",
            font=("Times New Roman", 20),
            command=self.__create_deposit_window
        )

        self.button_take_money = Button(
            self.root,
            text="Снять деньги",
            font=("Times New Roman", 20)
        )

    def _pack_widgets(self):
        self.label_main_window.place(x=20, y=20, width=460, height=60)
        self.button_get_balance.place(x=20, y=140, width=460, height=60)
        self.button_deposit.place(x=20, y=230, width=460, height=60)
        self.button_take_money.place(x=20, y=320, width=460, height=60)


class DepositWindow(Window):
    def __init__(self, main_window):
        self.main_window = main_window
        self._balance_user = main_window._balance_user
        self.root = Tk()
        self.root.geometry("600x300")
        self.root.title("BankSystem")

    def __deposit(self):
        try:
            __entered_value = float(self.input_amount.get())
            self.main_window.update_balance(__entered_value)

            self._balance_user = self.main_window._balance_user
            self.main_label.config(text=f"Ваш баланс: {self._balance_user}")
            self.input_amount.delete(0, END)
            self.input_amount.insert(0, "0")

        except ValueError:
            messagebox.showerror("Ошибка", "Ввод должен быть только чисел")

    def _create_widgets(self):
        self.main_label = Label(
            self.root,
            text=f"Ваш баланс: {self._balance_user}",
            font=("Times New Roman", 40)
        )

        self.sum_label = Label(
            self.root,
            text="Введите сумму пополнения:",
            font=("Times New Roman", 20)
        )

        self.input_amount = Entry(
            self.root,
            justify=RIGHT,
            font=("Times New Roman", 20)
        )

        self.button_deposit = Button(
            self.root,
            text="Пополнить баланс",
            font=("Times New Roman", 20),
            command=self.__deposit
        )

    def _pack_widgets(self):
        self.main_label.place(x=20, y=20, width=560, height=60)
        self.sum_label.place(x=20, y=80, width=560, height=60)
        self.input_amount.place(x=20, y=160, width=320, height=60)
        self.button_deposit.place(x=360, y=160, width=220, height=60)

class LoginWindow(Window):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x450")
        self.root.title("BankSystemLogin")
        self.__accounts = {
            "adm69": "6969"
        }

    def __enter(self):
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

    def _create_widgets(self):
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

    def _pack_widgets(self):
        self.login_label.place(x=20, y=20, width=360, height=60)
        self.login_input.place(x=20, y=80, width=360, height=60)
        self.password_label.place(x=20, y=160, width=360, height=60)
        self.password_input.place(x=20, y=220, width=360, height=60)
        self.alert_label.place(x=20, y=280, width=360, height=60)
        self.enter_button.place(x=20, y=340, width=360, height=60)

login_window = LoginWindow()
login_window.main()