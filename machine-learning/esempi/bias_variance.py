import numpy as np
from sklearn.model_selection import train_test_split
from scipy.special import legendre
from numpy.linalg import solve
from sklearn.model_selection import KFold

legendre_d = lambda x, d : np.sqrt(2*d+1)*(legendre(d))(2*x-1)

def polynomial_regression(x_train, x_test, y_train, y_test, D) :

    """
        Peforms least-squares polynomial regression using Legendre polynomial as basis.

        x_train = coordinated of training data
        y_train = values of training data
        x_test = coordinated of test data
        y_train = values of test data
        D = polynomial order + 1
    """

    N_train = len(x_train)
    N_test = len(x_test)

    X = np.ones((N_train,1))
    for d in range(1,D) :
        x_d = legendre_d(x_train,d)
        x_d = x_d.reshape(-1, 1)
        X = np.concatenate((X, x_d), axis=1)

    S = X.T@X/N_train
    y_star = X.T@y_train/N_train
    w_star = solve(S,y_star)

    y_model = lambda x, w: sum([w[d]*legendre_d(x,d) for d in range(D)])

    ls_err_train = np.sqrt(np.sum((y_model(x_train,w_star)-y_train)**2)/N_train)
    ls_err_test = np.sqrt(np.sum((y_model(x_test,w_star)-y_test)**2)/N_test)
    w_norm = np.sqrt(np.sum(w_star**2))/D

    return ls_err_train, ls_err_test, w_norm


def cross_validation(x_data, y_data, D, Nk=4, seed=42) :

    """
        Peforms k-means on a given 1D dataset

        x_data = coordinates
        y_data = values
        D = polynomial order + 1
        Nk = #chunks [4]
        seed = random seed for train/test split [42]
    """

    kf = KFold(n_splits=Nk, shuffle=True, random_state=seed)

    lse_tr_vec = []
    lse_te_vec = []
    wn_vec = []

    for fold, (train_index, test_index) in enumerate(kf.split(x_data)):

        x_train, x_test = x_data[train_index], x_data[test_index]
        y_train, y_test = y_data[train_index], y_data[test_index]

        lse_tr, lse_te, wn = polynomial_regression(x_train, x_test, y_train, y_test, D)

        lse_tr_vec.append(lse_tr)
        lse_te_vec.append(lse_te)
        wn_vec.append(wn)

    lse_tr_vec = np.array(lse_tr_vec)
    lse_te_vec = np.array(lse_te_vec)
    wn_vec = np.array(wn_vec)

    return np.mean(lse_tr_vec), np.mean(lse_te_vec), np.mean(wn_vec)
        



if __name__ == "__main__" :

    true_poly = lambda x : 1-8.67857*x+25.875*x**2-28.9286*x**3+7.23214*x**4+4.33929*x**5
    N = 50
    x_data = np.linspace(0.0,1.0,N)
    y_data = true_poly(x_data)
    std_noise = 0.03
    y_noise = np.random.normal(loc=0.0,scale=std_noise,size=N)
    y_data += y_noise

    lse_train, lse_test, wn = cross_validation(x_data, y_data, 5)
    print("Average LS training error =",lse_train)
    print("Average LS test error =",lse_test)
    print("Average 2-norm of the weights =",wn)