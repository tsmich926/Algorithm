from collections import deque
d = deque([1,2,3,4,5])

d.append(6)
# deque([1, 2, 3, 4, 5, 6])

d.appendleft(0)
# deque([0, 1, 2, 3, 4, 5, 6])

d.pop()
# deque([0, 1, 2, 3, 4, 5])

d.popleft()
# deque([1, 2, 3, 4, 5])

d.rotate(2)
# deque([4, 5, 1, 2, 3])
# print(d)





from collections import Counter

# counter = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# Counter({'hi': 3, 'hey': 2, 'hello': 1})

# a = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# print(dict(a))
# # {'hi': 3, 'hey': 2, 'hello': 1}

# counter = Counter("hello world")
# # Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# counter = Counter('hello world').most_common()
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

counter = Counter('hello world').most_common(2)
# [('l', 3)]
print(counter)