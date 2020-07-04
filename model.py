''' Projeto ...

'''

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import time
from numpy import savetxt

def main():
    ##################### Initial Conditions #############################
    ## get values for p(a,0) or n(a,0)
    p0 = set_p0()
    savetxt('p0.csv', p0, delimiter=',')
    ## get values for x(a,0)
    x = get_x0()
    savetxt('x0.csv', x, delimiter=',')
    ## get values for y(a,0)
    y = get_y0()
    savetxt('y0.csv', y, delimiter=',')
    ## get values for s(a,0)
    # s0 = get_s0(x0,p0)
    # ## get values for i(a,0)
    # i0 = get_i0(y0,p0)
    # ## get values for r(a,0)
    # r0 = get_r0(p0,s0,i0)
    # #######################################################################

    # ################ Mortality Rate (2018 - BA Brasil) ####################
    µ = get_µ(p0)
    savetxt('mi.csv', µ, delimiter=',')

    #################### Estimated Parameters ############################
    ## Recovery Rate 
    gamma = 1/14 # roughly 8 days to full recovery
    ## Contact Rate
    ß = get_ß(p0)
    savetxt('beta.csv', ß, delimiter=',')
    #######################################################################

    #######################################################################

    ########################## Main Loop ##################################
    # for t in range(599):
    #     for a in range(150):
    #         if (a==0):
    #             x[a,t]=1.0
    #             y[a,t]=0.0
    #         else:
    #             el_lambda = get_lambda(a,t,p0,ß,y)
    #             # print("lambda",el_lambda)
    #             # print("vacina",vacina(a))
    #             x[a,t+1]= x[a,t] - el_lambda*x[a,t] - vacina(a)*x[a,t] + (x[a,t] - x[a-1,t])/365.0
    #             if (x[a,t+1] <0):
    #                 x[a,t+1] = 0
    #             # if (x[a,t+1] >1.0):
    #             #     x[a,t+1] = 1.0
    #             # print("x(a,t):",x[a,t])
    #             # print("x(a,t+1):",x[a,t+1])
    #             y[a,t+1]= y[a,t] + el_lambda*x[a,t] - gamma*y[a,t] + (y[a,t] - y[a-1,t])/365.0
    #             if (y[a,t+1] <0):
    #                 y[a,t+1] = 0
    #             # if (y[a,t+1] >1.0):
    #             #     y[a,t+1] = 1.0
    #             # print("y(a,t):",y[a,t])
    #             # print("y(a,t+1):",y[a,t+1])

    #     # print("x",x[:,t])
    #     # print("y",y[:,t])
    #     # time.sleep(10)

    # # print(x)

    # t = np.linspace(0, 49, 50,dtype=int)
    # a = np.linspace(0, 49, 50,dtype=int)
    # T, A = np.meshgrid(t, a)
    # Z = y[A,T]

    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # ax.contour3D(T, A, Z, 50, cmap='binary')
    # ax.set_xlabel('t')
    # ax.set_ylabel('a')
    # ax.set_zlabel('y')
    # plt.show()


##########################################################################################################################
##  Function vaccine, for different policies
##########################################################################################################################   
def vacina(a):
    return (0.1*0.9)

