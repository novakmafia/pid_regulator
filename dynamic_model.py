class MassSpringDamper: 
    def __init__(self, k, c, m, x0=0, v0=0, dt=0.01):
        self.k = k
        self.c = c
        self.m = m
        self.dt = dt
        self.x = x0
        self.v = v0

    def update(self, F):
        xnew = self.v * self.dt + self.x
        vnew = self.dt / self.m * (F - self.c * self.v - self.k * self.x) + self.v
        self.x = xnew
        self.v = vnew
        return self.x