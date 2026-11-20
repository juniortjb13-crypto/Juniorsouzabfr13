
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from cadastro import salvar_cliente
from metricas import classificar_satisfacao


def salvar_avaliacao():
    nome = campo_nome.get().strip()
    idade_texto = campo_idade.get().strip()
    cidade = campo_cidade.get().strip()
    nota_texto = campo_nota.get().strip()

    # Validar os campos
    if not nome or not idade_texto or not cidade or not nota_texto:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    try:
        idade = int(idade_texto)

        if idade <= 0:
            messagebox.showwarning("Atenção", "Digite uma idade válida.")
            return

        nota = int(nota_texto)

    except ValueError:
        messagebox.showwarning("Atenção", "Verifique a idade e a satisfação.")
        return

    # Organizar os dados do cliente
    cliente = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "nota": nota,
        "data": date.today().isoformat()
    }

    # Salvar no arquivo CSV
    try:
        salvar_cliente(cliente)

        resultado = classificar_satisfacao(nota)

        messagebox.showinfo(
            "Cadastro realizado",
            f"Avaliação salva com sucesso!\n\n{resultado}"
        )

        # Limpar os campos
        campo_nome.delete(0, tk.END)
        campo_idade.delete(0, tk.END)
        campo_cidade.delete(0, tk.END)
        campo_nota.set("")

        campo_nome.focus()

    except Exception as erro:
        messagebox.showerror("Erro", f"Não foi possível salvar:\n{erro}")


# Janela principal
janela = tk.Tk()
janela.title("ConectaMais | Gestão de Satisfação")
janela.geometry("650x520")
janela.configure(bg="#F1F5F9")
janela.resizable(False, False)

# Cabeçalho
cabecalho = tk.Frame(janela, bg="#173B65", height=110)
cabecalho.pack(fill="x")

tk.Label(
    cabecalho,
    text="CONECTAMAIS",
    font=("Arial", 23, "bold"),
    fg="white",
    bg="#173B65"
).pack(pady=(20, 5))

tk.Label(
    cabecalho,
    text="Sistema de Gestão da Satisfação de Clientes",
    font=("Arial", 11),
    fg="#DCEAFE",
    bg="#173B65"
).pack()

# Área do formulário
formulario = tk.Frame(janela, bg="white", padx=35, pady=25)
formulario.pack(padx=45, pady=30, fill="both")

tk.Label(
    formulario,
    text="NOVO CADASTRO",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#173B65"
).pack(anchor="w", pady=(0, 20))


def criar_campo(texto):
    tk.Label(
        formulario,
        text=texto,
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#334155"
    ).pack(anchor="w", pady=(8, 4))


criar_campo("Nome do cliente")
campo_nome = ttk.Entry(formulario, font=("Arial", 11))
campo_nome.pack(fill="x")

criar_campo("Idade")
campo_idade = ttk.Entry(formulario, font=("Arial", 11))
campo_idade.pack(fill="x")

criar_campo("Cidade")
campo_cidade = ttk.Entry(formulario, font=("Arial", 11))
campo_cidade.pack(fill="x")

criar_campo("Satisfação com o atendimento")

campo_nota = ttk.Combobox(
    formulario,
    values=["1", "2", "3", "4", "5"],
    state="readonly",
    font=("Arial", 11)
)
campo_nota.pack(fill="x")

# Botão salvar
botao_salvar = tk.Button(
    formulario,
    text="SALVAR AVALIAÇÃO",
    command=salvar_avaliacao,
    font=("Arial", 11, "bold"),
    bg="#167D58",
    fg="white",
    activebackground="#116344",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    pady=12
)
botao_salvar.pack(fill="x", pady=(25, 5))

tk.Label(
    janela,
    text="ConectaMais © 2026",
    font=("Arial", 9),
    bg="#F1F5F9",
    fg="#64748B"
).pack()

campo_nome.focus()

janela.mainloop()
