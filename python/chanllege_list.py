orignal='I like cheese cake'
empty_set=set()
for char in orignal:
    if char.lower()  not in ("a",'e','i','o','u',' '):
        empty_set.add(char)

print(sorted(empty_set))

vow=frozenset('aeiou')
empty_set_2=print(set(orignal).difference(vow))


