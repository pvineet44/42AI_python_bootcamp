class Vector:
    def __init__(self, values):
      """Initializes Vector with a list of values and size.
          Example: V(1.0, 2.0, 3.0)"""
        if (isinstance(values,list)):
            self.values = list(values)
        elif (isinstance(values,tuple)):
            l1 = []
            for i in range(values[0],values[1]):
                l1.append(i * 1.0)
            self.values = list(l1)
        elif (str(values).isdigit()):
            l1 = []
            for i in range(int(values)):
                l1.append(i * 1.0)
            self.values = list(l1)
        self.length=len(values)


    def __mul__(self, other):
      """Multiplies two values"""
        i = 0
        l2 = []
        while i < len(self.values):
         l2.append(other * self.values[i])
         i += 1
        return Vector(l2)


    def __add__(self, other):
      """Adds two values"""
       if (other.isdigit()):
            i = 0
            l2 = []
            while i < len(self.values):
                l2.append(other + self.values[i])
                i += 1
       return Vector(l2)
       if (isinstance(other.values,list)):
            other_len = len(other.values)
            if (other_len != len(self.values)):
               print("Error: Can't add vectors of unequal length")
               sys.exit(0)
            i = 0
            while (i < self.length):
               self.values[i] += other.values[i]
               i += 1
            return self


    def __radd__(self, other):
      """Adds two values. Example: 5 + Vector"""
            i = 0
            l2 = []
            while i < len(self.values):
                l2.append(other + self.values[i])
                i += 1
            return Vector(l2)


    def __sub__(self, other):
      """Subtracts two values"""
       if (isinstance(other.values,list)):
            other_len = len(other.values)
            if (other_len != len(self.values)):
               print("Error: Can't subtract vectors of unequal length")
               sys.exit(0)
            i = 0
            while (i < self.length):
               self.values[i] -= other.values[i]
               i += 1
            return self
       i = 0
       l2 = []
       while i < len(self.values):
        l2.append(self.values[i] - other)
        i += 1
       return l2  


    def __rsub__(self, other):
      """Subtracts two values. Example: 5 - Vector"""
            i = 0
            l2 = []
            while i < len(self.values):
                l2.append(other - self.values[i])
                i += 1
            return Vector(l2)


    def __div__(self, other):
      """Divides two values"""
       i = 0
       l2 = []
       while i < len(self.values):
        l2.append(self.values[i] / other)
        i += 1
       return l2


    def __str__(self):
        """docstring for __str_"""
        return str(self.values)
        