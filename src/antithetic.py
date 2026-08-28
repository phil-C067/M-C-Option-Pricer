import numpy as np
def antithetic_call_price(S0,r,sigma,T,K,N):
    Z = np.random.normal(0, 1, N)
    ST_plus = S0 * np.exp((r - sigma**2 / 2) * T+ sigma * np.sqrt(T) * Z)
    ST_minus= S0 * np.exp((r - sigma**2 / 2) * T- sigma * np.sqrt(T) * Z)

    payoff_plus = np.maximum(ST_plus - K, 0)
    payoff_minus = np.maximum(ST_minus - K, 0)
    payoff_average = (payoff_plus + payoff_minus) / 2

    price = np.exp(-r * T) * np.mean(payoff_average)
    return price