import numpy as np
import math
from math import pi

class NormalBayes(object):
    """"Bayes classifier.

    Parameters
    ------------
    none
    
    Attributes
    -----------
    mean_ : mean vectors of each class
    kova_ : kovariance matrices
    apri_ : a-priori probabilities
    """
 
    labels_ = []
    mean_ = {}
    kova_ = {}
    freq_ = {}
    apri_ = {}
        
    def __init__(self):
        pass
    
    # calculate normal density
    def norm_pdf(self, x, mu, sigma):
        size = len(x)
        if size == len(mu) and (size, size) == sigma.shape:
            # determinant
            det = np.linalg.det(2*pi*sigma)
            if det == 0:
                raise NameError("Die Kovarianzmatrix darf nicht singulär sein")

            # factor in front of exp
            norm_const = 1.0 / math.pow(det,0.5)
            x_mu = np.matrix(x - mu)
            inv = np.linalg.inv(sigma)       
            result = math.pow(math.e, -0.5 * (x_mu * inv * x_mu.T))
            return norm_const * result
        else:
            raise NameError("Dimensionen passen nicht")
    
    
    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X : {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like, shape = [n_samples]
            Target values.

        Returns
        -------
        none

        """
        
        self.labels_ = []
        self.mean_ = {}
        self.kova_ = {}
        self.freq_ = {}
        self.apri_ = {}
        
        # estimate mean vectors
        for sample,k in zip(X,y):
            if k not in self.labels_:
                self.labels_.append(k)
                self.mean_[k] = sample
                self.freq_[k] = 1
            else:
                self.mean_[k] += sample
                self.freq_[k] += 1
        
        for k in self.labels_:
            self.mean_[k] /= self.freq_[k]
            
        # estimate covariance matrices
        for sample,k in zip(X,y):
            x_minus_mu = sample - self.mean_[k]
            if k not in self.kova_:
                self.kova_[k] = np.outer(x_minus_mu,x_minus_mu)
            else:
                self.kova_[k] += np.outer(x_minus_mu,x_minus_mu)
                
        for k in self.labels_:
            self.kova_[k] /= self.freq_[k]
            
        # estimate a-priori
        samples = len(X)
        for k in self.labels_:
            self.apri_[k] = self.freq_[k]/samples
            
       
    def predict(self,X):
        """Return class label with highest a-posteriori probability"""
        Y = []
        for sample in X:
            results = []
            for k in self.labels_:
                results.append(self.norm_pdf(sample,self.mean_[k],self.kova_[k])*self.apri_[k])
            Y.append(self.labels_[np.argmax(results)])
        return Y