"""
LifeQuest AI
Version 1.0
Main Application
"""

import streamlit as st
import pandas as pd

from config import *
from player import Player
from game_engine import GameEngine

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="LifeQuest AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM THEME
# -------------------------------------------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(135deg,#07070d,#14001f,#1b1035);
color:white;
}

section[data-testid="stSidebar"]{
background:#09090f;
}

h1,h2,h3{
color:#bb86fc;
}

.stat-card{
background:#171722;
padding:18px;
border-radius:15px;
border:1px solid #7c3aed;
text-align:center;
box-shadow:0 0 15px rgba(124,58,237,.3);
margin-bottom:10px;
}

.scenario-card{
background:#15151f;
padding:25px;
border-radius:20px;
border:2px solid #8b5cf6;
box-shadow:0 0 20px rgba(139,92,246,.25);
}

.choice-btn button{
width:100%;
height:55px;
border-radius:15px;
font-size:17px;
font-weight:bold;
background:linear-gradient(90deg,#7c3aed,#ec4899);
color:white;
}

.footer{
text-align:center;
padding:20px;
color:gray;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "player" not in st.session_state:
    st.session_state.player = None

if "engine" not in st.session_state:
    st.session_state.engine = None

if "started" not in st.session_state:
    st.session_state.started = False

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🌍 LifeQuest AI")

st.caption("Every Decision Creates Your Future")

st.divider()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.header("🎮 New Game")

    player_name = st.text_input(
        "Player Name",
        value="Player"
    )

    role = st.selectbox(
        "Choose Role",
        ROLES
    )

    if st.button("🚀 Start Journey", use_container_width=True):

        player = Player(
            name=player_name,
            role=role
        )

        engine = GameEngine(player)

        st.session_state.player = player
        st.session_state.engine = engine
        st.session_state.started = True

        st.success("Journey Started!")

# -------------------------------------------------
# START SCREEN
# -------------------------------------------------

if not st.session_state.started:

    st.markdown("""

# Welcome to LifeQuest AI

LifeQuest AI is an AI-powered life simulation game.

Choose your role and begin your journey.

### Available Roles

🎓 Student

👨‍💼 Employee

🚜 Farmer

👨‍👩‍👧 Parent

👮 Officer

💼 Entrepreneur

Every decision changes your future.

""")

    st.stop()

player = st.session_state.player
engine = st.session_state.engine
# =====================================================
# PLAYER DASHBOARD
# =====================================================

st.markdown("## 🎮 Player Dashboard")

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown(
        f"""
<div class="stat-card">

<h2>👤 {player.name}</h2>

<h4>{player.role}</h4>

<h3>⭐ Level {player.level}</h3>

</div>
""",
        unsafe_allow_html=True,
    )

with col2:

    st.markdown(
        f"""
<div class="stat-card">

<h3>🏆 Achievements</h3>

<h1>{len(player.achievements)}</h1>

</div>
""",
        unsafe_allow_html=True,
    )

st.write("")

# =====================================================
# PLAYER STATS
# =====================================================

stats = player.stats

col1, col2 = st.columns(2)

with col1:

    st.markdown("### ❤️ Health")
    st.progress(stats["Health"] / 100)

    st.markdown("### 💰 Money")
    st.progress(min(stats["Money"], 100) / 100)

    st.markdown("### 🧠 Knowledge")
    st.progress(stats["Knowledge"] / 100)

    st.markdown("### 😊 Happiness")
    st.progress(stats["Happiness"] / 100)

with col2:

    st.markdown("### ⭐ Reputation")
    st.progress(stats["Reputation"] / 100)

    st.markdown("### ⚡ Energy")
    st.progress(stats["Energy"] / 100)

    xp_progress = (stats["Experience"] % 100) / 100

    st.markdown("### 📈 Experience")
    st.progress(xp_progress)

    st.metric(
        "Total XP",
        stats["Experience"]
    )

st.divider()

# =====================================================
# QUICK PLAYER SUMMARY
# =====================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Completed Scenarios",
        player.completed_scenarios
    )

with c2:
    st.metric(
        "Player Level",
        player.level
    )

with c3:
    st.metric(
        "Achievements",
        len(player.achievements)
    )

with c4:
    st.metric(
        "Current Role",
        player.role
    )

st.divider()
# =====================================================
# GAMEPLAY
# =====================================================

st.markdown("## 📖 Today's Challenge")

# Load first scenario
if "current_scenario" not in st.session_state:
    st.session_state.current_scenario = engine.next_scenario()

scenario = st.session_state.current_scenario

if scenario is None:
    st.error("No scenarios available for this role.")
    st.stop()

# -----------------------------------------------------
# Scenario Card
# -----------------------------------------------------

st.markdown(
    f"""
<div class="scenario-card">

<h2>{scenario['title']}</h2>

<p style="font-size:18px;">
{scenario['story']}
</p>

</div>
""",
    unsafe_allow_html=True
)

st.write("")

st.subheader("Choose your action")

# -----------------------------------------------------
# Choice Buttons
# -----------------------------------------------------

cols = st.columns(3)

for i, choice in enumerate(scenario["choices"]):

    with cols[i]:

        if st.button(
            choice,
            key=f"choice_{i}",
            use_container_width=True
        ):

            result = engine.choose(i)

            if result["success"]:

                st.success("Decision completed!")

                # Show stat changes
                st.markdown("### 📊 Consequences")

                for stat, value in result["effects"].items():

                    emoji = "📈" if value >= 0 else "📉"

                    st.write(
                        f"{emoji} **{stat}** : {value:+}"
                    )

                # Show achievements
                if result["achievements"]:

                    st.balloons()

                    st.markdown("## 🏆 Achievement Unlocked!")

                    for achievement in result["achievements"]:

                        st.success(achievement)

                # Generate next scenario
                st.session_state.current_scenario = engine.next_scenario()

                st.rerun()

            else:

                st.error(result["message"])

st.divider()

# -----------------------------------------------------
# Next Scenario Button
# -----------------------------------------------------

if st.button(
    "🎲 Skip To Another Scenario",
    use_container_width=True
):

    st.session_state.current_scenario = engine.next_scenario()

    st.rerun()
  # =====================================================
# ACHIEVEMENTS
# =====================================================

st.markdown("## 🏆 Achievement Gallery")

if player.achievements:

    cols = st.columns(3)

    for i, achievement in enumerate(player.achievements):
        with cols[i % 3]:
            st.success(achievement)

else:

    st.info(
        "No achievements unlocked yet.\n\n"
        "Complete more scenarios to unlock badges!"
    )

st.divider()

# =====================================================
# PLAYER STATISTICS
# =====================================================

st.markdown("## 📊 Current Statistics")

stats_df = pd.DataFrame(
    {
        "Statistic": list(player.stats.keys()),
        "Value": list(player.stats.values())
    }
)

st.dataframe(
    stats_df,
    use_container_width=True,
    hide_index=True
)

st.bar_chart(
    stats_df.set_index("Statistic")
)

st.divider()

# =====================================================
# GAME SUMMARY
# =====================================================

st.markdown("## 🌍 Journey Summary")

left, right = st.columns(2)

with left:

    st.info(f"""
### 👤 Player

**Name:** {player.name}

**Role:** {player.role}

**Level:** {player.level}

**Completed Scenarios:** {player.completed_scenarios}
""")

with right:

    st.success(f"""
### ⭐ Progress

Experience : {player.stats["Experience"]}

Achievements : {len(player.achievements)}

Knowledge : {player.stats["Knowledge"]}

Reputation : {player.stats["Reputation"]}
""")

st.divider()

# =====================================================
# RESTART
# =====================================================

if st.button(
    "🔄 Start New Journey",
    use_container_width=True
):

    st.session_state.clear()

    st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    """
<div class="footer">

<h3>🌍 LifeQuest AI</h3>

<p>
Version 1.0
</p>

<p>
Every Decision Creates Your Future
</p>

</div>
""",
    unsafe_allow_html=True
)
