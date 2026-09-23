import numpy as np
q1=np.array([
    [2,3,4],
    [5,6,7],
    [8,9,10]
])
q2=np.array([
    [2,3,4],
    [5,6,7],
    [8,9,10]
])
print ("sum of two matrix is: \n",q1+q2)

prices=np.array([
    [2,3,4],
    [5,6,7],
    [8,9,10]
])

q1_revenue=prices*q1
print("revenue of the q1 is :\n",q1_revenue)

q1_discount=q1_revenue*0.2

net_revenue=q1_revenue-q1_discount
print("net revnue is: \n",net_revenue)

print("sum of the net revenue",np.sum(net_revenue))