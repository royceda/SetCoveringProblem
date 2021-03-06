import numpy as np;


x_map = {}



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
    history = problem[3]
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
            history.append(k-lc)
            x = np.delete(x, k-lc);
            c = np.delete(c, k-lc);
            print "x[",k-lc,"] = 1"
            lc += 1;
            for l in range(0, n):
                if(T[l,k] == 1 and l != i):
                    if(verbose): print " supp T[l][k] : ", l," ",k
                    temp = np.delete(temp, l-lr, axis=0);
                    lr += 1
    return [temp, x, c, history]




def rebuild(problem):
    'rebuild the mapping from the deleted index history'
    T = problem[0]
    s = T.shape[1]
    hist = problem[3]
    hist_index = []
    for i in range(len(hist)-1, -1, -1):
        d = hist[i] #from end
        index = {}
        print d
        for k in range(d, s):
            if index.has_key(k):
                index[k] += 1
            else:
                index[k] = k+1
        for k in range(0, d):
            if index.has_key(k):
                index[k] = index[k]
            else:
                index[k] = k
        hist_index.append(index)
        s+=1
    return hist_index







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
    return [temp, problem[1], problem[2], problem[3] ];


def test_rule_3(temp, c):
    #print "test rule 3 : "
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
    history = problem[3]
    n = temp.shape[1];
    lr = 0;
    while test_rule_3(temp, c):
        for i in range(0,n):
            for l in range(0,n):
                if(i != l and i >= lr and l >= lr):
                    #print "lr = ", lr
                    #print ' i : ',i, " l :  ",l
                    if(is_include(temp[:,i-lr], temp[:,l-lr]) and c[i-lr] >= c[l-lr]):
                        if(verbose): print "Iteration ",i,". Vector : ", temp[:,i-lr]," is include in ", temp[:,l-lr];
                        temp = np.delete(temp, l-lr, axis=1);
                        history.append(l-lr)
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
                        history.append(i-lr)
                        print "x[",i-lr,"] = 0"
                        lr += 1;
                        n = temp.shape[1];
    return [temp, x, c, history];


#Todo
def rule_4(problem, verbose=False):
    temp = problem[0]
    x = problem[1]
    c = problem[2]
    lr = 0;

    for j in range(0, temp.shape[1]):
        if(np.linalg.norm(temp[:,j]) > 1 ):
            s_list = []
            #compute min
            for i in range(0, temp.shape[0]):
                tmp_list = []
                for k in range(0, temp.shape[1]):
                    if( temp[i][k] == 1):
                        tmp_list.append(c[k]);
                s_list.append(min(tmp_list))
            #prepare sum with list min
            s = sum(s_list);
            if(c[j] >= s):
                x[j] = 0;
                temp = np.delete(temp, j-lr, axis=1);
                lr += 1;
                x[j] = 0;
    return [temp, x, c];
