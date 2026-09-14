# Mindfulness & Mental Clarity Platform

An interactive, zero-clutter web dashboard designed for somatic grounding, attention hygiene, and cognitive reset. Built with Python, Streamlit, and SQLite, featuring a high-contrast dark aesthetic with no visual noise or emojis.

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

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git

### Installation

1. Clone the repository:
   git clone [https://github.com/qbsgsjqk2102/Mindfulness.git](https://github.com/qbsgsjqk2102/Mindfulness.git)
   cd Mindfulness

2. Create and activate a virtual environment:
   macOS / Linux:
     python3 -m venv venv
     source venv/bin/activate
   Windows:
     python -m venv venv
     venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Launch the application:
   streamlit run app.py

The dashboard will open automatically in your browser at http://localhost:8501.

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

## Deployment (Streamlit Cloud)

1. Push your local changes to GitHub:
   git add .
   git commit -m "feat: complete platform setup"
   git push origin main

2. Log in to Streamlit Community Cloud ([https://share.streamlit.io/](https://share.streamlit.io/)) using your GitHub account.
3. Click New app.
4. Configure application settings:
   - Repository: qbsgsjqk2102/Mindfulness
   - Branch: main
   - Main file path: app.py
5. Click Deploy.

---

## License

Distributed under the MIT License. See LICENSE for details.
