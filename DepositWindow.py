from Window import *
from tkinter import *
from tkinter import messagebox

class DepositWindow(Window):
    _instance = None

    def __new__(cls, *args, **kwargs): #Реализация Singletone
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, main_window): #Конструктор
        if not hasattr(self, "initialized"):
            self.main_window = main_window
            self._balance_user = main_window._balance_user
            self.root = Tk()
            self.root.configure(bg='black')
            self.root.geometry("600x300")
            self.root.title("BankSystemDeposit")
            self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
            self.initialized = True

    def _on_closing(self): #Обработка закрытия окна
        self.main_window.deposit_window = None
        self.root.destroy()

    def __deposit(self): #Пополнение баланса
        try:
            __entered_value = float(self.input_amount.get())
            if __entered_value > 0:
                self.main_window._update_balance(__entered_value)
                self._balance_user = self.main_window._balance_user
                self.main_label.config(text=f"Ваш баланс: {self._balance_user}")
                self.input_amount.delete(0, END)
                self.input_amount.insert(0, "0")
                messagebox.showinfo("Успех", "Баланс успешно пополнен!")
            else:
                messagebox.showerror("Ошибка", "Сумма должна быть положительной")
        except ValueError:
            messagebox.showerror("Ошибка", "Ввод должен быть только чисел")
            self.input_amount.delete(0, END)
            self.input_amount.insert(0, "0")

    def _create_widgets(self): #Создание виджетов
        self.main_label = Label(
            self.root,
            text=f"Ваш баланс: {self._balance_user}",
            font=("Times New Roman", 40),
            bg='black',
            fg='white'
        )

        self.sum_label = Label(
            self.root,
            text="Введите сумму пополнения:",
            font=("Times New Roman", 20),
            bg='black',
            fg='white'
        )

        self.input_amount = Entry(
            self.root,
            justify=RIGHT,
            font=("Times New Roman", 20),
            bg='white',
            fg='black'
        )

        self.button_deposit = Button(
            self.root,
            text="Пополнить баланс",
            font=("Times New Roman", 20),
            command=self.__deposit,
            bg='#ef4b3f',
            fg='black',
            activebackground='#ef4b3f',
            activeforeground='black',
            relief=FLAT
        )

    def _pack_widgets(self): #Размещение виджетов
        self.main_label.place(x=20, y=20, width=560, height=60)
        self.sum_label.place(x=20, y=80, width=560, height=60)
        self.input_amount.place(x=20, y=160, width=320, height=60)
        self.button_deposit.place(x=360, y=160, width=220, height=60)

    def main(self):  # Главный метод запуска окна
        self._create_widgets()
        self._pack_widgets()
        self.root.mainloop()