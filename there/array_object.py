# 一維轉二維
import numpy as np
a = np.array([1, 2, 3])
b = a[:, np.newaxis]
c = a[np.newaxis, :]
print('array b = ', b, 'shape of b is ', b.shape)
print('array c = ', c, 'shape of c is ', c.shape)

# 二維轉三維

d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
e = d[:, np.newaxis]
f = d[np.newaxis, :]

print(d, d.shape)
print(e, e.shape)
print(f, f.shape)
print(e[1][0][2])
print(f[0][1][1])


# object

class Cars:
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat

    def drive(self):
        print(f'My car is {self.color} and {self.seat} seats.')


mazda = Cars("blue", 4)
mazda.drive()
