# Walrus Operator
# :=

list = [1,2,3,4,5]

#normal case
# n = len(list)
# if n > 4:
#     print (f"List is oversized: {n}")
if (n := len(list)) > 4:
    print (f"List is oversized:  {n}")
