nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
answer = [c for a in nice_list for b in a for c in b]
print(answer)