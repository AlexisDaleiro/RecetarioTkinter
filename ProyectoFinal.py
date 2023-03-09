import tkinter as tk
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = tk.Tk()
root.geometry("700x700")
root.title("Recetario")
root.resizable(width=True, height=True)
root.config(bd=30, bg="cyan")

label = Label(
    root, text="Bienvenido al recetario del proyecto Python de Alexis Daleiro")
label.pack(fill=BOTH)
label.config(fg="black", bg="aquamarine", font=("Verdana"))

frame = Frame(root)
frame.pack(expand=False, fill="both", padx=20, pady=20)
frame.config(width=300, height=300, bg="lightblue")

frame1 = Frame(root)
frame1.pack(expand=False, fill="both", padx=20, pady=20, side=tk.LEFT)
frame1.config(width=150, height=150, bg="lightblue")

frame2 = Frame(root)
frame2.pack(expand=False, fill="both", padx=20, pady=20, side=tk.RIGHT)
frame2.config(width=150, height=150, bg="lightblue")


listbox1 = tk.Listbox(frame1)
scrollbar = tk.Scrollbar(frame1, command=listbox1.yview)
listbox1.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
listbox1.pack(fill="both", expand=False, side=tk.RIGHT)

listbox2 = tk.Listbox(frame2)
scrollbar1 = tk.Scrollbar(frame2, command=listbox2.yview)
listbox2.config(yscrollcommand=scrollbar1.set)
scrollbar1.pack(side="right", fill="y")
listbox2.pack(fill="both", expand=False, side=tk.LEFT)

recetas = [{
    "nombre": ["Milanesas con puré"],
    "ingredientes": [
        "Carne", "Pan rallado", "Huevo", "Adobo", "Aceite", "Sal", "Papa",
        "Manteca", "Leche", "Pimienta", "Nuez Moscada"
    ],
    "preparacion":
    "Salar la carne, batir los huevos, ponerle adobo al huevo batido, pasar los churrascos de carne por el pan rallado, luego por el huevo, y luego por el pan rallado nuevamente, fritar.<br> Hervir las papas, luego pisarlas, ponerle manteca y leche hirviendo, un poco de sal, pimienta y nuez moscada y seguir pisando hasta que el puré que quede uniforme"
}, {
    "nombre": ["Pan de pollo"],
    "ingredientes": [
        "Harina", "Mayonesa", "Leche", "Sal", "Huevo", "Pollo", "Cebolla",
        "Morron", "Ajo", "Perejil", "Queso Cheddar", "Queso muzzarella"
    ],
    "preparacion":
    "Para hacer la masa: 8 Cucharadas de leche, 4 cucharadas de mayoensa, una taza de harina, sal a gusto, amasar y estirar la masa.<br>Para preparar el relleno: Pollo previamente cocido, sofritar cebolla, morron, agregar el pollo, agregar ajo, perejil, llevar el relleno a la masa previamente preparada y ponerlo junto con los quesos, cerrar el pan, pintar con huevo y hornear"
}, {
    "nombre": ["Hamburguesa"],
    "ingredientes": [
        "Carne picada", "Pan", "Huevo", "Ajo", "Perejil", "Oregano", "Tomillo",
        "Morron", "Cebolla", "Aceite", "Sal", "Pimienta"
    ],
    "preparacion": [
        "Condimentar la carne picada con, ajo, perejil, cebolla, morron, oregano, tomillo, pimienta, ponerle trocitos de pan, un huevo, y mezclar los ingredientes hasta que se unan bien, armar las hamburguesas, poner en una asadera un poco de aceite, llevar al horno."
    ]
}, {
    "nombre": ["test"],
    "ingredientes": ["asd"],
    "preparacion": ["a"]
}]

ingredientesDisponibles = []


def volverAlMenu():
    if(len(ingredientesDisponibles)==0):
        texto1.delete("1.0", tk.END)
        texto1.insert(tk.END, "\nNo hay ingredientes disponibles\n")
        texto1.insert(tk.END,
                      "Por favor, ingresa los ingredientes que tienes disponibles para cocinar\n")
        texto1.insert(tk.END, "\n")
    else:
        texto1.delete("1.0", tk.END)
        texto1.insert(tk.END, "Ingredientes disponibles: \n")
        for i in range(len(ingredientesDisponibles)):
            texto1.insert(tk.END, ingredientesDisponibles[i])
    menu()

def menu():
    if (len(ingredientesDisponibles) == 0):
        print("\n")
        print("No hay ingredientes disponibles")
        print("\n")
        print(
            ""
        )
        print("\n")
    else:
        print(
            str("Ingredientes disponibles actualmente: \n") +
            str(ingredientesDisponibles))


