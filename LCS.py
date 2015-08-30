#Group 8
#Title: Code for Faster algorithm for computing string edit distances
#Course: Algorithms
#Author: Shivyansh, Dhwanit, Divyansh, Amitansh, Akshay
#Instructor: Akash Anand


# The following functions define cost of delete, insert and replace operations appropriately
#replace function
def replace(x, y):
    if x == 'c':
        return insert(y)
    if y == 'c':
        return delete(x)
    if x == y:
        return 0;
    else:
        return 2;

#delete function
def delete(x):
    if x == 'c':
        return 0;
    else:
        return 1;

#insert function
def insert(x):
    if x == 'c':
        return 0;
    else:
        return 1;

#finding string index value
def index_alp(x, alphabet):
    counter = 0
    for i in alphabet:
        if x == i:
            return counter

        counter+= 1

#Coverts a string of m length to its index in RAM
def string_to_index(a, alphabet):
    index = 0
    for i in range(len(a)):
        index = index + index_alp(a[i])*(alp_num**(i))

    return index



#_main_Program


#alphabet = raw_input('Enter the alphabet list: ')
alphabet = 'abc'
A_raw = raw_input('Enter the first string: ')
size_Araw = len(A_raw)
A  = A_raw
if size_Araw%3 != 0:
    for i in range(3*(int(size_Araw/3)+1) - size_Araw):
        A = A + 'c'        #Padding of A

#A = 'aba'
size_A = len(A)
B_raw = raw_input('Enter the second string: ')
size_Braw = len(B_raw)
B = B_raw
if size_Braw%3 != 0:
    for i in range(3*(int(size_Braw/3)+1) - size_Braw):
        B = B + 'c'         #padding of B
#B = 'bab'
size_B = len(B)
#print A
#print B
#*****************edit on num for the entire algorithm Y
#num = raw_input('Enter m:')
num = 3 # This is m
num = int(num)
k = int(num) + 1
alp_num = len(alphabet)

#ENUMERATING STRINGS of length m
from itertools import product
enum = [''.join(x) for x in product(alphabet, repeat=num)]

#initialising intermediate variables
T = [[0 for x in range(num+1)] for x in range(num+1)]
U = [[0 for x in range(num+1)] for x in range(num+1)]

#initialising storage vectors
Rfinal = [[[[[0 for x in range(num)] for x in range(3**num+3)]for x in range(3**num+3)]for x in range(3**num+3)]for x in range(3**num+3)]
Sfinal = [[[[[0 for x in range(num)] for x in range(3**num+3)]for x in range(3**num+3)]for x in range(3**num+3)]for x in range(3**num+3)]

#CALCULATING STEP VECTORS of length m
R = [''.join(x) for x in product('*01', repeat=num)]
#print R

init_vec1 = [0 for x in range(num)]
init_vec2 = [0 for x in range(num)]
#C = [0 for x in range(num)]
#D = [0 for x in range(num)]

