# Bug reports for exercise2.py

Line: 12
Problem: clamp returns max(low, min(x, low)), which incorrectly limits x to low or below, but the docstring says "x, limited to the range from low to high", meaning it should be bounded below by low and above by high. The current code incorrectly uses min(x, low) and then max(low, ...), which results in x being clamped to low or below, not to the full range [low, high].
Example: clamp(3, 1, 5) returns 1, expected 3.
Fix: return max(low, min(x, high))
