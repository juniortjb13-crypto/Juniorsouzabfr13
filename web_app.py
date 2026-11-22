
import streamlit as st
import pandas as pd
import os
from datetime import date
from supabase import create_client
from supabase import create_client
import plotly.graph_objects as go
import random
from streamlit_image_select import image_select

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


/* =====================================
   CONECTAMAIS - TEMA FUTURISTA NEON
===================================== */

.stApp,
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse at 75% 5%, rgba(0, 180, 255, 0.13), transparent 35%),
        radial-gradient(ellipse at 15% 80%, rgba(0, 90, 220, 0.12), transparent 40%),
        #050B18 !important;
    color: #EAF4FF !important;
}

[data-testid="stHeader"] {
    background: rgba(5, 11, 24, 0.85) !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #08162C, #050B18) !important;
    border-right: 1px solid rgba(0, 200, 255, 0.25);
}

[data-testid="stSidebar"] * {
    color: #DCEBFF;
}

h1, h2, h3, h4 {
    color: #F4F9FF !important;
}

p, label, span {
    color: #D5E4F5;
}

/* Cartões e indicadores */
[data-testid="stMetric"],
[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(
        145deg,
        rgba(13, 34, 62, 0.92),
        rgba(7, 18, 38, 0.96)
    ) !important;
    border: 1px solid rgba(0, 190, 255, 0.30) !important;
    border-radius: 16px !important;
    box-shadow: 0 5px 22px rgba(0, 150, 255, 0.10);
}

/* Números dos indicadores */
[data-testid="stMetricValue"] {
    color: #35D9FF !important;
    font-weight: 800;
}

/* Textos dos indicadores */
[data-testid="stMetricLabel"] {
    color: #B8D3EE !important;
}

/* Campos de formulário */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: #101F36 !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(0, 190, 255, 0.35) !important;
    border-radius: 10px !important;
}

/* Botões */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(135deg, #087BCE, #04C9C4) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(70, 220, 255, 0.45) !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    transition: all 0.25s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    box-shadow: 0 0 18px rgba(0, 200, 255, 0.45);
    transform: translateY(-2px);
}

/* Gráficos */
[data-testid="stPlotlyChart"] {
    background: rgba(8, 22, 43, 0.65);
    border: 1px solid rgba(0, 190, 255, 0.20);
    border-radius: 16px;
    padding: 8px;
}

/* Tabelas */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background: #0B1930 !important;
    border-radius: 12px;
}

/* Links */
a {
    color: #35D9FF !important;
}

/* Rodapé */
footer {
    visibility: hidden;
}


/* ===== CONECTAMAIS - MENU LATERAL ===== */

.cm-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 245px;
    height: 100vh;
    padding: 35px 20px;
    background: linear-gradient(180deg, #06152F, #020B1B);
    border-right: 1px solid rgba(0, 200, 255, 0.35);
    box-shadow: 5px 0 30px rgba(0, 120, 255, 0.12);
    z-index: 9999;
    display: flex;
    flex-direction: column;
}

.cm-brand {
    text-align: center;
    margin-bottom: 55px;
}

.cm-logo {
    font-size: 48px;
    color: #16D9FF;
    margin-bottom: 10px;
}

.cm-brand-name {
    font-size: 25px;
    font-weight: 800;
    color: #FFFFFF;
}

.cm-brand-name span {
    color: #16D9FF;
}

.cm-brand p {
    color: #AFC8E8;
    font-size: 13px;
    line-height: 1.6;
}

