# Histogram for Poisson Process

In this last exercise we are going to compute a histogram for the random variable that we sampled in the last exercise.   Notice that this random variable is a discrete random variable so you need to employ the procedures for computing histograms for a discrete random variables.  Notice, furthermore, that the random variable can take any integer value that is greater than or equal to zero.  We thus have to truncate the number of bins and assume that generating large values is unlikely.

I have written some code to start you off in the cell on the left as always.   To complete the code you need to:

1. Write a function called `poisson` that takes in two parameters `lam` (the lambda parameter for the poisson process) and `time` the time that you will simulate the poisson process for.  This function should return the number of events that occur during the time window of length `time`.
2. You need to write a loop that will generate multiple random variables and that will update the elements of the array called `counts` to reflect how often each of the elements in  the sample space for the random variable come up.  Notice, furthermore, that in order to pass the tests you will need to set the lam and time parameters of the poisson function equal to the variables `lamd` and `time` respectively.
3. Lastly, note that the variable called `noutcomes` should be set equal to the maximum number of outcomes that you would expect to occur in the time interval.  This variable determines how many bars there will be in the histogram and it is important that it is set as it is used in the tests.
