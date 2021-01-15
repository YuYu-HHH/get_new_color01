# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:06:33 2020

@author: lenovo
"""
import numpy as  np
import math
from numpy import linalg as la

def pca2(data):
    
    [M,N] = data.shape;
    
    mn = [];
    for i in range(3):
        nmn = data[i];
        mn.append([np.mean(nmn)]);
    mn = np.array(mn);

    data = data - np.tile(mn,(1,N));
    data = np.transpose(data)
    Y = data/ math.sqrt(N-1);
    
    [u,S,PC] = la.svd(Y);

    V = S * S;
    PC = np.transpose(PC)
    data = np.transpose(data)
    
    signals = np.dot(PC,data);
    #signals = PC * data;
    
    return signals,PC,V;