def add(x, y):
    total = x + y
    return(total)

print(add(8,8))


#this will add a default value for y
def add(x, y=3):
    total = x + y
    return(total)

#passes 8 to x and leaves default for y
print(add(8))

#overrides default
print(add(8,8))
