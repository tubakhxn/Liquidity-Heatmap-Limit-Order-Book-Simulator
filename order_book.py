"""
order_book.py
Core logic for the Limit Order Book (LOB) data structure and updates.
"""
import numpy as np

class LimitOrderBook:
    def __init__(self, price_levels=100, max_depth=10):
        self.price_levels = price_levels
        self.max_depth = max_depth
        self.mid_price = price_levels // 2
        self.bids = np.zeros((price_levels,))
        self.asks = np.zeros((price_levels,))
        self.spread = 1
        self.liquidity = []
        self.imbalance = []

    def reset(self):
        self.bids[:] = 0
        self.asks[:] = 0
        self.bids[self.mid_price-5:self.mid_price] = np.random.poisson(10, 5)
        self.asks[self.mid_price:self.mid_price+5] = np.random.poisson(10, 5)
        self.update_metrics()

    def update(self, bid_changes, ask_changes):
        self.bids += bid_changes
        self.asks += ask_changes
        self.bids = np.clip(self.bids, 0, None)
        self.asks = np.clip(self.asks, 0, None)
        self.update_metrics()

    def update_metrics(self):
        best_bid = np.max(np.where(self.bids > 0)[0]) if np.any(self.bids > 0) else 0
        best_ask = np.min(np.where(self.asks > 0)[0]) if np.any(self.asks > 0) else self.price_levels-1
        self.spread = max(1, best_ask - best_bid)
        self.mid_price = (best_bid + best_ask) // 2
        total_bid = np.sum(self.bids)
        total_ask = np.sum(self.asks)
        liq = total_bid + total_ask
        imb = (total_bid - total_ask) / (liq + 1e-6)
        self.liquidity.append(liq)
        self.imbalance.append(imb)

    def get_snapshot(self):
        return self.bids.copy(), self.asks.copy(), self.mid_price, self.spread

    def get_metrics(self):
        return self.liquidity, self.imbalance
