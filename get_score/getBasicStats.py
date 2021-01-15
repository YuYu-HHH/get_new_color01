# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:39:59 2020

@author: lenovo
"""
import numpy as np
import math

def getBasicStats(x,addLog):
    x = np.array(x);
    
    if len(x)>0:

        log_x = [];
        for i in range(len(x)):
            log_x.append(math.log(x[i]+0.000001));
        log_x = log_x;
        mean1 = np.mean(x);
        dtd1 = np.std(x,ddof = 1);
        min1 = min(x);
        max1 = max(x);
        mean2 = np.mean(log_x);
        std2 = np.std(log_x,ddof = 1);
        min2 = min(log_x);
        max2 = max(log_x);
        features = np.array([np.mean(x),np.std(x,ddof = 1),min(x)[0],max(x)[0],np.mean(log_x),np.std(log_x,ddof = 1),min(log_x),max(log_x)]);
    else:
        features=np.zeros(8);
    
    #print("---------------")
    #print(features)
    features = np.array(features);
    features[np.isinf(features)]=0;
    features[np.isnan(features)]=0;
    
    return features;
    
def getBasicStats_2(x,addLog):
    x = np.array(x);
    
    if len(x)>0:
        #log_x=math.log(x+0.000001);
        log_x = [];
        for i in range(len(x)):
            log_x.append(math.log(x[i]+0.000001));
        features = np.array([np.mean(x),np.std(x,ddof = 1),min(x),max(x),np.mean(log_x),np.std(log_x,ddof = 1),min(log_x),max(log_x)]);
    else:
        features=np.zeros(8);

    features = np.array(features);
    features[np.isinf(features)]=0;
    features[np.isnan(features)]=0;
    
    return features;
        