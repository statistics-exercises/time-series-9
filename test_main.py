import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self):
        fighand=plt.gca()
        fact, eps, power = 1, np.exp(-lamd*time), 1
        for i in range(noutcomes) :
           pval = (power/fact)*eps
           fact = fact * (i+1)
           power = power*(lamd*time)
           bar = np.sqrt( pval*(1-pval)  )*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( fighand.patches[i].get_height() - pval )<bar, "the heights of the bars in your histogram appear to be incorrect" )
  
    def test_xplot(self) :
        fighand = plt.gca()
        for i in range(noutcomes) :
            x, y = fighand.patches[i].get_xy() 
            self.assertTrue( np.fabs(x+0.5*fighand.patches[i].get_width()-i)<1e-7, "the x-coordinates of the bars in your histogram appear to be incorrect" )
  
    def test_normalisation(self) : 
        ssum = 0.
        fighand=plt.gca()
        for i in range(noutcomes) : ssum = ssum + fighand.patches[i].get_height()
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "the histogram you have drawn does not appear to have been normalised" )
