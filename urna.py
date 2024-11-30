import tkinter as tk
from tkinter import messagebox

class UrnaEletronica:
    def __init__(self, master):
        self.master = master
        self.master.title("Urna Eletrônica")
        self.master.geometry("400x400")

        self.titulo_elector = None
        self.voto = {}

        # Dicionário simulando a base de dados de eleitores
        self.eleitores = {
            "123456": {"nome": "Gabriel Frade", "estado": "Minas Gerais"},
            "654321": {"nome": "Ana Silva", "estado": "São Paulo"},
            "987654": {"nome": "Carlos Souza", "estado": "Rio de Janeiro"},
            # Adicione mais títulos e eleitores conforme necessário
        }

        self.create_tela_inicial()

    def create_tela_inicial(self):
        """Cria a tela inicial onde o eleitor entra com o título de eleitor"""
        self.clear_screen()

        tk.Label(self.master, text="Título de Eleitor", font=("Arial", 14)).pack(pady=20)
        self.titulo_entry = tk.Entry(self.master, font=("Arial", 12))
        self.titulo_entry.pack(pady=10)
        
        tk.Button(self.master, text="Confirmar", font=("Arial", 12), command=self.validar_titulo).pack(pady=20)

    def validar_titulo(self):
        """Valida o título de eleitor e exibe as informações do eleitor"""
        titulo = self.titulo_entry.get()
        
        if titulo in self.eleitores:  # Verifica se o título existe no dicionário
            self.titulo_elector = titulo
            eleitor = self.eleitores[titulo]
            self.create_tela_votacao(eleitor)
        else:
            messagebox.showerror("Erro", "Título de eleitor inválido!")

    def create_tela_votacao(self, eleitor):
        """Cria a tela de votação com cargos e candidatos"""
        self.clear_screen()

        # Exibe as informações do eleitor (nome e estado)
        tk.Label(self.master, text=f"Eleitor: {eleitor['nome']} de {eleitor['estado']}", font=("Arial", 14)).pack(pady=20)

        cargos = ['Presidente', 'Governador', 'Senador']
        self.candidatos = {
            'Presidente': ['João da Silva', 'Tilápia Frade'],
            'Governador': ['Manoel Gomes', 'Ronaldinho Gaúcho'],
            'Senador': ['Frederico José', 'Tranquedo Neves']
        }

        for cargo in cargos:
            tk.Label(self.master, text=f"Escolha um candidato para {cargo}:").pack(pady=5)
            var = tk.StringVar()
            var.set(None)
            for candidato in self.candidatos[cargo]:
                tk.Radiobutton(self.master, text=candidato, variable=var, value=candidato).pack(anchor="w")
            self.voto[cargo] = var

        tk.Button(self.master, text="Confirmar Voto", font=("Arial", 12), command=self.confirmar_voto).pack(pady=20)

    def confirmar_voto(self):
        """Confirma o voto e simula a ação de votar"""
        votos = {}
        for cargo, var in self.voto.items():
            votos[cargo] = var.get()

        if all(voto for voto in votos.values()):
            self.voto = votos
            self.create_tela_confirmacao()
        else:
            messagebox.showerror("Erro", "Você precisa votar em todos os cargos!")

    def create_tela_confirmacao(self):
        """Cria a tela de confirmação do voto"""
        self.clear_screen()

        tk.Label(self.master, text="Confirmação de Voto", font=("Arial", 14)).pack(pady=20)

        for cargo, candidato in self.voto.items():
            tk.Label(self.master, text=f"{cargo}: {candidato}", font=("Arial", 12)).pack(pady=5)

        tk.Button(self.master, text="Confirmar", font=("Arial", 12), command=self.finalizar_voto).pack(pady=20)
        tk.Button(self.master, text="Cancelar", font=("Arial", 12), command=self.create_tela_votacao).pack(pady=5)

    def salvar_voto(self):
        """Salva o voto em um arquivo de texto"""
        with open("votos.txt", "a") as f:
            f.write(f"Título de Eleitor: {self.titulo_elector}\n")
            for cargo, candidato in self.voto.items():
                f.write(f"{cargo}: {candidato}\n")
            f.write("-" * 40 + "\n")

    def finalizar_voto(self):
        """Finaliza o processo de votação e salva o voto"""
        # Salvar voto no arquivo
        self.salvar_voto()

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", "Voto registrado com sucesso!")

        # Encerrar o aplicativo
        self.master.quit()

    def clear_screen(self):
        """Limpa a tela para mostrar uma nova interface"""
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = UrnaEletronica(root)
    root.mainloop()