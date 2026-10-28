import requests
import streamlit as st


QUERY = """
query ($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

@st.cache_data(ttl="1d", max_entries=32)
def fetch_contributions(username, token, year, end_date):
    response = requests.post(
        "https://api.github.com/graphql",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "query": QUERY,
            "variables": {
                "login": username,
                "from": f"{year}-01-01T00:00:00Z",
                "to": f"{end_date}T23:59:59Z",
            },
        },
        timeout=15,
    )
    response.raise_for_status()
    result = response.json()

    if result.get("errors"):
        messages = "; ".join(error["message"] for error in result["errors"])
        raise ValueError(f"GitHub API error: {messages}")

    user = result.get("data", {}).get("user")
    if user is None:
        raise ValueError(f"GitHub user not found: {username}")

    weeks = user["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [
        day
        for week in weeks
        for day in week["contributionDays"]
    ]