```python
# RPG SYSTEM COMPLETO ATUALIZADO

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
import sys

# ==========================================
# CAMINHO DO BANCO DE DADOS (PYINSTALLER)
# ==========================================

def caminho_arquivo(nome_arquivo):

    if getattr(sys, 'frozen', False):
        pasta_base = sys._MEIPASS
    else:
        pasta_base = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(pasta_base, nome_arquivo)


db_path = caminho_arquivo("rpg_system.db")

# ==========================================
# BANCO DE DADOS
# ==========================================

conexao = sqlite3.connect(db_path)
cursor = conexao.cursor()

# PERSONAGENS
cursor.execute("""
CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    classe TEXT
)
""")

# NPCS
cursor.execute("""
CREATE TABLE IF NOT EXISTS npcs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    funcao TEXT
)
""")

# CAMPANHAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS campanhas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    historia TEXT
)
""")

# SESSÕES
cursor.execute("""
CREATE TABLE IF NOT EXISTS sessoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    campanha_id INTEGER,
    descricao TEXT
)
""")

conexao.commit()

# ==========================================
# JANELA
# ==========================================

janela = tk.Tk()
janela.title("RPG SYSTEM")
janela.geometry("1400x800")
janela.config(bg="#0f172a")

# ==========================================
# CORES
# ==========================================

FUNDO = "#0f172a"
MENU = "#111827"
ROXO = "#6d28d9"
ROXO_CLARO = "#c084fc"
VERMELHO = "#dc2626"
TEXTO = "white"

# ==========================================
# FRAME PRINCIPAL
# ==========================================

frame_principal = tk.Frame(janela, bg=FUNDO)
frame_principal.pack(fill="both", expand=True)

# MENU
menu_lateral = tk.Frame(frame_principal, bg=MENU, width=250)
menu_lateral.pack(side="left", fill="y")

# ÁREA
area = tk.Frame(frame_principal, bg=FUNDO)
area.pack(side="right", fill="both", expand=True)

# ==========================================
# FUNÇÕES AUXILIARES
# ==========================================

def limpar_area():
    for widget in area.winfo_children():
        widget.destroy()


def titulo(texto):
    tk.Label(
        area,
        text=texto,
        font=("Arial", 24, "bold"),
        bg=FUNDO,
        fg=ROXO_CLARO
    ).pack(pady=20)

# ==========================================
# INICIAR
# ==========================================

tela_personagens()

janela.mainloop()

conexao.close()
```
