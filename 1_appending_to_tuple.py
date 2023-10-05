
# 1.	Appending to a Tuple

# Write a function that takes in a tuple and a value.
# The function should return another tuple with the value appended to the input tuple
# If the first input argument isn’t a tuple then the function should raise an Exception.



def add_to_tuple(t,x):
    result=[]
    try:
        if not(isinstance(t, tuple)):
            raise TypeError("Not a tuple")
        else:
            for i in t:
                result.append(i)
            result.append(x)
    except TypeError:
        print("Not a tuple")
    return result

print(add_to_tuple((1,2,3), 4))

print(add_to_tuple([1,2,3], 4))


