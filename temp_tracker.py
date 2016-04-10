""" You decide to test if your oddly-mathematical heating company is fulfilling
its All-Time Max, Min, Mean and Mode Temperature Guarantee.

Write a class TempTracker with these methods:
insert() - records a new temperature
get_max() - returns the highest temp we've seen so far
get_min() - returns the lowest temp we've seen so far
get_mean() - returns the mean of all temps we've seen so far
get_mode() - returns the mode of all temps we've seen so far

Optimize for space and time. Favor speeding up the getter functions over
speeding up the insert function.

get_mean() should return a float, but the rest of the getter functions can
return integers. Temperatures will all be inserted as integers. We'll record
our temperatures in Fahrenheit, so we can assume they'll all be in the range
0 .. 110

If there is more than one mode, return any of the modes.
"""

class TempTracker(object):
    def __init__(self):
        self.max_temp = None
        self.min_temp = None
        self.mean_temp = None
        self.mode_temp = None
        self.mode_freq = 0
        self.frequencies = {}
        self.count = 0

    def insert(self, new_temp):
        self.max_temp = self._find_max(new_temp)
        self.min_temp = self._find_min(new_temp)
        self.mean_temp = self._build_mean(new_temp)
        self._log_new_temp(new_temp)
        self.mode_temp = self._find_mode(new_temp)

        self.count += 1

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean_temp

    def get_mode(self):
        return self.mode_temp


    def _find_max(self, new_temp):
        if self.max_temp is None:
            return new_temp
        elif new_temp > self.max_temp:
            return new_temp
        else:
            return self.max_temp

    def _find_min(self, new_temp):
        if self.min_temp is None:
            return new_temp
        elif new_temp < self.min_temp:
            return new_temp
        else:
            return self.min_temp

    def _build_mean(self, new_temp):
        if self.mean_temp is None:
            return new_temp
        else:
            product = self.count * self.mean_temp
            product += new_temp
            new_mean = float(product)/(self.count+1)
            return new_mean

    def _log_new_temp(self, new_temp):
        if new_temp not in self.frequencies:
            self.frequencies[new_temp] = 1
        else:
            self.frequencies[new_temp] += 1

    def _find_mode(self, new_temp):
        new_freq = self.frequencies[new_temp]
        if new_freq > self.mode_freq or self.mode_temp is None:
            self.mode_temp = new_temp
            self.mode_freq = new_freq
        return self.mode_temp


thermo = TempTracker()
thermo.insert(72)
thermo.insert(59)
thermo.insert(72)
thermo.insert(67)
thermo.insert(59)
thermo.insert(59)
thermo.insert(80)
print thermo.get_max()
print thermo.get_min()
print thermo.get_mean()
print thermo.get_mode()

