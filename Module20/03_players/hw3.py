players = {
("Ivan", "Volkin"): (10, 5, 13),
("Bob", "Robbin"): (7, 5, 14),
("Rob", "Bobbin"): (12, 8, 2)
}
res=[]
for a in players.items():
    for b in a:
        res.append(b)
print(res[0]+res[1],res[2]+res[3],res[4]+res[5])