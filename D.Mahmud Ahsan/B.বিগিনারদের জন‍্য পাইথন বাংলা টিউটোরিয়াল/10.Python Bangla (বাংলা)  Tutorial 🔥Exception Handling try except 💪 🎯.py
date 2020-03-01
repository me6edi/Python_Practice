#--------------------
#      Exception
#-------------------

## Hello Exception
def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print ("Unknown error occurred")
        return None
    return result


print (div(4, 2))
print (div(4, 0))


def div(x, y):
    return x /y


try:
    div_result = div(8,2)
except:
    print ("Division by zero not possible")
else:
    print ("Div resul is: " + str(div_result))
