import numpy as np
import matplotlib.pyplot as plt

#Standard normal distribution
# L=1000000
# mu=0
# sigma=1
# Z=np.random.normal(mu,sigma,L)
# mean=np.mean(Z)
# sd=np.std(Z)
# mean_error=abs(mu-mean)
# sd_error=abs(sigma-sd)
# print("The estimated mean is ",mean," with error ", mean_error)
# print("The estimated standard deviation is ",sd," with error ", sd_error)

#Histogram
# plt.hist(Z,bins=100,density=True)
# x_curve = np.linspace(mean-5*sd, mean+5*sd, 200)
# plt.plot(x_curve, 1/(sigma*np.sqrt(2 * np.pi))*np.exp(-(x_curve - mu)**2/(2 * sigma**2)),
#          linewidth=2)
# plt.show()

#Black-Scholes
S_0=100       # current stock price
r=0.05       # risk-free interest rate
sigma=0.20   # volatility
T=1          # time to maturity (years)
#N=10000     # number of simulations
for N in [100,1000,10000,100000,1000000]:
    Z=np.random.normal(0,1,N)
    ST=S_0*np.exp((r-(sigma**2)/2)*T+sigma*np.sqrt(T)*Z)

# ST_mean=np.mean(ST)
# ST_sd=np.std(ST)
# ST_min=np.min(ST)
# ST_max=np.max(ST)
# print(ST_mean,ST_sd,ST_min,ST_max)
# ST_theomax=S_0*np.exp(r*T)
# print(ST_theomax)
# plt.hist(ST,bins=100,density=True)
# plt.show()

    K=100 # strike price
    payoff=np.maximum(0,ST-K)
    payoff_mean=np.mean(payoff)
    payoff_min=np.min(payoff)
    payoff_max=np.max(payoff)

# print(payoff_mean,payoff_min,payoff_max)
# plt.hist(payoff,bins=100,density=True)
# plt.show()

    C=payoff_mean*np.exp(-r*T) #option price
    error=abs(C-10.4506) #10.4506 is analytical
    print(N,C,error)




