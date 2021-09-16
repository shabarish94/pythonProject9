# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


num = 9
for i in range(1 ,num+1):
    if(i % 2 != 0):
         print(" "*(num-i)+"* "*i)
for i in range(num-2,0,-2):
    print(" "*(num-i)+"* "*i)

