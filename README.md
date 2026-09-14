# Mindfulness & Mental Clarity Platform

An interactive, zero-clutter web dashboard designed for somatic grounding, attention hygiene, and cognitive reset. Built with Python, Streamlit, and SQLite, featuring a high-contrast dark aesthetic with no visual noise or emojis.

---

## Live Demo

Try the live application directly in your browser:
**https://mindfulness-bamjgj5nyszq4ksg9bqy5j.streamlit.app/**

---

## Overview

The platform strips away abstract esoteric advice and focuses on practical, evidence-grounded mechanisms to de-escalate workday overload, re-establish physiological baseline, and reduce mental residue.

### Key Capabilities

- Actionable Knowledge Base: Deep, practical strategies targeting desk-level stress de-escalation, 2:00 AM insomnia loops, and digital context-switching costs.
- Somatic & Breathing Visualizers: Synchronized CSS cadence animations paired with live interval guides (Cadence 4-7-8 and Box Breathing 4-4-4-4).
- Protocol-Driven Meditations: Neutral, secular cognitive training modes (Systematic Body Scan, Anchor Point Attention, and Thought Detachment) with integrated countdown controls.
- Persistent Clarity Journal: Offline-first reflection and thought-dump logging backed by an embedded SQLite database (journal.db) with dynamic capacity indexing and record management.

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| Framework | Streamlit |
| Language | Python 3.10+ |
| Database | SQLite3 |
| Styling | Custom CSS & CSS3 Keyframe Animations via streamlit.components.v1 |
| Data Handling | Pandas |

---

## Project Structure

Mindfulness/
├── app.py              # Main application logic and UI
├── requirements.txt    # Python dependencies
├── journal.db          # Auto-generated SQLite database (git-ignored)
├── .gitignore          # Environment and database exclusions
└── README.md           # Project documentation

---

## Database Architecture

The application automatically initializes an embedded SQLite database (journal.db) on first launch:

CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    capacity TEXT,
    focus TEXT,
    notes TEXT
);

- All entries persist locally across sessions.
- Records render in reverse chronological order.
- Items can be removed directly from the interface using their dedicated record IDs.

---

## Local Development

If you want to run the project locally:

1. Clone repo:
   git clone https://github.com/qbsgsjqk2102/Mindfulness.git
   cd Mindfulness

2. Install dependencies:
   pip install -r requirements.txt

3. Run app:
   streamlit run app.py

---

## License

Distributed under the MIT License. See LICENSE for details.

