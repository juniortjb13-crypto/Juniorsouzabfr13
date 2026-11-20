
import streamlit as st
import pandas as pd
import os
from datetime import date
from supabase import create_client
from supabase import create_client
import plotly.graph_objects as go

# Conexão com o Supabase
supabase = create_client(
    st.secrets["supabase"]["url"],
    st.secrets["supabase"]["key"]
)

# =====================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================

st.set_page_config(
    page_title="ConectaMais | Gestão de Satisfação",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================
# IDENTIDADE VISUAL CONECTAMAIS
# =====================================

st.markdown("""
<style>

/* Fundo original */
.stApp,
[data-testid="stAppViewContainer"] {
    background-color: #F1F6FB;
}

/* Cabeçalho transparente */
[data-testid="stHeader"] {
    background: transparent;
}

/* Barra lateral */
[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #DFE8F1;
}

/* Área principal */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Títulos */
h1, h2, h3 {
    color: #173B65 !important;
    font-family: Arial, sans-serif;
}

/* Texto */
p, label, span {
    font-family: Arial, sans-serif;
}

/* Cartões de métricas */
/* Cartões modernos do Dashboard */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #FFFFFF, #F5F9FF);
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #DCE8F5;
    box-shadow: 0 5px 16px rgba(23, 59, 101, 0.08);
    transition: all 0.25s ease;
}

/* Efeito ao passar o mouse */
[data-testid="stMetric"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 9px 22px rgba(23, 59, 101, 0.13);
    border-color: #A9C9ED;
}

/* Títulos dos indicadores */
[data-testid="stMetricLabel"] {
    color: #58718E;
    font-weight: 600;
}

/* Números dos indicadores */
[data-testid="stMetricValue"] {
    color: #1053A3;
    font-weight: 800;
}

/* Valores das métricas */
[data-testid="stMetricValue"] {
    color: #173B65;
    font-weight: 700;
}

/* Botões */
/* Botões */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(135deg, #1557A5, #2185D0);
    color: #FFFFFF;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 46px;
    padding: 0 22px;
    box-shadow: 0 4px 10px rgba(21, 87, 165, 0.18);
    transition: all 0.25s ease;
}

/* Efeito ao passar o mouse */
.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #104580;
    color: #FFFFFF;
    border: none;
}
/* Estrelas de avaliação */
[data-testid="stFeedback"] button {
    background: transparent !important;
    border: none !important;
    border-radius: 10px;
    padding: 8px !important;
    transition: all 0.2s ease;
}

/* Efeito ao passar o mouse */
[data-testid="stFeedback"] button:hover {
    background: #E5F0FF !important;
    transform: scale(1.18);
}

/* Cor dourada das estrelas */
[data-testid="stFeedback"] button svg {
    color: #F5B301 !important;
    fill: #F5B301 !important;
}

/* Campos de formulário */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 9px;
}

/* Barra lateral */
[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #DFE8F1;
}

/* Divisórias */
hr {
    border-color: #DFE8F1;
}

/* Avaliação por estrelas */
[data-testid="stRadio"] [role="radiogroup"] {
    gap: 18px;
    align-items: center;
}

[data-testid="stRadio"] [role="radio"] {
    font-size: 30px;
    color: #F5B82E;
}

[data-testid="stRadio"] [role="radio"][aria-checked="true"] {
    color: #D99B00;
    font-weight: 900;
}
/* =================================
   HERO - CABEÇALHO CONECTAMAIS
================================= */

.hero-conectamais {
    background: linear-gradient(120deg, #0B3D91, #1176C9, #21A1E1);
    border-radius: 22px;
    padding: 55px 50px;
    min-height: 280px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 30px rgba(11, 61, 145, 0.18);
    margin-bottom: 35px;
}

.hero-conteudo {
    max-width: 700px;
    position: relative;
    z-index: 2;
}

.hero-etiqueta {
    color: #C7E8FF;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-conectamais h1 {
    color: #FFFFFF !important;
    font-size: 42px;
    font-weight: 800;
    line-height: 1.15;
    margin: 18px 0;
}

.hero-conectamais p {
    color: #E5F3FF;
    font-size: 17px;
    line-height: 1.7;
    max-width: 600px;
}

.hero-icone {
    color: rgba(255, 255, 255, 0.18);
    font-size: 170px;
    font-weight: 700;
    padding-right: 35px;
}

/* ===== AJUSTES PARA CELULARES ===== */
@media screen and (max-width: 768px) {

    .block-container {
        padding: 1rem 0.8rem 2rem !important;
        max-width: 100% !important;
    }

    .hero-conectamais h1 {
    width: 100% !important;
    max-width: 100% !important;
    font-size: 2rem !important;
    line-height: 1.2 !important;
    white-space: normal !important;
    overflow-wrap: break-word !important;
    word-break: normal !important;
    text-align: left !important;
    box-sizing: border-box !important;
}

    h2 {
        font-size: 1.45rem !important;
    }

    h3 {
        font-size: 1.2rem !important;
    }

    .hero-conectamais {
        width: 100% !important;
        max-width: 100% !important;
        padding: 24px 20px !important;
        box-sizing: border-box !important;
        overflow-wrap: normal !important;
        word-break: normal !important;
    }

    .hero-conectamais h1,
.hero-conectamais p {
    width: 100% !important;
    max-width: 100% !important;
    white-space: normal !important;
    overflow-wrap: break-word !important;
    word-break: normal !important;
    box-sizing: border-box !important;
}

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100% !important;
        min-height: 46px !important;
    }

    [data-testid="stMetric"] {
        padding: 14px !important;
    }

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        max-width: 100% !important;
    }
}

</style> 
""", unsafe_allow_html=True)

ARQUIVO_DADOS = "clientes.csv"

# CABEÇALHO PRINCIPAL


st.markdown("""
<div style="display:flex; align-items:center; gap:22px; flex-wrap:wrap;
padding:18px 24px; margin-bottom:24px; background:#FFFFFF;
border:1px solid #E2EAF4; border-radius:14px;
box-shadow:0 4px 16px rgba(15,50,100,0.06);">

<div style="font-size:23px;font-weight:800;color:#1053A3;">
ConectaMais<span style="color:#20A4E8;">.</span>
</div>

<div style="display:flex;align-items:center;gap:22px;flex-wrap:wrap;">
<a href="#inicio" style="color:#173B65;text-decoration:none;font-weight:600;">Início</a>
<a href="#avaliar-servico" style="color:#173B65;text-decoration:none;font-weight:600;">Avaliar serviço</a>
<a href="#comentarios" style="color:#173B65;text-decoration:none;font-weight:600;">Comentários</a>
<a href="#dashboard" style="color:#173B65;text-decoration:none;font-weight:600;">Dashboard</a>
<a href="#avaliar-servico" style="background:#1053A3;color:white;padding:11px 18px;border-radius:9px;text-decoration:none;font-weight:700;">Avaliar agora →</a>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-conectamais">
    <div class="hero-conteudo">
        <span class="hero-etiqueta">CONECTAMAIS • EXPERIÊNCIA E QUALIDADE</span>
        <h1>Sua opinião transforma serviços.</h1>
        <p>
            Avalie experiências, compartilhe sua opinião e ajude
            estabelecimentos a oferecer um atendimento cada vez melhor.
        </p>
    </div>
    <div class="hero-icone">✦</div>
</div>
""", unsafe_allow_html=True)
# ==============================
# ACESSO DO ADMINISTRADOR
# ==============================

if "admin_autenticado" not in st.session_state:
    st.session_state.admin_autenticado = False

with st.sidebar:
    st.subheader("Área administrativa")

    senha_digitada = st.text_input(
        "Senha de administrador",
        type="password"
    )

    if st.button("Entrar"):
        if senha_digitada == st.secrets["admin"]["senha"]:
            st.session_state.admin_autenticado = True
            st.success("Acesso autorizado!")
            st.rerun()
        else:
            st.error("Senha incorreta.")

    if st.session_state.admin_autenticado:
        st.success("Administrador conectado.")

        if st.button("Sair da administração"):
            st.session_state.admin_autenticado = False
            st.rerun()

# =====================================
# CARREGAMENTO DOS DADOS
# =====================================


def carregar_dados():
    resposta = supabase.table("avaliacoes").select(
        "id,tipo_servico,estabelecimento,cidade,nota,comentario,data"
    ).order("data", desc=True).execute()

    dados = pd.DataFrame(resposta.data)

    colunas = [
        "id",
        "tipo_servico",
        "estabelecimento",
        "cidade",
        "nota",
        "comentario",
        "data"
    ]

    if dados.empty:
        return pd.DataFrame(columns=colunas)

    return dados

# =====================================

# ==================================
# FORMULÁRIO DE AVALIAÇÃO
# ==================================
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
st.markdown('<div id="avaliar-servico"></div>', unsafe_allow_html=True)
st.header("📝 Avalie um serviço")

with st.form("formulario_avaliacao"):
    tipo_servico = st.selectbox(
        "Qual serviço você utilizou?",
        [
            "Barbearia",
            "Salão de beleza",
            "Restaurante",
            "Lanchonete",
            "Oficina mecânica",
            "Mercado",
            "Outro"
        ]
    )

    estabelecimento = st.text_input(
        "Nome do estabelecimento (opcional)"
    )

    cidade = st.text_input("Cidade")

    avaliacao_estrelas = st.feedback("stars")

    nota = None if avaliacao_estrelas is None else avaliacao_estrelas + 1
    if avaliacao_estrelas is not None:
        st.caption(f"⭐ Nota selecionada: {nota}/5")
    else:
        st.caption("Selecione uma estrela para avaliar.")
    comentario = st.text_area(
        "Conte um pouco sobre sua experiência (opcional)"
    )

    enviar = st.form_submit_button("Enviar avaliação")

if enviar:
    if nota is None:
        st.warning("Selecione uma nota antes de enviar sua avaliação.")
    elif not cidade.strip():
        st.warning("Informe a cidade onde utilizou o serviço.")
    else:
        novo_registro = {
            "tipo_servico": tipo_servico,
            "estabelecimento": estabelecimento.strip(),
            "cidade": cidade.strip(),
            "nota": nota,
            "comentario": comentario.strip()
        }

        supabase.table("avaliacoes").insert(novo_registro).execute()

        st.success("Obrigado! Sua avaliação foi registrada.")


# ==================================
# GERENCIAMENTO DE AVALIAÇÕES
# ==================================

if st.session_state.admin_autenticado:
    st.divider()
    st.header("🗑️ Gerenciar avaliações")

    dados_exclusao = carregar_dados()

    if dados_exclusao.empty:
        st.info("Não existem avaliações para excluir.")
    else:
        def identificar_avaliacao(id_avaliacao):
            registro = dados_exclusao[
                dados_exclusao["id"] == id_avaliacao
            ].iloc[0]

            estabelecimento = registro["estabelecimento"]

            if not estabelecimento:
                estabelecimento = "Estabelecimento não informado"

            return (
                f"{registro['tipo_servico']} | "
                f"{estabelecimento} | "
                f"{registro['cidade']} | "
                f"Nota: {registro['nota']}"
            )

        selecionada = st.selectbox(
            "Selecione a avaliação que deseja excluir:",
            options=dados_exclusao["id"].tolist(),
            format_func=identificar_avaliacao
        )

        confirmar = st.checkbox(
            "Confirmo que desejo excluir esta avaliação."
        )

        if st.button("Excluir avaliação"):
            if confirmar:
                supabase.table("avaliacoes").delete().eq(
                    "id", selecionada
                ).execute()

                st.success("Avaliação excluída com sucesso!")
                st.rerun()
            else:
                st.warning("Marque a confirmação antes de excluir.")


# =====================================
# DASHBOARD
# =====================================

st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)
st.divider()
st.header("📊 Dashboard de satisfação")

