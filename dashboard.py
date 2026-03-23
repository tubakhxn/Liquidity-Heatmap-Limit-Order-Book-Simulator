"""
dashboad.py
Streamlit dashboard for real-time LOB simulation and parameter control.
"""
import streamlit as st
import numpy as np
from order_book import LimitOrderBook
from events import event_imbalance, event_spoofing, event_flash_crash
from visualization import animate_lob

def auto_install():
    import subprocess, sys
    for pkg in ['numpy', 'matplotlib', 'plotly', 'streamlit']:
        try:
            __import__(pkg)
        except ImportError:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])

def main():
    auto_install()
    st.title("Liquidity Heatmap Limit Order Book Simulator")
    price_levels = st.slider("Price Levels", 50, 200, 100)
    n_steps = st.slider("Simulation Steps", 50, 500, 200)
    event_prob = st.slider("Event Probability", 0.0, 0.5, 0.1)
    use_plotly = st.checkbox("Use Plotly for 3D Animation", value=True)
    lob = LimitOrderBook(price_levels=price_levels)
    lob.reset()
    snapshots = []
    event_types = [event_imbalance, event_spoofing, event_flash_crash]
    for t in range(n_steps):
        bid_changes = np.random.poisson(1, lob.price_levels) - np.random.binomial(1, 0.5, lob.price_levels)
        ask_changes = np.random.poisson(1, lob.price_levels) - np.random.binomial(1, 0.5, lob.price_levels)
        lob.update(bid_changes, ask_changes)
        if np.random.rand() < event_prob:
            np.random.choice(event_types)(lob)
        snapshots.append(lob.get_snapshot())
    st.write(f"Final Mid-Price: {lob.mid_price}, Spread: {lob.spread}")
    st.write(f"Liquidity: {lob.liquidity[-1]:.2f}, Imbalance: {lob.imbalance[-1]:.2f}")
    if st.button("Show 3D Animation"):
        animate_lob(snapshots, use_plotly=use_plotly)

if __name__ == "__main__":
    main()
