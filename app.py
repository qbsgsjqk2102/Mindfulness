import streamlit as st
import streamlit.components.v1 as components
import time
import sqlite3
from datetime import datetime

DB_NAME = "journal.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            capacity TEXT,
            focus TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_entry(capacity, focus, notes):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    c.execute(
        "INSERT INTO journal (timestamp, capacity, focus, notes) VALUES (?, ?, ?, ?)",
        (created_at, capacity, focus, notes)
    )
    conn.commit()
    conn.close()

def fetch_entries():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, timestamp, capacity, focus, notes FROM journal ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_entry(entry_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM journal WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

init_db()

st.set_page_config(
    page_title="Mindfulness & Mental Clarity",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,500;1,400&display=swap');

    /* Global Base */
    .stApp {
        background-color: #0f1416 !important;
        color: #e6edf3 !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Headings */
    h1, h2, h3, h4 {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 600;
        color: #f0f6fc !important;
        letter-spacing: -0.02em;
    }

    p, li, span, label {
        color: #c9d1d9 !important;
        font-size: 15px;
        line-height: 1.65;
    }

    /* Cards */
    .content-card {
        background: #161e22;
        border: 1px solid #28373e;
        border-radius: 12px;
        padding: 26px;
        margin-bottom: 22px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.28);
    }

    .card-meta {
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #7ee787;
        margin-bottom: 8px;
    }

    .card-title {
        font-size: 22px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 12px;
    }

    .card-text {
        font-size: 15px;
        color: #a2b0ba;
        line-height: 1.65;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #12191c !important;
        border-right: 1px solid #232f35;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(180deg, #238636 0%, #1e702e 100%);
        color: #ffffff !important;
        border: 1px solid #2ea043;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease-in-out;
    }

    .stButton > button:hover {
        background: linear-gradient(180deg, #2ea043 0%, #238636 100%);
        border-color: #3fb950;
        box-shadow: 0 0 12px rgba(46, 160, 67, 0.4);
    }

    /* Form Controls & Inputs */
    .stTextInput > div > div > input, 
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background-color: #192329 !important;
        color: #f0f6fc !important;
        border: 1px solid #33444d !important;
        border-radius: 8px;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 1px solid #28373e;
        gap: 16px;
    }

    .stTabs [data-baseweb="tab"] {
        color: #8b949e !important;
        font-size: 15px;
        font-weight: 500;
        padding: 12px 4px;
    }

    .stTabs [aria-selected="true"] {
        color: #7ee787 !important;
        border-bottom: 2px solid #7ee787 !important;
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# session storage
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

# sidebar navigation
with st.sidebar:
    st.markdown("### Navigation")
    section = st.radio(
        label="Select Section:",
        options=[
            "Practical Articles",
            "Breathing & Somatics",
            "Guided Meditations",
            "Clarity Journal"
        ],
        index=0
    )
    st.markdown("---")
    st.markdown("""
    **Mindfulness Platform**  
    A minimalist tool for grounding, attention hygiene, and active cognitive recovery.
    """)
    
# section1
if section == "Practical Articles":
    st.markdown("## Practical Insights & Guides")
    st.markdown(
        "Straightforward strategies to reduce mental friction, prevent burnout, and manage attention without spiritual jargon.")
    st.markdown("<br>", unsafe_allow_html=True)

    filter_option = st.selectbox(
        "Filter by theme:",
        ["All Topics", "Daily Stress & Overwhelm", "Sleep & Night Recovery", "Digital Fatigue & Focus"]
    )

    articles = [
        {
            "category": "Daily Stress & Overwhelm",
            "title": "De-escalating Chronic Tension When Your Day Goes Off Track",
            "reading_time": "5 min read",
            "preview": "When workloads surge, advice like 'take a warm bath' feels useless. Here is what you can do at your desk in under 3 minutes to stop the physical panic spiral.",
            "body": """
### The Reality of Acute Work Stress

When deadlines collapse and demands stack up simultaneously, telling yourself to 'calm down' rarely produces any positive effect. The mind cannot easily talk the body out of a state that the body believes is a legitimate emergency.

Instead of fighting your thoughts, change the physical input first:

#### 1. The 30-Second Physical Anchor
When panic spikes, your posture usually collapses forward and breathing shifts to the upper clavicles. Sit upright, plant both feet firmly against the floor, and press the soles down deliberately. Notice the resistance of the ground. This sounds basic, but providing tactile resistance pulls activity away from racing anticipatory loops and back to somatic sensory input.

#### 2. The Rapid Exhale Shift
Take a sharp inhale through the nose, immediately follow it with a short top-off sniff to fill the lung bases, and let out a prolonged sigh through parted lips. Repeat this two to three times. This mechanically stimulates the vagus nerve and gently pulls your resting pulse rate down.

#### 3. The 3-Task Triage Rule
When overwhelmed, your working memory tries to process ten competing emergencies at once. Write everything down on a physical scrap of paper. Cross out everything except the single immediate task that unlocks the rest. Everything else gets paused for 45 minutes. Focus is not about feeling relaxed; it is about eliminating choices.
            """
        },
        {
            "category": "Sleep & Night Recovery",
            "title": "Stopping the 2:00 AM Mental Loop",
            "reading_time": "6 min read",
            "preview": "You feel completely drained all day, but the moment your head hits the pillow, your brain decides to audit every conversation you had since 2019. Here is how to break the habit.",
            "body": """
### Why Your Brain Awakens Right at Bedtime

During waking hours, a constant stream of external inputs (messages, notifications, tasks, media) occupies your cognitive bandwidth. The moment you close your eyes in a quiet room, those external inputs vanish. The brain, noticing an idle queue, immediately fills the void with unresolved emotional and logistical backlogs.

Here is an actionable protocol to reclaim deep rest:

#### 1. The Pre-Bed Brain Dump (1 Hour Before Rest)
Keep an analog notepad on your bedside table or workspace. Set a timer for five minutes. Write down every unfinished obligation, every reminder, and every persistent worry without filtering grammar or structure. Once it is physically preserved on paper, the unconscious mind stops working overtime to keep it active in short-term memory.

#### 2. The 20-Minute Departure Rule
If you lie awake tossing for longer than 20 minutes, your brain begins associating your bed with vigilance and frustration. Get out of bed. Move to a dimly lit room or comfortable chair. Open a physical book (avoid screens and intense literature) or practice passive breath counting. Return to bed only when genuine drowsiness sets in.

#### 3. Progressive Body Uncoupling
Instead of forcing yourself to sleep, adopt the mindset that resting motionless with relaxed eyes is already 80% as restorative as light sleep. Soften your jaw, let your shoulders drop away from your ears, and release the tension around your eyes. The physical release often lets sleep arrive on its own.
            """
        },
        {
            "category": "Digital Fatigue & Focus",
            "title": "The Low-Friction Digital Reset for Scattered Attention",
            "reading_time": "5 min read",
            "preview": "Constant micro-switches between browser tabs and instant messages leave you exhausted even when you have not finished much. How to establish sustainable boundaries.",
            "body": """
### The Invisible Cost of Micro-Switching

Every time you glance away from an active task to read a notification, your attention does not seamlessly hop back. A small fraction remains tethered to that message for minutes. This phenomenon—attention residue—explains why you can feel completely depleted at the end of the day despite feeling like you accomplished very little.

#### Tactical Interventions:

#### 1. Batching and Tab Hygiene
Close tabs that are not directly serving the task in front of you. If you need them later, bookmark them into a single temporary folder named 'Later'. Having 30 visible tabs creates persistent cognitive clutter that drains executive energy.

#### 2. The 45/10 Protocol
Work in continuous 45-minute blocks dedicated solely to one objective. Turn off desktop banner notifications. When the 45-minute block ends, step away from the monitor for 10 minutes. Look out a window, drink water, or stretch. Do not use the break to browse social media, as that continues to demand visual and cognitive attention.

#### 3. Establish a Shutdown Boundary
End your workday with a concrete ritual: close work software, check your agenda for tomorrow morning, and physically close your laptop or leave the desk. A tangible closing boundary trains your nervous system to disengage rather than remain in perpetual readiness.
            """
        }
    ]

    for art in articles:
        if filter_option == "All Topics" or art["category"] == filter_option:
            st.markdown(f"""
            <div class="content-card">
                <div class="card-meta">{art['category']} &bull; {art['reading_time']}</div>
                <div class="card-title">{art['title']}</div>
                <div class="card-text">{art['preview']}</div>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("Read Article"):
                st.markdown(art["body"])

# section2
elif section == "Breathing & Somatics":
    st.markdown("## Interactive Somatic Practices")
    st.markdown("Follow the visual rhythm to reset autonomic tone and regain physical composure.")
    st.markdown("<br>", unsafe_allow_html=True)

    practice_tabs = st.tabs(["Cadence Breathing (4-7-8)", "Box Reset (4-4-4-4)", "5-Step Grounding Protocol"])

    with practice_tabs[0]:
        col_anim, col_info = st.columns([1, 1], gap="large")

        with col_anim:
            st.markdown("#### Visual Breathing Anchor")
            
            components.html("""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
                body {
                    margin: 0;
                    background: transparent;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 280px;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                }
                .circle-container {
                    position: relative;
                    width: 200px;
                    height: 200px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .outer-pulse {
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    border-radius: 50%;
                    background: radial-gradient(circle, rgba(126, 231, 135, 0.25) 0%, rgba(35, 134, 54, 0.05) 70%);
                    animation: cadence 19s infinite ease-in-out;
                }
                .core-circle {
                    width: 70px;
                    height: 70px;
                    background-color: #238636;
                    border: 2px solid #7ee787;
                    border-radius: 50%;
                    box-shadow: 0 0 20px rgba(126, 231, 135, 0.4);
                }
                @keyframes cadence {
                    0% { transform: scale(0.6); opacity: 0.4; }
                    21% { transform: scale(1.3); opacity: 0.9; }    /* Inhale 4s */
                    58% { transform: scale(1.3); opacity: 0.8; }    /* Hold 7s */
                    100% { transform: scale(0.6); opacity: 0.4; }   /* Exhale 8s */
                }
            </style>
            </head>
            <body>
                <div class="circle-container">
                    <div class="outer-pulse"></div>
                    <div class="core-circle"></div>
                </div>
            </body>
            </html>
            """, height=300)

        with col_info:
            st.markdown("#### How to execute 4-7-8:")
            st.markdown("""
            * **Inhale (4 seconds):** Breathe in smoothly through your nose into the diaphragm.
            * **Hold (7 seconds):** Keep your chest still and throat open without tensing.
            * **Exhale (8 seconds):** Release the breath completely through your mouth with a gentle, steady sound.
            """)
            cycles_input = st.slider("Select practice cycles:", min_value=2, max_value=8, value=3)

            if st.button("Start Live Cadence Guide", key="start_cadence"):
                status_placeholder = st.empty()
                progress_bar = st.progress(0)
                total_duration = cycles_input * 19
                elapsed = 0

                for cycle in range(cycles_input):
                
                    for s in range(4, 0, -1):
                        status_placeholder.markdown(f"### Inhale through nose... ({s}s)")
                        time.sleep(1)
                        elapsed += 1
                        progress_bar.progress(elapsed / total_duration)
                    
                    for s in range(7, 0, -1):
                        status_placeholder.markdown(f"### Hold breath steady... ({s}s)")
                        time.sleep(1)
                        elapsed += 1
                        progress_bar.progress(elapsed / total_duration)
                    
                    for s in range(8, 0, -1):
                        status_placeholder.markdown(f"### Exhale completely... ({s}s)")
                        time.sleep(1)
                        elapsed += 1
                        progress_bar.progress(elapsed / total_duration)

                status_placeholder.markdown("### Protocol complete. Return to your natural breathing.")

    with practice_tabs[1]:
        st.markdown("#### Box Breathing (Equal Cadence)")
        st.write(
            "Four equal parts: 4s inhale, 4s hold, 4s exhale, 4s hold. Used to quickly stabilize acute physiological arousal.")

        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {
                margin: 0;
                background: transparent;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 240px;
            }
            .box-wrapper {
                width: 140px;
                height: 140px;
                border: 2px solid #33444d;
                border-radius: 12px;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
            }
            .box-fill {
                width: 100%;
                height: 100%;
                background: rgba(56, 139, 253, 0.15);
                border-radius: 10px;
                animation: boxpulse 16s infinite ease-in-out;
            }
            @keyframes boxpulse {
                0% { transform: scale(0.3); opacity: 0.3; }
                25% { transform: scale(1.0); opacity: 0.9; }   /* Inhale 4s */
                50% { transform: scale(1.0); opacity: 0.8; }   /* Hold 4s */
                75% { transform: scale(0.3); opacity: 0.3; }   /* Exhale 4s */
                100% { transform: scale(0.3); opacity: 0.3; }  /* Hold 4s */
            }
        </style>
        </head>
        <body>
            <div class="box-wrapper">
                <div class="box-fill"></div>
            </div>
        </body>
        </html>
        """, height=250)

    with practice_tabs[2]:
        st.markdown("#### The 5-4-3-2-1 Sensory Anchor")
        st.write("Use this sequence whenever racing thoughts detach you from your immediate surroundings.")

        st.markdown("""
        1. **5 Things You Can See:** Notice fine details around you: the grain of your desk, light reflections, edge alignment.
        2. **4 Things You Can Touch:** Feel your feet in your shoes, the texture of your clothing, the cool surface of a tabletop.
        3. **3 Sounds You Can Hear:** Identify ambient noise: background traffic, air circulation, distant keys typing.
        4. **2 Scents You Can Sense:** Notice any subtle scent in the room or simply the neutral air intake.
        5. **1 Physical Sensation:** Notice your tongue resting comfortably at the roof of your mouth.
        """)

# section3
elif section == "Guided Meditations":
    st.markdown("## Structured Meditation Sessions")
    st.markdown(
        "Functional, step-by-step attention sessions designed to cultivate psychological distance from stressful thoughts.")
    st.markdown("<br>", unsafe_allow_html=True)

    session_type = st.selectbox(
        "Select Session Mode:",
        [
            "De-escalation & Body Reset (10 min)",
            "Single-Point Focus (5 min)",
            "Open Cognitive Observation (15 min)"
        ]
    )

    col_med_guide, col_med_timer = st.columns([3, 2], gap="large")

    with col_med_guide:
        if "De-escalation" in session_type:
            st.markdown("### Protocol: Systematic Body Scan")
            st.write("""
            **Core Objective:** Notice and release accumulated muscular armor without forcing an emotional state.

            1. Settle into a neutral sitting position with your back supported. Close your eyes or soften your gaze downward.
            2. Direct attention to where your feet contact the floor. Observe temperature, pressure, or stillness.
            3. Move attention upward: calves, knees, thighs. Where you sense tightening, consciously allow it to soften on the exhale.
            4. Notice the abdomen. Allow your belly to expand naturally on each inhale without holding it in.
            5. Release the jaw, let your teeth unclench, and smooth the skin around your temples.
            6. When thoughts intrude, acknowledge them as mental noise, and return your focus to the physical sensation of sitting.
            """)
        elif "Single-Point Focus" in session_type:
            st.markdown("### Protocol: Anchor Point Attention")
            st.write("""
            **Core Objective:** Build sustained attentional endurance.

            1. Choose a single point of breath contact: either the cool sensation at your nostrils or the gentle rise of your chest.
            2. Keep your focus anchored strictly on that single spot.
            3. Count each complete breath cycle (inhale + exhale = 1) up to 10, then start again at 1.
            4. If you lose count or catch your mind planning, simply notice it without frustration and reset the count back to 1.
            """)
        else:
            st.markdown("### Protocol: Thought Detachment")
            st.write("""
            **Core Objective:** Observe thoughts as transient mental events rather than immediate directives for action.

            1. Sit quietly and broaden your awareness to take in everything happening right now.
            2. Instead of focusing on one object, observe whatever enters consciousness: sounds, physical aches, thoughts, memories.
            3. Treat thoughts like passing traffic on a distant road. You do not need to flag down every car; let them arrive, stay briefly, and leave.
            """)

    with col_med_timer:
        st.markdown("### Session Timer")
        duration_minutes = st.number_input("Session length (minutes):", min_value=1, max_value=60, value=5)

        if st.button("Start Meditation Timer", key="start_meditation"):
            timer_box = st.empty()
            total_sec = int(duration_minutes * 60)

            while total_sec > 0:
                mins, secs = divmod(total_sec, 60)
                timer_box.markdown(
                    f"<h2 style='color:#7ee787; font-family:monospace;'>Time Remaining: {mins:02d}:{secs:02d}</h2>",
                    unsafe_allow_html=True)
                time.sleep(1)
                total_sec -= 1

            timer_box.markdown("<h2 style='color:#7ee787;'>Session Completed</h2>", unsafe_allow_html=True)
            st.success("Practice recorded. Take a moment before returning to your screen.")

# section4
elif section == "Clarity Journal":
    st.markdown("## Clarity & Attention Journal")
    st.markdown("Externalize mental noise to free up working memory. All reflections are persistently stored.")
    st.markdown("<br>", unsafe_allow_html=True)

    with st.form("journal_entry_form", clear_on_submit=True):
        st.markdown("#### Record a Reflection")
        clarity_rating = st.select_slider(
            "Current Cognitive Capacity:",
            options=["Depleted", "Low / Fragmented", "Moderate", "Clear", "Sharp & Energized"],
            value="Moderate"
        )
        current_focus = st.text_input(
            "Dominant Task or Theme:",
            placeholder="E.g., Presentation prep, afternoon fatigue, restless focus..."
        )
        notes = st.text_area(
            "Unfiltered Brain Dump:",
            placeholder="Write down unfinished thoughts, current tensions, or immediate priorities...",
            height=130
        )

        submitted = st.form_submit_button("Persist Entry")
        if submitted:
            if current_focus.strip() or notes.strip():
                save_entry(
                    capacity=clarity_rating,
                    focus=current_focus.strip() if current_focus.strip() else "Untitled Observation",
                    notes=notes.strip()
                )
                st.success("Entry saved permanently to the database.")
            else:
                st.warning("Please provide a title or write down notes before saving.")

    entries = fetch_entries()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### Journal History ({len(entries)} entries)")

    if not entries:
        st.info("No journal entries found yet. Submit your first entry above.")
    else:
        for entry in entries:
            entry_id, timestamp, capacity, focus, body_text = entry

            with st.container():
                st.markdown(f"""
                <div class="content-card">
                    <div class="card-meta">{timestamp} &bull; Capacity: {capacity}</div>
                    <div class="card-title">{focus}</div>
                    <div class="card-text">{body_text}</div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("Delete Entry", key=f"del_{entry_id}"):
                    delete_entry(entry_id)
                    st.rerun()
