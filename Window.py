from tkinter import *

class Window: #Абстрактный класс окна
    _instance = None

    def __new__(cls, *args, **kwargs): #Реализация Singletone
        if cls._instance is None:     
            cls._instance = super().__new__(cls) 
        return cls._instance       

    def __init__(self): #Конструктор
        self.root = Tk()              
        self.root.geometry("500x500")    
        self.root.title("BankSystem")    

    def _create_widgets(self): #Метод для создания виджетов
        pass                       

    def _pack_widgets(self): #Метод для размещения виджетов
        pass                  

    def _on_closing(self): #Метод для обработки закрытия
        pass                        

    def main(self): #Главный метод запуска окна
        self._create_widgets()         
        self._pack_widgets()              
        self.root.mainloop()               