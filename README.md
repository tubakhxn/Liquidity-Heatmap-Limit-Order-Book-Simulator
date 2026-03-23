# Liquidity Heatmap Limit Order Book Simulator

## Dev / Creator
**tubakhxn**

# Liquidity Heatmap Limit Order Book Simulator

## Problem Overview
Simulating a realistic limit order book (LOB) is crucial for understanding market microstructure, liquidity, and the impact of various trading events. This project provides a modular Python simulator for a 3D LOB, visualizing real-time liquidity and order flow dynamics, and supporting interactive exploration.

## What is this project about?
This project is a Python-based simulator for a 3D Limit Order Book (LOB) with real-time animated visualizations. It models realistic bid/ask order flows, simulates market events (like imbalance, spoofing, and flash crashes), and provides interactive dashboards for exploring liquidity and market microstructure. The simulator is designed for research, education, and prototyping trading strategies.

**Relevant Wikipedia links:**
- [Limit order book](https://en.wikipedia.org/wiki/Order_book_(trading))
- [Market liquidity](https://en.wikipedia.org/wiki/Market_liquidity)
- [Flash crash](https://en.wikipedia.org/wiki/2010_flash_crash)
- [Spoofing (finance)](https://en.wikipedia.org/wiki/Spoofing_(finance))


## Features

## Features
...existing code...

## Test Cases
- Simulate normal market conditions and verify LOB stability
- Trigger spoofing and flash crash events, observe LOB response
- Adjust market parameters via dashboard sliders and confirm real-time updates

## Key Insight
A modular, animated LOB simulator enables deep exploration of liquidity dynamics and the effects of market events, providing valuable intuition for traders, researchers, and students.

## How to Run
1. **Install dependencies** (auto-installs on first run):
   ```bash
   pip install -r requirements.txt
   ```
2. **Run in Python window**:
   ```bash
   python simulation.py
   ```
3. **Run Streamlit dashboard** (optional):
   ```bash
   streamlit run dashboard.py
   ```

## Output
- Animated 3D surface plots of the LOB
- Real-time metrics: liquidity, imbalance, mid-price, spread
- Interactive dashboard for parameter tuning

## Tech Stack
- Python 3.8+
- numpy
- matplotlib
- plotly
- streamlit

## Applications
- Market microstructure research
- Trading strategy prototyping
- Educational visualization

## Future Improvements
- Add support for multiple assets
- Integrate real market data for calibration
- Expand event types (e.g., news shocks)
- GPU acceleration for large-scale simulation
