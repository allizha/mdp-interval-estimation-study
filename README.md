# Model-Based Interval Estimation for MDPs

### Reproduction & Extension Study
### Seminar — Advanced Topics in Reinforcement Learning and Decision Making
### Prof. Christos Dimitrakakis — University of Neuchâtel

This repository contains the implementation and results of a seminar project conducted in **Advanced Topics in Reinforcement Learning and Decision Making**, within the [Swiss Joint Master in Computer Science](https://mcs.unibnf.ch/).

The project reproduces and extends the results of:

> Strehl, A. L., & Littman, M. L. (2008).  
> [An Analysis of Model-Based Interval Estimation for Markov Decision Processes](https://www.sciencedirect.com/science/article/pii/S0022000008000767?ref=pdf_download&fr=RR-2&rr=9dfde5654e296aa0).  
> Journal of Computer and System Sciences, 74(8), pages 1309–1331.

---

## Project Overview

This project investigates model-based reinforcement learning methods for Markov Decision Processes (MDPs), with a focus on interval estimation techniques for efficient exploration. We reproduce the key theoretical and experimental results from Strehl & Littman (2008) and extend them through six additional experiments that probe the algorithms' behaviour across different parameter regimes and environments.

---

## What We Did

### Reproduction
We reproduced Figures 2 and 3 of the paper — cumulative reward after 5000 steps on RiverSwim and SixArms — using the paper's exact parameter settings. All four algorithms were implemented from scratch:

- **MBIE** — Model-Based Interval Estimation (Strehl & Littman, 2008)
- **MBIE-EB** — MBIE with Exploration Bonus (Strehl & Littman, 2008)
- **R-Max** — Brafman & Tennenholtz (2002)
- **E3** — Explicit Explore or Exploit (Kearns & Singh, 2002)

### Extensions
Six extensions were implemented beyond the paper:

| # | Extension | Description |
|---|-----------|-------------|
| 1 | Learning curves | Full cumulative reward trajectory over time, revealing when each algorithm transitions from exploration to exploitation |
| 2 | Sensitivity to m | How the visit threshold affects all four algorithms across m ∈ {1, 2, 4, 8, 16, 32, 64, 128} |
| 3 | Sensitivity to A and B | Heatmap of MBIE's confidence interval width parameters on both environments |
| 4 | Sensitivity to γ | Discount factor sweep γ ∈ {0.5, 0.7, 0.8, 0.9, 0.95, 0.99} |
| 5 | Epsilon-greedy baseline | Quantifying the value of principled exploration over naive random perturbation |
| 6 | FrozenLake 8×8 | Benchmarking all four algorithms on a new stochastic environment from OpenAI Gymnasium |

---

## Key Findings

- **Reproduction confirmed**: MBIE ≈ MBIE-EB > R-Max > E3 on RiverSwim; MBIE-EB ≈ MBIE >> R-Max > E3 on SixArms — matching the paper's ordering.
- **CI-based methods are robust**: MBIE and MBIE-EB are nearly insensitive to the visit threshold m, whereas R-Max and E3 show a clear U-shaped sensitivity.
- **B=0 works well**: Transition CI width has minimal effect on RiverSwim — this explains why MBIE-EB (which ignores transition uncertainty entirely) matches MBIE's performance.
- **γ=0.95 is well-chosen**: All algorithms peak near the paper's value; very low γ causes myopic behaviour on RiverSwim, very high γ causes numerical instability.
- **ε-greedy fails on RiverSwim**: Random exploration cannot generate the sustained rightward sequences needed to find the large reward at state 5.
- **FrozenLake generalises**: All PAC-MDP algorithms find the goal on the slippery 8×8 grid, confirming the optimism principle generalises beyond the paper's environments.

---

## Repository Contents

- `mdp-interval-estimation.ipynb` — full implementation, experiments and analysis
- `README.md`

---

## How to Run

1. Clone the repository:

        git clone https://github.com/allizha/mdp-interval-estimation-study.git

2. Install dependencies:

        pip install numpy matplotlib gymnasium tqdm

3. Open and run the notebook:

        jupyter notebook mdp-interval-estimation.ipynb

Or open directly in Google Colab:
[Open in Colab](https://colab.research.google.com/drive/176gtQHemaMMu74CpQFYok-z5dZPgixPE?usp=sharing)

---

## Environments

### RiverSwim
6 states in a chain. The agent swims left (easy, small reward) or right (hard, stochastic, large reward). Tests whether algorithms can commit to long exploratory sequences against resistance.

### SixArms
7 states: one hub connected to 6 rooms. Higher-probability arms give lower rewards. Tests whether algorithms can efficiently rule out clearly inferior actions.

### FrozenLake 8×8 (slippery)
64-state grid from OpenAI Gymnasium. Stochastic transitions — each intended action succeeds with prob 1/3 and slips sideways with prob 2/3. Tests generalisation to larger, standard benchmark environments.

---

## Authors

- **Allizha Theiventhiram** — University of Neuchâtel
- **Rithika Shyam Kumar** — University of Bern
- **Aurélie Wasem** — University of Neuchâtel
- **Boris Verdecia Echarte** — University of Neuchâtel

Seminar supervised by **Prof. Christos Dimitrakakis**, with assistance from **Victor Villin**.

---

## Reference

Strehl, A. L., & Littman, M. L. (2008).  
*An Analysis of Model-Based Interval Estimation for Markov Decision Processes*.  
Journal of Computer and System Sciences, 74(8), 1309–1331.

---

## License

This project is shared for academic and educational purposes.
