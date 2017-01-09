import numpy as np


# define I[i]
# define J[i]


#define f
norm  = 1 #card(I[j] union Ib) for all j in Jb

f  = lambda x: c[j]/norm
f2 = lambda x: c[j]/norm**2
f3 = lambda x: np.sqrt(c[j])/norm



def criteria(problem):
    temp = problem[0]
    f = np.zeros(temp.shape[1]);
    I0 = [] #I barre on the doc
    J = []
    for j in range(0, temp.shape[1]): #range(0, J.length)
        I1 = [] # I_j on the doc
        ens = list(set(I0) & set(I1));
        card = 1.0*ens.length;
        f[j] = c[j]/card
    return f


def select(problem, f):
    k = min(f);
