import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import datetime
import pandas as pd

# Banco de dados
conn = sqlite3.connect('fazenda.db')
c = conn.cursor()

# Tabelas
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    nome TEXT PRIMARY KEY,
    idade INTEGER,
    endereco TEXT,
    pessoas_casa INTEGER,
    renda REAL,
    profissao TEXT,
    apto TEXT,
    local_designado TEXT,
    prazo_comparecimento TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS locais (
    nome_local TEXT PRIMARY KEY,
    endereco TEXT,
    responsavel TEXT,
    contato TEXT,
    andares INTEGER,
    area REAL,
    capacidade_producao REAL,
    apto TEXT,
    mensagem TEXT
)''')

conn.commit()

def verificar_aptidao_usuario(idade, renda):
    return idade >= 18 and renda <= 2000

def calcular_capacidade_producao(andares, area):
    return andares * area * 2

# ---------- Funções de Usuários ----------

def adicionar_usuario():
    def salvar():
        nome = e_nome.get()
        idade = int(e_idade.get())
        endereco = e_endereco.get()
        pessoas_casa = int(e_pessoas.get())
        renda = float(e_renda.get())
        profissao = e_profissao.get()

        apto = verificar_aptidao_usuario(idade, renda)
        local = endereco if apto else "N/A"
        prazo = (datetime.date.today() + datetime.timedelta(days=15)).isoformat() if apto else "N/A"

        c.execute("INSERT OR REPLACE INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (nome, idade, endereco, pessoas_casa, renda, profissao, "Sim" if apto else "Não", local, prazo))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário adicionado.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Adicionar Usuário")

    campos = ["Nome", "Idade", "Endereço", "Pessoas na casa", "Renda", "Profissão"]
    entries = []
    for i, campo in enumerate(campos):
        tk.Label(win, text=f"{campo}:").grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    e_nome, e_idade, e_endereco, e_pessoas, e_renda, e_profissao = entries
    tk.Button(win, text="Salvar", command=salvar).grid(row=len(campos), columnspan=2)

def listar_usuarios():
    win = tk.Toplevel()
    win.title("Usuários")

    c.execute("SELECT * FROM usuarios")
    dados = c.fetchall()
    colunas = [desc[0] for desc in c.description]
    df = pd.DataFrame(dados, columns=colunas)

    tree = ttk.Treeview(win, columns=colunas, show="headings")
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    for row in df.values.tolist():
        tree.insert("", "end", values=row)

    tree.pack(fill='both', expand=True)

def atualizar_usuario():
    def atualizar():
        idade = int(e_idade.get())
        renda = float(e_renda.get())
        apto = verificar_aptidao_usuario(idade, renda)
        local = user[2] if apto else "N/A"
        prazo = (datetime.date.today() + datetime.timedelta(days=30)).isoformat() if apto else "N/A"

        c.execute("UPDATE usuarios SET idade=?, renda=?, apto=?, local_designado=?, prazo_comparecimento=? WHERE nome=?",
                  (idade, renda, "Sim" if apto else "Não", local, prazo, nome))
        conn.commit()
        messagebox.showinfo("Atualizado", "Usuário atualizado.")
        win.destroy()

    nome = simple_input("Nome do usuário a atualizar:")
    c.execute("SELECT * FROM usuarios WHERE nome=?", (nome,))
    user = c.fetchone()
    if not user:
        messagebox.showerror("Erro", "Usuário não encontrado.")
        return

    win = tk.Toplevel()
    win.title("Atualizar Usuário")

    tk.Label(win, text="Idade:").grid(row=0, column=0)
    e_idade = tk.Entry(win)
    e_idade.insert(0, str(user[1]))
    e_idade.grid(row=0, column=1)

    tk.Label(win, text="Renda:").grid(row=1, column=0)
    e_renda = tk.Entry(win)
    e_renda.insert(0, str(user[4]))
    e_renda.grid(row=1, column=1)

    tk.Button(win, text="Atualizar", command=atualizar).grid(row=2, columnspan=2)

def remover_usuario():
    nome = simple_input("Nome do usuário a remover:")
    c.execute("DELETE FROM usuarios WHERE nome=?", (nome,))
    conn.commit()
    messagebox.showinfo("Removido", "Usuário removido.")

# ---------- Funções de Locais ----------

def adicionar_local():
    def salvar():
        nome = e_nome.get()
        endereco = e_endereco.get()
        responsavel = e_resp.get()
        contato = e_contato.get()
        andares = int(e_andares.get())
        area = float(e_area.get())

        capacidade = calcular_capacidade_producao(andares, area)
        apto = "Sim" if capacidade >= 1000 else "Não"
        mensagem = "O responsável será contatado para mais informações."

        c.execute("INSERT OR REPLACE INTO locais VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (nome, endereco, responsavel, contato, andares, area, capacidade, apto, mensagem))
        conn.commit()
        messagebox.showinfo("Sucesso", "Local adicionado.")
        win.destroy()

    win = tk.Toplevel()
    win.title("Adicionar Local")

    labels = ["Nome", "Endereço", "Responsável", "Contato", "Andares", "Área (m²)"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(win, text=f"{label}:").grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    e_nome, e_endereco, e_resp, e_contato, e_andares, e_area = entries
    tk.Button(win, text="Salvar", command=salvar).grid(row=len(labels), columnspan=2)

def listar_locais():
    win = tk.Toplevel()
    win.title("Locais")

    c.execute("SELECT * FROM locais")
    dados = c.fetchall()
    colunas = [desc[0] for desc in c.description]
    df = pd.DataFrame(dados, columns=colunas)

    tree = ttk.Treeview(win, columns=colunas, show="headings")
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    for row in df.values.tolist():
        tree.insert("", "end", values=row)

    tree.pack(fill='both', expand=True)

def atualizar_local():
    def atualizar():
        andares = int(e_andares.get())
        area = float(e_area.get())
        capacidade = calcular_capacidade_producao(andares, area)
        apto = "Sim" if capacidade >= 1000 else "Não"

        c.execute("UPDATE locais SET andares=?, area=?, capacidade_producao=?, apto=? WHERE nome_local=?",
                  (andares, area, capacidade, apto, nome))
        conn.commit()
        messagebox.showinfo("Atualizado", "Local atualizado.")
        win.destroy()

    nome = simple_input("Nome do local a atualizar:")
    c.execute("SELECT * FROM locais WHERE nome_local=?", (nome,))
    local = c.fetchone()
    if not local:
        messagebox.showerror("Erro", "Local não encontrado.")
        return

    win = tk.Toplevel()
    win.title("Atualizar Local")

    tk.Label(win, text="Andares:").grid(row=0, column=0)
    e_andares = tk.Entry(win)
    e_andares.insert(0, str(local[4]))
    e_andares.grid(row=0, column=1)

    tk.Label(win, text="Área:").grid(row=1, column=0)
    e_area = tk.Entry(win)
    e_area.insert(0, str(local[5]))
    e_area.grid(row=1, column=1)

    tk.Button(win, text="Atualizar", command=atualizar).grid(row=2, columnspan=2)

def remover_local():
    nome = simple_input("Nome do local a remover:")
    c.execute("DELETE FROM locais WHERE nome_local=?", (nome,))
    conn.commit()
    messagebox.showinfo("Removido", "Local removido.")

# Utilitário simples de input

def simple_input(msg):
    import tkinter.simpledialog
    return tkinter.simpledialog.askstring("Entrada", msg)

# Menu principal com abas

def menu_principal():
    root = tk.Tk()
    root.title("Gerenciamento de Fazendas Verticais")
    notebook = ttk.Notebook(root)

    # Aba Usuários
    frame_usuarios = tk.Frame(notebook)
    ttk.Button(frame_usuarios, text="Adicionar Usuário", command=adicionar_usuario).pack(pady=5)
    ttk.Button(frame_usuarios, text="Listar Usuários", command=listar_usuarios).pack(pady=5)
    ttk.Button(frame_usuarios, text="Atualizar Usuário", command=atualizar_usuario).pack(pady=5)
    ttk.Button(frame_usuarios, text="Remover Usuário", command=remover_usuario).pack(pady=5)

    # Aba Locais
    frame_locais = tk.Frame(notebook)
    ttk.Button(frame_locais, text="Adicionar Local", command=adicionar_local).pack(pady=5)
    ttk.Button(frame_locais, text="Listar Locais", command=listar_locais).pack(pady=5)
    ttk.Button(frame_locais, text="Atualizar Local", command=atualizar_local).pack(pady=5)
    ttk.Button(frame_locais, text="Remover Local", command=remover_local).pack(pady=5)

    notebook.add(frame_usuarios, text="Gerenciar Usuários")
    notebook.add(frame_locais, text="Gerenciar Locais")
    notebook.pack(expand=True, fill='both')

    root.mainloop()

menu_principal()
