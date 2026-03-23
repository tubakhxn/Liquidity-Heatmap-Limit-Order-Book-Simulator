"""
events.py
Market event logic: imbalance, spoofing, flash crash.
"""
import numpy as np

def event_imbalance(order_book, strength=0.2):
    """Increase bid or ask side to create imbalance."""
    side = np.random.choice(['bid', 'ask'])
    if side == 'bid':
        order_book.bids[order_book.mid_price-10:order_book.mid_price] += int(20 * strength)
    else:
        order_book.asks[order_book.mid_price:order_book.mid_price+10] += int(20 * strength)
    order_book.update_metrics()

def event_spoofing(order_book, size=50):
    """Add large fake orders far from mid-price."""
    spoof_side = np.random.choice(['bid', 'ask'])
    if spoof_side == 'bid':
        idx = order_book.mid_price - np.random.randint(15, 25)
        order_book.bids[idx] += size
    else:
        idx = order_book.mid_price + np.random.randint(15, 25)
        order_book.asks[idx] += size
    order_book.update_metrics()

def event_flash_crash(order_book, drop=0.3):
    """Remove liquidity and shift mid-price suddenly."""
    # Remove bids, shift mid-price down
    crash_depth = int(order_book.price_levels * drop)
    order_book.bids[:order_book.mid_price] = 0
    order_book.asks[:order_book.mid_price] = 0
    order_book.mid_price = max(5, order_book.mid_price - crash_depth)
    order_book.update_metrics()
