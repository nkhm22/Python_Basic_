import os

zen_file=open('zen.txt','r')
zen_list=[]
for string in zen_file:
    zen_list.append(string)
conversely_file=open('conversely.txt','w')
for conversely_string in zen_list[::-1]:
    conversely_file.write(conversely_string)
conversely_file.close()