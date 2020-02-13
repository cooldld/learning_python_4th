spam = 'Hello'
print("spam = 'Hello' -->", 'spam =', spam)

spam, ham = 'Hello', 'World'
print("spam, ham = 'Hello', 'World' -->", 'spam, ham =', spam, ham)

[spam, ham] = ['Hello', 'World']
print("[spam, ham] = ['Hello', 'World'] -->", 'spam, ham =', spam, ham)

a, b, c, d = 'spam'
print("a, b, c, d = 'spam' -->", 'a, b, c, d =', a, b, c, d)

a, *b = 'spam'
print("a, *b = 'spam' -->", 'a =', a)
print("a, *b = 'spam' -->", 'b =', b)

spam = ham = 'lunch'
print("spam = ham = 'lunch' -->", 'spam, ham =', spam, ham)

spam = 0
spam += 2
print("spam += 2 -->", 'spam =', spam)
