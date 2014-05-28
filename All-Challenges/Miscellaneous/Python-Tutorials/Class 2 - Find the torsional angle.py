# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
class points(object):
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
def distance(A,B):
  C = points(0,0,0)
  C.x = A.x - B.x
  C.y = A.y - B.y
  C.z = A.z - B.z
  return C
def crossProduct(AB,BC):
  E = points(0,0,0)
  E.x = AB.y*BC.z - AB.z*BC.y
  E.y = AB.z*BC.x - AB.x*BC.z
  E.z = AB.x*BC.y - AB.y*BC.x
  return E
def dotProduct(X,Y):
  return X.x*Y.x + X.y*Y.y + X.z*Y.z

def modulus(X,Y):
  return math.sqrt((X.x**2+X.y**2+X.z**2)*(Y.x**2+Y.y**2+Y.z**2))
  
[p,q,r] = [float(i) for i in raw_input().split()]
A = points(p,q,r)
[p,q,r] = [float(i) for i in raw_input().split()]
B = points(p,q,r)
[p,q,r] = [float(i) for i in raw_input().split()]
C = points(p,q,r)
[p,q,r] = [float(i) for i in raw_input().split()]
D = points(p,q,r)

AB = distance(A,B)
BC = distance(B,C)
CD = distance(C,D)
X = crossProduct(AB,BC)
Y = crossProduct(BC,CD)

print "%.2f"%math.degrees(math.acos(dotProduct(X,Y)/modulus(X,Y)))