.cm-menu {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.cm-menu a {
    display: block;
    padding: 14px;
    color: #C7D9F2 !important;
    text-decoration: none !important;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.25s ease;
}

.cm-menu a:hover,
.cm-menu a.active {
    color: #FFFFFF !important;
    background: linear-gradient(90deg, #0755A8, #087FC4);
    box-shadow: 0 0 18px rgba(0, 190, 255, 0.25);
}

.cm-sidebar-footer {
    margin-top: auto;
    padding: 16px;
    border: 1px solid rgba(0, 190, 255, 0.2);
    border-radius: 14px;
    color: #C7D9F2;
    text-align: center;
    background: rgba(0, 100, 180, 0.08);
}

.cm-sidebar-footer span {
    font-size: 28px;
}

.cm-sidebar-footer p {
    font-size: 13px;
}

.cm-status {
    color: #39E6A0;
    font-size: 12px;
    margin-top: 15px;
}

/* Conteúdo ao lado do menu */
@media (min-width: 769px) {
    .stMainBlockContainer {
        margin-left: 245px !important;
        max-width: calc(100% - 270px) !important;
    }
}


/* ===== ADAPTAÇÃO PARA CELULARES ===== */

/* ===== CONECTAMAIS - RESPONSIVIDADE MOBILE ===== */
@media (max-width: 768px) {

    /* Menu lateral transformado em menu superior */
    .cm-sidebar {
        position: relative !important;
        left: auto !important;
        top: auto !important;
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        padding: 12px !important;
        margin: 0 !important;
        box-sizing: border-box !important;
        display: block !important;
    }

    .cm-brand {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 10px !important;
        margin-bottom: 12px !important;
        text-align: center !important;
    }

    .cm-logo {
        font-size: 28px !important;
        margin: 0 !important;
    }

    .cm-brand-name {
        font-size: 21px !important;
        margin: 0 !important;
    }

    .cm-brand p,
    .cm-sidebar-footer {
        display: none !important;
    }

    .cm-menu {
        display: grid !important;
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 8px !important;
        width: 100% !important;
    }

    .cm-menu a {
        width: 100% !important;
        min-width: 0 !important;
        box-sizing: border-box !important;
        justify-content: center !important;
        text-align: center !important;
        padding: 11px 5px !important;
        font-size: 12px !important;
        margin: 0 !important;
    }

    /* Conteúdo principal ocupa a tela inteira */
    .stMainBlockContainer {
        margin-left: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
        padding-left: 12px !important;
        padding-right: 12px !important;
        box-sizing: border-box !important;
    }

    /* Globo */
    .cm-hero-top {
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
    }

    .cm-planet-area {
        transform: scale(0.75) !important;
        margin: -15px auto !important;
    }

    /* Avatares e colunas */
    div[data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
        gap: 10px !important;
    }

    div[data-testid="column"] {
        min-width: 100% !important;
        flex: 1 1 100% !important;
    }

    div[data-testid="stImage"] {
        max-width: 100% !important;
    }

    /* Campos */
    input,
    textarea,
    select {
        max-width: 100% !important;
    }

    /* Títulos */
    h1 {
        font-size: 26px !important;
    }

    h2 {
        font-size: 22px !important;
    }

    h3 {
        font-size: 19px !important;
    }

    /* Evitar rolagem horizontal */
    html,
    body {
        overflow-x: hidden !important;
    }
}



/* ===== UNIVERSO CONECTAMAIS ===== */

.stApp,
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse at 78% 12%, rgba(0, 180, 255, 0.16), transparent 32%),
        radial-gradient(ellipse at 18% 75%, rgba(0, 90, 220, 0.13), transparent 38%),
        linear-gradient(135deg, #020817, #06152D 55%, #020817) !important;
}

/* Cabeçalho principal */
.cm-universe {
    position: relative;
    min-height: 340px;
    padding: 35px 20px;
    overflow: hidden;
    background:
        radial-gradient(circle at 78% 45%, rgba(0, 190, 255, 0.12), transparent 28%);
}

.cm-hero-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 300px;
    gap: 25px;
}

