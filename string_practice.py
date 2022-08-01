first = 'i am mouly'
print(first)
index1 = first[2]
print(index1)
concetanate1 = first[2:7:1]
print(concetanate1)
i = 0
while i < len(first):
        print(first[i])
        i += 1

for j in range(len(first)):
        print(first[j])

second = 'I have a laptop'
g = first +'. '+ second
print(g)
third = 'This is a \'great\' movie'
print(third)
now = ord('a')
print(now)
now2 = chr(97)
print(now2)
#formatting:
forth = 'I want to {} {}'.format('watch', 'movies')
print(forth)
fifth = 'I want to draw {1} before I {0}'.format('watch', 'cartoons')
print(fifth)
sixth = '{a1} are {a2}'.format(a1 = 'movies', a2 = 'overrated')
print(sixth)
#for formatting numbers we need to define whether it is decimal or float number.
seven = 'Hello {0}, I have only {1:d} with me but I need {2:4.2f} taka'.format('finn',100,300.3456)
print(seven)
#Number formatting with alignment:
#will learn it later.. not in the mood :(
