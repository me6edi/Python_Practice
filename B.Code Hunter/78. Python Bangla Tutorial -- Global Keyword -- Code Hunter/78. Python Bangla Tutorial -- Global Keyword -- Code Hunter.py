#global
#function and class -- outside

i = 5 #6


def func():
    print(i)
def chang():
    global i
    i = 6
    print(i)

func()
chang()
func()


