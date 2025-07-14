try : 
    var1 = 6
    var2 = 18/var1

except ZeroDivisionError:
    print("Enter a Valid Divisor")

else :
    print(var2)

finally : 
    print("Hello World")