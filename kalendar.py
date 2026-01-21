import math
datum = input('zadaj den, mesuiac, rok (DD.MM.YYYY):')
dni = ['Sobota','Nedela','Pondelok','Utorok','STreda','Stvrtok','Piatok']
casti_datumu = datum.split(".")
q = int(casti_datumu[0])
k = int(casti_datumu[2])
m = int(casti_datumu[1])
#print(q,m,k)
K = k % 100
J = k // 100
#print(K,J)
if m == 1 or m == 2:
    m +=12
    K -= 1
    #print(m)
x=math.floor((13*(m + 1)) / 5)
print(x)
#h = (q + math.floor((13*(m + 1)) / 5) + K + math.floor(K/4) + math.floor(J/4) - (2*J)) % 7

#print(dni[h])