from code1 import total

def test_total () :
    a = total([1, 2 ,3]) == 6
    b = total([1, -1]) == 0
    c = total([-1, -1]) == -2
    d = total([1]) == 1
    e = total([]) == 0
    return (a, b, c, d, e)

print(test_total())