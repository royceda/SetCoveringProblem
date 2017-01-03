import numpy as np;



def delete(tab, index):
    tmp = [];
    for i in range(0, tab.shape[0]):
        if(i != index):
            tmp.append(tab[i]);
    return tmp;


def search_k(v):
    'given a binary unit vector, return the index of 1'
    n = v.shape[0]
    for i in range(0, n):
        if(v[i] == 1):
            return i;


#OK
def rule_1(problem, verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    T = problem[0];
    temp = T;
    x = problem[1];
    c = problem[2];
    if(verbose): print("rule 1 : \n")
    n = T.shape[0];
    lc = 0; #offset col
    lr = 0; #offset row
    for i in range(0,n):
        v = T[i,:];
        if(verbose): print " line ",i," : ", v
        if(np.linalg.norm(v) == 1):
            k = search_k(v);
            if(verbose): print "k : ",k," for line : ",i
            temp = np.delete(temp, i-lr, axis=0);
            lr += 1
            temp = np.delete(temp, k-lc, axis=1);
            x[k-lc] = 1;
            x = np.delete(x, k-lc);
            c = np.delete(c, k-lc);
            lc += 1;
            for l in range(0, n):
                if(T[l,k] == 1 and l != i):
                    if(verbose): print "T[l][k] : ", l," ",k
                    temp = np.delete(temp, l-lr, axis=0);
                    lr += 1
    return [temp, x, c]



def is_include(u, v):
    'Given two vector, return if u is included in v'
    for i in range(0, u.shape[0]):
        if(u[i] == 1 and u[i] != v[i]):
            return False
    return True

#OK
def rule_2(problem, verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    temp = problem[0];
    n = temp.shape[0];
    lr = 0;
    i = 0;
    l = 0;
    while i < n:
        while l < n:
            #print i, " ",l
            if(i != l):
                if(is_include(temp[i-lr,:], temp[l-lr,:]) == True):
                    if(verbose): print "Iteration ",i,". Vector : ", temp[i-lr,:]," is include in ", T[l-lr,:];
                    temp = np.delete(temp, l-lr, axis=0);
                    lr += 1;
                    n = temp.shape[0]
                elif(is_include(temp[l-lr,:], temp[i-lr,:]) == True):
                    if(verbose): print "Iteration ",l,". Vector : ", temp[l-lr,:]," is include in ", temp[i-lr,:];
                    temp = np.delete(temp, i-lr, axis=0);
                    lr += 1;
                    n = temp.shape[0]
            l += 1;
        i += 1;
    return [temp, problem[1], problem[2]];


#debug
def rule_3(problem, verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    if(verbose): print problem[0];
    temp = problem[0];
    T = problem[0];
    x = problem[1];
    c = problem[2];
    m = T.shape[1];
    lc = 0;
    j = 0; k = 0;
    while j < m:
        while k < m:
            #print j, " ",k
            if(j != k):
                if(is_include(temp[:,j-lc], temp[:,k-lc]) and c[j-lc] >= c[k-lc]):
                    if(verbose): print "Iteration1 ",j, " ", k,". Vector : ", temp[:,j-lc]," is include in ", temp[:,k-lc];
                    print " j = ",j," k = ", k
                    temp = np.delete(temp, j-lc, axis=1);
                    x[j-lc] = -1;
                    x = np.delete(x, j-lc);
                    c = np.delete(c, j-lc);
                    lc += 1;
                elif(is_include(temp[:,k-lc], temp[:,j-lc])  and c[k-lc] >= c[j-lc]):
                    if(verbose): print "Iteration ",k,". Vector : ", temp[:,k-lc]," is include in ", temp[:,j-lc];
                    temp = np.delete(temp, k-lc, axis=1);
                    x[k-lc] = -1;
                    x = np.delete(x, k-lc);
                    c = np.delete(c, k-lc);
                    lc += 1;
            k += 1;
        j += 1;
    return [temp, x, c]


#Todo
def rule_4(T, x, verbose=False):
    return 0;
