import tkinter as tk
from tkinter import messagebox
import random

class FortuneTigerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fortune Tiger")

        # Configurações da interface
        self.label = tk.Label(root, text="Clique no botão para girar", font=("Arial", 14))
        self.label.pack(pady=20)

        self.spin_button = tk.Button(root, text="Girar", command=self.girar)
        self.spin_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 24))
        self.result_label.pack(pady=20)

    def girar(self):
        # Gira e mostra o resultado
        resultados = ['🍒', '🍋', '🍊', '🍉', '🍇']
        resultado = [random.choice(resultados) for _ in range(3)]
        self.result_label.config(text=' | '.join(resultado))

        # Verifica se o usuário ganhou
        if resultado[0] == resultado[1] == resultado[2]:
            messagebox.showinfo("Parabéns!", "Você ganhou!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FortuneTigerApp(root)
    root.mainloop()
