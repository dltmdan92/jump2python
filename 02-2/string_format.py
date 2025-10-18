a = "I eat %d apples." % 3
print(a)

b = "I eat %s apples." % "five"
print(b)

number_c = 3
c = "I eat %d apples." % number_c
print(c)

number_d = 10
day_d = "three"
d = "I ate %d apples. so I was sick for %s days." % (number_d, day_d)
print(d)

# %s 포맷 코드의 경우 어떤 형태의 값이든 string으로 변환해 넣을 수 있다.
e = "I have %s apples" % 3
print(e)

f = "rate is %s" % 3.234
print(f)

## '문자열 포맷 코드 (%d, %s, %f 등등)와 '%'가 같은 문자열 안에 존재하는 경우, '%'를 나타내려면 반드시 '%%'를 써야 한다.' 라는 법칙이 있다.
g = "Error is %d%%." % 98
print(g)

h = "I eat {0} apples".format(3)
print(h)

i = "I eat {0} apples".format("five")
print(i)

number_j = 3
j = "I eat {0} apples".format(number_j)
print(j)

number_k = 10
day_k = "three"
k = "I ate {0} apples. so I was sick for {1} days.".format(number_k, day_k)
print(k)

l = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(l)

m = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(m)

n = "{0:<10}".format("hi")  # 총 자릿수 10자의 문자열로 해서 왼쪽 정렬
print(n)

o = "{0:>10}".format("hi")  # 총 자릿수 10자의 문자열로 해서 오른쪽 정렬
print(o)

p = "{0:^10}".format("hi")  # 총 자릿수 10자의 문자열로 해서 가운데 정렬
print(p)

q = "{0:=^10}".format("hi")  # 총 자릿수 10자의 문자열로 해서 가운데 정렬하고, 빈칸을 '='로 채움
print(q)

r = "{0:!<10}".format("hi")  # 총 자릿수 10자의 문자열로 해서 왼쪽 정렬하고, 빈칸을 '!'로 채움
print(r)