D = {'a': 1, 'b': 2}
print('D =', D)

L = [1, 2, 3, 4]
print('L =', L)

pickle_file = 'ch09_pickle.data'
print('pickle_file =', pickle_file)

F = open(pickle_file, 'wb')

import pickle
pickle.dump(D, F)
print('pickle.dump(D, F)')
pickle.dump(D, F)
print('pickle.dump(D, F)')
pickle.dump(L, F)
print('pickle.dump(L, F)')
pickle.dump(L, F)
print('pickle.dump(L, F)')

F.close()

F = open(pickle_file, 'rb')
E = pickle.load(F)
print('pickle.load(F) =', E)
E = pickle.load(F)
print('pickle.load(F) =', E)
E = pickle.load(F)
print('pickle.load(F) =', E)
E = pickle.load(F)
print('pickle.load(F) =', E)
E = pickle.load(F)
print('pickle.load(F) =', E)
