class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if self.current <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError

    def set_max(self, max_max):
        if max_max >= self.min_value:
            self.max_value = max_max
        else:
            raise ValueError

    def set_min(self, min_min):
        if min_min <= self.max_value:
            self.min_value = min_min
            if self.current < self.min_value:
                self.current = self.min_value
        else:
            raise ValueError

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
