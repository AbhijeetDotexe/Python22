# Collection : Counter, Namedtuple, OrderedDict, Defaultdict, deque

from collections import Counter
a = 'aaaaaaaaaaaaaaabbbbbbbbbccccccccccc'
my_counter = Counter(a)
print(my_counter)
# print(my_counter.elements())
# print(list(my_counter.elements()))
print(my_counter.most_common(1))
print(my_counter.values())


from collections import  namedtuple
point =namedtuple('point', 'x,y')
pt= point(4,20)
print(pt)
print(pt.x, pt.y)


from collections import  OrderedDict
dict = OrderedDict()

dict['b'] = 2
dict['c'] = 3
dict['d'] = 4
dict['e'] = 5
dict['f'] = 6
dict['a'] = 1
print(dict)


from collections import  defaultdict
d = defaultdict(int)
d['a']=2
d['b']=3
d['c']=4
d['d']=5
d['e']=6
print(d)

from collections import  deque
# double ended queue it adds or removes element from both the ends
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.appendleft(97)
print(d)

d.pop()
print(d)

d.popleft()
print(d)
d.extend([5,6,7,8])
print(d)
d.rotate(-1)
print(d)
d.clear()
print(d)