dados = carregar_dados()

if dados.empty:
    st.info("Ainda não existem avaliações cadastradas.")
else:
    dados["nota"] = pd.to_numeric(dados["nota"], errors="coerce")
    dados = dados.dropna(subset=["nota"])


    # FILTROS DO DASHBOARD
    st.subheader("🔎 Filtrar avaliações")

    coluna1, coluna2, coluna3 = st.columns(3)

    servicos = ["Todos"] + sorted(dados["tipo_servico"].dropna().astype(str).unique().tolist())
    estabelecimentos = ["Todos"] + sorted(dados["estabelecimento"].dropna().astype(str).unique().tolist())
    cidades = ["Todas"] + sorted(dados["cidade"].dropna().astype(str).unique().tolist())

    with coluna1:
        filtro_servico = st.selectbox("Tipo de serviço", servicos)

    with coluna2:
        filtro_estabelecimento = st.selectbox("Estabelecimento", estabelecimentos)

    with coluna3:
        filtro_cidade = st.selectbox("Cidade", cidades)

    dados_filtrados = dados.copy()

    if filtro_servico != "Todos":
        dados_filtrados = dados_filtrados[dados_filtrados["tipo_servico"] == filtro_servico]

    if filtro_estabelecimento != "Todos":
        dados_filtrados = dados_filtrados[dados_filtrados["estabelecimento"] == filtro_estabelecimento]

    if filtro_cidade != "Todas":
        dados_filtrados = dados_filtrados[dados_filtrados["cidade"] == filtro_cidade]

    if dados_filtrados.empty:
        st.info("Nenhuma avaliação encontrada para os filtros selecionados.")


    total = len(dados_filtrados)
    media = dados_filtrados["nota"].mean()
    satisfeitos = (dados_filtrados["nota"] >= 4).sum()
    regulares = (dados_filtrados["nota"] == 3).sum()
    insatisfeitos = (dados_filtrados["nota"] < 3).sum()

    coluna1, coluna2, coluna3, coluna4 = st.columns(4)

    coluna1.metric("Total de avaliações", total)
    coluna2.metric("Média de satisfação", f"{media:.2f}/5")
    coluna3.metric("Satisfeitos", int(satisfeitos))
    coluna4.metric("Insatisfeitos", int(insatisfeitos))

    

    # DISTRIBUIÇÃO DAS AVALIAÇÕES
    st.subheader("Distribuição das avaliações")

    distribuicao = (
        dados_filtrados["nota"]
        .value_counts()
        .reindex([1, 2, 3, 4, 5], fill_value=0)
    )

    fig_distribuicao = go.Figure()

    fig_distribuicao.add_trace(go.Bar(
    x=["1", "2", "3", "4", "5"],
    y=distribuicao.values,
    marker=dict(
        color=[
            "#E05252",
            "#E05252",
            "#F2C94C",
            "#27AE60",
            "#27AE60"
        ],
        line=dict(color="#FFFFFF", width=1.5)
    ),
    text=distribuicao.values,
    textposition="outside",
    textfont=dict(size=15, color="#173B65"),
    hovertemplate="Nota: %{x}<br>Avaliações: %{y}<extra></extra>"
))

    fig_distribuicao.update_layout(
        height=390,
        template="plotly_white",
        xaxis_title="Nota atribuída",
        yaxis_title="Quantidade de avaliações",
        xaxis=dict(
            tickmode="array",
            tickvals=["1", "2", "3", "4", "5"],
            showgrid=False
        ),
        yaxis=dict(
            rangemode="tozero",
            gridcolor="#E5EDF6",
            zeroline=False
        ),
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=25, r=25, t=35, b=45),
        font=dict(
            family="Arial",
            color="#173B65",
            size=13
        ),
        showlegend=False
    )

    st.plotly_chart(fig_distribuicao, use_container_width=True)

    # EVOLUÇÃO MENSAL
    st.subheader("Evolução mensal")

    dados_filtrados["data"] = pd.to_datetime(
        dados_filtrados["data"],
        errors="coerce",
        utc=True
    ).dt.tz_convert(None)

    dados_validos = dados_filtrados.dropna(subset=["data"]).copy()

    if not dados_validos.empty:

        dados_validos["mes"] = (
            dados_validos["data"].dt.to_period("M").astype(str)
        )

        evolucao = (
    dados_validos.groupby("mes")
    .agg(
        Media=("nota", "mean"),
        Quantidade=("nota", "count")
    )
    .reset_index()
    .sort_values("mes")
)
        evolucao["mes_exibicao"] = pd.to_datetime(
        evolucao["mes"]
        ).dt.strftime("%b/%Y")
        fig_evolucao = go.Figure()

        fig_evolucao.add_trace(go.Scatter(
                x=evolucao["mes"],
                y=evolucao["Media"],
                mode="lines+markers+text",
                line=dict(
                    color="#1769C2",
                    width=4,
                    shape="spline"
                ),
                marker=dict(
                    size=11,
                    color="#1769C2",
                    line=dict(color="white", width=2)
                ),
                fill="tozeroy",
                fillcolor="rgba(23, 105, 194, 0.13)",
                text=evolucao["Media"].round(2),
                textposition="top center",
                textfont=dict(
                    size=13,
                    color="#173B65"
                ),
                hovertemplate=(
                    "Mês: %{x}<br>"
                    "Média de satisfação: %{y:.2f}/5"
                    "<extra></extra>"
                )
            ))

        fig_evolucao.add_trace(go.Bar(
    x=evolucao["mes"],
    y=evolucao["Quantidade"],
    name="Quantidade de avaliações",
    marker_color="#119B83",
    yaxis="y2",
    opacity=0.65
))
        fig_evolucao.update_layout(
                height=410,
                template="plotly_white",
                xaxis_title="Período",
                yaxis_title="Média das notas",
                yaxis=dict(
                    range=[0, 5.5],
                    dtick=1,
                    gridcolor="#E5EDF6"
                ),
                        yaxis2=dict(
            title="Quantidade de avaliações",
            overlaying="y",
            side="right",
            showgrid=False,
            rangemode="tozero"
        ),
                xaxis=dict(
        type="category",
        title="Mês",
        showgrid=False,
        tickangle=0,
        categoryorder="array",
        categoryarray=evolucao["mes"].tolist()
        ),
                plot_bgcolor="white",
                paper_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=25, r=25, t=45, b=45),
                font=dict(
                    family="Arial",
                    color="#173B65",
                    size=13
                ),
            )

        st.plotly_chart(fig_evolucao, use_container_width=True)

    else:
        st.info("Não há dados suficientes para exibir a evolução mensal.")


    if st.session_state.admin_autenticado:
        st.subheader("Avaliações registradas")
        st.dataframe(dados_filtrados, use_container_width=True)
    else:
        st.info("Os registros individuais são restritos à área administrativa.")

    # COMENTÁRIOS DOS PARTICIPANTES
    st.markdown('<div id="comentarios"></div>', unsafe_allow_html=True)
    st.divider()
    st.subheader("💬 Comentários dos participantes")

    comentarios_publicos = dados_filtrados[
        dados_filtrados["comentario"].fillna("").astype(str).str.strip() != ""
    ].sort_values("data", ascending=False)

    if not comentarios_publicos.empty:
        for _, avaliacao in comentarios_publicos.iterrows():
            with st.container(border=True):
                coluna1, coluna2 = st.columns([3, 1])

                with coluna1:
                    st.markdown(f"**{avaliacao['tipo_servico']}**")

                with coluna2:
                    st.markdown(f"⭐ **{avaliacao['nota']}/5**")

                st.markdown("---")
                st.write(avaliacao["comentario"])
    else:
        st.info("Ainda não existem comentários registrados.")
    st.caption("ConectaMais © 2026 | Conectando dados e decisões")


st.markdown("""
<style>
.footer-conectamais {
    text-align: center;
    padding: 30px 15px;
    margin-top: 40px;
    border-top: 1px solid #DCE8F5;
}

.footer-conectamais p {
    color: #58718E;
    font-size: 14px;
    line-height: 1.6;
}

.footer-conectamais a {
    display: inline-block;
    margin-top: 10px;
    color: #168A52 !important;
    font-weight: 700;
    text-decoration: none;
}
</style>

<div class="footer-conectamais">
    <h3>Desenvolvido por Adriano Junior</h3>
    <p>
        Estudante de Análise e Desenvolvimento de Sistemas,
        transformando conhecimento em soluções que conectam
        pessoas e geram impacto.
    </p>
    <a href="https://wa.me/5521983142168"
       target="_blank">
        💬 Fale comigo pelo WhatsApp
<img src="https://cdn.simpleicons.org/whatsapp/25D366"
     width="18"
     style="vertical-align:middle; margin-left:5px;">
    </a>
</div>
""", unsafe_allow_html=True)

