"""
simulation.py
Main simulation loop for the LOB, including event triggers and animation.
"""
import numpy as np
import time
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
    lob = LimitOrderBook()
    lob.reset()
    n_steps = 200
    event_steps = np.random.choice(range(20, n_steps), 5, replace=False)
    event_types = [event_imbalance, event_spoofing, event_flash_crash]
    event_map = dict(zip(event_steps, np.random.choice(event_types, 5)))
    snapshots = []
    for t in range(n_steps):
        # Random order flow
        bid_changes = np.random.poisson(1, lob.price_levels) - np.random.binomial(1, 0.5, lob.price_levels)
        ask_changes = np.random.poisson(1, lob.price_levels) - np.random.binomial(1, 0.5, lob.price_levels)
        lob.update(bid_changes, ask_changes)
        # Trigger events
        if t in event_map:
            event_map[t](lob)
        if t % 5 == 0:
            print(f"Step {t}: Mid={lob.mid_price}, Spread={lob.spread}")
        snapshots.append(lob.get_snapshot())
    animate_lob(snapshots)

if __name__ == "__main__":
    main()
