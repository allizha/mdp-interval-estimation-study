# Model-Based Interval Estimation for MDPs

### Reproduction & Extension Study
### Seminar — Advanced Topics in Reinforcement Learning and Decision Making

This repository contains the implementation and ongoing work for a seminar project conducted in **Advanced Topics in Reinforcement Learning and Decision Making**, within the [Swiss Joint Master in Computer Science](https://mcs.unibnf.ch/).

The project focuses on reproducing and extending the results of the paper:

> Strehl, A. L., & Littman, M. L. (2008).  
> [An Analysis of Model-Based Interval Estimation for Markov Decision Processes](https://www.sciencedirect.com/science/article/pii/S0022000008000767?ref=pdf_download&fr=RR-2&rr=9dfde5654e296aa0).

---

## Project Overview

This project investigates model-based reinforcement learning methods for Markov Decision Processes (MDPs), with a focus on interval estimation techniques for efficient exploration.

We aim to reproduce key theoretical and experimental results from the original paper and explore extensions to better understand the behavior and performance of these algorithms in different environments.

---

# Project Roadmap

---

## Current Status

- [x] Theoretical foundations of reinforcement learning and MDPs  
- [x] Interval Estimation and optimism principle  
- [x] PAC-MDP framework and performance metrics  
- [x] Detailed presentation of MBIE and MBIE-EB  

---

## Part 1 — Final Improvements (Theory)

- [ ] Add MBIE pseudocode for clarity and completeness  
- [ ] Add a small numerical example for average loss  
- [ ] Add comparison with other PAC-MDP algorithms (R-max, E3)  

---

## Part 2 — Implementation

### 2.1 Environment Setup
- [ ] Implement benchmark environments:
  - [ ] RiverSwim  
  - [ ] SixArms  
- [ ] Define MDP structure (states, actions, rewards, transitions)

---

### 2.2 Algorithms

- [ ] Implement MBIE
  - [ ] Empirical model ($\hat{R}$, $\hat{T}$)
  - [ ] Confidence intervals
  - [ ] Optimistic planning

- [ ] Implement MBIE-EB
  - [ ] Exploration bonus term
  - [ ] Value iteration / planning

- [ ] Implement baselines:
  - [ ] R-max  
  - [ ] (Optional) E3  

---

### 2.3 Verification

- [ ] Unit tests for:
  - [ ] Transition updates  
  - [ ] Reward estimation  
  - [ ] Value iteration  

- [ ] Debug on small toy MDPs  

---

## Part 3 — Experiments

### 3.1 Experimental Setup
- [ ] Define evaluation metrics:
  - [ ] Cumulative reward  
  - [ ] Regret / loss  
  - [ ] Convergence speed  

- [ ] Set hyperparameters:
  - [ ] $\gamma$, $\varepsilon$, $\delta$  
  - [ ] Exploration constants  

---

### 3.2 Benchmark Experiments
- [ ] Run experiments on:
  - [ ] RiverSwim  
  - [ ] SixArms  

- [ ] Compare:
  - [ ] MBIE vs MBIE-EB  
  - [ ] vs R-max  

---

### 3.3 Results Analysis
- [ ] Plot learning curves  
- [ ] Analyze exploration efficiency  
- [ ] Compare sample efficiency  
- [ ] Interpret differences between algorithms  

---

## Part 4 — Extensions

- [ ] Test alternative exploration bonuses  
- [ ] Study sensitivity to parameters  
- [ ] Try larger or stochastic environments  
- [ ] (Optional) Compare with modern RL methods  

---

## Part 5 — Final Report

- [ ] Summarize theoretical insights  
- [ ] Present experimental findings  
- [ ] Discuss limitations of MBIE  
- [ ] Provide conclusions and future work  

---

## Deliverables

- [ ] Clean and reproducible code  
- [ ] Well-documented notebook  
- [ ] Final report with figures and analysis  

---

## Repository Contents

- `mdp-interval-estimation.ipynb` — implementation and ongoing experiments  

---

## How to Run

1. Clone the repository:

    git clone https://github.com/allizha/mdp-interval-estimation-study.git

2. Open the notebook:

    mdp-interval-estimation.ipynb

3. Run all cells to explore the current implementation.

---

## Skills Demonstrated (in progress)

- Python  
- Reinforcement Learning  
- Markov Decision Processes (MDPs)  
- Model-based learning  
- Experimental analysis  

---

## Authors & Collaboration

- Allizha Theiventhiram — University of Neuchâtel  
- Rithika Shyam Kumar — University of Bern  
- Aurélie Wasem — University of Neuchâtel  
- Boris Verdecia Echarte — University of Neuchâtel  

This project is being developed collaboratively as part of a seminar.

---

## Reference

Strehl, A. L., & Littman, M. L. (2008).  
*An Analysis of Model-Based Interval Estimation for Markov Decision Processes*.  
Journal of Computer and System Sciences.

---

## License

This project is shared for academic and educational purposes.
