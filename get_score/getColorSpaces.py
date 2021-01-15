# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:51:42 2020

@author: lenovo
"""
import math
import numpy as np

from scipy import interpolate

from utils import rgbhsv, rgblab


def getColorSpaces(rgb,hueMapping):
    
    labs = [];
    # print(rgb);
    for i in range(5):
        
        rgb1 = rgb[:,i];
        lab1 = rgblab.rgb2lab(rgb1);
        labs.append(lab1);
    # print(labs)
    lab = labs;
    '''[lab[1,:],lab[2,:],lab(3,:)] = rgblab.rgb2lab(np.array([rgb[1,:],rgb[2,:],rgb[3,:]));'''
    a = np.array([100 ,128 ,128]);
    lab = lab/(np.tile(a,(len(lab),1)));
    
    # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    # print(lab);
    hsvs = [];
    r,g,b = rgb[0,0] ,rgb[1,0] , rgb[2,0];
    hsv = rgbhsv.rgb2hsv(r,g,b);
    hsv = np.array(hsv);
    hsvs.append(hsv);
    r,g,b = rgb[0,1] ,rgb[1,1] , rgb[2,1];
    hsv = rgbhsv.rgb2hsv(r,g,b);
    hsv = np.array(hsv);
    hsvs.append(hsv);
    r,g,b = rgb[0,2] ,rgb[1,2] , rgb[2,2];
    hsv = rgbhsv.rgb2hsv(r,g,b);
    hsv = np.array(hsv);
    hsvs.append(hsv);
    r,g,b = rgb[0,3] ,rgb[1,3] , rgb[2,3];
    hsv = rgbhsv.rgb2hsv(r,g,b);
    hsv = np.array(hsv);
    hsvs.append(hsv);
    r,g,b = rgb[0,4] ,rgb[1,4] , rgb[2,4];
    hsv = rgbhsv.rgb2hsv(r,g,b);
    hsv = np.array(hsv);
    hsvs.append(hsv);

    hsv = np.array(hsvs)

    hsv = hsv;
    hsvRemap=hsv/255;
    hsvRemap = np.transpose(hsvRemap)

    hsvRemap[0,:] = interpolate.splev(hsvRemap[0,:], hueMapping)
    
    # print('----------------')
    
    '''
    hsvRemap[1,:]= ppval(hueMapping,hsvRemap[1,:]);
    '''
    #print(hsvRemap)
    hsvRemap = np.array(hsvRemap);
    #print(hsvRemap[:,2])
    #math.sin(math.radians(90))
    #print(360*hsvRemap[:,1])
    one = 360*hsvRemap[0,:];

    two = 360*hsvRemap[1,:];
    three = 360*hsvRemap[2,:];
    x = []
    y = []
    z = []
    for i in range(5):
        use = math.radians(one[i])
        xs = math.cos(use)
        x.append(xs)
    for i in range(5):
        use = math.radians(one[i])
        ys = math.sin(use)
        y.append(ys)
    for i in range(5):
        use = math.radians(three[i])
        zs = math.cos(use)
        z.append(zs)

    chsv = [[hsvRemap[1,:]* x ],
            [ -(hsvRemap[1,:]* y)],
            [ hsvRemap[2,:]]];
    
    chsv = np.array(chsv);

    # print('---------hsv------')
    return hsv ,lab ,chsv ;
    