.cm-hero-text {
    position: relative;
    z-index: 2;
    max-width: 540px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cm-universe">
<div class="cm-hero-top">
<div class="cm-hero-text">
<span class="cm-hero-label">CONECTAMAIS • EXPERIÊNCIA E QUALIDADE</span>
<h1>Conecta<span>Mais</span></h1>
<p>Avaliações reais. Dados confiáveis.<br>
Uma comunidade mais conectada.</p>
<div class="cm-hero-line"></div>
</div>
<div class="cm-planet-area">
<div class="cm-orbit cm-orbit-one"></div>
<div class="cm-orbit cm-orbit-two"></div>
<div class="cm-planet"></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.cm-hero-text h1 span {
    color: #18C7D9 !important;
}
.cm-hero-text p {
    color: #B9CCE3;
    font-size: 19px;
    line-height: 1.5;
}

.cm-hero-line {
    width: 100px;
    height: 3px;
    margin-top: 20px;
    background: linear-gradient(90deg, #20D6C2, #168BFF, transparent);
    box-shadow: 0 0 15px #00CFFF;
}


/* GLOBO REALISTA CONECTAMAIS */

.cm-planet-area {
    position: relative;
    width: 390px;
    height: 340px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    perspective: 1000px;
}

/* Planeta Terra */
.cm-planet {
    position: relative;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    z-index: 1;

    background-image:
        url("https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg");

    background-size: auto 100%;
    background-position: 0 center;
    background-repeat: repeat-x;

    box-shadow:
        inset -25px -10px 40px rgba(0, 5, 25, .85),
        inset 10px 5px 25px rgba(80, 190, 255, .25),
        0 0 30px rgba(0, 180, 255, .55),
        0 0 75px rgba(0, 130, 255, .35);

    animation:
        cm-earth-spin 50s linear infinite;
}

/* Atmosfera azul */
.cm-planet::before {
    content: "";
    position: absolute;
    inset: -5px;
    border-radius: 50%;
    pointer-events: none;

    background:
        radial-gradient(
            circle at 35% 30%,
            transparent 55%,
            rgba(0, 190, 255, .22) 75%,
            rgba(0, 100, 255, .45) 100%
        );

    box-shadow:
        0 0 18px rgba(0, 190, 255, .55),
        inset 0 0 15px rgba(0, 180, 255, .35);
}


/* Anéis orbitais envolvendo a Terra */
.cm-orbit {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 350px;
    height: 125px;
    border: 2px solid rgba(0, 220, 255, .85);
    border-radius: 50%;
    box-shadow:
        0 0 12px rgba(0, 210, 255, .75),
        0 0 25px rgba(0, 130, 255, .35);
    z-index: 3;
}

.cm-orbit-one {
    animation:
        cm-orbit-rotate-one 35s linear infinite,
        cm-orbit-glow 6s ease-in-out infinite;
}

.cm-orbit-two {
    width: 370px;
    height: 145px;
    border-color: rgba(0, 150, 255, .65);
    animation:
        cm-orbit-rotate-two 45s linear infinite,
        cm-orbit-glow 8s ease-in-out infinite reverse;
}

@keyframes cm-orbit-rotate-one {
    from { transform: translate(-50%, -50%) rotate(-24deg); }
    to { transform: translate(-50%, -50%) rotate(336deg); }
}

@keyframes cm-orbit-rotate-two {
    from { transform: translate(-50%, -50%) rotate(25deg); }
    to { transform: translate(-50%, -50%) rotate(385deg); }
}



/* Rotação lenta da Terra */
@keyframes cm-earth-spin {
    from {
        background-position: 0 center;
    }
    to {
        background-position: -460px center;
    }
}

/* Brilho dos anéis */
@keyframes cm-orbit-glow {
    0%, 100% {
        opacity: .55;
    }
    50% {
        opacity: 1;
    }
}

/* Telas menores */
@media (max-width: 768px) {
    .cm-hero-top {
        flex-direction: column;
        align-items: flex-start;
    }

    .cm-planet-area {
        width: 100%;
        transform: scale(.8);
        margin-top: -15px;
    }
}

</style> 
""", unsafe_allow_html=True)

ARQUIVO_DADOS = "clientes.csv"

# CABEÇALHO PRINCIPAL




st.markdown("""
<div class="cm-sidebar">
<div class="cm-brand">
<div class="cm-logo">🌐</div>
<div class="cm-brand-name">Conecta<span>Mais</span></div>
<p>Conectando pessoas<br>e serviços de qualidade</p>
</div>
<nav class="cm-menu">
<a href="#inicio" class="active">🏠 Início</a>
<a href="#avaliar-servico">⭐ Avaliar serviço</a>
<a href="#comentarios">💬 Comentários</a>
<a href="#dashboard">📊 Dashboard</a>
</nav>
<div class="cm-sidebar-footer">
<span>🚀</span>
<p>Juntos por uma experiência cada vez melhor!</p>
<div class="cm-status">🟢 Sistema online</div>
</div>
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
    "id,nome_avaliador,avatar,tipo_servico,estabelecimento,cidade,nota,comentario,data"
).order("data", desc=True).execute()

    dados = pd.DataFrame(resposta.data)

    colunas = [
    "id",
    "nome_avaliador",
    "avatar",
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


# Galeria de avatares clicáveis
st.markdown("### Escolha seu avatar")
st.caption("Clique diretamente no personagem desejado.")

if "avatar_selecionado" not in st.session_state:
    st.session_state.avatar_selecionado = "avatar_01"

colunas_avatares = st.columns(5)

for i in range(1, 11):
    avatar = f"avatar_{i:02d}"
    with colunas_avatares[(i - 1) % 5]:
        st.image(f"assets/avatares/{avatar}.png", width=90)
        if st.button(
            "✓ Selecionado" if st.session_state.avatar_selecionado == avatar else f"Avatar {i:02d}",
            key=f"botao_{avatar}",
            use_container_width=True
        ):
            st.session_state.avatar_selecionado = avatar
            st.rerun()

with st.form("formulario_avaliacao"):
    tipo_servico = st.selectbox(
        "Qual serviço você utilizou?",
        [
            "Barbearia", "Salão de beleza", "Restaurante", "Lanchonete",
            "Oficina mecânica", "Mercado", "Farmácia", "Pet shop",
            "Padaria", "Supermercado", "Loja de roupas",
            "Loja de eletrônicos", "Hotel e pousada", "Transporte",
            "Assistência técnica", "Dentista", "Escola e cursos",
            "Lava-jato", "Imobiliária", "Academia", "Clínica", "Outro"
        ]
    )

    nome_avaliador = st.text_input("Seu nome")
    estabelecimento = st.text_input("Nome do estabelecimento")
    cidade = st.text_input("Cidade")
    avaliacao_estrelas = st.feedback("stars")

    nota = None if avaliacao_estrelas is None else avaliacao_estrelas + 1

    if nota is not None:
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
            "nome_avaliador": nome_avaliador.strip(),
            "avatar": st.session_state.avatar_selecionado,
            "tipo_servico": tipo_servico,
            "estabelecimento": estabelecimento.strip(),
            "cidade": cidade.strip(),
            "nota": nota,
            "comentario": comentario.strip()
        }

        supabase.table("avaliacoes").insert(novo_registro).execute()
        st.markdown("""
<div style="
    background: linear-gradient(90deg, #063b50, #075b68);
    border: 1px solid #00d9c5;
    border-radius: 12px;
    padding: 16px 20px;
    color: #ffffff;
    font-size: 16px;
    font-weight: 600;
    margin-top: 12px;
">
    ✅ Avaliação enviada com sucesso! Obrigado por contribuir com o ConectaMais.
</div>
""", unsafe_allow_html=True)





    


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
dados_filtrados = dados.copy()

if dados.empty:
    st.markdown("""
<div style="
    background: rgba(10, 35, 65, 0.85);
    border: 1px solid rgba(0, 200, 230, 0.45);
    border-radius: 12px;
    padding: 18px;
    color: #EAF6FF;
    font-size: 15px;
">
    📊 Ainda não existem avaliações cadastradas.
    <br>
    <span style="color: #8FC5DF;">
        Assim que os clientes avaliarem os serviços, os indicadores aparecerão aqui.
    </span>
</div>
""", unsafe_allow_html=True)
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
    
st.subheader("💬 O que os clientes estão dizendo")

comentarios_publicos = dados_filtrados[
    dados_filtrados["comentario"].fillna("").astype(str).str.strip() != ""
].sort_values("data", ascending=False)

emojis_servicos = {
    "salão de beleza": "💅",
    "barbearia": "💈",
    "restaurante": "🍽️",
    "academia": "🏋️",
    "clínica": "🏥",
    "mercado": "🛒",
    "oficina": "🔧",
    "farmácia": "💊",
    "pet shop": "🐾",
    "padaria": "🥖",
    "supermercado": "🛒",
    "loja de roupas": "👕",
    "loja de eletrônicos": "📱",
    "hotel e pousada": "🏨",
    "transporte": "🚕",
    "assistência técnica": "🛠️",
    "dentista": "🦷",
    "escola e cursos": "🎓",
    "lava-jato": "🚗",
    "imobiliária": "🏠",
}

avatares = {
    "masculino": "👨🏻",
    "feminino": "👩🏻",
    "neutro": "🧑🏻",
}

if not comentarios_publicos.empty:
    for _, avaliacao in comentarios_publicos.iterrows():

        with st.container(border=True):

            coluna_avatar, coluna_nome, coluna_nota = st.columns([0.8, 4, 1.2])

            # Avatar do avaliador
                        # Avatar real do avaliador
            avatar_tipo = avaliacao.get("avatar", "avatar_03")

            if pd.isna(avatar_tipo):
                avatar_tipo = "avatar_03"

            avatar_tipo = str(avatar_tipo).strip().lower()

            if avatar_tipo not in [
                f"avatar_{i:02d}" for i in range(1, 11)
            ]:
                avatar_tipo = "avatar_03"

            caminho_avatar = f"assets/avatares/{avatar_tipo}.png"

            with coluna_avatar:
                st.image(caminho_avatar, width=75)

            # Nome do avaliador
            nome_avaliador = avaliacao.get("nome_avaliador", "")

            if pd.isna(nome_avaliador):
                nome_avaliador = ""

            nome_avaliador = str(nome_avaliador).strip()

            with coluna_nome:
                if nome_avaliador:
                    st.markdown(f"**{nome_avaliador}**")
                else:
                    st.markdown("**Avaliação anônima**")

                st.caption("Cliente ConectaMais")

            # Nota
            with coluna_nota:
                st.markdown(f"⭐ **{avaliacao['nota']}/5**")

            st.divider()

            # Etiquetas da avaliação
            servico = str(avaliacao.get("tipo_servico", "Outro"))
            emoji = emojis_servicos.get(servico.strip().lower(), "📌")

            estabelecimento = avaliacao.get("estabelecimento", "")

            if pd.isna(estabelecimento):
                estabelecimento = ""

            estabelecimento = str(estabelecimento).strip()

            st.caption(f"🏷️ {emoji} {servico}")

            if estabelecimento:
                st.caption(f"📍 {estabelecimento}")

            # Comentário
            st.write(avaliacao["comentario"])

else:
    st.markdown("""
<div style="
    background: rgba(10, 35, 65, 0.85);
    border: 1px solid rgba(0, 200, 230, 0.45);
    border-radius: 12px;
    padding: 18px;
    color: #EAF6FF;
    font-size: 15px;
">
    💬 Ainda não existem comentários registrados.
    <br>
    <span style="color: #8FC5DF;">
        Seja o primeiro a compartilhar sua experiência com a comunidade!
    </span>
</div>
""", unsafe_allow_html=True)

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

