import numexpr as ne

s = input('Enter math expression ')

print(ne.evaluate(s.strip()))