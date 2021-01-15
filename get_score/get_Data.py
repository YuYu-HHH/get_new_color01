# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:14:50 2020
@author: lenovo
"""

import os
import scipy.io
import numpy as np

def get_KulerX():
    mat_file= './data/KulerX.mat';
    KulerX = scipy.io.loadmat(mat_file);
    x = KulerX['x'];
    return x;
 
def get_HueProb():
    mat_file= './data/hueProbsRGB.mat';
    KulerX = scipy.io.loadmat(mat_file);
    x = KulerX['hueProbs']
    y = x[0,0]['hueProb']
    
    return y;

def get_HueJoint():
    mat_file= './data/hueProbsRGB.mat';
    KulerX = scipy.io.loadmat(mat_file);
    x = KulerX['hueProbs']
    y = x[0,0]['hueJoint']
    #print(np.array(y))
    #print(y.shape)
    return y;

def get_HueAdjacency():
    mat_file= './data/hueProbsRGB.mat';
    KulerX = scipy.io.loadmat(mat_file);
    x = KulerX['hueProbs']
    y = x[0,0]['hueAdjacency']
    
    return y;

def get_HueSaturation():
    mat_file= './data/hueProbsRGB.mat';
    KulerX = scipy.io.loadmat(mat_file);
    x = KulerX['hueProbs']
    y = x[0,0]['hueSaturation']
    
    return y;