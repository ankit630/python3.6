def varLenArgFunc(*varvallist):
   print("The Output is: ")
   for varval in varvallist:
        print(varval)
   return;
print("Calling with single value")
varLenArgFunc(55)
print("Calling with multiple values")
varLenArgFunc(50,60,70,80)
