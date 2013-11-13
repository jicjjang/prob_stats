import random
import math

class RandomVariable(object):
    """Parent class for all random variables."""

class Exponential(RandomVariable):
    def __init__(self, lam):
        self.lam = lam

    def generate(self):
        return random.expovariate(self.lam)

class Erlang(RandomVariable):
    def __init__(self, lam, k):
        self.lam = lam
        self.k = k
        self.expo = Exponential(lam)

    def generate(self):
        total = 0
        for i in range(self.k):
            total += self.expo.generate()
        return total

class Gumbel(RandomVariable):
    def __init__(self, mu, beta):
        self.mu = mu
        self.beta = beta

    def generate(self):
        x = random.random()
        return self.mu - self.beta * math.log(-math.log(x))

class Normal(RandomVariable):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def generate(self):
        return random.normalvariate(self.mu, self.sigma)

if __name__=='__main__':
    erlang = Erlang(1, 3)
    print erlang.generate()

    gumbel = Gumbel(1, 2)
    print gumbel.generate()
