def main():
    name=input("What is your name?")
    hello(name)
    hello()




    def hello(z="WORLD"):
        """
        The function "hello" takes an optional parameter "z" with a default value of "WORLD".
        
        :param z: The parameter "z" is a string variable with a default value of "WORLD". If no argument
        is passed when the function is called, "WORLD" will be used as the value of "z", defaults to
        WORLD (optional)
        """
        print("hello,",z)

        main()