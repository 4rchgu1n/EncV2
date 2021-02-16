from tkinter import *
import random
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

Ventana = Tk()
Ventana.title("Enc")
Ventana.config(bg="gray")
Ventana.geometry("800x800")

Texto1 = Label(Ventana, text="Escribe el texto aquí para encriptarlo", bg="gray")
Texto1.grid(row=0,column=0)

Espacio1 = Label(Ventana, text="        ",bg="gray")
Espacio1.grid(row=0,column=1)

Texto2 = Label(Ventana, text="Escribe el texto aquí para desencriptarlo", bg="gray")
Texto2.grid(row=0,column=2)

Enc = StringVar()
Enc.get()
Entrada1= Entry(Ventana,textvariable=Enc)
Entrada1.grid(row=1,column=0)

DEnc = StringVar()
DEnc.get()
Entrada2= Entry(Ventana,textvariable=DEnc)
Entrada2.grid(row=1,column=2)

Texto4 = Label(Ventana, text="", bg="gray")
Texto4.place(x=280,y=50)

def cClave():
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    print("".join(random.sample(abecedario,27)))
    Texto5 = Label(Ventana, text=abecedario, bg="gray")
    Texto5.grid(row=8,column=2)


Clave=StringVar()
Entrada3 = Entry(Ventana,textvariable=Clave)
Entrada3.grid(row=7,column=2)

opcion = StringVar()
radioBoton1 = Radiobutton(text="Clave por defecto",variable=opcion,value="defecto",bg="gray")
radioBoton2 = Radiobutton(text="Selecionar clave",variable=opcion,value="selecionar",bg="gray")
radioBoton3 = Radiobutton(text="Crear clave aleatoria",variable=opcion,value="crear",command=lambda: cClave(),bg="gray")
radioBoton1.grid(row=6,column=0)
radioBoton2.grid(row=7,column=0)
radioBoton3.grid(row=8,column=0)
opcion.get()

def Encriptar():
    print(opcion.get())
    if opcion.get() == "defecto":
        abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        print(abecedario)
    elif opcion.get() == "selecionar":
        abecedario = Clave.get()
        print(Clave.get())

    ENC = Enc.get().upper()
    ENC2 = []
    n = 0
    for i in ENC:
        if abecedario.find(i) != -1:
            ni = abecedario.find(i) + n
            while ni > 26:
                ni = ni-27
            print(ni)
            ENC2.append(abecedario[ni])
            n = n + 1
        else:
            ENC2.append(i)
    print(ENC2)

    TENC = "".join(ENC2)
    Texto3 = Label(Ventana, text=TENC, bg="gray")
    Texto3.grid(row=3,column=0)
    print(TENC)

Boton1 = Button(Ventana, text="Encriptar", command=lambda:Encriptar())
Boton1.grid(row=2,column=0)

def Desencriptar():
    print(opcion.get())
    if opcion.get() == "defecto":
        abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        print(abecedario)
    elif opcion.get() == "selecionar":
        abecedario = Clave.get()
        print(Clave.get())
    DENC = Enc.get().upper()
    DENC = DEnc.get().upper()
    DENC2 = ""
    n = 0
    for i in DENC:
        if abecedario.find(i) != -1:
            ni = abecedario.find(i) - n
            while ni > 26:
                ni = ni-27
            print(ni)
            DENC2 += abecedario[ni]
            n = n + 1
        else:
            DENC2 += i
    print(DENC2)

    TDENC = "".join(DENC2)
    Texto4 = Label(Ventana, text=TDENC, bg="gray")
    Texto4.grid(row=3,column=2)
    print(TDENC)

Boton1 = Button(Ventana, text="Desencriptar", command=lambda:Desencriptar())
Boton1.grid(row=2,column=2)

Ventana.mainloop()
