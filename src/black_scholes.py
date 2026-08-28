import numpy as np
from scipy.stats import norm

def call_price(S_0,r,sigma,T,K):
    d1=(np.log(S_0/K)+(r+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    price=S_0*norm.cdf(x=d1)-K*np.exp(-r*T)*norm.cdf(x=d2)
    return price

print(call_price(100, 0.05, 0.20, 1, 100))

def call_delta(S_0,r,sigma,T,K):
    d1 = (np.log(S_0 / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    return norm.cdf(d1)

print(call_delta(100, 0.05, 0.20, 1, 100))