##########################################################################################################################
##  Function populates vector p0(a) with values, having a belonging to the interval [0,150]
##########################################################################################################################
def set_p0():
    p0 = np.zeros((150)) ## Vetor que representa s0(a), a entre 0 e 149
    for item in range (150):
        if (item <= 4):
            p0[item]=round(1019486.0/5)
        elif (item >= 5 and  item <= 9):
            p0[item]=round(146900.0 *7.18/5)
        elif (item >= 10 and  item <= 14):
            p0[item]=round(146900.0 *7.82/5)
        elif (item >= 15 and  item <= 19):
            p0[item]=round(146900.0 *8.48/5)
        elif (item >= 20 and  item <= 24):
            p0[item]=round(146900.0 *8.62/5)
        elif (item >= 25 and  item <= 29):
            p0[item]=round(146900.0 *8.16/5)
        elif (item >= 30 and  item <= 34):
            p0[item]=round(146900.0 *8.36/5)
        elif (item >= 35 and  item <= 39):
            p0[item]=round(146900.0 *8.29/5)
        elif (item >= 40 and  item <= 44):
            p0[item]=round(146900.0 *7.19/5)
        elif (item >= 45 and  item <= 49):
            p0[item]=round(146900.0 *6.19/5)
        elif (item >= 50 and  item <= 54):
            p0[item]=round(146900.0 *5.57/5)
        elif (item >= 55 and  item <= 59):
            p0[item]=round(146900.0 *4.68/5)
        elif (item >= 60 and  item <= 64):
            p0[item]=round(146900.0 *3.8/5)
        elif (item >= 65 and  item <= 69):
            p0[item]=round(146900.0 *2.96/5)
        elif (item >= 70 and  item <= 74):
            p0[item]=round(146900.0 *2.26/5)
        elif (item >= 75 and  item <= 79):
            p0[item]=round(146900.0 *1.59/5)
        elif (item >= 80 and  item <= 84):
            p0[item]=round(146900.0 *1.02/5)
        elif (item >= 85 and  item <= 89):
            p0[item]=round(146900.0 *0.54/5)
        elif (item >= 90 and  item <= 99):
            p0[item]=round(146900.0 *0.37/10)
        
    return(p0)

##########################################################################################################################
##  Function populates matrix x(a,t) having t=0 and a in the interval [0,150]
##########################################################################################################################
def get_x0():
    x = np.zeros((150,600),dtype=np.float64) ## Vetor que representa s0(a), a entre 0 e 149
    for item in range (150):
        if (item == 0):
            x[item,0]=1
        if (item >= 1 and item <= 4):
            x[item,0]=0.8
        elif (item >= 5 and  item <= 9):
            x[item,0]=0.8
        elif (item >= 10 and  item <= 14):
            x[item,0]=0.5
        elif (item >= 15 and  item <= 19):
            x[item,0]=0.5
        elif (item >= 20 and  item <= 24):
            x[item,0]=0.4
        elif (item >= 25 and  item <= 29):
            x[item,0]=0.4
        elif (item >= 30 and  item <= 34):
            x[item,0]=0.2
        elif (item >= 35 and  item <= 39):
            x[item,0]=0.2
        elif (item >= 40 and  item <= 44):
            x[item,0]=0.2
        elif (item >= 45 and  item <= 49):
            x[item,0]=0.2
        elif (item >= 50 and  item <= 54):
            x[item,0]=0.2
        elif (item >= 55 and  item <= 59):
            x[item,0]=0.2
        elif (item >= 60 and  item <= 64):
            x[item,0]=0.2
        elif (item >= 65 and  item <= 69):
            x[item,0]=0.2
        elif (item >= 70 and  item <= 74):
            x[item,0]=0.2
        elif (item >= 75 and  item <= 79):
            x[item,0]=0.2
        elif (item >= 80 and  item <= 84):
            x[item,0]=0.2
        elif (item >= 85 and  item <= 89):
            x[item,0]=0.2
        elif (item >= 90 and  item <= 99):
            x[item,0]=0.2
        
    return(x)

##########################################################################################################################
##  Function populates matrix y(a,t) having t=0 and a in the interval [0,150]
##########################################################################################################################
def get_y0():
    y = np.zeros((150,600),dtype=np.float64) ## Vetor que representa s0(a), a entre 0 e 149
    for item in range (150):
        if (item >= 1 and item <= 4):
            y[item,0]=0.2
        elif (item >= 5 and  item <= 9):
            y[item,0]=0.2
        elif (item >= 10 and  item <= 14):
            y[item,0]=0.5
        elif (item >= 15 and  item <= 19):
            y[item,0]=0.1
        elif (item >= 20 and  item <= 24):
            y[item,0]=0.01
        elif (item >= 25 and  item <= 29):
            y[item,0]=0.01
        elif (item >= 30 and  item <= 34):
            y[item,0]=0.001
        elif (item >= 35 and  item <= 39):
            y[item,0]=0.001
        
    return(y)

