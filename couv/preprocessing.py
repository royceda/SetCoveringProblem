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
    'Apply the preprocessing rule number 1 to the problem [T, x, c]'
    print "rule 1"
    T = problem[0];
    temp = T;
    x = problem[1];
    c = problem[2];
    if(verbose): print("rule 1 : \n")
    n = T.shape[0];
    lc = 0; #offset col
    lr = 0; #offset row
    for i in range(0,n):
        v = temp[i-lr,:];
        if(verbose): print " line ",i," : ", v
        if(np.linalg.norm(v) == 1 and i >= lr ):
            k = search_k(v);
            if(verbose): print "k : ",k," for line : ",i
            temp = np.delete(temp, i-lr, axis=0);
            lr += 1
            temp = np.delete(temp, k-lc, axis=1);
            x[k-lc] = 1;
            print "x[",k-lc,"] = 1"
            x = np.delete(x, k-lc);
            c = np.delete(c, k-lc);
            lc += 1;
            for l in range(0, n):
                if(T[l,k] == 1 and l != i):
                    if(verbose): print " supp T[l][k] : ", l," ",k
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
    'Apply the preprocessing rule number 1 to the problem [T, x, c]'
    print "rule 2"
    temp = problem[0];
    n = temp.shape[0];
    lr = 0;
    for i in range(0, n):
        for l in range(0, n):
            if(i != l and i >= lr and l >= lr):
                #print "lr = ", lr
                if(is_include(temp[i-lr,:], temp[l-lr,:])):
                    if(verbose): print "Iteration ",i,". Vector : ", temp[i-lr,:]," is include in ", temp[l-lr,:];
                    temp = np.delete(temp, l-lr, axis=0);
                    lr += 1;
                    n = temp.shape[0]
                elif(is_include(temp[l-lr,:], temp[i-lr,:])):
                    if(verbose): print "Iteration ",l,". Vector : ", temp[l-lr,:]," is include in ", temp[i-lr,:];
                    temp = np.delete(temp, i-lr, axis=0);
                    lr += 1;
                    n = temp.shape[0]
    return [temp, problem[1], problem[2]];


def test_rule_3(temp, c):
    print "test rule 3 : "
    for i in range(0, temp.shape[1]):
        for j in range(0, temp.shape[1]):
            if(is_include(temp[:,i], temp[:,j]) and c[i] > c[j]):
                return True;
            elif(is_include(temp[:,j], temp[:,i]) and c[j] > c[i]):
                return True
    return False

#debug
def rule_3(problem, verbose=False):
    'Apply the preprocessing rule number 1 to the problem [T, x, c]'
    print "rule 3"
    print problem[0] , "\n"
    temp = problem[0];
    x = problem[1]
    c = problem[2]
    n = temp.shape[1];
    lr = 0;
    while test_rule_3(temp, c):
        for i in range(0,n):
            for l in range(0,n):
                if(i != l and i >= lr and l >= lr):
                    #print "lr = ", lr
                    print ' i : ',i, " l :  ",l
                    if(is_include(temp[:,i-lr], temp[:,l-lr]) and c[i-lr] >= c[l-lr]):
                        if(verbose): print "Iteration ",i,". Vector : ", temp[:,i-lr]," is include in ", temp[:,l-lr];
                        temp = np.delete(temp, l-lr, axis=1);
                        x = np.delete(x, l-lr);
                        c = np.delete(c, l-lr);
                        print "x[",l-lr,"] = 0"
                        lr += 1;
                        n = temp.shape[1];
                    elif(is_include(temp[:,l-lr], temp[:,i-lr]) and c[l-lr] >= c[i-lr]):
                        if(verbose): print "Iteration ",l,". Vector : ", temp[:,l-lr]," is include in ", temp[:,i-lr];
                        temp = np.delete(temp, i-lr, axis=1);
                        x = np.delete(x, i-lr);
                        c = np.delete(c, i-lr);
                        print "x[",i-lr,"] = 0"
                        lr += 1;
                        n = temp.shape[1];
    return [temp, x, c];


#Todo
def rule_4(T, x, verbose=False):
    return 0;
