from Window import *
from tkinter import *
from tkinter import messagebox
from DepositWindow import *
from WithdrawWindow import *

class MainWindow(Window): #Класс основого окна
    _instance = None

    def __new__(cls, *args, **kwargs):  # Реализация Singletone
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user_name): #Конструктор
        if not hasattr(self, "initialized"):
            self.root = Tk()
            self.root.geometry("500x500")
            self.deposit_window = None
            self.withdraw_window = None
            self.root.configure(bg='black')
            self.__accounts = {
                "adm69": 777.0
            }
            self._user_name = user_name
            if user_name in self.__accounts and self.__accounts[user_name]:
                self._balance_user = self.__accounts[user_name]
            else:
                self._balance_user = 0.0
            self.root.title(f"BankSystemMain - {user_name}")
            self.initialized = True

    def __get_balance_message(self):  #Показ сообщения с балансом
        return messagebox.showinfo("Баланс", f"Ваш баланс: {self._balance_user}")

    def __create_deposit_window(self): #Создание окна пополнения
        if self.deposit_window is None:
            self.deposit_window = DepositWindow(self)
            self.deposit_window.main()

    def __create_withdraw_window(self): #Создание окна снятия
        if self.withdraw_window is None:
            self.withdraw_window = WithdrawWindow(self)
            self.withdraw_window.main()

    def _update_balance(self, amount, isDeposit=True):
        if isDeposit:
            self._balance_user += amount
        else:
            self._balance_user -= amount

    def _create_widgets(self): #Создание виджетов
        self.label_main_window = Label(
            self.root,
            text=f"Привет, {self._user_name}",
            font=("Times New Roman", 40),
            bg='black',
            fg='white'
        )

        self.button_get_balance = Button(
            self.root,
            text="Узнать баланс",
            font=("Times New Roman", 20),
            command=self.__get_balance_message,
            bg='#ef4b3f',
            fg='black',
            activebackground='#ef4b3f',
            activeforeground='black',
            relief=FLAT
        )

        self.button_deposit = Button(
            self.root,
            text="Пополнить баланс",
            font=("Times New Roman", 20),
            command=self.__create_deposit_window,
            bg='#ef4b3f',
            fg='black',
            activebackground='#ef4b3f',
            activeforeground='black',
            relief=FLAT
        )

        self.button_take_money = Button(
            self.root,
            text="Снять деньги",
            font=("Times New Roman", 20),
            command=self.__create_withdraw_window,
            bg='#ef4b3f',
            fg='black',
            activebackground='#ef4b3f',
            activeforeground='black',
            relief=FLAT
        )

    def _pack_widgets(self): #Размещение виджетов
        self.label_main_window.place(x=20, y=20, width=460, height=60)
        self.button_get_balance.place(x=20, y=140, width=460, height=60)
        self.button_deposit.place(x=20, y=230, width=460, height=60)
        self.button_take_money.place(x=20, y=320, width=460, height=60)

    def main(self):  # Главный метод запуска окна
        self._create_widgets()
        self._pack_widgets()
        self.root.mainloop()