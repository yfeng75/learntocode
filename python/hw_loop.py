def myfunction(list):  
options=["red", "green","blue","purple","black","brown","gray","silver", "orange"]
print("please choose form the list below: ")

# for i in range (0,len(options)):
#     print( str(i+1) +". " + "{}".format(options[i]))

i=1
for guess in options:
    print( str(i) +". " + guess)
    i+=1
     
print("0. exit")
chosen=""
while chosen !=0:
    chosen=int(input("Please make your choice: "))
    if 0<=chosen<=len(options):
        print("Your choice is : {}".format(chosen))
         

    








