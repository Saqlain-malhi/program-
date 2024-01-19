def fuc():
  try:
    x=int(input("Enter the number:"))
    print()
    list1=[23,43,54,654,4,5]
    print("the number ",list1[x])
  except:
    print("error")
    return 0 
  finally:
   print("error")
   return 1

x=fuc()
print(x)