enum1 = ['bbb']
enum2 = ['aaa']
R1 = ['*11']
R2 = ['*11']
#MAIN LOOP
#ALGORITHM Y------------------------------------------------------------
for x in enum:   #looping through all substrings
    '''counter1 = 1
    for temp in x:   #storing the current substring (C)
        C[counter1] = temp     #current substring C
        counter1+=1'''
    for y in enum:    #looping through all substrings
        '''counter2 = 1
        for temp2 in y:   #storing the current substring (D)
            D[counter2] = temp2    #current substring D
            counter2+=1'''
        for p in R:        #storing the values initial step vector R
            a = 0
            for t in p:
                if t == '*':
                    init_vec1[a] = -1
                    a+=1
                elif t == '0':
                    init_vec1[a] = 0
                    a+=1
                elif t == '1':
                    init_vec1[a] = 1
                    a+=1
            for q in R:    #storing the values initial step vector S
                a = 0
                for t in q:
                    if t == '*':
                        init_vec2[a] = -1
                        a+=1
                    elif t == '0':
                        init_vec2[a] = 0
                        a+=1
                    elif t == '1':
                        init_vec2[a] = 1
                        a+=1
                for i in range(1,num+1):  #assigning the initial values to intermediate variables
                    T[i][0] = init_vec1[i-1]
                    U[0][i] = init_vec2[i-1]

                for i in range(1,num+1):    #main computation for final step vectors
                    for j in range(1,num+1):
                        T[i][j] = min(replace(x[i-1],y[j-1]) - U[i-1][j], delete(x[i-1]), insert(y[j-1]) + T[i][j-1] - U[i-1][j]);
                        U[i][j] = min(replace(x[i-1],y[j-1]) - T[i][j-1], insert(y[j-1]), delete(x[i-1]) + U[i-1][j] - T[i][j-1]);

                #print T
                #print U
                #calculating index value for initial step vectors
                Rvalue = 0
                Svalue = 0
                Cvalue = 0
                Dvalue = 0
                for z in range (num):
                    Rvalue+=(init_vec1[z]+1)*(3**(z))
                    Svalue+=(init_vec2[z]+1)*(3**(z))
                    Cvalue+=(index_alp(x[z], alphabet))*(alp_num**(z))
                    Dvalue+=(index_alp(y[z], alphabet))*(alp_num**(z))

                #print Cvalue, Dvalue, Rvalue, Svalue
                #storing final vectors
                for i in range(num):
                    Rfinal[Cvalue][Dvalue][Rvalue][Svalue][i] = T[i+1][num];
                    Sfinal[Cvalue][Dvalue][Rvalue][Svalue][i] = U[num][i+1];

#ALGORITHM Z-------------------------------------------------------------
#initialising intermediate variables

Anum = size_A/num
Anum = int(Anum)
Bnum = size_B/num
Bnum = int(Bnum)

P = [[0 for x in range(Bnum+1)] for x in range(Anum+1)]
Q = [[0 for x in range(Bnum+1)] for x in range(Anum+1)]


for i in range(1,Anum+1):
    P[i][0] = [delete(A[j-1])for j in range((i-1)*num+1, i*num+1)]    #****check with algo   1 less as array stored
    #print P[i][0]
for j in range(1,Bnum+1):
    Q[0][j] = [insert(B[(i-1)])for i in range((j-1)*num+1, j*num+1)]    #****check with algo
    #print Q[0][j]

for i in range(1,Anum+1):
    for j in range(1,Bnum+1):
        #finding the index value
        Avalue = 0
        Bvalue = 0
        temp7=0
        temp8=0
        for z in range((i-1)*num+1,i*num+1):
            Avalue+=(index_alp(A[z-1], alphabet))*(alp_num**(temp7))
            temp7+=1
        for z in range((j-1)*num+1,j*num+1):
            Bvalue+=(index_alp(B[z-1], alphabet))*(alp_num**(temp8))
            temp8+=1
        Pvalue = 0
        Qvalue = 0
        temp5=0
        temp6=0
        #print P[i][j-1]
        for x in P[i][j-1]:             #EDIT if cost function changes
            Pvalue+=(x+1)*(3**(temp5))
            temp5+=1
        #print Q[i-1][j]
        for x in Q[i-1][j]:
            Qvalue+=(x+1)*(3**(temp6))
            temp6+=1
        #if i == 2 and j ==2:
            #print Avalue, Bvalue, Pvalue, Qvalue
        P[i][j] = Rfinal[Avalue][Bvalue][Pvalue][Qvalue]  #****CHECK
        Q[i][j] = Sfinal[Avalue][Bvalue][Pvalue][Qvalue]  #****CHECK



cost = 0
for i in range(1,Anum+1):
    cost+=sum(P[i][0])

#print cost
#print Q[1][1]
#print Q[1][2]
for j in range(1,Bnum+1):
    #print Q[Anum][j]
    cost+=sum(Q[Anum][j])


print 'Strings: ' + A_raw + ' , ' + B_raw
print 'Cost:', cost
print 'Length of longest common subsequence:', (size_Araw + size_Braw - cost)/2

