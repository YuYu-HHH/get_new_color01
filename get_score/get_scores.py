# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 22:46:18 2020

@author: lenovo
"""

import numpy as np

from get_score import createFeatures, createFeatureMatrix


class Datapoints():
    def __init__(self):
        self.rgb = [];
        self.lab = [];
        self.allFeatures = [];
        
def get_score(color):
    maxDatapoints = 50000;

    allFeatures,numThemes,rgbs,labs = createFeatures.createFeatures(color);

    datapoints = Datapoints();
    datapoints.rgb = rgbs;
    datapoints.lab = labs;
    datapoints.allFeatures=allFeatures;

    features=createFeatureMatrix.createFeatureMatrix(datapoints,['*'],1);

    weight = [1.3829, 0	,0	,0,	0,	0	,0	,0.0631	,0	,0	,0.0447	,0	,-0.0096,	0,	0,	0	,-0.0011	,0.052,	0,	0.0644,	0.0863,	0	,0.11,	0.0011	,-0.0308	,0.1072	,-0.0401,	0,	0.0851,	-0.0692,	0,	0	,0.02,	0	,0	,0.0425	,-0.0488,	0.0263,	-0.0666,	-0.0189,	0,	0,	0.003,	-0.1537	,0.0707	,-0.0076,	0.1888,	-0.0666,	-0.016,	0,	0.0689	,-0.1108,	0,	-0.0151,	0.0097,	0	,0,	0	,0	,-0.2103	,-0.7016,	0.1969,	0.0246	,-0.0151,	-0.0244	,0,	0,	0	,-0.0713,	0	,0	,0.017,	0.2601,	0.02,	-0.0256	,0.0096	,0	,0.0167,	-0.0025,	0.0017	,0	,0	,0.0583,	0	,-0.0021,	0	,0.0353	,-0.295,	-0.0105	,0.2555,	-0.0048	,0,	0.0321,	0	,0	,0.0204	,-0.0778,	0,	0.0231,	0.0421,	-0.1244	,0.0396,	0,	0.0367,	0	,-0.0566	,0.2264	,0.0077	,-0.0428,	0	,0.1971,	0,	0	,0,	0	,0	,0,	0.0393,	0,	-0.1081	,0.0966,	0	,0,0.1369	,0.0062	,0.0551,	0.0965	,0.076	,-0.0016	,-0.201,	0,	0.0106	,-0.1023,	-0.0077	,2.1472,	0,	0,	-0.4775	,-0.3121	,-0.278,	-0.0088,	-0.2247,	0	,0.852,	-0.0145,	0,	0,	0,	-0.1562	,0,	0	,0	,-0.0009,	0.0015,	-0.0164,	-0.0082	,0.0309	,-0.0097,	-0.0182	,0.0166,	0	,0	,-0.0088,	0,	-0.0004	,-0.0132,	0.0059,	0	,0	,0.0115	,0	,0.0102,	0	,0	,0.0478,	0.085	,-0.4671	,-0.0054,	0.076	,-0.5252	,0.0118,	0.0607	,-0.1337	,-0.0159	,0	,0,	0.0028,	-0.0486,	0	,0.0029,	0	,-0.0031	,-0.0064,	0.013	,0,	0,	0	,0	,0,	0,	0,	-0.0455	,-0.0024,	0.0496	,0.0639,	-0.0276	,0.0315,	0.0132,	0.0445,	-0.0434	,0.0002,	0,	0.0181,	0	,0	,0	,0	,0	,-0.4384	,0,	0.0398	,0,	-0.0019,	-0.0322	,0	,0,	0,	0	,-0.0625	,-0.0006,	0.258,	0.1077,	-0.2337,	-0.3576,	0.1626,	0	,-0.1014	,0	,0	,0.539,	-0.2323,	-0.6451	,0.0102,	0,	-0.0995	,-0.0321	,0.3901,	0	,-0.395,	-0.0159,	0.2506,	0	,-0.3185,	-0.6885	,0.6108,	-0.3838	,-0.0444	,0	, 0.0579,	0	,0	,0	,0,	0	,0,	-0.0727	,-0.0168,	0	,-0.0452	,0,	0.0486	,-0.0123,	-0.069,	0	,0	,-0.0709,	0.0358,	0,	-0.0449,	0.085,	0.0274,	-0.0171	,0.1458,	-0.0119	,0	,0.0052	,0.0008	,0,	-0.0152	,0	,0,	0	,-0.0072,	0	,-0.0143,	0,	0,	0	,0	,0.0121	,-0.0714,	0	,-0.0637,	0.0442,	-0.1012	,0.0445	,-0.0115,	0.0039	,-0.0169	,0.0108	,-0.1424	,-0.3017,	0.0327	,-0.0653	,-0.2185	,-0.4257	,0.0272	,0	,0.072	,0.0047	,0	,0.236,	0,	-0.337	,0,	0.109	,0.254,	0.1119	,-0.0282	,-0.0001	,0.0255	,0	,-0.0396,	0.0616,	0.2235];
    weight = np.array(weight);

    feature = [];
    feature.append(1);
    for i in range(len(features)):
        feature.append(features[i])

    features = np.array(feature);
    featuresT = features.T

    score = np.dot(weight,featuresT);
    
    return score;

