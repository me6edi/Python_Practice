class TestClass:
    def _init_(self):
        print("I am a constructor")
            
    def fun1(self):
       print("I am a function")
        
    def fun2(self):
       print("I am another function")
            
ob = TestClass()
ob.fun1()