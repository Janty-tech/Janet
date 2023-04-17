def main():
    expression= input("exzpression")
    print(cal(expression))

    def calc(result):
        result= result.split()
        x= int(result[0])
        y= result[1]
        z= int(result[2])
        if result[1]=="+":
            return float(x+z)
        elif result[1]=="-":
            return float(x-z)
        elif result[1]=="*":
            return float(x*z)
        elif rewsult[1]=="/":
            return float(x/z)
        else:
            print("sorry, expression is not recognized")
            
                