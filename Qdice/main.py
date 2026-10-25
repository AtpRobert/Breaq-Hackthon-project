import random
import math

V1=[0,1,0,0,1,0,1,0,1,1,1,0,0]
Vb1=["Z","X","Z","X","X","X","Z","X","Z","X","X","Z","Z"]
Vr1=[1,2,3,4,5,6,7,8,9,10,11,12,13]

VrTransmis=[]

V2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
Vb2=["X","Z","Z","Z","X","Z","Z","X","Z","X","Z","X","Z"]
Vr2=[1,2,3,4,5,6,7,8,9,10,11,12,13]


#starea Alice
#Alice masoara bitii(V1) ei in raport cu bazele(Vb1) si salvam masuratoarea(Vr1)
for i in range(0,len(V1)):
  if V1[i]==0:
    if Vb1[i]=="Z":
      Vr1[i]="|0>"
    else:
      Vr1[i] = "|+>"
  else:
    if Vb1[i]=="Z":
      Vr1[i]="|1>"
    else:
      Vr1[i]="|->"

print("Alice", Vr1)

VrTransmis=Vr1
#print("Transmis", VrTransmis)


#We deploy Eve >:)

VbEve=["Z","Z","X","X","X","Z","Z","X","Z","Z","Z","X","X"]
VrEve=[1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in range(0,len(V1)):
  if VbEve[i]=="Z":
    if Vr1[i]=="|+>" or Vr1[i]=="|->":
      a=random.randint(0,9)
      if(a%2==0):
        VrEve[i]="|+>"
      else:
        VrEve[i] = "|->"
    else:
      VrEve[i] = Vr1[i]
  else:
    if Vr1[i]=="|0>" or Vr1[i]=="|1>":
      a=random.randint(0,9)
      if a%2==0:
        VrEve[i]="|0>"
      else:
        VrEve[i] = "|1>"
    else:
      VrEve[i] = Vr1[i]

print("Alice modificat de Eve",VrEve)
VrTransmis=VrEve

#Gata Eve







#Stare Bob
#Bob prelucreaza masuratoarea primita de la Alice (VrTransmis) (interceptata de Eve sau nu)
#in raport cu bazele(Vb2) sale si salveaza in Vr2
for i in range(0,len(V1)):
  if Vb2[i]=="Z":
    if VrTransmis[i]=="|+>" or VrTransmis[i]=="|->":
      a=random.randint(0,9)
      if(a%2==0):
        Vr2[i]="|+>"
      else:
        Vr2[i] = "|->"
    else:
      Vr2[i] = Vr1[i]
  else:
    if VrTransmis[i]=="|0>" or VrTransmis[i]=="|1>":
      a=random.randint(0,9)
      if a%2==0:
        Vr2[i]="|0>"
      else:
        Vr2[i] = "|1>"
    else:
      Vr2[i] = Vr1[i]

print("Bob",Vr2)


#intersectie baze
intersectie=[0,1,2,3,4,5,6,7,8,9,10,11,12]

for i in range(0,len(V1)):
  if Vb1[i]!=Vb2[i]:
    intersectie[i]=-1


nr=0
ramas=[]
for i in range(0,len(intersectie)):
  if intersectie[i]!=-1:
    print(intersectie[i]+1," ",end="")
    nr=nr+1
    ramas.append(intersectie[i])

print()
print("Ramas", ramas)

#Biti Bob
for i in range(0,len(Vb2)):
  if Vb2[i]=="Z":
    if Vr2[i]=="|0>":
      V2[i]=0
    else:
      V2[i] = 1
  else:
    if Vr2[i]=="|+>":
      V2[i]=0
    else:
      V2[i]=1


print()

print("Bob biti", V2)







print("Bazele intersectate")
for i in range(0, len(intersectie)):
  if intersectie[i] != -1:
    print(Vb1[i], " ", end="")

print()

#print(random.choice(ramas))

eroare=0
pozitie_eroare=[]

cantitate_baze_matched=nr

#rata de masurat, 25+
rata=25
nr=nr*rata/100
#print(int(nr))


for i in range(1,int(nr)+1):
  a=random.choice(ramas)
  print("a =",a)
  if V1[a]!=V2[a]:
    eroare=eroare+1
    pozitie_eroare.append(a)
  ramas.remove(a)

print("Eroare",eroare)

Q_hat=eroare/cantitate_baze_matched

print("Q_hat: ",Q_hat)

#epsilon e pre-stabilit ca fiind 10^10
epsilon=1e-10
Q_u=Q_hat+math.sqrt(math.log((1/epsilon))/2*cantitate_baze_matched)

if Q_u > 11/100:
  print("Abandonam, Eve ne asculta!")


#PT CORECTAREA ERORII

#bloc=0.73/Q_hat

#for i in range(0,int())

print("Cheia ramasa")
for i in ramas:
  print(V1[i]," ",end="")
print()



