import numpy as np
s = b"Hello Word"
# from buffer  input to ndarry dynamic
a = np.frombuffer(s,dtype='S1')
print(a)
list =range(5)
it = iter(list)
# from iterator input ot ndarry
b = np.fromiter(it,dtype=float,count=-1)# count=-1 obtain all data
print(b)
