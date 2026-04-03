from tkinter import *
from abc import ABC, abstractmethod

class Window: #Абстрактный класс окна
    _instance = None

    @abstractmethod
    def _create_widgets(self): #Метод для создания виджетов
        pass

    @abstractmethod
    def _pack_widgets(self): #Метод для размещения виджетов
        pass

    @abstractmethod
    def _on_closing(self): #Метод для обработки закрытия
        pass

    @abstractmethod
    def main(self): #Главный метод запуска окна
        pass