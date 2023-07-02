# A list and a target value
def linear_search(mylist, target):
    """Return the index position tarhet value if found, 
    else return None if not found """
    for i in range(0, len(mylist)):
        if mylist[i]==target:
            return i
    return None
# verify index
def verify(index):
    if index is not None:
        print('target index found:', index)
    else:
        print('target not found in the list')
number=[1,2,3,4,5,6,7,8,9,10]
result=linear_search(number, 13)
verify(result)
result=linear_search(number, 10)
verify(result)