# Hector Alejandro Ortega García  21310248   7F
# Sistemas Expertos
# -------------Practica 03: Adivina Quien--------------------
#
import random
import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

# Base de datos de superhéroes con sus características
superheroes = [
    {"nombre": "Superman", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "sí", "liga_justicia": "sí", "inmortal": "no", "combate": "sí", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Batman", "vuelo": "no", "fuerza": "no", "magia": "no", "tecnologia": "sí", "origen_extraterrestre": "no", "liga_justicia": "sí", "inmortal": "no", "combate": "sí", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Wonder Woman", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "no", "liga_justicia": "sí", "inmortal": "sí", "combate": "sí", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Flash", "vuelo": "no", "fuerza": "no", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "no", "liga_justicia": "sí", "inmortal": "no", "combate": "sí", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Aquaman", "vuelo": "no", "fuerza": "sí", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "no", "liga_justicia": "sí", "inmortal": "no", "combate": "sí", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Green Lantern", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "sí", "origen_extraterrestre": "no", "liga_justicia": "sí", "inmortal": "no", "combate": "no", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Cyborg", "vuelo": "no", "fuerza": "sí", "magia": "no", "tecnologia": "sí", "origen_extraterrestre": "no", "liga_justicia": "sí", "inmortal": "no", "combate": "sí", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Shazam", "vuelo": "sí", "fuerza": "sí", "magia": "sí", "tecnologia": "no", "origen_extraterrestre": "no", "liga_justicia": "no", "inmortal": "no", "combate": "sí", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Zatanna", "vuelo": "no", "fuerza": "no", "magia": "sí", "tecnologia": "no", "origen_extraterrestre": "no", "liga_justicia": "no", "inmortal": "no", "combate": "no", "invisibilidad": "no", "telepatia": "no"},
    {"nombre": "Martian Manhunter", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "sí", "liga_justicia": "sí", "inmortal": "no", "combate": "sí", "invisibilidad": "sí", "telepatia": "sí"},
    #{"nombre": "John Constantine", "vuelo": "no", "fuerza": "no", "magia": "sí", "tecnologia": "no", "origen_extraterrestre": "no", "liga_justicia": "no", "inmortal": "no", "combate": "no", "invisibilidad": "no", "telepatia": "no"}
]

# Diccionario que relaciona preguntas con características
preguntas = {
    "¿El superhéroe puede volar?": "vuelo",
    "¿El superhéroe tiene fuerza sobrehumana?": "fuerza",
    "¿El superhéroe utiliza magia?": "magia",
    "¿El superhéroe tiene una conexión con la tecnología?": "tecnologia",
    "¿El superhéroe es de origen extraterrestre?": "origen_extraterrestre",
    "¿El superhéroe es miembro de la Liga de la Justicia?": "liga_justicia",
    "¿El superhéroe es inmortal?": "inmortal",
    "¿El superhéroe tiene habilidades de combate cuerpo a cuerpo?": "combate",
    "¿El superhéroe tiene habilidades de invisibilidad?": "invisibilidad",
    "¿El superhéroe posee habilidades telepáticas o psíquicas?": "telepatia"
}

