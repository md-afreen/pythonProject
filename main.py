# str ="WELCOME"
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str * 2)
# print(str+"CSE")

#
# str1="hello"
# print(str1.capitalize())
# str1="welcome"
# print(str1.center(15,"*"))
# str1="welcome"
# print(len(str1))
#str1="welcome"
#print(str1.count('e',0,len(str1)))
#tuple to list
#data=[1,2,3,"cat"]
#c=list(data)
#print(c)
#class Rectangle:
 #   a = 2
   # b = 3
 #   c = 5
  #  diam=10
 #   r=diam/2
  #  perimeter = 2 * (a + b)
  #  area = a*b
 #   POT = a + b + c
 #   POA = 1 / 2 * a * b
  #  AOC = 3.14 * r * r
  #  POC=2*3.14*r
#    print(perimeter)
  #  print(area)
 #   print(POT)
 #   print(POA)
  #  print(AOC)
   # print(POC)


# print(perimeter)
# print(area)
# print(POT)
# print(area1)
# print(AOC)
# class Train:
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
#         def getStatus(self):
#             print("name of train is (self.name)")
#             print("number of seats is (self.seats)")
#             def fareInfo(self):
#                 if(self.seats>0):
#                     print("your tickets has been booked and your seatnum is:(self.seats)")
#                 else:
#                     print("sorry this train is full")
#                     def cancel(self,seatNo):
#                         pass
#                     intercity=Train("intercity Express: 123456",50,2)
#                     intercity.getStatus()
#                     intercity.bookTicket()
#                     intercity.bookTicket()
#                     intercity.bookTicket()
#                     intercity.bookTicket()
#                     intercity.getStatus()

print("\n\nTicket Booking System\n")
restart = ('Y')

while restart != ('N','NO','n','no'):
  print("1.Check PNR status")
  print("2.Ticket Reservation")
  option = int(input("\nEnter your option : "))

  if option == 1:
    print("Your PNR status is t3")
    exit(0)

  elif option == 2:
    people = int(input("\nEnter no. of Ticket you want : "))
    name_l = []
    age_l = []
    sex_l = []
    for p in range(people):
      name = str(input("\nName : "))
      name_l.append(name)
      age  = int(input("\nAge  : "))
      age_l.append(age)
      sex  = str(input("\nMale or Female : "))
      sex_l.append(sex)

    restart = str(input("\nDid you forgot someone? y/n: "))
    if restart in ('y','YES','yes','Yes'):
      restart = ('Y')
    else :
      x = 0
      print("\nTotal Ticket : ",people)
      for p in range(1,people+1):
        print("Ticket : ",p)
        print("Name : ", name_l[x])
        print("Age  : ", age_l[x])
        print("Sex : ",sex_l[x])
        x += 1

