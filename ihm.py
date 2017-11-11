#!/usr/bin/python3

from tkinter import Frame, Button
from serial import Serial


class App:

    """ Class principal do aplicativo """

    def __init__(self, master):
        self.ser = Serial('/dev/ttyACM0', '9600')
        frame = Frame(master)
        frame.title = "Janela"
        frame.pack()

        self.display = 0
        self.button01 = Button(frame, text="Desligado", fg="red")
        self.button01.grid(row=0, column=0)
        self.button01.configure(
            command=lambda btn=self.button01: self.trata_botoes(1, btn))

        self.button02 = Button(frame, text="Desligado", fg="red")
        self.button02.grid(row=0, column=1)
        self.button02.configure(
            command=lambda btn=self.button02: self.trata_botoes(2, btn))

        self.button03 = Button(frame, text="Desligado", fg="red")
        self.button03.grid(row=0, column=2)
        self.button03.configure(
            command=lambda btn=self.button03: self.trata_botoes(3, btn))

        self.button04 = Button(frame, text="Desligado", fg="red")
        self.button04.grid(row=0, column=3)
        self.button04.configure(
            command=lambda btn=self.button04: self.trata_botoes(4, btn))

        self.button05 = Button(frame, text="Desligado", fg="red")
        self.button05.grid(row=1, column=0)
        self.button05.configure(
            command=lambda btn=self.button05: self.trata_botoes(5, btn))

        self.button06 = Button(frame, text="Desligado", fg="red")
        self.button06.grid(row=1, column=1)
        self.button06.configure(
            command=lambda btn=self.button06: self.trata_botoes(6, btn))

        self.button07 = Button(frame, text="Desligado", fg="red")
        self.button07.grid(row=1, column=2)
        self.button07.configure(
            command=lambda btn=self.button07: self.trata_botoes(7, btn))

        self.button08 = Button(frame, text="Desligado", fg="red")
        self.button08.grid(row=1, column=3)
        self.button08.configure(
            command=lambda btn=self.button08: self.trata_botoes(8, btn))

        self.button09 = Button(frame, text="Sequencial01")
        self.button09.grid(row=2, columnspan=4)
        self.button09.configure(
            command=lambda btn=self.button09: self.sequencial(btn))

        self.button10 = Button(frame, text="Sequuencial02")
        self.button10.grid(row=3, columnspan=4)
        self.button10.configure(
            command=lambda btn=self.button10: self.sequencial(btn))

        self.button11 = Button(frame, text="Apaga_tudo")
        self.button11.grid(row=4, columnspan=4)
        self.button11.configure(
            command=lambda btn=self.button11: self.sequencial(btn))

    def sequencial(self, botao):
        """
            sequencial(self, a) -> void
            define execução dos botões sequênciais.
        """
        if botao['text'] == "Sequencial01":
            self.ser.write(b'00000002')
            print(b'00000002')
            self.limpa_campos()

        if botao['text'] == "Sequuencial02":
            self.ser.write(b'00000003')
            print(b'00000003')
            self.limpa_campos()

        if botao['text'] == "Apaga_tudo":
            self.ser.write(b'00000004')
            print(b'00000004')
            self.limpa_campos()

    def limpa_campos(self):
        """"
            método para resetar os botões ligados do form
        """
        self.button01.configure(text="Desligado")
        self.button02.configure(text="Desligado")
        self.button03.configure(text="Desligado")
        self.button04.configure(text="Desligado")
        self.button05.configure(text="Desligado")
        self.button06.configure(text="Desligado")
        self.button07.configure(text="Desligado")
        self.button08.configure(text="Desligado")
        self.display = 0

    def trata_botoes(self, button_id, botao):
        aux = 0
        temp = 0
        print(temp)
        if botao['text'] == "Desligado":

            aux = 1 << (button_id - 1)
            self.display = self.display | aux
            temp = bin(self.display).lstrip('-0b').zfill(8).encode()
            print(temp)

            self.ser.write(temp)
            self.ser.flush()
            botao.configure(text='Ligado')
        else:
            aux = 1 << (button_id - 1)
            self.display = self.display & ~aux
            temp = bin(self.display).lstrip('-0b').zfill(8).encode()
            print(temp)

            self.ser.write(temp)
            self.ser.flush()
            botao.configure(text='Desligado')
