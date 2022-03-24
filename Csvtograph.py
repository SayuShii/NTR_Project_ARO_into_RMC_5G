# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:01:34 2022

@author: Pierre
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("1_cell_MAX_SNR_percentage_ur_used_of_cell_number_1.csv")
df[['epoch', 'acc', 'val_acc']].plot(
    x='epoch',
    xlabel='x',
    ylabel='y',
    title='Accuracy VS Val_acc'
)

plt.show()