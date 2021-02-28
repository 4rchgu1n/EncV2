import tkinter as tk
import random

abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

ventana = tk.Tk()
ventana.title("Enc")
ventana.config(bg="gray")
ventana.geometry(f"800x800+{round(ventana.winfo_screenwidth() / 4)}+0")

texto_uno = tk.Label(
    ventana, text="Escribe el texto aquí para encriptarlo", bg="gray")
texto_uno.grid(row=0, column=0)

espacio_uno = tk.Label(ventana, text=" " * 8, bg="gray")
espacio_uno.grid(row=0, column=1)

texto_2 = tk.Label(
    ventana, text="Escribe el texto aquí para desencriptarlo", bg="gray")
texto_2.grid(row=0, column=2)

enc = tk.StringVar()
enc.get()

entrada_uno = tk.Entry(ventana, textvariable=enc)
entrada_uno.grid(row=1, column=0)

de_nc = tk.StringVar()
de_nc.get()

entrada_dos = tk.Entry(ventana, textvariable=de_nc)
entrada_dos.grid(row=1, column=2)

text_cuatro = tk.Label(ventana, text="", bg="gray")
text_cuatro.place(x=280, y=50)


def c_clave():
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    print("".join(random.sample(abecedario, 27)))
    Texto5 = tk.Label(ventana, text=abecedario, bg="gray")
    Texto5.grid(row=8, column=2)


clave = tk.StringVar()
entrada_tres = tk.Entry(ventana, textvariable=clave)
entrada_tres.grid(row=7, column=2)

opcion = tk.IntVar()
radio_boton_uno = tk.Radiobutton(
    text="Clave por defecto", variable=opcion, value=1, bg="gray")
radio_boton_dos = tk.Radiobutton(
    text="Selecionar clave", variable=opcion, value=2, bg="gray")
radio_boton_tres = tk.Radiobutton(
    text="Crear clave aleatoria", variable=opcion,
    value=3, command=lambda: c_clave(), bg="gray")

radio_boton_uno.grid(row=6, column=0)
radio_boton_dos.grid(row=7, column=0)
radio_boton_tres.grid(row=8, column=0)
opcion.get()


def encriptar():
    print(opcion.get())
    if opcion.get() == 1:
        abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        print(abecedario)
    elif opcion.get() == 2:
        abecedario = clave.get()
        print(clave.get())

    ENC = enc.get().upper()
    enc_dos = []
    n = 0
    for i in ENC:
        if abecedario.find(i) != -1:
            ni = abecedario.find(i) + n
            while ni > 26:
                ni = ni-27
            print(ni)
            enc_dos.append(abecedario[ni])
            n = n + 1
        else:
            enc_dos.append(i)
    print(enc_dos)

    TENC = "".join(enc_dos)
    texto_tres = tk.Label(ventana, text=TENC, bg="gray")
    texto_tres.grid(row=3, column=0)
    print(TENC)


boton_uno = tk.Button(ventana, text="Encriptar", command=encriptar)
boton_uno.grid(row=2, column=0)


def desencriptar():
    print(opcion.get())
    if opcion.get() == 1:
        abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        print(abecedario)
    elif opcion.get() == 2:
        abecedario = clave.get()
        print(clave.get())
    DENC = enc.get().upper()
    DENC = de_nc.get().upper()
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
    text_cuatro = tk.Label(ventana, text=TDENC, bg="gray")
    text_cuatro.grid(row=3, column=2)
    print(TDENC)


boton_uno = tk.Button(ventana, text="Desencriptar", command=desencriptar)
boton_uno.grid(row=2, column=2)

ventana.mainloop()
