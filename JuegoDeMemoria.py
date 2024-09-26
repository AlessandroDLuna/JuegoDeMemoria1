import tkinter as tk
import random
from tkinter import messagebox, simpledialog

# Clase principal del juego
class JuegoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Memoria")
        self.jugador = None
        self.puntaje = 0
        self.nivel = 1
        self.secuencia = []

        # Estructura temporal para guardar los datos del jugador
        self.datos_jugadores = {}

        # Crear el menú principal
        self.menu_principal()

    def menu_principal(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Bienvenido al Juego de Memoria", font=("Arial", 24)).pack(pady=20)

        # Opción para comenzar un nuevo juego
        tk.Button(self.root, text="Nuevo Juego", command=self.nuevo_juego, font=("Arial", 14)).pack(pady=10)

        # Opción para ver las instrucciones
        tk.Button(self.root, text="Instrucciones", command=self.mostrar_instrucciones, font=("Arial", 14)).pack(pady=10)

        # Opción para mostrar puntuaciones
        tk.Button(self.root, text="Ver Puntajes", command=self.mostrar_puntajes, font=("Arial", 14)).pack(pady=10)

    def nuevo_juego(self):
        # Pedir el nombre del jugador
        self.jugador = simpledialog.askstring("Nombre", "Ingresa tu nombre:")
        if not self.jugador:
            return

        # Inicializar el progreso del jugador
        self.puntaje = 0
        self.nivel = 1
        self.datos_jugadores[self.jugador] = {"nivel": self.nivel, "puntaje": self.puntaje}

        self.iniciar_nivel()

    def iniciar_nivel(self):
        self.secuencia = [random.randint(1, 9) for _ in range(self.nivel)]  # Generar secuencia aleatoria
        self.mostrar_secuencia()

    def mostrar_secuencia(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        secuencia_texto = " ".join(map(str, self.secuencia))
        tk.Label(self.root, text=f"Nivel {self.nivel}: Memoriza la secuencia", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text=secuencia_texto, font=("Arial", 24)).pack(pady=20)

        self.root.after(2000, self.esperar_respuesta)  # Dar tiempo para memorizar la secuencia

    def esperar_respuesta(self):
        # Limpiar la ventana para la entrada del jugador
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Nivel {self.nivel}: Ingresa la secuencia", font=("Arial", 18)).pack(pady=20)
        self.entrada = tk.Entry(self.root, font=("Arial", 18))
        self.entrada.pack(pady=20)
        self.entrada.bind('<Return>', self.verificar_respuesta)  # Verificar al presionar Enter
        self.entrada.focus()

    def verificar_respuesta(self, event):
        respuesta = self.entrada.get().split()
        if respuesta == list(map(str, self.secuencia)):
            self.datos_jugadores[self.jugador]["puntaje"] += 10 * self.nivel
            self.nivel += 1
            self.datos_jugadores[self.jugador]["nivel"] = self.nivel
            self.iniciar_nivel()
        else:
            messagebox.showinfo("Error", "Secuencia incorrecta. Inténtalo de nuevo.")
            self.menu_principal()

    def mostrar_instrucciones(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        instrucciones = (
            "Instrucciones:\n\n"
            "1. Se mostrará una secuencia de números.\n"
            "2. Memoriza la secuencia.\n"
            "3. Cuando desaparezca, debes ingresar la secuencia correctamente.\n"
            "4. Cada nivel aumenta la longitud de la secuencia.\n"
            "5. ¡Buena suerte!"
        )
        tk.Label(self.root, text=instrucciones, font=("Arial", 14), justify="left").pack(pady=20)
        tk.Button(self.root, text="Volver al menú", command=self.menu_principal).pack(pady=20)

    def mostrar_puntajes(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Puntajes", font=("Arial", 18)).pack(pady=20)

        for jugador, datos in self.datos_jugadores.items():
            tk.Label(self.root, text=f"{jugador}: Nivel {datos['nivel']}, Puntaje: {datos['puntaje']}",
                     font=("Arial", 14)).pack(pady=5)

        tk.Button(self.root, text="Volver al menú", command=self.menu_principal).pack(pady=20)

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoMemoria(root)
    root.mainloop()
