import base64
from pathlib import Path

import streamlit as st

image_dir = Path(__file__).resolve().parent.parent / "assets" / "images"
background_data = base64.b64encode(
    (image_dir / "contact.png").read_bytes()
).decode("ascii")
social_links = [
    ("LinkedIn", "linkedin.png", "https://www.linkedin.com/in/vince-mathew-silva-755080365/"),
    ("GitHub", "github.png", "https://github.com/neaterpoint"),
    ("Email", "email.png", "mailto:silvavincemathew@gmail.com"),
]

cards = []
for label, image_name, url in social_links:
    image_data = base64.b64encode((image_dir / image_name).read_bytes()).decode("ascii")
    cards.append(
        f"""
        <a class="contact-card" href="{url}">
            <img src="data:image/png;base64,{image_data}" alt="" />
            <span>{label}</span>
        </a>
        """
    )

st.title("Connect", text_alignment="center")

st.html(f"""
<style>
.stApp {{
    background:
        linear-gradient(rgba(0, 0, 0, 0.18), rgba(0, 0, 0, 0.18)),
        url("data:image/png;base64,{background_data}") center center / cover no-repeat fixed;
}}

.contact-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.5rem;
}}

.contact-card {{
    min-height: 15rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    padding: 1.5rem;
    border-radius: 0.75rem;
    color: inherit;
    text-decoration: none;
    font-size: 1.5rem;
    font-weight: 600;
    transition: transform 160ms ease, box-shadow 160ms ease;
}}

.contact-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 0.5rem 1.5rem rgba(132, 204, 22, 0.35);
}}

.contact-card:focus-visible {{
    outline: 3px solid #84cc16;
    outline-offset: 3px;
}}

.contact-card img {{
    width: 256px;
    height: 256px;
    max-width: 100%;
    object-fit: contain;
}}

@media (max-width: 640px) {{
    .contact-grid {{
        grid-template-columns: 1fr;
    }}
}}

@media (prefers-reduced-motion: reduce) {{
    .contact-card {{
        transition: none;
    }}
}}
</style>

<div class="contact-grid">
    {''.join(cards)}
</div>
""")
