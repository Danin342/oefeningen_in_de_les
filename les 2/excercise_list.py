lst = [159.99, 160.00, 205.95, 128.83, 175.49]

lst.append(160.00)

print(lst)

#b
print(lst.count(160.00))

#c
min_price = min(lst)
print(min_price)

#d
print(lst.index(min_price))

#e
lst.remove(min_price)
print(lst)

#f
lst.sort()
print(lst)
