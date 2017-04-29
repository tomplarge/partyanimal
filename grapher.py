
'''
sns.set(style="darkgrid")

# Load the long-form example gammas dataset
gammas = sns.load_dataset("gammas")

# Plot the response with standard error
sns.tsplot(data=gammas, time="timepoint", unit="subject",
           condition="ROI", value="BOLD signal")
'''

import numpy as np;
import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt
