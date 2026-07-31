# IdeaLoom

> **AI-powered story idea generator — July AI Builders Challenge**
> *Reimagine Creative Industries with AI*

---

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Solution](#2-solution)
3. [AI Approach & Architecture](#3-ai-approach--architecture)
4. [Challenge Theme](#4-challenge-theme)
5. [How IBM Bob Was Used](#5-how-ibm-bob-was-used)
6. [Project Structure](#6-project-structure)
7. [Setup & Running Locally](#7-setup--running-locally)
8. [Usage](#8-usage)

---

## 1. Problem Statement

Writers, screenwriters, game designers, and creative professionals frequently encounter **writer's block** — a well-documented phenomenon where the blank page becomes an obstacle rather than a canvas. The ideation phase of any creative project is often the slowest and most frustrating:

- Staring at an empty document waiting for a spark that doesn't come.
- Generating story seeds manually is time-consuming and mentally draining.
- Generic "story prompt" lists online offer no personalisation — the same prompts for every mood, every genre, every writer.
- Creative teams in studios, agencies, and classrooms waste billable hours on early-stage ideation that a well-designed tool could accelerate dramatically.

The creative industries — publishing, film, games, advertising — all depend on a steady flow of fresh ideas. Anything that unblocks that flow at low cost and high speed has outsized value.

---

## 2. Solution

**IdeaLoom** is a lightweight, web-based story idea generator that turns two simple inputs — a **mood** and a **theme** — into a personalised narrative seed in under a second.

A writer selects how they want the story to *feel* (Mysterious, Whimsical, Romantic, Adventurous, Melancholic, or Playful), types in a central theme (e.g. *"lost memories"*, *"forbidden knowledge"*, *"a second chance"*), and clicks **Generate Idea**. IdeaLoom weaves those two dimensions together into a rich, evocative story concept that gives the writer something concrete to react to — a launchpad, not a script.

### Key design principles

| Principle | Implementation |
|---|---|
| **Zero friction** | No sign-up, no API key, runs entirely locally |
| **Mood-aware output** | Six distinct emotional registers, each with its own narrative voice |
| **Instantaneous** | Sub-100 ms response; no waiting for an external LLM call |
| **Visually immersive** | Dusk-sky gradient UI with SVG nature illustrations to prime creative thinking |

---

## 3. AI Approach & Architecture

### Approach — Mood-Based Template Generation

IdeaLoom uses a **structured, mood-conditioned text generation** approach. Rather than calling a large language model for every request (which would add latency, cost, and an external dependency), the system encodes creative intelligence directly into the application layer through curated *mood flavor phrases*:

```python
MOOD_PROMPTS = {
    "Mysterious": "shrouded in secrets and half-spoken truths",
    "Whimsical":  "filled with delightful absurdities and unexpected magic",
    "Romantic":   "woven through with longing, connection, and tender feeling",
    "Adventurous":"driven by daring choices and uncharted horizons",
    "Melancholic":"tinged with beautiful sadness and quiet reflection",
    "Playful":    "bursting with humor, mischief, and lighthearted twists",
}
```

Each phrase is a **compressed creative vector** — a carefully chosen string that, when combined with a free-text theme, reliably produces a coherent narrative tone. The generation function then constructs the idea by threading the mood flavor and user theme through a narrative template that hits four story-relevant beats:

1. **World-setting** — the mood establishes the emotional atmosphere of the story world.
2. **Protagonist conflict** — the theme becomes the character's central struggle.
3. **Narrative tension** — both dimensions are woven together to create a sense of stakes.
4. **Thematic resonance** — the reader is left with the mood as an emotional aftertaste.

This is an intentionally **explainable AI** design: the logic is transparent, auditable, and deterministic — important properties for a tool aimed at creative professionals who need to understand and trust the output.

### Architecture

```
Browser (HTML + Vanilla JS)
        │
        │  POST /generate  { mood, theme }
        ▼
Flask Backend (app.py)
        │
        ├─ Input validation (mood in allowed set, theme non-empty)
        ├─ Mood flavor lookup  (O(1) dictionary access)
        ├─ Template composition (f-string narrative weaving)
        └─ JSON response  { idea: "..." }
        │
        ▼
Browser — renders idea in the output area
```

**Stack:**

| Layer | Technology |
|---|---|
| Web framework | Python / Flask |
| Templating | Jinja2 (server-side HTML rendering) |
| Frontend | Vanilla HTML5, CSS3, JavaScript (ES2017 async/await) |
| AI layer | Mood-conditioned template generation (pure Python) |
| Styling | CSS custom properties, glassmorphism, inline SVG illustrations |

No database, no external APIs, no build step. The entire application is two files — `app.py` and `templates/index.html`.

---

## 4. Challenge Theme

**Selected challenge:** July AI Builders Challenge — *Reimagine Creative Industries with AI*

IdeaLoom directly addresses this theme by applying AI-assisted ideation to the **writing and storytelling industry**. The creative industries generate enormous economic and cultural value, yet the earliest, most fragile stage of the creative process — the blank-page moment — has historically had no meaningful tooling support.

IdeaLoom demonstrates that you do not need a billion-parameter model to add genuine creative value. A thoughtfully designed, mood-aware generation system built on sound linguistic principles can unblock a writer in seconds, accelerate early-stage ideation for creative teams, and make the creative process more accessible to people who struggle to find their starting point.

The project is intentionally small-scope and completable by a solo developer in a single session, proving that impactful AI tools for creative industries can be built fast, deployed cheaply, and used immediately — with no infrastructure overhead.

---

## 5. How IBM Bob Was Used

IBM Bob (the AI coding assistant embedded in the development environment) was the primary engineering collaborator for this project. Every file was created through a structured, conversational development process with Bob acting as a pair programmer.

### What Bob built

| Task | Bob's contribution |
|---|---|
| **Flask application scaffold** | Generated the full `app.py` from a plain-English description, including the route structure, `MOOD_PROMPTS` dictionary design, input validation, and JSON response format |
| **Frontend HTML/CSS** | Wrote the complete `templates/index.html` with glassmorphism card styling, dusk-sky gradient background, custom `<select>` chevron, and async form submission with loading state |
| **SVG decorative layer** | Generated all inline SVG illustrations (sun, crescent moon, four-point stars, mountain silhouettes, citrus slices, seashells) positioned around the page edges as a fixed background layer |
| **Design decisions** | Proposed the `position: fixed; z-index: 0; pointer-events: none` pattern for the decoration layer so it never interferes with form interaction |
| **This README** | Structured and written entirely through a single prompt describing the required sections |

### Development workflow

The entire project was built through **natural language instruction** — no manual file editing outside of Bob's suggestions. The workflow for each feature was:

1. Describe the requirement in plain English.
2. Bob reads the existing files, reasons about the minimal change needed, and writes or edits the code.
3. Review the output; iterate if needed.

This is a practical demonstration of the challenge theme itself: AI tools (like Bob) are already reimagining how software for creative industries gets built — faster, with less boilerplate friction, and accessible to developers at all experience levels.

---

## 6. Project Structure

```
IdeaLoom Submission/
├── app.py                  # Flask application — routes and generation logic
├── templates/
│   └── index.html          # Single-page frontend with inline CSS and JS
└── README.md               # This file
```

---

## 7. Setup & Running Locally

### Prerequisites

- Python 3.8 or later
- `pip`

### Installation

```bash
# 1. Clone or download the project folder
cd "IdeaLoom Submission"

# 2. (Recommended) Create a virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS / Linux
source venv/bin/activate

# 3. Install Flask
pip install flask
```

### Running the app

```bash
python app.py
```

Flask will start a development server. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

The app is ready to use — no further configuration required.

### Stopping the server

Press `Ctrl + C` in the terminal.

---

## 8. Usage

1. **Select a Mood** from the dropdown — choose the emotional register that fits the story you want to tell.
2. **Enter a Theme** — type any concept, emotion, situation, or phrase that interests you.
3. **Click Generate Idea** — IdeaLoom will compose a story seed tailored to your inputs.
4. **Read and react** — use the generated idea as a launchpad. Rewrite it, expand it, contradict it. The goal is to break the blank-page barrier, not to hand you a finished story.
5. **Iterate** — change the mood, refine the theme, generate again. Each combination produces a distinct narrative direction.

### Example inputs

| Mood | Theme | What you get |
|---|---|---|
| Mysterious | forgotten maps | A world of half-spoken cartographic secrets, a protagonist who can only navigate places that no longer exist |
| Whimsical | tax regulations | A delightfully absurd story where bureaucracy has become a form of ancient magic |
| Melancholic | the last summer | A quietly devastating narrative about endings that felt, at the time, like ordinary days |
| Adventurous | borrowed time | A race across uncharted horizons where every clock ticks backwards |

---

*Built with [IBM Bob](https://www.ibm.com/products/watson) for the July AI Builders Challenge.*
