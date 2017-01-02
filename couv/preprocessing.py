import numpy as np;


def search_k(v):
    'given a binary unit vector, return the index of 1'
    n = v.shape[0]
    for i in range(0, n):
        if(v[i] == 1):
            return i;



def rule_1(T, x, verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    temp = T
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
            lc += 1;
            x[k] = 1; #item k we take the bin k
            for l in range(0, n):
                if(T[l,k] == 1 and l != i):
                    if(verbose): print "T[l][k] : ", l," ",k
                    temp = np.delete(temp, l-lr, axis=0);
                    lr += 1
    return temp



def is_include(u, v):
    'Given two vector, return if u is included in v'
    for i in range(0, u.shape[0]):
        if(u[i] == 1 and u[i] != v[i]):
            return False
    return True


#debug
def rule_2(T, verbose=False):
    'Apply the preprocessing rule number 1 to the matrix T'
    temp = T;
    print temp
    n = T.shape[0];
    lr = 0;
    for i in range(0, n):
        for l in range(0, n):
            if(lr < n):
                if(is_include(T[i,:], T[l,:])):
                    if(verbose): print "line : ", l, " ", lr
                    temp = np.delete(temp, l-lr, axis=0); lr += 1
                elif(is_include(T[l,:], T[i,:])):
                    if(verbose): print "line : ", l, " ", lr
                    temp = np.delete(temp, i-lr, axis=0); lr += 1
    return temp


def rule_3(T,x,c,verbose=False):
    return 0


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
print ref, "\n"
print rule_2(ref, True)
