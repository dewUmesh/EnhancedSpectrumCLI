
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Sigmoid(object):

    def segmoid(self,z):
       return 1.0/(1.0 + np.exp(-z))

    def plot(self,z):
        sns.set()
        plt.plot(z,self.segmoid(z))
        plt.xlabel('z')
        plt.ylabel('$\phi (z)$')
        plt.axvline(0.0, color='k')
        plt.axhline(y=0.5, ls='dotted', color='k')
        plt.axhspan(0.0, 1.0, facecolor='1.0', alpha=1.0, ls='dotted')

        plt.show()

