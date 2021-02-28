import tkinter as tk
import random
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

Ventana = tk.Tk()
Ventana.title("Enc")
Ventana.config(bg="gray")
Ventana.geometry("800x800")

Texto1 = tk.Label(Ventana, text="Escribe el texto aquí para encriptarlo", bg="gray")
Texto1.grid(row=0,column=0)

Espacio1 = tk.Label(Ventana, text="        ",bg="gray")
Espacio1.grid(row=0,column=1)

Texto2 = tk.Label(Ventana, text="Escribe el texto aquí para desencriptarlo", bg="gray")
Texto2.grid(row=0,column=2)

Enc = tk.StringVar()
Enc.get()
Entrada1= tk.Entry(Ventana,textvariable=Enc)
Entrada1.grid(row=1,column=0)

DEnc = tk.StringVar()
DEnc.get()
Entrada2= tk.Entry(Ventana,textvariable=DEnc)
Entrada2.grid(row=1,column=2)

Texto4 = tk.Label(Ventana, text="", bg="gray")
Texto4.place(x=280,y=50)

def cClave():
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    print("".join(random.sample(abecedario,27)))
    Texto5 = tk.Label(Ventana, text=abecedario, bg="gray")
    Texto5.grid(row=8,column=2)


Clave=tk.StringVar()
Entrada3 = tk.Entry(Ventana,textvariable=Clave)
Entrada3.grid(row=7,column=2)

opcion = tk.StringVar()
radioBoton1 = tk.Radiobutton(text="Clave por defecto",variable=opcion,value="defecto",bg="gray")
radioBoton2 = tk.Radiobutton(text="Selecionar clave",variable=opcion,value="selecionar",bg="gray")
radioBoton3 = tk.Radiobutton(text="Crear clave aleatoria",variable=opcion,value="crear",command=lambda: cClave(),bg="gray")
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
    Texto3 = tk.Label(Ventana, text=TENC, bg="gray")
    Texto3.grid(row=3,column=0)
    print(TENC)

Boton1 = tk.Button(Ventana, text="Encriptar", command=lambda:Encriptar())
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
    Texto4 = tk.Label(Ventana, text=TDENC, bg="gray")
    Texto4.grid(row=3,column=2)
    print(TDENC)

Boton1 = tk.Button(Ventana, text="Desencriptar", command=lambda:Desencriptar())
Boton1.grid(row=2,column=2)

Ventana.mainloop()
