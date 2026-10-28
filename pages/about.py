from datetime import date
import base64
from pathlib import Path

import pandas as pd
import requests
import streamlit as st
import altair as alt

from services.github import fetch_contributions

image_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "about.png"
image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")

st.html(f"""
<style>
.stApp {{
    background:
        linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
        url("data:image/png;base64,{image_data}") right center / cover no-repeat fixed;
}}

.stMarkdown p {{
    font-size: 20px;
}}

.bio {{
    font-size: 20px;
}}
</style>
""")

today = date.today()

st.title("Autobiography")
st.markdown(
    '<p class="bio">I’m Vince Mathew L. Silva, a third-year BSCS student from Philippines. '
    'My senior high school experience and the people I met there helped shape who I am today. '
    'Outside of studying, I enjoy listening to music—I have more than 5,000 liked songs on Spotify—and exploring wherever I can take myself. '
    'I value trust, honesty, and reliability, and I hope to build practical projects that make a meaningful difference in the real world.</p>',
    unsafe_allow_html=True,
)

st.subheader(f"My GitHub contributions in {today.year}")

try:
    days = fetch_contributions(
        username="neaterpoint",
        token=st.secrets["github_token"],
        year=today.year,
        end_date=today.isoformat(),
    )
except KeyError:
    st.error("Add github_token to .streamlit/secrets.toml.")
    st.stop()
except (requests.RequestException, ValueError) as error:
    st.error(f"Could not load GitHub contributions: {error}")
    st.stop()

df = pd.DataFrame(days).rename(columns={"contributionCount": "count"})
df["date"] = pd.to_datetime(df["date"])

chart = (
    alt.Chart(df)
    .mark_line(color="#90ee90")
    .encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("count:Q", title="Contributions"),
    )
    .configure(background="transparent")
    .configure_view(fill="transparent", strokeOpacity=0)
)

st.altair_chart(
    chart,
    width="stretch",
    alt="Daily GitHub contributions this year",
)