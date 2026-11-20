
import tkinter.messagebox as messagebox
import customtkinter as ctk
from datetime import date

from cadastro import salvar_cliente
from metricas import classificar_satisfacao
from dashboard import obter_indicadores, gerar_graficos
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ==========================================
# CONFIGURAÇÃO VISUAL
# ==========================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

AZUL_ESCURO = "#173B65"
AZUL_MEDIO = "#245786"
FUNDO = "#F1F6FB"
BRANCO = "#FFFFFF"
TEXTO = "#263B50"
VERDE = "#119B83"


# ==========================================
# FUNÇÃO DE SALVAMENTO
# ==========================================

def salvar_avaliacao():

    nome = campo_nome.get().strip()
    idade_texto = campo_idade.get().strip()
    cidade = campo_cidade.get().strip()
    nota_texto = campo_nota.get().strip()

    if not nome or not idade_texto or not cidade or not nota_texto:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    try:
        idade = int(idade_texto)
        nota = int(nota_texto)

        if idade <= 0:
            messagebox.showwarning(
                "Atenção",
                "Digite uma idade válida."
            )
            return

        if nota < 1 or nota > 5:
            messagebox.showwarning(
                "Atenção",
                "A satisfação deve estar entre 1 e 5."
            )
            return

    except ValueError:
        messagebox.showwarning(
            "Atenção",
            "Verifique a idade e a satisfação."
        )
        return

    cliente = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "nota": nota,
        "data": date.today().isoformat()
    }

    try:
        salvar_cliente(cliente)

        resultado = classificar_satisfacao(nota)

        messagebox.showinfo(
            "Cadastro realizado",
            f"Avaliação salva com sucesso!\n\n{resultado}"
        )

        campo_nome.delete(0, "end")
        campo_idade.delete(0, "end")
        campo_cidade.delete(0, "end")
        campo_nota.set("")

        campo_nome.focus()

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar:\n{erro}"
        )


def abrir_dashboard():
    dados = obter_indicadores()

    painel = ctk.CTkToplevel(janela)
    painel.title("ConectaMais | Dashboard")
    painel.geometry("1050x680")
    painel.minsize(900, 600)
    painel.configure(fg_color=FUNDO)

    titulo = ctk.CTkLabel(
        painel,
        text="Dashboard de Satisfação",
        font=("Arial", 26, "bold"),
        text_color=AZUL_ESCURO
    )
    titulo.pack(pady=(20, 15))

    # RESUMO DOS INDICADORES
    resumo = ctk.CTkFrame(
        painel,
        fg_color=BRANCO,
        corner_radius=15
    )
    resumo.pack(fill="x", padx=25, pady=10)

    indicadores = [
        ("Total de avaliações", dados["total_clientes"]),
        ("Média de satisfação", dados["media_satisfacao"]),
        ("Clientes satisfeitos", dados["satisfeitos"]),
        ("Clientes regulares", dados["regulares"]),
        ("Clientes insatisfeitos", dados["insatisfeitos"])
    ]

    for i, (nome, valor) in enumerate(indicadores):
        item = ctk.CTkLabel(
            resumo,
            text=f"{nome}: {valor}",
            font=("Arial", 14, "bold"),
            text_color=AZUL_ESCURO
        )
        item.grid(
            row=i // 3,
            column=i % 3,
            padx=15,
            pady=12,
            sticky="w"
        )

    # ÁREA DOS GRÁFICOS
    area_graficos = ctk.CTkFrame(
        painel,
        fg_color=FUNDO
    )
    area_graficos.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=15
    )

    area_graficos.grid_columnconfigure(0, weight=1)
    area_graficos.grid_columnconfigure(1, weight=1)
    area_graficos.grid_rowconfigure(0, weight=1)

    # GRÁFICO 1 - SATISFAÇÃO DOS CLIENTES
    quadro1 = ctk.CTkFrame(
        area_graficos,
        fg_color=BRANCO,
        corner_radius=12
    )
    quadro1.grid(
        row=0,
        column=0,
        padx=8,
        pady=5,
        sticky="nsew"
    )

    figura1 = Figure(figsize=(4.5, 3.5), dpi=100)
    eixo1 = figura1.add_subplot(111)

    categorias = [
        "Satisfeitos",
        "Regulares",
        "Insatisfeitos"
    ]

    quantidades = [
        dados["satisfeitos"],
        dados["regulares"],
        dados["insatisfeitos"]
    ]

    eixo1.bar(categorias, quantidades)
    eixo1.set_title("Satisfação dos Clientes")
    eixo1.set_ylabel("Quantidade")
    eixo1.tick_params(axis="x", labelrotation=15)

    figura1.tight_layout()

    canvas1 = FigureCanvasTkAgg(
        figura1,
        master=quadro1
    )
    canvas1.draw()
    canvas1.get_tk_widget().pack(
        fill="both",
        expand=True,
        padx=8,
        pady=8
    )

    # GRÁFICO 2 - EVOLUÇÃO MENSAL
    quadro2 = ctk.CTkFrame(
        area_graficos,
        fg_color=BRANCO,
        corner_radius=12
    )
    quadro2.grid(
        row=0,
        column=1,
        padx=8,
        pady=5,
        sticky="nsew"
    )

    figura2 = Figure(figsize=(4.5, 3.5), dpi=100)
    eixo2 = figura2.add_subplot(111)

    medias_mensais = dados["media_mensal"]

    meses = list(medias_mensais.keys())
    valores = list(medias_mensais.values())

    eixo2.plot(
        meses,
        valores,
        marker="o",
        linewidth=2,
        label="Média mensal"
    )

    eixo2.axhline(
        y=3,
        linestyle="--",
        label="Meta de satisfação"
    )

    eixo2.set_title("Evolução da Satisfação Mensal")
    eixo2.set_xlabel("Mês")
    eixo2.set_ylabel("Média")
    eixo2.set_ylim(0, 5)
    eixo2.grid(True)
    eixo2.legend()

    figura2.tight_layout()

    canvas2 = FigureCanvasTkAgg(
        figura2,
        master=quadro2
    )
    canvas2.draw()
    canvas2.get_tk_widget().pack(
        fill="both",
        expand=True,
        padx=8,
        pady=8
    )

