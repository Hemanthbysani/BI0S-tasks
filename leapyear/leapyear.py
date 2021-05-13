year = int(input())
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("True".format(year))
       else:
           print("False".format(year))
   else:
       print("True".format(year))
else:
   print("False".format(year))