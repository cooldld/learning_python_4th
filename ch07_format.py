str = '{0}, {1} and {2}'
print(str.format('spam', 'ham', 'eggs'))

str = '{motto}, {pork} and {food}'
print(str.format(motto='spam', pork='ham', food='eggs'))

str = '{motto}, {0} and {food}'
print(str.format('ham', motto='spam', food='eggs'))

import sys
str = 'My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'})
print("'My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}) =", str)
