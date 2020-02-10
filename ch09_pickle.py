D = {'a': 1, 'b': 2}
print('D =', D)
F = open('ch09_data.pickle', 'wb')

import pickle
pickle.dump(D, F)
print('pickle.dump(D, F)')

F.close()

F = open('ch09_data.pickle', 'rb')
E = pickle.load(F)
print('pickle.load(F) =', E)
