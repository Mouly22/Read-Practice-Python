def function1(arg1, arg2):
    sum = arg2 + arg1
    print(sum)
function1(10, 30)

def function2(*vals):
    for elm in vals:
        g = 0
        x = ''
        if type(elm) == int:
            g =  g + elm
            print(g, end=' ')
        elif type(elm) == str:
            x = x + elm
            print(x, end=' ')
        
function2(2,1,2,3,44)
function2('Bangladesh', 'is', 'a', 'prosperous', 'country')
print()

def function3(v1, v2, v3):
    value = 'catch zebra '
    value += v1
    print(value)
function3(v1= 'mouly', v2 = 'in', v3 = 'danger')

def function4(**values):
    for i in values:
        print(i)
        print(values[i])
        print(values['s3'])   #[] er vitore 'key' te '' dite hobe.
function4(s1 = 'We', s2 = 'want', s3 = '300', s4 = 'taka')

def function5(*args):
    lst =[]
    for x in args:

        lst.append(x)
    print(lst, end='')
        #return(lst)

function5('Trust', 'me!','Practice', 'makes', 'a', 'person', 'perfect')
print()
#when we return:
def function6(*args):
    lst =[]
    for y in args:

        lst.append(y)
        return(lst)

print(function6('Trust', 'me!','Practice', 'makes', 'a', 'person', 'perfect'))
#see the difference:
def function7(*args):
    lst =[]
    for z in args:

        lst.append(z)
    return(lst)

print(function7('Trust', 'me!','Practice', 'makes', 'a', 'person', 'perfect'))


