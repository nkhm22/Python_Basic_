import os

open_file=open('numbers.txt','r')
num_sum=0
for line in open_file:
    if line.rstrip():
        num_sum+=int(line.rstrip())
open_file.close()
file_in = open("answer.txt", "w")
file_in.write(str(num_sum))
file_in.close()
