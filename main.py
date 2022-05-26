from cmath import sqrt
import pandas as pd
import numpy as np
import ssl
import matplotlib.pyplot as plt
import scipy
from scipy.stats import binom, hypergeom, poisson, norm, t, f, chi2, ttest_1samp
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.proportion import proportions_ztest
ssl._create_default_https_context = ssl._create_unverified_context

#terminal colors
OKGREEN = '\033[92m'
ENDCOL = '\033[0m'

# read file
df_samp = pd.read_csv('https://projects.fivethirtyeight.com/mlb-api/mlb_elo.csv')
# isolate scores column, representing each team's score
scores = df_samp.loc[:, ["score1", "score2"]]

# create or modify dataframe for analysis
# filter scores for non NULL values
scores = scores.dropna()
# determine the length of the sample
n = len(scores.index)

# number of samples, n, required to satisfy confidence interval of 90% using z = 1.645
#find the population mean
c = scores.loc[:, ["score1", "score2"]].sum()
mean = (c.sum()/n)

# find the population standard deviation of combined runs per game
# create new column for sum of each game, call std deviation on that col
scores['total'] = scores.loc[:, ["score1", "score2"]].sum(axis=1)
stdDev = scores['total'].std()

# sample size for quantitative variable
samples = (1.645 * stdDev / 0.5) ** 2
print("the number of games required to say with 90% confidence that the sample will be within a 1/2 run of the all-time average is " + OKGREEN + format(round(samples, 0)) + ENDCOL)


#margin of error
# me = 1.645 * (stdDev / sqrt(n))
# print('margin of error: ' + OKGREEN + format(me) + ENDCOL)