a = "20251011Rainy"
date = a[:8]
year = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]

print(date)
print(year)
print(month)
print(day)
print(weather)

b = 'pithon'
print(b[:1] + 'y' + b[2:])  # 문자열 사이에 문자를 삽입하려면 슬라이싱과 더하기(+)를 사용