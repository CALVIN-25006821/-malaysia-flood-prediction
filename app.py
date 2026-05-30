import streamlit as st
import numpy as np

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Malaysia Flood Prediction",
    page_icon="🌧️",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans', sans-serif;
    }
    .main { background-color: #0d1117; }
    .block-container { padding: 2rem 3rem; }

    .app-title {
        font-size: 2rem;
        font-weight: 600;
        color: #e6edf3;
        margin-bottom: 0.2rem;
    }
    .app-subtitle {
        font-size: 0.95rem;
        color: #8b949e;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 0.75rem;
        font-weight: 500;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #8b949e;
        margin-bottom: 0.75rem;
        margin-top: 1.5rem;
    }
    .result-high {
        background: #1a0a0a;
        border: 1px solid #f85149;
        border-radius: 10px;
        padding: 1.25rem 1.5rem;
        color: #f85149;
    }
    .result-moderate {
        background: #1a130a;
        border: 1px solid #e3b341;
        border-radius: 10px;
        padding: 1.25rem 1.5rem;
        color: #e3b341;
    }
    .result-low {
        background: #0a1a10;
        border: 1px solid #3fb950;
        border-radius: 10px;
        padding: 1.25rem 1.5rem;
        color: #3fb950;
    }
    .result-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.4rem;
    }
    .result-reason {
        font-size: 0.88rem;
        opacity: 0.85;
        line-height: 1.6;
    }
    .metric-row {
        display: flex;
        gap: 12px;
        margin-top: 1rem;
    }
    .metric-card {
        flex: 1;
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }
    .metric-label {
        font-size: 0.72rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .metric-value {
        font-size: 1.4rem;
        font-weight: 500;
        color: #e6edf3;
        margin-top: 2px;
    }
    hr { border-color: #21262d; margin: 1.5rem 0; }
    label { color: #c9d1d9 !important; }
</style>
""", unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="app-title">🌧️ Malaysia Flood Prediction</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Decision support tool for assessing flood risk '
    'across Malaysian states and territories</div>',
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Layout ────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="section-header">1 — Weather Parameters</div>', unsafe_allow_html=True)

    ALL_STATES = [
        "Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan",
        "Pahang", "Perak", "Perlis", "Pulau Pinang", "Selangor", "Terengganu",
        "Sabah", "Sarawak",
        "W.P. Kuala Lumpur", "W.P. Labuan", "W.P. Putrajaya",
    ]

    state = st.selectbox("Target State / Territory", ALL_STATES)
    monthly_rainfall = st.slider("Monthly Rainfall (mm)", 0, 1200, 250, step=5)
    humidity = st.slider("Relative Humidity (%)", 50, 100, 85, step=1)
    temperature = st.number_input(
        "Average Temperature (°C)", min_value=15.0, max_value=40.0, value=27.5, step=0.5
    )
    run = st.button("▶  Run Flood Risk Analysis", use_container_width=True, type="primary")

with col2:
    st.markdown('<div class="section-header">2 — Prediction Output</div>', unsafe_allow_html=True)

    if run:
        # ── Scoring ───────────────────────────────────────────────────────────
        HIGH_RISK_STATES = {"Kelantan", "Terengganu", "Pahang", "Johor", "Sabah", "Sarawak"}

        score = 0
        if monthly_rainfall > 600:
            score += 55
        elif monthly_rainfall > 400:
            score += 35
        elif monthly_rainfall > 250:
            score += 18
        elif monthly_rainfall > 150:
            score += 8

        if humidity > 92:
            score += 20
        elif humidity > 85:
            score += 12
        elif humidity > 78:
            score += 6

        if temperature < 22:
            score += 8
        elif temperature > 32:
            score += 5

        if state in HIGH_RISK_STATES:
            score += 15

        score = int(np.clip(score, 0, 100))

        # ── Risk level ────────────────────────────────────────────────────────
        if score >= 60:
            css_class = "result-high"
            icon = "🚨"
            level = "High Flood Risk"
            reason = (
                f"Extreme precipitation patterns in <strong>{state}</strong> match historical "
                "monsoon flood data. Immediate monitoring and precautionary measures are strongly "
                "advised. Activate early warning systems and check river gauging stations."
            )
            tags = ["Activate early warning", "Monitor river levels", "Prepare evacuation routes"]
            bar_color = "#f85149"

        elif score >= 35:
            css_class = "result-moderate"
            icon = "⚠️"
            level = "Moderate Flood Risk"
            reason = (
                f"Weather parameters in <strong>{state}</strong> show elevated precipitation with "
                "potential for localised flooding. Monitor conditions closely over the next 24–48 "
                "hours and ensure drainage systems are clear."
            )
            tags = ["Monitor rainfall trends", "Check drainage capacity", "Standby alert"]
            bar_color = "#e3b341"

        else:
            css_class = "result-low"
            icon = "✅"
            level = "Low Flood Risk"
            reason = (
                f"Weather parameters for <strong>{state}</strong> are within stable baseline "
                "conditions. No significant flood indicators detected at this time. "
                "Continue routine monitoring."
            )
            tags = ["Conditions stable", "Normal operations", "Routine monitoring"]
            bar_color = "#3fb950"

        # ── Render ────────────────────────────────────────────────────────────
        tag_html = "".join(
            f'<span style="display:inline-block;margin:4px 4px 0 0;padding:3px 10px;'
            f'border-radius:4px;font-size:0.75rem;background:#21262d;color:#8b949e;">{t}</span>'
            for t in tags
        )

        st.markdown(f"""
        <div class="{css_class}">
            <div class="result-title">{icon} {level} — {state}</div>
            <div class="result-reason">{reason}</div>
            <div style="margin-top:0.75rem;">{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="margin-top:1.25rem;">
            <div style="display:flex;justify-content:space-between;font-size:0.8rem;
                        color:#8b949e;margin-bottom:5px;">
                <span>Risk Score</span>
                <span style="font-weight:500;color:#e6edf3;">{score} / 100</span>
            </div>
            <div style="background:#21262d;border-radius:4px;height:6px;">
                <div style="width:{score}%;background:{bar_color};height:6px;border-radius:4px;">
                </div>
            </div>
        </div>

        <div class="metric-row">
            <div class="metric-card">
                <div class="metric-label">Rainfall</div>
                <div class="metric-value">{monthly_rainfall} mm</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Humidity</div>
                <div class="metric-value">{humidity}%</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Temperature</div>
                <div class="metric-value">{temperature:.1f} °C</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="background:#161b22;border:1px dashed #30363d;border-radius:10px;
                    padding:2.5rem;text-align:center;color:#484f58;margin-top:0.5rem;">
            <div style="font-size:2rem;margin-bottom:0.5rem;">🌦️</div>
            <div style="font-size:0.9rem;">
                Set parameters on the left and click
                <strong style="color:#8b949e;">Run Flood Risk Analysis</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<p style="font-size:0.75rem;color:#484f58;text-align:center;">'
    "Malaysia Flood Prediction · For decision support use only · "
    "Data inputs are manually entered</p>",
    unsafe_allow_html=True,
)
