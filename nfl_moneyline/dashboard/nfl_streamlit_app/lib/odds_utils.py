from __future__ import annotations

def moneyline_to_prob(ml: float) -> float:
    if ml is None or ml != ml:
        return float("nan")
    return (-ml) / ((-ml) + 100) if ml < 0 else 100 / (ml + 100)

def prob_to_moneyline(p: float) -> int:
    if p is None or p != p or p <= 0 or p >= 1:
        return 0
    return int(round(-100 * p / (1 - p))) if p > 0.5 else int(round(100 * (1 - p) / p))

def american_to_decimal(ml: float) -> float:
    if ml is None or ml != ml:
        return float("nan")
    return 1 + (100/(-ml)) if ml < 0 else 1 + (ml/100)

def fair_moneyline_from_prob(p: float) -> int:
    return prob_to_moneyline(p)

def edge(p_model: float, p_market: float) -> float:
    if any([(x!=x) for x in [p_model, p_market]]):
        return float("nan")
    return p_model - p_market

def kelly_fraction(p: float, ml: float, kelly_factor: float=0.5) -> float:
    o = american_to_decimal(ml)
    f = (p*(o-1) - (1-p)) / (o-1)
    return max(0.0, f * kelly_factor)
