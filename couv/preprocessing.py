import numpy as np;


def search_k(v):
    'given a binary unit vector, return the index of 1'
    n = v.shape[0]
    for i in range(0, n):
        if(v[i] == 1):
            return i;



def rule_1(T, x, c, verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    temp = T;
    x0 = x; c0 = c;
    if(verbose): print("rule 1 : \n")
    n = T.shape[0];
    m = T.shape[1];
    lc = 0;
    lr = 0;
    for i in range(0,n):
        v = T[i,:];
        if(verbose): print " line ",i," : ", v
        if(np.linalg.norm(v) == 1):
            k = search_k(v);
            if(verbose): print "k : ",k," for line : ",i
            temp = np.delete(temp, i-lr, axis=0);
            lr += 1
            temp = np.delete(temp, k-lc, axis=1);
            x0[k-lc] = 1;
            #x0 = np.delete(x0, k-lc);
            c0 = np.delete(c0, k-lc, axis=0);
            lc += 1;
            for l in range(0, n):
                if(T[l,k] == 1 and l != i):
                    if(verbose): print "T[l][k] : ", l," ",k
                    temp = np.delete(temp, l-lr, axis=0);
                    lr += 1
    return [temp, x0, c0]



def is_include(u, v):
    'Given two vector, return if u is included in v'
    for i in range(0, u.shape[0]):
        if(u[i] == 1 and u[i] != v[i]):
            return False
    return True


def rule_2(T, verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    temp = T;
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
    return temp


#debug
def rule_3(T,x,c,verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    temp = T;
    x0 = x;
    c0 = c;
    m = temp.shape[1];
    lc = 0;
    j = 0;
    k = 0;
    while j < m:
        while k < m:
            #print j, " ",k
            if(j != k):
                if(is_include(temp[:,j-lc], temp[:,k-lc]) == True and c[j-lc] >= c[k-lc]):
                    if(verbose): print "Iteration ",j,". Vector : ", temp[:,j-lc]," is include in ", T[:,k-lc];
                    temp = np.delete(temp, j-lc, axis=1);
                    x0[j-lc] = -1;
                    x0 = np.delete(x0, j-lc, axis=0)
                    c0 = np.delete(c0, k-lc, axis=0);
                    lc += 1;
                elif(is_include(temp[:,k-lc], temp[:,j-lc]) == True and c[k-lc] >= c[j-lc]):
                    if(verbose): print "Iteration ",k,". Vector : ", temp[:,k-lc]," is include in ", T[:,j-lc];
                    temp = np.delete(temp, k-lc, axis=1);
                    x0[k-lc] = -1;
                    x0 = np.delete(x0, k-lc, axis=0);
                    c0 = np.delete(c0, k-lc, axis=0);
                    lc += 1;
            k += 1;
        j += 1;
    return [temp, x0, c0]


#Todo
def rule_4(T,x,c,verbose=False):
    return 0;




ref = np.array([
        [1,1,1,0,1,0,1,1,0],
        [0,1,1,0,0,0,0,1,0],
        [0,1,0,0,1,1,0,1,1],
        [0,0,0,1,0,0,0,0,0],
        [1,0,1,0,1,1,0,0,1],
        [0,1,1,0,0,0,1,0,1],
        [1,0,0,1,1,0,0,1,1]]);
#print ref, "\n"
#print rule_2(ref, True)
