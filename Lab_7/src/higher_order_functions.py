# Second task

def forall(pred, iterable):
    return all(map(pred, iterable))

def exists(pred, iterable):
    return any(map(pred, iterable))

def atleast(n, pred, iterable):
    return len(list(filter(pred, iterable))) >= n

def atmost(n, pred, iterable):
    return len(list(filter(pred, iterable))) <= n

# Test task 2
if __name__ == "__main__":
    iterable = [1,2,3,4,5,6,7,8,9,10]
    pred = lambda x: x > 0
    n = 6
    print(forall(pred, iterable))
    print(exists(pred, iterable))
    print(atleast(n, pred, iterable))
    print(atmost(n, pred, iterable))