# Cargar la base de datos desde un archivo JSON, si existe
def cargar_base_datos():
    try:
        with open("superheroes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return superheroes  # Usa la base de datos inicial si no existe archivo

# Guardar la base de datos actual en un archivo JSON
def guardar_base_datos():
    with open("superheroes.json", "w") as file:
        json.dump(superheroes, file, indent=4)

# Agregar un nuevo héroe a la base de datos
def agregar_nuevo_heroe():
    nuevo_heroe = {}
    nombre = simpledialog.askstring("Nuevo Héroe", "Parece que no conozco a este superhéroe. ¿Cuál es su nombre?")
    if not nombre:
        return  # Si no se proporciona un nombre, salir

    nuevo_heroe["nombre"] = nombre

    for pregunta, caracteristica in preguntas.items():
        respuesta = simpledialog.askstring("Pregunta", f"{pregunta} (sí/no):").lower()
        if respuesta not in ["sí", "no"]:
            messagebox.showwarning("Error", "Por favor, responde con 'sí' o 'no'.")
            return
        nuevo_heroe[caracteristica] = "sí" if respuesta == "sí" else "no"

    superheroes.append(nuevo_heroe)  # Agregar a la base de datos
    guardar_base_datos()  # Guardar la base de datos actualizada
    messagebox.showinfo("Éxito", f"Gracias, {nombre} ha sido agregado al sistema.")

# Lógica del juego
class AdivinaElSuperheroe:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina el Superhéroe")
        self.héroes_restantes = cargar_base_datos()
        self.preguntas_realizadas = set()
        self.intentos = 0

        # Cargar y establecer la imagen de fondo
        self.fondo_img = Image.open("fondo.jpg")  # Cambia "fondo.jpg" a tu imagen
        self.fondo_img = self.fondo_img.resize((800, 600), Image.Resampling.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.fondo_img)

        self.label_fondo = tk.Label(master, image=self.fondo)
        self.label_fondo.place(relwidth=1, relheight=1)

        self.label = tk.Label(master, text="¡Bienvenido a Adivina el Superhéroe!", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        #Es la etiqueta donde se mostrará la pregunta
        self.pregunta_label = tk.Label(master, text="")
        self.pregunta_label.pack(pady=5)

        self.boton_si = tk.Button(master, text="Sí", command=lambda: self.responder("sí"))
        self.boton_si.pack(side=tk.LEFT, ipadx=100, ipady=10, padx=5, pady=1)

        self.boton_no = tk.Button(master, text="No", command=lambda: self.responder("no"))
        self.boton_no.pack(side=tk.RIGHT, padx=5, pady=5, ipadx=100, ipady=10)

        self.boton_salir = tk.Button(master, text="Salir", bg="red", command=master.quit)
        self.boton_salir.pack(side=tk.BOTTOM, ipadx=100, ipady=10, pady=5)

        #self.boton_pregunta = tk.Button(master, text="Hacer Pregunta", command=self.hacer_pregunta)
        #self.boton_pregunta.pack()
        self.boton_iniciar = tk.Button(master, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton_iniciar.pack(pady=20)

        self.boton_reiniciar = tk.Button(master, text="Reiniciar Juego", command=self.reiniciar_juego, state="disabled")
        self.boton_reiniciar.place(x=10, y=10)
        #self.boton_reiniciar.pack(side=tk.LEFT)

        self.heroe_img_label = tk.Label(master)  # Etiqueta para la imagen del héroe
        self.heroe_img_label.pack(side=tk.BOTTOM,pady=10)

    def iniciar_juego(self):
        self.boton_iniciar.config(state="disabled")
        self.boton_reiniciar.config(state="disabled")
        self.hacer_pregunta()

    def hacer_pregunta(self):
        if len(self.héroes_restantes) <= 1:
            self.finalizar_juego()
            return
        
        self.intentos += 1
        # Elegir una pregunta que no se haya hecho
        pregunta = random.choice([p for p in preguntas.keys() if p not in self.preguntas_realizadas])
        self.preguntas_realizadas.add(pregunta)
        self.pregunta_label.config(text=pregunta)

    def responder(self, respuesta):
        if not self.pregunta_label.cget("text"):
            return  # Si no hay pregunta, no hacer nada

        caracteristica = preguntas[self.pregunta_label.cget("text")]
        self.héroes_restantes = [h for h in self.héroes_restantes if h[caracteristica] == ("sí" if respuesta == "sí" else "no")]

        if len(self.héroes_restantes) == 1:
            self.confirmar_heroe()
        elif len(self.héroes_restantes) == 0:
            messagebox.showinfo("Error", "No hay ningún superhéroe que coincida con esa descripción.")
            agregar_nuevo_heroe()
            self.héroes_restantes = cargar_base_datos()
        else:
            messagebox.showinfo("Información", f"{len(self.héroes_restantes)} héroes restantes. Sigue respondiendo preguntas...")
            self.hacer_pregunta()

    def confirmar_heroe(self):
        posible_heroe = self.héroes_restantes[0]["nombre"]
        confirmacion = messagebox.askyesno("Confirmación", f"¿Es {posible_heroe}?")
        if confirmacion:
            self.mostrar_imagen_heroe(posible_heroe)
            messagebox.showinfo("¡Correcto!", f"¡El superhéroe es {posible_heroe} en {self.intentos} intentos!")
        else:
            messagebox.showinfo("Error", "Parece que me equivoqué. Vamos a agregar este superhéroe al sistema.")
            agregar_nuevo_heroe()

    def mostrar_imagen_heroe(self, nombre_heroe):
        try:
            img_path = f"{nombre_heroe}.png"  # Ruta de la imagen
            img = Image.open(img_path).resize((200, 200), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.heroe_img_label.config(image=img)
            self.heroe_img_label.image = img
        except FileNotFoundError:
            messagebox.showerror("Imagen no encontrada", f"No se encontró la imagen para {nombre_heroe}.")
        self.boton_reiniciar.config(state="normal")
        
    def finalizar_juego(self):
        if len(self.héroes_restantes) == 1:
            self.confirmar_heroe()
        else:
            messagebox.showinfo("Finalizado", "No se pudo adivinar el superhéroe.")
        self.boton_reiniciar.config(state="normal")
    
    def reiniciar_juego(self):
        self.héroes_restantes = superheroes[:]
        self.preguntas_realizadas.clear()
        self.intentos = 0
        self.pregunta_label.config(text="")
        self.boton_iniciar.config(state="normal")
        self.boton_reiniciar.config(state="disabled")

#root = tk.Tk()
#app = AdivinaElSuperheroe(root)
#root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    juego = AdivinaElSuperheroe(root)
    root.mainloop()