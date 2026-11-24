# Constraint Satisfaction & Adversarial Search

Two complementary AI modules from *Introduction to Artificial Intelligence* (Amirkabir University of Technology):

1. **Map coloring with CSP** — backtracking search over region adjacency graphs  
2. **Chess AI** — Minimax, Alpha-Beta pruning, and Expectimax with a Pygame board UI

**Resume-ready summary:** *Solved map coloring as a CSP with backtracking heuristics, and built a chess agent using Minimax / Alpha-Beta / Expectimax.*

---

## Part 1 — Map coloring (`BAI_HW2/CSP`)

Colors political map regions so no two neighbors share a color. Regions are extracted from images; the problem is solved as a **constraint satisfaction problem** with backtracking (optional variable/value ordering and filtering).

### Setup & run

```bash
cd BAI_HW2/CSP
pip install -r requirements.txt
python solver.py
```

Sample maps: `iran.jpg`, `usa.png`, `tehran_province.jpg`.

### Topics

- CSP formulation (variables, domains, constraints)
- Backtracking search
- Heuristics: variable ordering / value ordering / filtering

### Stack

Python · OpenCV · NumPy · SciPy

---

## Part 2 — Chess Grandmaster AI (`Chess-Grandmaster-AI`)

Play against or watch AI agents on a full chessboard. Game rules are handled by `python-chess`; the GUI is Pygame.

### Setup & run

```bash
cd Chess-Grandmaster-AI
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

### Agents & modes

| Option | Values |
|--------|--------|
| `-p` play type | `PlayerVsBot`, `BotVsBot` |
| `-af` / `-as` agents | `RandomAgent`, `MinimaxAgent`, `AlphaBetaAgent`, `ExpectimaxAgent` |
| `-df` / `-ds` depth | search depth (default `2`) |

```bash
python src/main.py -p BotVsBot -af AlphaBetaAgent -as AlphaBetaAgent -df 3 -ds 3
```

### Topics

- Adversarial search (Minimax)
- Alpha-Beta pruning
- Expectimax for stochastic opponent models
- Evaluation functions & search depth vs. play strength

### Stack

Python · Pygame · python-chess · NumPy

---

## Course

Introduction to Artificial Intelligence — Amirkabir University of Technology