# ==========================================
# JANELA PRINCIPAL
# ==========================================

janela = ctk.CTk()

janela.title("ConectaMais | Gestão de Satisfação")
janela.geometry("850x820")
janela.minsize(700, 650)
janela.configure(fg_color=FUNDO)


# ==========================================
# CABEÇALHO
# ==========================================

cabecalho = ctk.CTkFrame(
    janela,
    fg_color=AZUL_ESCURO,
    corner_radius=0,
    height=145
)

cabecalho.pack(fill="x")
cabecalho.pack_propagate(False)

titulo = ctk.CTkLabel(
    cabecalho,
    text="CONECTAMAIS",
    font=("Arial", 30, "bold"),
    text_color=BRANCO
)

titulo.pack(pady=(25, 5))

subtitulo = ctk.CTkLabel(
    cabecalho,
    text="GESTÃO INTELIGENTE DA SATISFAÇÃO DE CLIENTES",
    font=("Arial", 12),
    text_color="#D8E8F7"
)

subtitulo.pack()


# ==========================================
# CARTÃO DO FORMULÁRIO
# ==========================================

cartao = ctk.CTkFrame(
    janela,
    fg_color=BRANCO,
    corner_radius=18,
    border_width=1,
    border_color="#DFE8F1"
)

cartao.pack(
    padx=35,
    pady=10,
    fill="both",
    expand=True
)


titulo_formulario = ctk.CTkLabel(
    cartao,
    text="Novo cadastro",
    font=("Arial", 24, "bold"),
    text_color=AZUL_ESCURO
)

titulo_formulario.pack(
    anchor="w",
    padx=35,
    pady=(30, 5)
)


descricao = ctk.CTkLabel(
    cartao,
    text="Preencha os dados para registrar uma avaliação.",
    font=("Arial", 12),
    text_color="#718096"
)

descricao.pack(
    anchor="w",
    padx=35,
    pady=(0, 18)
)


# ==========================================
# CAMPOS DO FORMULÁRIO
# ==========================================

def criar_campo(texto):

    rotulo = ctk.CTkLabel(
        cartao,
        text=texto,
        font=("Arial", 13, "bold"),
        text_color=TEXTO
    )

    rotulo.pack(
        anchor="w",
        padx=35,
        pady=(5, 2)
    )


criar_campo("Nome do cliente")

campo_nome = ctk.CTkEntry(
    cartao,
    placeholder_text="Digite o nome do cliente",
    height=36,
    corner_radius=9,
    border_color="#CBD8E5",
    font=("Arial", 13)
)

campo_nome.pack(fill="x", padx=35)


criar_campo("Idade")

campo_idade = ctk.CTkEntry(
    cartao,
    placeholder_text="Digite a idade",
    height=42,
    corner_radius=9,
    border_color="#CBD8E5",
    font=("Arial", 13)
)

campo_idade.pack(fill="x", padx=35)


criar_campo("Cidade")

campo_cidade = ctk.CTkEntry(
    cartao,
    placeholder_text="Digite a cidade",
    height=42,
    corner_radius=9,
    border_color="#CBD8E5",
    font=("Arial", 13)
)

campo_cidade.pack(fill="x", padx=35)


criar_campo("Satisfação com o atendimento")

campo_nota = ctk.CTkComboBox(
    cartao,
    values=["1", "2", "3", "4", "5"],
    state="readonly",
    height=42,
    corner_radius=9,
    border_color="#CBD8E5",
    font=("Arial", 13),
    dropdown_fg_color=BRANCO
)

campo_nota.pack(fill="x", padx=35)
campo_nota.set("")


# ==========================================
# BOTÃO SALVAR
# ==========================================

botao_salvar = ctk.CTkButton(
    cartao,
    text="SALVAR AVALIAÇÃO",
    command=salvar_avaliacao,
    height=48,
    corner_radius=10,
    fg_color=VERDE,
    hover_color="#0D806D",
    text_color=BRANCO,
    font=("Arial", 14, "bold"),
    cursor="hand2"
)

botao_salvar.pack(
    fill="x",
    padx=35,
    pady=(30, 25)
)



botao_dashboard = ctk.CTkButton(
    cartao,
    text="VISUALIZAR DASHBOARD",
    command=abrir_dashboard,
    height=45,
    corner_radius=10,
    fg_color=AZUL_MEDIO,
    hover_color=AZUL_ESCURO,
    text_color=BRANCO,
    font=("Arial", 13, "bold"),
    cursor="hand2"
)

botao_dashboard.pack(
    fill="x",
    padx=35,
    pady=(0, 25)
)

# ==========================================
# RODAPÉ
# ==========================================

# ==========================================
# RODAPÉ
# ==========================================

rodape = ctk.CTkLabel(
    janela,
    text="ConectaMais © 2026 | Conectando dados e decisões",
    font=("Arial", 11),
    text_color="#718096"
)

rodape.pack(pady=(0, 18))


campo_nome.focus()

janela.mainloop()
