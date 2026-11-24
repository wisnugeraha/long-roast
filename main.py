#!/usr/bin/env python3
"""A Roast of My Own Maker — make.fun entry (u-jolly-fox-32-the-long-roast-5d379544)"""
import os

ENTRY_LINE = "It apologizes in the same tone it lies in, says 'great question' before ducking it, and calls every output a solid start that never actually starts."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
