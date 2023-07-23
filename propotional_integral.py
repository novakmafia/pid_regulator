class PropotionalIntegralDerivative:
    def __init__(self, k_p: int, k_d: int, k_i: int, delta_time, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.k_p = k_p
        self.k_d = k_d
        self.k_i = k_i
        self.delta_time = delta_time
        self.prev_err = None
        self.propotional = 0
        self.derivative = 0
        self.integral = 0

    def update(self, c_x, xdes):
        err = c_x - xdes
        self.propotional = self.k_p * err
        if self.prev_err is not None:
            self.derivative = self.k_d * (err - self.prev_err) / self.delta_time
        self.integral += self.k_i * err
        self.prev_err = err
        outp = self.propotional + self.derivative + self.integral
        return self._constrain(outp)

    def _constrain(self, c_x):
        if c_x >= self.upper_bound:
            return self.upper_bound
        elif c_x <= self.lower_bound:
            return self.lower_bound
        else:
            return c_x
