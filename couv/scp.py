import numpy as np
from preprocessing import rule_1, rule_2, rule_3, is_include, search_k, rule_4, rebuild




if __name__ == "__main__":

    ref = np.array([
    [1,1,1,0,1,0,1,1,0],
    [0,1,1,0,0,0,0,1,0],
    [0,1,0,0,1,1,0,1,1],
    [0,0,0,1,0,0,0,0,0],
    [1,0,1,0,1,1,0,0,1],
    [0,1,1,0,0,0,1,0,1],
    [1,0,0,1,1,0,0,1,1]]);




    index = [];
    for i in range(0, ref.shape[1]):
        index.append(i);
    #print index

    x = np.array(np.zeros(ref.shape[1])) #final x
    c = np.array([10,5,8,6,9,13,11,4,6]) #final
    #print c


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



    #rebuild test
    M = np.array([
        [0,1,1,1],
        [1,0,1,0],
        [0,0,1,1]]);
    hist = [];
    M = np.delete(M, 2,axis=1);
    hist.append(2);
    M = np.delete(M, 0, axis=1);
    hist.append(0)
    M = np.delete(M, 1, axis=1);
    hist.append(1)

    rebuild_index = rebuild([M, [], [], hist]);

    print rebuild_index
    last = rebuild_index[0]
    assert last[0] == 0
    last = rebuild_index[1]
    assert last[0] == 1
    assert last[1] == 2
    last = rebuild_index[2]
    assert last[0] == 0
    assert last[1] == 1
    assert last[2] == 3




    prob = [ref, x, c, []];

    print ref
    #test rule 1 and 2
    prob = rule_1(prob,False);
    prob = rule_2(prob,False);
    prob = rule_3(prob,False);
    # OK
    #print "before : \n",ref
    #print "after : \n", rule_2(ref, True);

    #test rule_3
    #print "before : \n",ref
    #print "after : \n", rule_3(ref,x,c, True);


    #prob = rule_4(prob, False);
    #prob = rule_2(prob, True);
    #prob = rule_3(prob, False);
    #prob = rule_2(prob, False);
    #prob = rule_3(prob, False);

    print "Before rule 4:\n", prob[0]
    print "History : \n", prob[3]
    print rebuild(prob)
