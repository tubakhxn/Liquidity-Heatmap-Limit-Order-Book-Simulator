"""
visualization.py
Animated 3D surface plots for the LOB using matplotlib and plotly.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import plotly.graph_objs as go
import plotly.io as pio


def animate_lob(snapshots, use_plotly=False):
    """Animate LOB snapshots as 3D surface plot."""
    bids_list, asks_list, mids, spreads = [], [], [], []
    for bids, asks, mid, spread in snapshots:
        bids_list.append(bids)
        asks_list.append(asks)
        mids.append(mid)
        spreads.append(spread)
    X = np.arange(len(bids_list[0]))
    T = len(bids_list)
    if use_plotly:
        # Plotly animation
        frames = []
        for t in range(T):
            z = np.vstack([bids_list[t], asks_list[t]])
            frames.append(go.Frame(data=[go.Surface(z=z, x=[X, X], y=[[0,1],[0,1]])]))
        fig = go.Figure(
            data=[go.Surface(z=np.vstack([bids_list[0], asks_list[0]]), x=[X, X], y=[[0,1],[0,1]])],
            frames=frames
        )
        fig.update_layout(title="LOB 3D Animation", scene=dict(zaxis_title="Volume", xaxis_title="Price", yaxis_title="Side"))
        pio.show(fig)
    else:
        # Matplotlib animation
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.arange(len(bids_list[0])), [0, 1])
        def update(frame):
            ax.clear()
            Z = np.vstack([bids_list[frame], asks_list[frame]])
            surf = ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_zlim(0, np.max(Z)+1)
            ax.set_xlabel('Price')
            ax.set_ylabel('Side (0=Bid, 1=Ask)')
            ax.set_title(f"Step {frame}")
            return surf,
        ani = animation.FuncAnimation(fig, update, frames=len(bids_list), interval=100, blit=False)
        plt.show()
