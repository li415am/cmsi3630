
###
# filename: HighArray.py
# purpose: homework02 description at:
#    https://bjohnson.lmu.build/cmsi3530web/homework02.html
# author:   Teddy Jones
# date:     2023-01-31
###

# global to the entire file
a = []         # empty listpuy

# the class
class HighArray():

   # fields

   # initializer
   def __init__( self, maxSize ):
      a = []         # initialize the list to be empty [still]

   # find if a value is in the list
   def find( self, value ):
      for x in a:
         if( x == value ):
            return True
      return False

   # insert a value at the end of the list
   def insert( self, value ):
      a.append( value )
      return

   # delete a specific value
   def delete( self, value ):
      a.remove( value )
      return value

   # display the lists contents
   def display( self ):
        contents = print(*a)
        return contents

   # get max goes here
   def getMax(self):
        if len(a) > 0:
            a.sort()
            max=a[-1]
        else:
            max = -1
        print("The maximum value is ", max)
        return 

   # used more help from geeks for geeks here
   # noDupes goes here
   ##newa= []
      #for i in a:
         #if i not in a:
            #newa.append(i)
      #return newa
   def noDupes(self):
      copy = a.copy()
      newA = []
      for i in range(len(copy)):
         if copy[i] not in newA:
            newA.append(copy[i])
            #print("appending...")
      print(*newA)
      return 


# a little test to make sure the interpreter won't barf
h1 = HighArray( 10 )
h1.display()