def encontrarReceta():
    texto1.delete(1.0, tk.END)
    recetasDisponibles = []
    for i in range(len(recetas)):
        tengoIngredientes = True
        for j in recetas[i]["ingredientes"]:
            if j not in ingredientesDisponibles:
                tengoIngredientes = False
                break
        if tengoIngredientes:
            recetasDisponibles.append(recetas[i]["nombre"])
    if len(recetasDisponibles) == 0:
        texto1.insert(tk.END, "\nNo hay recetas disponibles\n")
        texto1.insert(tk.END,
                      "Por favor, ingresa los ingredientes necesarios\n")
        texto1.insert(tk.END, "\n")

    else:
        texto1.insert(tk.END, "\nRecetas disponibles:\n")
        for i in range(len(recetas)):
            if recetas[i]["nombre"] in recetasDisponibles:
                texto1.insert(tk.END, recetas[i]["nombre"])

texto1 = tk.Text(listbox1, width=32, height=100, wrap=tk.WORD)
texto1.pack()


def mostrarReceta():
    texto.delete(1.0, tk.END)
    for i in range(len(recetas)):
        nombre = recetas[i]["nombre"]
        ingredientes = recetas[i]["ingredientes"]
        preparacion = recetas[i]["preparacion"]

        texto.insert(tk.END, "".join(nombre) + "\n\n")
        texto.insert(tk.END, "Ingredientes: \n")
        for j in ingredientes:
            texto.insert(tk.END, j + "\n")
        texto.insert(tk.END, "\nPreparación: \n" + str(preparacion) + "\n\n")
        texto.insert(tk.END, "\n")
texto = tk.Text(listbox2, width=32, height=100, wrap=tk.WORD)
texto.pack()


def eliminarReceta():
    nombre = tkinter.simpledialog.askstring("nombre",
                                            "Nombre de la receta a eliminar")
    for i in range(len(recetas)):
        if recetas[i]["nombre"][0] == nombre:
            recetas.pop(i)
            tkinter.messagebox.showinfo("Aviso", "La receta ha sido eliminada.")
            return
    tkinter.messagebox.showinfo("Aviso", "La receta no se encontró.")


def agregarIngredienteDisponible():

    cerrar = tkinter.messagebox.askokcancel(
        "Input",
        "Pulsa aceptar si quieres seguir agregando ingredientes, de lo contrario, cancela"
    )

    if cerrar == True:
        print("\n")
        ingredientesDisponibles.append(
            tkinter.simpledialog.askstring("ingrediente",
                                           "Dime el ingrediente a agregar: ",
                                           parent=root))
        cerrar = tkinter.messagebox.askokcancel(
            "Input",
            "Pulsa aceptar si quieres seguir agregando ingredientes, de lo contrario, cancela"
        )
        while cerrar == True:
            ingredientesDisponibles.append(
                input("Dime el ingrediente a agregar: "))
            cerrar = tkinter.messagebox.askokcancel(
                "Input",
                "Introduzca 0 si quiere agregar más ingredientes, 1 si quiere cerrar esta ventana."
            )


def crearNuevaReceta():
    nombre = tkinter.simpledialog.askstring("nombre",
                                            "Dime el nombre de la receta",
                                            parent=root)
    root.focus_force
    ingredientes = []
    cantidadIngredientes = None
    while type(cantidadIngredientes) != int:
        try:
            cantidadIngredientes = int(
                tkinter.simpledialog.askstring(
                    "cantidadIngredientes",
                    "Cuantos ingredientes lleva la receta? ",
                    parent=root))
            root.focus_force
        except ValueError:
            tkinter.messagebox.showerror(
                "Error", "La cantidad de ingredientes debe ser un número")
    for i in range(cantidadIngredientes):
        ingrediente = tkinter.simpledialog.askstring("ingredientes",
                                                     "Ingresar ingrediente",
                                                     parent=root)
        root.focus_force
        ingredientes.append(ingrediente)

    preparacion = tkinter.simpledialog.askstring("preparacion",
                                                 "Preparacion",
                                                 parent=root)
    root.focus_force
    recetas.append({
        "nombre": nombre,
        "ingredientes": ingredientes,
        "preparacion": preparacion
    })

    print("La receta " + nombre + " se guardo correctamente")
    print("\nIngredientes: ")
    for ingrediente in ingredientes:
        print(ingrediente + ", ")
    print("\nPreparacion: ")
    print(preparacion)


boton1 = tk.Button(frame,
                   text="Agregar ingredientes disponibles",
                   command=agregarIngredienteDisponible,
                   bg="alice blue")
boton1.pack()
boton2 = tk.Button(frame,
                   text="Crear nueva receta",
                   command=crearNuevaReceta,
                   bg="alice blue")
boton2.pack()
boton3 = tk.Button(frame,
                   text="Mostrar receta",
                   command=mostrarReceta,
                   bg="alice blue")
boton3.pack()
boton4 = tk.Button(frame,
                   text="Encontrar receta",
                   command=encontrarReceta,
                   bg="alice blue")
boton4.pack()
boton5 = tk.Button(frame,
                   text="Eliminar receta",
                   command=eliminarReceta,
                   bg="alice blue")
boton5.pack()
boton6 = tk.Button(frame,
                   text="Volver al menu",
                   command=volverAlMenu,
                   bg="alice blue").pack(side=tk.BOTTOM)

root.mainloop()
