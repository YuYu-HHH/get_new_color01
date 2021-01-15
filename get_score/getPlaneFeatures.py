# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:03:07 2020

@author: lenovo
"""
import numpy as np

from get_score import pca2


def getPlaneFeatures(X):
    
    
    signals,coeff,roots = pca2.pca2(X);
    X = np.transpose(X);
    normal = coeff[:,2];
    
    if normal[0]<0:
        normal = normal*-1;
    
    if sum(roots) == 0:
        pctExplained = np.array([0 ,0 ,0]);
    else:
        pctExplained = roots/ sum(roots);
        
    [n,p] = X.shape;
    meanX = np.mean(X,0);
    
    
    aaa = np.tile(meanX,(n,1));
    
    a = X -np.tile(meanX,(n,1))
    
    error = abs(np.dot(a,normal));
    sse = sum(error**2);
    
    return normal ,pctExplained ,meanX ,sse;
    