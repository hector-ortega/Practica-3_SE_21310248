import random
import json

# Base de datos de superhéroes con sus características
superheroes = [
    {"nombre": "Superman", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "sí"},
    {"nombre": "Batman", "vuelo": "no", "fuerza": "no", "magia": "no", "tecnologia": "sí", "origen_extraterrestre": "no"},
    {"nombre": "Wonder Woman", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "no"},
    {"nombre": "Flash", "vuelo": "no", "fuerza": "no", "magia": "no", "tecnologia": "no", "velocidad": "sí"},
    {"nombre": "Green Lantern", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "sí", "origen_extraterrestre": "no"},
    {"nombre": "Aquaman", "vuelo": "no", "fuerza": "sí", "magia": "no", "tecnologia": "no", "naturaleza": "sí"},
    {"nombre": "Martian Manhunter", "vuelo": "sí", "fuerza": "sí", "magia": "no", "tecnologia": "no", "origen_extraterrestre": "sí"},
    {"nombre": "Shazam", "vuelo": "sí", "fuerza": "sí", "magia": "sí", "tecnologia": "no", "origen_extraterrestre": "no"},
    {"nombre": "Cyborg", "vuelo": "no", "fuerza": "sí", "magia": "no", "tecnologia": "sí", "origen_extraterrestre": "no"}
]

# Diccionario que relaciona preguntas con características
preguntas = {
    "¿El superhéroe puede volar?": "vuelo",
    "¿El superhéroe tiene fuerza sobrehumana?": "fuerza",
    "¿El superhéroe utiliza magia?": "magia",
    "¿El superhéroe tiene habilidades sobrehumanas de velocidad?": "velocidad",
    "¿El superhéroe tiene una conexión con la tecnología?": "tecnologia",
    "¿El superhéroe tiene una conexión con la naturaleza o los animales?": "naturaleza",
    "¿El superhéroe es de origen extraterrestre?": "origen_extraterrestre"
}

def cargar_base_datos():
    """Carga la base de datos desde un archivo JSON, si existe."""
    try:
        with open("superheroes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return superheroes  # Usa la base de datos inicial si no existe archivo

def guardar_base_datos():
    """Guarda la base de datos actual en un archivo JSON."""
    with open("superheroes.json", "w") as file:
        json.dump(superheroes, file, indent=4)

def generar_pregunta(preguntas_posibles):
    """Selecciona una pregunta al azar."""
    return random.choice(list(preguntas_posibles.keys()))

def agregar_nuevo_heroe():
    """Agrega un nuevo héroe a la base de datos con sus características."""
    nuevo_heroe = {}
    nombre = input("Parece que no conozco a este superhéroe. ¿Cuál es su nombre? ")
    nuevo_heroe["nombre"] = nombre

    # Preguntar por cada característica en el diccionario de preguntas
    for pregunta, caracteristica in preguntas.items():
        respuesta = input(f"{pregunta} (sí/no): ").lower()
        nuevo_heroe[caracteristica] = "sí" if respuesta == "sí" else "no"

    superheroes.append(nuevo_heroe)  # Agregar a la base de datos
    guardar_base_datos()  # Guardar la base de datos actualizada
    print(f"Gracias, {nombre} ha sido agregado al sistema.")

def jugar():
    # Cargar la base de datos desde el archivo (si existe)
    global superheroes
    superheroes = cargar_base_datos()
    
    heroes_restantes = superheroes.copy()
    intentos = 0

    print("¡Bienvenido a Adivina el Superhéroe! Tu objetivo es adivinar el superhéroe de DC Comics.")

    while len(heroes_restantes) > 1:
        intentos += 1
        pregunta = generar_pregunta(preguntas)
        caracteristica = preguntas[pregunta]  # Característica asociada a la pregunta

        respuesta = input(pregunta + " (sí/no): ").lower()
        if respuesta not in ["sí", "no"]:
            print("Por favor, responde con 'sí' o 'no'.")
            continue

        # Filtrar los héroes según la respuesta
        if respuesta == "sí":
            heroes_restantes = [heroe for heroe in heroes_restantes if heroe.get(caracteristica) == "sí"]
        else:
            heroes_restantes = [heroe for heroe in heroes_restantes if heroe.get(caracteristica) == "no"]

        if len(heroes_restantes) == 1:
            # Cuando se llega a un héroe, el programa pide confirmación
            posible_heroe = heroes_restantes[0]["nombre"]
            confirmacion = input(f"¿Es {posible_heroe}? (sí/no): ").lower()
            
            if confirmacion == "sí":
                print(f"¡Correcto! El superhéroe es {posible_heroe} en {intentos} intentos.")
                break
            else:
                print("Parece que me equivoqué. Vamos a agregar este superhéroe al sistema.")
                agregar_nuevo_heroe()
                break

        elif len(heroes_restantes) == 0:
            print("No hay ningún superhéroe que coincida con esa descripción.")
            agregar_nuevo_heroe()
            break
        else:
            print(f"{len(heroes_restantes)} héroes restantes. Sigue respondiendo preguntas...")

if __name__ == "__main__":
    jugar()