##########################################################################################################################
##  Function populates vector µ(a) having  a in the interval [0,150]
##########################################################################################################################

# def get_s0(x0,p0):
#     s = np.zeros((150,600),dtype=np.float64) ## Vetor que representa s0(a), a entre 0 e 149
#     for item in range (150):
#         if item = 0:
#             s[item]
#     return(y)

##########################################################################################################################
##  Function populates vector µ(a) having  a in the interval [0,150]
##########################################################################################################################
def get_µ(p0):
    µ = np.zeros((150)) ## Vetor que representa s0(a), a entre 0 e 149
    for item in range (150):
        if (item == 0):
            µ[item] = 2000.0/(p0[item]*365)
        elif (item >= 1 and item <= 4):
            µ[item] = 380.0/(p0[item]*365*3)
        elif (item >= 5 and  item <= 9):
            µ[item] = 226.0/(p0[item]*365*4)
        elif (item >= 10 and  item <= 14):
            µ[item] = 367.0/(p0[item]*365*4)
        elif (item >= 15 and  item <= 19):
            µ[item] = 2032.0/(p0[item]*365*4)
        elif (item >= 20 and  item <= 29):
            µ[item] = 5151.0/(p0[item]*3650)
        elif (item >= 30 and  item <= 39):
            µ[item] = 5217.0/(p0[item]*3650)
        elif (item >= 40 and  item <= 49):
            µ[item] = 6693.0/(p0[item]*3650)
        elif (item >= 50 and  item <= 59):
            µ[item] = 2000.0/(p0[item]*3650)
        elif (item >= 60 and  item <= 69):
            µ[item] = 10131.0/(p0[item]*3650)
        elif (item >= 70 and  item <= 79):
            µ[item] = 13820.0/(p0[item]*3650)
        elif (item >= 80 and  item <= 99):
            µ[item] = 16829.0/(p0[item]*3650)
        else:
            µ[item] = 16829.0/(p0[99]*3650)
    return(µ)
   

##########################################################################################################################
##  Function populates Matrix ß(a,a') having  a,a' in the interval [0,150]
##########################################################################################################################
def get_ß(p0):

    ## get ai vector (infected)
    a = np.zeros((150))
    for item in range (150):
        if (item == 0):
            a[item] = 1.0
        elif (item >= 1 and item <= 4):
            a[item] = 5.8
        elif (item >= 5 and  item <= 9):
            a[item] = 5.8
        elif (item >= 10 and  item <= 14):
            a[item] = 3.0
        elif (item >= 15 and  item <= 19):
            a[item] = 3.0
        elif (item >= 20 and  item <= 24):
            a[item] = 2.8
        elif (item >= 25 and  item <= 29):
            a[item] = 2.8
        elif (item >= 30 and  item <= 34):
            a[item] = 1.0
        elif (item >= 35 and  item <= 39):
            a[item] = 0.8
        else:
            a[item] = 0.4

    ## get Sum of ak*p[k] (infecteds)
    ak = 0.0
    for item in range (150):
        ak = ak + a[item]*p0[item]

    ## get bj vectors (susceptibles)
    b = np.zeros((150))
    for item in range (150):
        b[item] = (a[item]*p0[item])/ak
        
    ## write matrice ß
    ß = np.zeros((150,150))
    for infected in range (150):
        for susceptible in range (150):
            ß[susceptible,infected] = b[susceptible]*a[infected]

    ## return ß matrice
    return(ß)

## Function Gamma:
def get_lambda(a,t,p0,ß,y):
    soma = 0.0
    for s in range(150):
        # term = ß[a,s]*p0[s]
        term = ß[a,s]
        term = term*y[s,t]
        
        soma = soma + term
        # print("term:",term)
        # print("soma:",soma, ß[a,s] ,y[s,t])
    # if p0[a] > 0.0:
    #     soma = soma/p0[a]
    # else:
    #     soma = 0
    # soma = soma/p0[a]
    return(soma)


##########################################################################################################################
if __name__ == "__main__":

    main()

    exit()