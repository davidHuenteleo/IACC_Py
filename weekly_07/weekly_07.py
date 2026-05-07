import tkinter as tk
from tkinter import messagebox

def ejecutar_accion():
    # Obtener datos de Entry y Text
    nombre = entrada_nombre.get()
    comentario = caja_texto.get("1.0", tk.END).strip()
    
    # Obtener estado de Checkbutton y Radiobutton
    genero = var_radio.get()
    suscrito = "Sí" if var_check.get() else "No"
    
    resumen = f"Nombre: {nombre}\nGénero: {genero}\nSuscrito: {suscrito}\nComentario: {comentario}"
    messagebox.showinfo("Datos Recogidos", resumen)

# 1. Ventana Principal
ventana = tk.Tk()
ventana.title("Catálogo de Widgets Tkinter")
ventana.geometry("500x600")

# 2. Menús
barra_menu = tk.Menu(ventana)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
ventana.config(menu=barra_menu)

# 3. Frames (Para organizar el diseño)
frame_superior = tk.LabelFrame(ventana, text=" Datos Personales ", padx=10, pady=10)
frame_superior.pack(padx=20, pady=10, fill="x")

# 4. Labels y Entry
tk.Label(frame_superior, text="Nombre:").grid(row=0, column=0, sticky="w")
entrada_nombre = tk.Entry(frame_superior)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

# 5. Radiobuttons
tk.Label(frame_superior, text="Género:").grid(row=1, column=0, sticky="w")
var_radio = tk.StringVar(value="Otro")
tk.Radiobutton(frame_superior, text="Masc", variable=var_radio, value="Masc").grid(row=1, column=1, sticky="w")
tk.Radiobutton(frame_superior, text="Fem", variable=var_radio, value="Fem").grid(row=1, column=2, sticky="w")

# 6. Checkbuttons
var_check = tk.BooleanVar()
check_sub = tk.Checkbutton(ventana, text="Suscribirse al boletín", variable=var_check)
check_sub.pack()

# 7. Text (Caja de texto multilínea)
tk.Label(ventana, text="Comentarios:").pack(pady=(10, 0))
caja_texto = tk.Text(ventana, height=5, width=40)
caja_texto.pack(pady=5)

# 8. Buttons
boton_enviar = tk.Button(ventana, text="Enviar Formulario", command=ejecutar_accion, bg="#4CAF50", fg="white")
boton_enviar.pack(pady=20)

ventana.mainloop()