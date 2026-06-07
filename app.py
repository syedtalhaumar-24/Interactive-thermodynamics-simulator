import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Thermodynamics Simulator",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CUSTOM CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

.stApp {
    background: linear-gradient(135deg, #060D1A 0%, #0A1628 50%, #0D1F3C 100%);
    color: #F0E6CC;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #060D1A 0%, #0A1628 100%);
    border-right: 1px solid #C9A84C;
}

.main-title {
    font-family: 'Cinzel', serif;
    font-size: 2.6rem;
    font-weight: 900;
    background: linear-gradient(90deg, #C9A84C, #F0C040, #C9A84C);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    letter-spacing: 4px;
    margin-bottom: 0;
    padding-top: 10px;
}

.sub-title {
    font-family: 'Crimson Text', serif;
    font-size: 1.1rem;
    color: #A08840;
    text-align: center;
    letter-spacing: 5px;
    font-style: italic;
    margin-bottom: 30px;
}

.section-header {
    font-family: 'Cinzel', serif;
    font-size: 0.9rem;
    color: #C9A84C;
    letter-spacing: 3px;
    border-left: 3px solid #C9A84C;
    padding-left: 12px;
    margin: 20px 0 15px 0;
    text-transform: uppercase;
}

.metric-card {
    background: linear-gradient(135deg, #0D1F3C, #112244);
    border: 1px solid #C9A84C;
    border-radius: 10px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(201, 168, 76, 0.1);
}

.metric-value {
    font-family: 'Cinzel', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #F0C040;
}

.metric-label {
    font-family: 'Crimson Text', serif;
    font-size: 0.85rem;
    color: #A08840;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.metric-unit {
    font-family: 'Crimson Text', serif;
    font-size: 0.8rem;
    color: #806830;
}

.info-box {
    background: rgba(201, 168, 76, 0.07);
    border: 1px solid #C9A84C44;
    border-radius: 10px;
    padding: 15px 20px;
    margin: 10px 0;
    font-family: 'Crimson Text', serif;
    font-size: 1rem;
    color: #D4C090;
}

.law-card {
    background: linear-gradient(135deg, #0D1F3C, #0A1628);
    border: 1px solid #C9A84C55;
    border-top: 3px solid #C9A84C;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 8px 0;
    font-family: 'Crimson Text', serif;
}

.law-title {
    color: #F0C040;
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 1px;
}

.law-desc {
    color: #A09070;
    font-size: 0.95rem;
    margin-top: 4px;
}

.team-card {
    background: linear-gradient(135deg, #0D1F3C, #060D1A);
    border: 1px solid #C9A84C44;
    border-radius: 8px;
    padding: 10px 16px;
    margin: 5px 0;
    display: flex;
    justify-content: space-between;
}

.gold-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #C9A84C, transparent);
    margin: 22px 0;
}

.formula-box {
    background: linear-gradient(135deg, #060D1A, #0D1F3C);
    border: 1px solid #C9A84C;
    border-radius: 8px;
    padding: 14px 20px;
    margin: 10px 0;
    font-family: 'Cinzel', serif;
    color: #F0C040;
    font-size: 1.1rem;
    text-align: center;
    letter-spacing: 2px;
}

label, .stSlider label, .stNumberInput label, .stSelectbox label {
    font-family: 'Crimson Text', serif !important;
    color: #A08840 !important;
    font-size: 0.95rem !important;
    letter-spacing: 1px !important;
}

.stNumberInput input {
    background: #0D1F3C !important;
    border: 1px solid #C9A84C55 !important;
    color: #F0C040 !important;
    border-radius: 6px !important;
}

.stSelectbox > div > div {
    background: #0D1F3C !important;
    border: 1px solid #C9A84C55 !important;
    color: #F0C040 !important;
}

.stTabs [data-baseweb="tab-list"] {
    background: #060D1A;
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
    border: 1px solid #C9A84C33;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #A08840;
    font-family: 'Cinzel', serif;
    font-weight: 600;
    letter-spacing: 2px;
    font-size: 0.82rem;
    border-radius: 8px;
    padding: 8px 14px;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #1B3A6B, #112244) !important;
    color: #F0C040 !important;
    border: 1px solid #C9A84C !important;
}

.stButton > button {
    background: linear-gradient(135deg, #1B3A6B, #112244);
    color: #F0C040;
    border: 1px solid #C9A84C;
    border-radius: 8px;
    font-family: 'Cinzel', serif;
    font-weight: 600;
    letter-spacing: 2px;
    font-size: 0.95rem;
    padding: 10px 30px;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2A5080, #1B3A6B);
    box-shadow: 0 0 20px rgba(201, 168, 76, 0.3);
}

.footer {
    text-align: center;
    font-family: 'Crimson Text', serif;
    color: #604820;
    font-size: 0.82rem;
    letter-spacing: 2px;
    padding: 20px 0 10px 0;
    font-style: italic;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─── CONSTANTS ─────────────────────────────────────────────────────────────────
R = 8.314        # Universal Gas Constant J/(mol·K)
TEAM = [
    ("Muhammad Ahmad",  "25-ME-131"),
    ("Muhammad Ali",    "25-ME-167"),
    ("Abdul Rahim",     "25-ME-199"),
    ("Jawad Ahmed",     "25-ME-67"),
]

GASES = {
    "Air":            {"gamma": 1.4,  "Cp": 1005, "Cv": 718,  "M": 28.97},
    "Nitrogen (N₂)":  {"gamma": 1.4,  "Cp": 1040, "Cv": 743,  "M": 28.02},
    "Oxygen (O₂)":    {"gamma": 1.4,  "Cp": 919,  "Cv": 659,  "M": 32.00},
    "Helium (He)":    {"gamma": 1.667,"Cp": 5193, "Cv": 3116, "M": 4.003},
    "Hydrogen (H₂)":  {"gamma": 1.41, "Cp": 14307,"Cv": 10141,"M": 2.016},
    "CO₂":            {"gamma": 1.289,"Cp": 844,  "Cv": 655,  "M": 44.01},
    "Steam (H₂O)":    {"gamma": 1.33, "Cp": 1996, "Cv": 1507, "M": 18.02},
}

PLOT_CFG = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(10,22,40,0.8)",
    font=dict(color="#A08840", family="Georgia"),
    title_font=dict(color="#C9A84C", size=15, family="Georgia"),
)

# ─── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="section-header">⚙️ Gas Properties</div>', unsafe_allow_html=True)
    gas_choice = st.selectbox("Select Gas", list(GASES.keys()))
    gas = GASES[gas_choice]
    gamma = gas["gamma"]
    Cp    = gas["Cp"]
    Cv    = gas["Cv"]

    st.markdown(f"""<div class="info-box">
    <b style="color:#F0C040;">γ (gamma)</b> = {gamma}<br>
    <b style="color:#F0C040;">Cp</b> = {Cp} J/(kg·K)<br>
    <b style="color:#F0C040;">Cv</b> = {Cv} J/(kg·K)<br>
    <b style="color:#F0C040;">M</b>  = {gas['M']} g/mol
    </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">👥 Project Team</div>', unsafe_allow_html=True)
    for name, reg in TEAM:
        st.markdown(f"""<div class="team-card">
            <span style="font-family:'Crimson Text',serif;color:#D4C090;font-weight:600;">🔬 {name}</span>
            <span style="font-family:'Courier New',monospace;color:#C9A84C;font-size:0.82rem;">{reg}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)
    st.markdown("""<div style="font-family:'Crimson Text',serif;color:#604820;font-size:0.78rem;text-align:center;letter-spacing:1px;font-style:italic;">
        ICT in Education<br>Mechanical Engineering<br>UET Taxila · 2025
    </div>""", unsafe_allow_html=True)

# ─── HEADER ────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">🔥 THERMODYNAMICS SIMULATOR</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Interactive Educational Tool for Engineering Students</div>', unsafe_allow_html=True)
st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

# ─── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔄  PROCESSES",
    "⚗️  GAS LAWS",
    "🌡️  HEAT ENGINE",
    "📊  P-V DIAGRAM",
    "ℹ️  THEORY",
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — THERMODYNAMIC PROCESSES
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown('<div class="section-header">🔄 Thermodynamic Process Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">Select a process, enter initial state, and the simulator calculates the final state and work/heat interactions.</div>', unsafe_allow_html=True)

    process = st.selectbox("Select Process", [
        "Isothermal (Constant Temperature)",
        "Isobaric (Constant Pressure)",
        "Isochoric (Constant Volume)",
        "Adiabatic (No Heat Transfer)",
        "Polytropic"
    ])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-header">Initial State</div>', unsafe_allow_html=True)
        P1 = st.number_input("Pressure P₁ (kPa)", min_value=1.0, value=100.0, step=10.0)
        V1 = st.number_input("Volume V₁ (m³)",    min_value=0.001, value=1.0, step=0.1)
        T1 = st.number_input("Temperature T₁ (K)", min_value=1.0, value=300.0, step=10.0)
        m  = st.number_input("Mass of Gas (kg)",   min_value=0.001, value=1.0, step=0.1)

    with col2:
        st.markdown('<div class="section-header">Process Parameter</div>', unsafe_allow_html=True)
        if "Isothermal" in process:
            V2 = st.number_input("Final Volume V₂ (m³)", min_value=0.001, value=2.0, step=0.1)
            n_poly = 1.0
        elif "Isobaric" in process:
            V2 = st.number_input("Final Volume V₂ (m³)", min_value=0.001, value=2.0, step=0.1)
            n_poly = 0.0
        elif "Isochoric" in process:
            T2_input = st.number_input("Final Temperature T₂ (K)", min_value=1.0, value=600.0, step=10.0)
            V2 = V1
            n_poly = float('inf')
        elif "Adiabatic" in process:
            V2 = st.number_input("Final Volume V₂ (m³)", min_value=0.001, value=2.0, step=0.1)
            n_poly = gamma
        else:  # Polytropic
            n_poly = st.slider("Polytropic Index n", min_value=0.0, max_value=3.0, value=1.3, step=0.05)
            V2 = st.number_input("Final Volume V₂ (m³)", min_value=0.001, value=2.0, step=0.1)

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

    if st.button("⚡  SIMULATE PROCESS", use_container_width=True):
        # ── Calculations ──────────────────────────────────────────────────
        if "Isothermal" in process:
            T2 = T1
            P2 = P1 * V1 / V2
            W  = P1 * V1 * 1000 * np.log(V2 / V1)   # J
            Q  = W
            dU = 0

        elif "Isobaric" in process:
            P2 = P1
            T2 = T1 * V2 / V1
            W  = P1 * 1000 * (V2 - V1)               # J
            dU = m * Cv * (T2 - T1)
            Q  = m * Cp * (T2 - T1)

        elif "Isochoric" in process:
            T2 = T2_input
            V2 = V1
            P2 = P1 * T2 / T1
            W  = 0
            dU = m * Cv * (T2 - T1)
            Q  = dU

        elif "Adiabatic" in process:
            P2 = P1 * (V1 / V2) ** gamma
            T2 = T1 * (V1 / V2) ** (gamma - 1)
            W  = (P1 * 1000 * V1 - P2 * 1000 * V2) / (gamma - 1)
            Q  = 0
            dU = -W

        else:  # Polytropic
            if n_poly != 1:
                P2 = P1 * (V1 / V2) ** n_poly
                T2 = T1 * (V1 / V2) ** (n_poly - 1)
                W  = (P1 * 1000 * V1 - P2 * 1000 * V2) / (n_poly - 1)
            else:
                P2 = P1 * V1 / V2
                T2 = T1
                W  = P1 * V1 * 1000 * np.log(V2 / V1)
            dU = m * Cv * (T2 - T1)
            Q  = dU + W

        # ── Results ──────────────────────────────────────────────────────
        st.markdown('<div class="section-header">📊 Results</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-value">{P2:.2f}</div>
                <div class="metric-unit">kPa</div>
                <div class="metric-label">Final Pressure P₂</div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-value">{V2:.3f}</div>
                <div class="metric-unit">m³</div>
                <div class="metric-label">Final Volume V₂</div>
            </div>""", unsafe_allow_html=True)
        with c3:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-value">{T2:.1f}</div>
                <div class="metric-unit">K</div>
                <div class="metric-label">Final Temperature T₂</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        c4, c5, c6 = st.columns(3)
        with c4:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-value">{W/1000:.2f}</div>
                <div class="metric-unit">kJ</div>
                <div class="metric-label">Work Done (W)</div>
            </div>""", unsafe_allow_html=True)
        with c5:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-value">{Q/1000:.2f}</div>
                <div class="metric-unit">kJ</div>
                <div class="metric-label">Heat Transfer (Q)</div>
            </div>""", unsafe_allow_html=True)
        with c6:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-value">{dU/1000:.2f}</div>
                <div class="metric-unit">kJ</div>
                <div class="metric-label">Internal Energy (ΔU)</div>
            </div>""", unsafe_allow_html=True)

        # ── P-V Process Chart ─────────────────────────────────────────────
        V_range = np.linspace(V1, V2, 200)
        if "Isothermal" in process:
            P_range = P1 * V1 / V_range
        elif "Isobaric" in process:
            P_range = np.full_like(V_range, P1)
        elif "Isochoric" in process:
            V_range = np.array([V1, V1])
            P_range = np.array([P1, P2])
        elif "Adiabatic" in process:
            P_range = P1 * (V1 / V_range) ** gamma
        else:
            if n_poly != 1:
                P_range = P1 * (V1 / V_range) ** n_poly
            else:
                P_range = P1 * V1 / V_range

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=V_range, y=P_range,
            mode="lines",
            line=dict(color="#C9A84C", width=3),
            fill="tozeroy",
            fillcolor="rgba(201,168,76,0.08)",
            name=process.split("(")[0].strip()
        ))
        fig.add_trace(go.Scatter(
            x=[V1, V2], y=[P1, P2],
            mode="markers",
            marker=dict(size=12, color=["#F0C040", "#FF6B35"], symbol="circle"),
            name="States"
        ))
        fig.update_layout(
            **PLOT_CFG,
            title=f"P-V Diagram — {process.split('(')[0].strip()}",
            xaxis=dict(title="Volume (m³)", gridcolor="#1B3A6B", color="#A08840"),
            yaxis=dict(title="Pressure (kPa)", gridcolor="#1B3A6B", color="#A08840"),
            height=350
        )
        fig.add_annotation(x=V1, y=P1, text=f" State 1<br>({V1:.2f}, {P1:.1f})", showarrow=True, arrowcolor="#F0C040", font=dict(color="#F0C040"))
        fig.add_annotation(x=V2, y=P2, text=f" State 2<br>({V2:.2f}, {P2:.1f})", showarrow=True, arrowcolor="#FF6B35", font=dict(color="#FF6B35"))
        st.plotly_chart(fig, use_container_width=True)

        # Energy balance check
        st.markdown(f"""<div class="info-box">
        ✅ <b>1st Law Check:</b> Q = ΔU + W &nbsp;→&nbsp; 
        {Q/1000:.2f} kJ = {dU/1000:.2f} + {W/1000:.2f} = <b>{(dU+W)/1000:.2f} kJ</b>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — GAS LAWS
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-header">⚗️ Ideal Gas Laws Simulator</div>', unsafe_allow_html=True)

    law = st.selectbox("Select Gas Law", [
        "Ideal Gas Law  (PV = nRT)",
        "Boyle's Law  (P₁V₁ = P₂V₂)",
        "Charles's Law  (V₁/T₁ = V₂/T₂)",
        "Gay-Lussac's Law  (P₁/T₁ = P₂/T₂)",
        "Combined Gas Law",
    ])

    col_l, col_r = st.columns(2)

    if "Ideal Gas" in law:
        with col_l:
            st.markdown('<div class="section-header">Known Variables</div>', unsafe_allow_html=True)
            solve_for = st.selectbox("Solve for:", ["Pressure (P)", "Volume (V)", "Temperature (T)", "Moles (n)"])
            n_mol = st.number_input("Moles (n)", min_value=0.001, value=1.0, step=0.1) if "Pressure" in solve_for or "Volume" in solve_for or "Temperature" in solve_for else None
            Pval  = st.number_input("Pressure (Pa)", min_value=1.0, value=101325.0, step=1000.0) if "Pressure" not in solve_for else None
            Vval  = st.number_input("Volume (m³)", min_value=0.001, value=0.0224, step=0.001) if "Volume" not in solve_for else None
            Tval  = st.number_input("Temperature (K)", min_value=1.0, value=273.15, step=1.0) if "Temperature" not in solve_for else None

        with col_r:
            st.markdown('<div class="section-header">Result</div>', unsafe_allow_html=True)
            st.markdown('<div class="formula-box">PV = nRT</div>', unsafe_allow_html=True)
            if st.button("⚡ CALCULATE", use_container_width=True):
                if "Pressure" in solve_for:
                    result = n_mol * R * Tval / Vval
                    st.markdown(f'<div class="metric-card"><div class="metric-value">{result:,.2f}</div><div class="metric-unit">Pa</div><div class="metric-label">Pressure (P)</div></div>', unsafe_allow_html=True)
                elif "Volume" in solve_for:
                    result = n_mol * R * Tval / Pval
                    st.markdown(f'<div class="metric-card"><div class="metric-value">{result:.4f}</div><div class="metric-unit">m³</div><div class="metric-label">Volume (V)</div></div>', unsafe_allow_html=True)
                elif "Temperature" in solve_for:
                    result = Pval * Vval / (n_mol * R)
                    st.markdown(f'<div class="metric-card"><div class="metric-value">{result:.2f}</div><div class="metric-unit">K</div><div class="metric-label">Temperature (T)</div></div>', unsafe_allow_html=True)
                else:
                    result = Pval * Vval / (R * Tval)
                    st.markdown(f'<div class="metric-card"><div class="metric-value">{result:.4f}</div><div class="metric-unit">mol</div><div class="metric-label">Moles (n)</div></div>', unsafe_allow_html=True)

    elif "Boyle" in law:
        with col_l:
            st.markdown('<div class="section-header">Initial State</div>', unsafe_allow_html=True)
            P1b = st.number_input("P₁ (kPa)", min_value=0.1, value=100.0)
            V1b = st.number_input("V₁ (m³)",  min_value=0.001, value=1.0)
            P2b = st.number_input("P₂ (kPa)", min_value=0.1, value=200.0)
        with col_r:
            st.markdown('<div class="section-header">Result</div>', unsafe_allow_html=True)
            st.markdown('<div class="formula-box">P₁V₁ = P₂V₂</div>', unsafe_allow_html=True)
            V2b = P1b * V1b / P2b
            st.m
