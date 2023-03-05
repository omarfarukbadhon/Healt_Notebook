# Omar Faruk Badhon
# Email: omarfarukbadhon@gmail.com

# Health NoteDown System
# 3 clients - Faruk, Ifti and Arpon
import datetime

# Function for date
def getdate():
    return datetime.datetime.now()

# Function for time
def gettime():
    return datetime.datetime.now()

# Here 6 txt files, 3 files to note food and 3 file to note exerxise
def take(k):
    if k==1:
        c=int(input("Enter 1 TO add excersise and 2 TO add food: "))
        if(c==1):
            value=input("type here\n")
            with open("Faruk-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully add in Faruk's notebook")
        elif(c==2):
            value = input("type here\n")
            with open("Faruk-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully add in Faruk's notebook")
    elif(k==2):
        c = int(input("Enter 1 TO add excersise and 2 TO add food: "))
        if (c == 1):
            value = input("type here\n")
            with open("Ifti-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully add in Ifti's notebook")
        elif (c == 2):
            value = input("type here\n")
            with open("Ifti-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully add in Ifti's notebook")
    elif (k == 3):
        c = int(input("Enter 1 TO add excersise and 2 TO add food: "))
        if (c == 1):
            value = input("type here\n")
            with open("Arpon-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully add in Arpon notebook")
        elif (c == 2):
            value = input("type here\n")
            with open("Arpon-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully add in Arpon notebook")

    else:
        print("plz enter valid input (1(Faruk),2(Ifti),3(Arpon))")

#Function for opening notebook
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 TO open excersise note and 2 TO open food note: "))
        if(c==1):
            with open("Faruk-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("Faruk-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 TO open excersise note and 2 TO open food note: "))
        if (c == 1):
            with open("Ifti-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Ifti-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("Enter 1 TO open excersise note and 2 TO open food note: "))
        if (c == 1):
            with open("Arpon-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Arpon-food.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("plz enter valid input (Faruk, Ifti, Arpon)")


#Start       
print("health notedown system: ")
a=int(input("Press 1 to Note your exercise or food and 2 for opeing your notebook: "))

if a==1:
    b = int(input("Press 1 for Faruk 2 for Ifti 3 for Arpon: "))
    take(b)
else:
    b = int(input("Press 1 for Faruk 2 for Ifti 3 for Arpon: "))
    retrieve(b)