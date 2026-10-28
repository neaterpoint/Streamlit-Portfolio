import base64
from pathlib import Path

import streamlit as st

image_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "home.png"
image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")

st.html(f"""
<style>
.stApp {{
    background-image:
        linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)),
        url("data:image/png;base64,{image_data}");
    background-size: cover;
    background-position: right;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.st-key-hero h1 {{
    font-size: clamp(3rem, 7vw, 6rem);
}}

.st-key-hero p {{
    font-size: clamp(1rem, 2vw, 2rem);
}}

.st-key-hero button {{
    position: relative;
    overflow: visible;
    padding: 0rem 1 1rem;
    transition: transform 160ms ease;
}}

.st-key-hero button::after {{
    content: "";
    position: absolute;
    width: 14px;
    height: 1px;
    border-radius: 999px;
    background: linear-gradient(
        90deg,
        transparent,
        #f97316,
        #ffd166,
        transparent
    );
    filter: drop-shadow(0 0 4px #f97316);
    pointer-events: none;
    offset-path: inset(-2px round 8px);
    offset-distance: 0%;
    offset-rotate: auto;
    animation: hero-border-trace 5s linear infinite;
}}

@keyframes hero-border-trace {{
    to {{
        offset-distance: 100%;
    }}
}}

@media (prefers-reduced-motion: reduce) {{
    .st-key-hero button::after {{
        animation: none;
    }}
}}

@keyframes hero-shine {{
    0%, 30% {{ transform: translateX(-120%); }}
    100% {{ transform: translateX(120%); }}
}}

@media (prefers-reduced-motion: reduce) {{
    .st-key-hero button::after {{
        animation: none;
    }}
}}

.st-key-hero button:hover {{
    color: gold;
    transform: scale(1.04);
}}
</style>
""")

with st.container(
    key="hero"
):
    st.title("Vince Mathew L. Silva")
    st.write("Welcome to my Streamlit site.")

    st.button(
        "Learn about me",
        on_click=st.switch_page,
        args=("pages/about.py",),
        type="tertiary",
    )

    st.button(
        "Let's connect",
        on_click=st.switch_page,
        args=("pages/contact.py",),
        type="tertiary",
    )