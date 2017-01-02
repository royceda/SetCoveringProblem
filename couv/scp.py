import numpy as np
from preprocessing import rule_1




if __name__ == "__main__":

    ref = np.array([
    [1,1,1,0,1,0,1,1,0],
    [0,1,1,0,0,0,0,1,0],
    [0,1,0,0,1,1,0,1,1],
    [0,0,0,1,0,0,0,0,0],
    [1,0,1,0,1,1,0,0,1],
    [0,1,1,0,0,0,1,0,1],
    [1,0,0,1,1,0,0,1,1]]);


    x = np.zeros(ref.shape[0])
    c = np.array([10,5,8,6,9,13,11,4,6])
    print x


    #test rule 1
    print "before : \n",ref
    print "after : \n", rule_1(ref,x,True);
