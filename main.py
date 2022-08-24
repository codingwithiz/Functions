#Example 1
#Create a function
def sayhi(name , age):   #arguments will enter into the parameters
    print("Hello " + name + ", you are " + str(age))

#Call your function
sayhi("Mike" , 35)       #arguments "Mike" and 35 will be passed to your function when it is called
sayhi("Tim" , 70)        ##arguments "Tim" and 70 will be passed to your function when it is called


#Example 2
#Create your function
def cube(num):           #num is your parameter
    return num*num*num   #will return your value into the calling function

#Call your function
print(cube(4))           #4 is argument, the number 4 will pass into your function as parameter
                         # when it is called

                         