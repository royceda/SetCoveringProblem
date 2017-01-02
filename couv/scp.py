import numpy as np
from preprocessing import rule_1, rule_2, rule_3, is_include, search_k




if __name__ == "__main__":

    ref = np.array([
    [1,1,1,0,1,0,1,1,0],
    [0,1,1,0,0,0,0,1,0],
    [0,1,0,0,1,1,0,1,1],
    [0,0,0,1,0,0,0,0,0],
    [1,0,1,0,1,1,0,0,1],
    [0,1,1,0,0,0,1,0,1],
    [1,0,0,1,1,0,0,1,1]]);


    x = np.zeros(ref.shape[1])
    c = np.array([10,5,8,6,9,13,11,4,6])
    print c


    #search_k test

    e1 = np.array([0,1,0,0,0]);
    e0 = np.array([1,0,0,0,0]);
    e4 = np.array([0,0,0,0,1]);
    assert search_k(e0) == 0
    assert search_k(e1) == 1
    assert search_k(e4) == 4

    #test rule 1
    #print "before : \n",ref
    #print "after : \n", rule_1(ref,x,True);


    #include test
    u = np.array([0,1,1,0,1]);
    v = np.array([0,1,0,1,1]);
    w = np.array([1,1,1,0,1]);
    assert is_include(u,v) == False
    assert is_include(u,w) == True
    assert is_include(v,w) == False
    assert is_include(w,v) == False


    #test rule 2
    ref = rule_1(ref,x,False);
    #print "before : \n",ref
    #print "after : \n", rule_2(ref, True);


    #test rule_3
    ref = rule_2(ref,False);
    #print "before : \n",ref
    #print "after : \n", rule_3(ref,x,c, True);

    ref = rule_3(ref,x,c, True);
    ref = rule_2(ref,False);
    ref = rule_3(ref,x,c,False);

    print "Before rule 4:\n", ref
    print "Before solving : ", x
