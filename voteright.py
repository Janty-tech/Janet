while True:
    try:

        age = int(input("please enter yur age:"))
    except ValueError:
        print("sorry, i didn't understand that.")

        continue
    else:

        break
if age >= 18
    print("you are able to vote in the united states!")
else:
    print("you are not able tovote in the united states.")