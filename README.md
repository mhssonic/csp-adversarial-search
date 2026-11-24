# AI Project 2 — CSP Map Coloring & Chess AI

Second project for **Introduction to AI** (Amirkabir University of Technology).

This repository contains two parts:

1. **Map coloring (CSP)** — constraint satisfaction with backtracking  
2. **Chess Grandmaster AI** — adversarial search (Minimax / Alpha-Beta / Expectimax) with a Pygame UI

---

## Part 1 — Map coloring (`BAI_HW2/CSP`)

Colors a political map so no two adjacent regions share a color, using CSP backtracking (optional MRV / LCV ordering and filtering).

### Setup

```bash
cd BAI_HW2/CSP
pip install -r requirements.txt
```

### Run

```bash
python solver.py
```

Uses map images in the same folder (`iran.jpg`, `usa.png`, etc.).

---

## Part 2 — Chess Grandmaster AI (`Chess-Grandmaster-AI`)

Play against (or watch) AI agents built with Minimax, Alpha-Beta pruning, and Expectimax.

### Setup

```bash
cd Chess-Grandmaster-AI
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
python src/main.py
```

Useful flags:

| Flag | Meaning | Default |
|------|---------|---------|
| `-p` / `--play-type` | `PlayerVsBot` or `BotVsBot` | `PlayerVsBot` |
| `-af` / `--main-agent` | `RandomAgent`, `MinimaxAgent`, `AlphaBetaAgent`, `ExpectimaxAgent` | `RandomAgent` |
| `-as` / `--second-agent` | Second bot (BotVsBot) | `RandomAgent` |
| `-df` / `--main-agent-depth` | Search depth | `2` |
| `-ds` / `--second-agent-depth` | Second agent depth | `2` |

Example (bots only):

```bash
python src/main.py -p BotVsBot -af AlphaBetaAgent -as AlphaBetaAgent -df 3 -ds 3
```

---

## Requirements

- Python 3.9+
- CSP: OpenCV, NumPy, SciPy (see `BAI_HW2/CSP/requirements.txt`)
- Chess: `pygame`, `python-chess`, `numpy` (see `Chess-Grandmaster-AI/requirements.txt`)
