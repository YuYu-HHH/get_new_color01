# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:13:08 2020

@author: lenovo
"""
import numpy as np

def createFeatureMatrix(datapointObj,selectedFeature,scaleFeatures):
    features=[];
    if selectedFeature[0] == '*':

        name = ['chsvCol'	,'chsvSortedCol',	'chsvDiff'	,'chsvSortedDiff'	,'chsvMean'	,'chsvStdDev',	
                'chsvMedian'	'chsvMax'	'chsvMin',	'chsvMaxMinDiff'	,'chsvPlane',	
                'labCol'	
                ,'labSortedCol',	'labDiff',	'labSortedDiff'	,'labMean'	'labStdDev'	'labMedian'	
                'labMax'	'labMin'	'labMaxMinDiff'	'labPlane'	'hsvCol'	'hsvSortedCol'	
                'hsvDiff'	'hsvSortedDiff'	'hsvMean'	'hsvStdDev'	'hsvMedian'	'hsvMax'	
                'hsvMin'	'hsvMaxMinDiff'	'hsvHueProb'	
                
                'rgbCol'	'rgbSortedCol'	'rgbDiff'	
                'rgbSortedDiff',	'rgbMean'	,'rgbStdDev',	'rgbMedian'	,'rgbMax',	'rgbMin'
                ,'rgbMaxMinDiff'	,'rgbPlane']

        for i in range(len(datapointObj.allFeatures.chsvCol[0])):
            features.append(datapointObj.allFeatures.chsvCol[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvSortedCol[0])):
            features.append(datapointObj.allFeatures.chsvSortedCol[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvDiff[0])):
            features.append(datapointObj.allFeatures.chsvDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvSortedDiff[0])):
            features.append(datapointObj.allFeatures.chsvSortedDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvMean[0])):
            features.append(datapointObj.allFeatures.chsvMean[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvStdDev[0])):
            features.append(datapointObj.allFeatures.chsvStdDev[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvMedian[0])):
            features.append(datapointObj.allFeatures.chsvMedian[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvMax[0])):
            features.append(datapointObj.allFeatures.chsvMax[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvMin[0])):
            features.append(datapointObj.allFeatures.chsvMin[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvMaxMinDiff[0])):
            features.append(datapointObj.allFeatures.chsvMaxMinDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.chsvPlane[0])):
            features.append(datapointObj.allFeatures.chsvPlane[0][i]);

        for i in range(len(datapointObj.allFeatures.labCol[0])):
            features.append(datapointObj.allFeatures.labCol[0][i]);

        for i in range(len(datapointObj.allFeatures.labSortedCol[0])):
            features.append(datapointObj.allFeatures.labSortedCol[0][i]);

        for i in range(len(datapointObj.allFeatures.labDiff[0])):
            features.append(datapointObj.allFeatures.labDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.labSortedDiff1[0])):
            features.append(datapointObj.allFeatures.labSortedDiff1[0][i]);

        for i in range(len(datapointObj.allFeatures.labMean[0])):
            features.append(datapointObj.allFeatures.labMean[0][i]);

        for i in range(len(datapointObj.allFeatures.labStdDev[0])):
            features.append(datapointObj.allFeatures.labStdDev[0][i]);

        for i in range(len(datapointObj.allFeatures.labMedian[0])):
            features.append(datapointObj.allFeatures.labMedian[0][i]);

        for i in range(len(datapointObj.allFeatures.labMax[0])):
            features.append(datapointObj.allFeatures.labMax[0][i]);

        for i in range(len(datapointObj.allFeatures.labMin[0])):
            features.append(datapointObj.allFeatures.labMin[0][i]);

        for i in range(len(datapointObj.allFeatures.labMaxMinDiff[0])):
            features.append(datapointObj.allFeatures.labMaxMinDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.labPlane[0])):
            features.append(datapointObj.allFeatures.labPlane[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvCol[0])):
            features.append(datapointObj.allFeatures.hsvCol[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvSortedCol[0])):
            features.append(datapointObj.allFeatures.hsvSortedCol[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvDiff[0])):
            features.append(datapointObj.allFeatures.hsvDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvSortedDiff[0])):
            features.append(datapointObj.allFeatures.hsvSortedDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvMean[0])):
            features.append(datapointObj.allFeatures.hsvMean[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvStdDev[0])):
            features.append(datapointObj.allFeatures.hsvStdDev[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvMedian[0])):
            features.append(datapointObj.allFeatures.hsvMedian[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvMax[0])):
            features.append(datapointObj.allFeatures.hsvMax[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvMin[0])):
            features.append(datapointObj.allFeatures.hsvMin[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvMaxMinDiff[0])):
            features.append(datapointObj.allFeatures.hsvMaxMinDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.hsvHueProb[0])):
            features.append(datapointObj.allFeatures.hsvHueProb[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbCol[0])):
            features.append(datapointObj.allFeatures.rgbCol[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbSortedCol[0])):
            features.append(datapointObj.allFeatures.rgbSortedCol[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbDiff[0])):
            features.append(datapointObj.allFeatures.rgbDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbSortedDiff[0])):
            features.append(datapointObj.allFeatures.rgbSortedDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbMean[0])):
            features.append(datapointObj.allFeatures.rgbMean[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbStdDev[0])):
            features.append(datapointObj.allFeatures.rgbStdDev[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbMedian[0])):
            features.append(datapointObj.allFeatures.rgbMedian[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbMax[0])):
            features.append(datapointObj.allFeatures.rgbMax[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbMin[0])):
            features.append(datapointObj.allFeatures.rgbMin[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbMaxMinDiff[0])):
            features.append(datapointObj.allFeatures.rgbMaxMinDiff[0][i]);

        for i in range(len(datapointObj.allFeatures.rgbPlane[0])):
            features.append(datapointObj.allFeatures.rgbPlane[0][i]);



        features = np.array(features);
        


    offsets = np.array([  -9.9988655e-01 , -9.9999221e-01 ,  0.0000000e+00  ,-9.9999962e-01 , -9.9999998e-01,   0.0000000e+00 , -9.9999670e-01,  -9.9999955e-01 ,  0.0000000e+00 , -9.9999894e-01 , -9.9999653e-01 ,  0.0000000e+00  ,-9.9998517e-01,  -9.9999221e-01 ,  0.0000000e+00 , -9.9999670e-01, -9.9992919e-01   ,0.0000000e+00  ,-9.9999894e-01  ,-9.9999998e-01 ,  0.0000000e+00 , -9.9988655e-01 , -9.9999697e-01 ,  0.0000000e+00 , -9.9999962e-01 , -9.9999653e-01  , 0.0000000e+00,  -9.9995143e-01 , -9.9999955e-01 ,  0.0000000e+00 , -1.9999996e+00, -1.9718453e+00  ,-1.9999989e+00,  -1.9998865e+00  ,-1.9075773e+00 , -1.9134392e+00  ,-1.7094300e+00 , -1.9639744e+00 , -1.0000000e+00  ,-1.0000000e+00  ,-1.0000000e+00 , -1.0000000e+00  ,-4.8018817e-01 , -8.8929213e-01  ,-1.9999989e+00,  -1.9999996e+00 , -3.1873333e-01,  -8.5679292e-01 , -1.6721540e+00  ,-1.9639744e+00  ,-2.0784314e-01 , -3.8039216e-01,  -1.0000000e+00 , -1.0000000e+00 , -9.6566712e-01 , -9.9917772e-01 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 , -9.7493516e-01, -9.9988248e-01,   0.0000000e+00 , -9.0317507e-01 , -9.9702137e-01 ,  0.0000000e+00 , -9.9999962e-01 , -9.9999998e-01 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  ,-1.0000000e+00 , -1.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 , -6.4214904e-01,  -8.4266990e-01 ,  0.0000000e+00 , -6.7329107e-01 , -8.4266990e-01 ,  0.0000000e+00 , -6.3275385e-01 , -8.4266990e-01 ,  0.0000000e+00 , -6.7329107e-01 , -8.4266990e-01,   0.0000000e+00,  -6.7329107e-01  ,-8.2235664e-01,   0.0000000e+00 , -6.3366543e-01,  -8.4266990e-01 ,  0.0000000e+00 , -6.3633909e-01 , -7.1335742e-01  , 0.0000000e+00 , -6.7329107e-01  ,-6.2316344e-01 ,  0.0000000e+00 , -6.7329107e-01  ,-5.0013609e-01  , 0.0000000e+00 , -6.7329107e-01 , -4.5252764e-01 , -1.0000000e+00 , -1.0000000e+00  ,-1.0000000e+00 , -1.0000000e+00 , -1.2919395e+00 , -1.2405553e+00 , -1.2919395e+00 , -1.4407532e+00 , -1.2589677e+00 , -1.5801098e+00 , -1.3593092e+00 , -1.3154104e+00 , -1.7004875e-01 , -3.5063394e-01 , -9.9246644e-01 , -1.0000000e+00 , -1.7908065e-01 , -5.2760818e-01 , -1.0692000e+00 , -1.4407532e+00  ,-1.7629508e-01 , -3.7339797e-01,  -8.8406312e-01  ,-1.5801098e+00  , 0.0000000e+00 , -4.8462769e-01 , -6.1757170e-01  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 , -5.0860788e-01 , -6.2316344e-01 ,  0.0000000e+00 , -3.8959114e-01 , -4.5252764e-01  , 0.0000000e+00 , -6.7329107e-01,  -8.4266990e-01 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  ,-9.9998636e-01,  -9.9992340e-01  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 , -1.0000000e+00,  -1.0000000e+00,  -1.0000000e+00,  -1.0000000e+00 , -1.0000000e+00,  -1.0000000e+00,  -1.0000000e+00 , -1.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 , -2.1875000e-01 , -5.0000000e-01  ,-1.0000000e+00 , -1.0000000e+00  ,-2.0784314e-01 , -3.8039216e-01 , -1.0000000e+00  ,-1.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00,   0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00,   0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00   ,0.0000000e+00 ,  0.0000000e+00   ,0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 , -3.1561453e+00 ,  0.0000000e+00  ,-3.2537814e+00 , -3.1561453e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00   ,0.0000000e+00 , -1.2426266e+01  , 0.0000000e+00 , -1.3798116e+01 , -1.2133712e+01 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 , -1.3815511e+01  , 0.0000000e+00 , -1.3815511e+01  ,-1.3815511e+01 ,  4.6006526e+00   ,0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00,   0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00,   0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00,   0.0000000e+00,   0.0000000e+00,   0.0000000e+00,   0.0000000e+00,  -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -1.0000000e+00 , -2.3137255e-01 , -4.4705882e-01 , -1.0000000e+00 , -1.0000000e+00  ,-2.3921569e-01 , -4.8235294e-01 , -1.0000000e+00 , -1.0000000e+00 , -2.4705882e-01 , -4.9019608e-01 , -1.0000000e+00 , -1.0000000e+00 ,  0.0000000e+00   ,0.0000000e+00   ,0.0000000e+00   ,0.0000000e+00   ,0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00 ,  0.0000000e+00  , 0.0000000e+00  , 0.0000000e+00,  -1.0000000e+00 , -9.9998698e-01  , 0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00 ,  0.0000000e+00]);
    scales = np.array([   1.9998865e+00  , 1.9998465e+00 ,  1.0000000e+00  , 1.9999996e+00  , 1.9998735e+00  , 1.0000000e+00 ,  1.9999967e+00  , 1.9999771e+00  , 1.0000000e+00 ,  1.9999989e+00 ,  1.9999761e+00 ,  1.0000000e+00  , 1.9999852e+00 ,  1.9999892e+00  , 1.0000000e+00 ,  1.9999967e+00 ,  1.9999261e+00  , 1.0000000e+00  , 1.9999989e+00  , 1.9999969e+00  , 1.0000000e+00  , 1.9998865e+00  , 1.9999766e+00,   1.0000000e+00  , 1.9999996e+00  , 1.9999024e+00   ,1.0000000e+00  , 1.9999514e+00   ,1.9999771e+00   ,1.0000000e+00  , 3.9885490e+00  , 3.9718449e+00 ,  3.9820820e+00 ,  3.9665811e+00   ,3.6695341e+00  , 3.9132132e+00  , 3.6403890e+00   ,3.9057797e+00 ,  2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00  , 2.0000000e+00,   2.4801878e+00   ,2.7464257e+00  , 2.7309932e+00  , 2.2867271e+00 ,  2.3185073e+00,   2.5289470e+00  , 2.5784088e+00 ,  2.3099827e+00  , 1.2078431e+00  , 1.3803922e+00 ,  1.3686275e+00 ,  1.2000000e+00  , 1.9656671e+00 ,  1.9980132e+00,   1.0000000e+00  , 1.0782885e+00  , 9.9691484e-01  , 5.4772256e-01   ,1.9749352e+00  , 1.9997388e+00 ,  1.0000000e+00 ,  1.9031751e+00  , 1.9970183e+00  , 1.0000000e+00 ,  1.9999996e+00 ,  1.9988354e+00  , 1.0000000e+00 ,  1.9999996e+00 , 1.9997740e+00 ,  1.0000000e+00 ,  1.0000000e+00 ,  2.0000000e+00  , 2.0000000e+00   ,1.0000000e+00 ,  4.9335677e-01  , 2.5973103e-01 ,  8.2015616e-01  , 1.0000000e+00 ,  1.4096112e+00  , 1.5807619e+00  , 1.0000000e+00 ,  1.4256409e+00   ,1.5807619e+00  , 1.0000000e+00  , 1.3981040e+00 ,  1.5807619e+00 ,  1.0000000e+00  , 1.4407532e+00  , 1.5807619e+00 ,  1.0000000e+00 ,  1.4407532e+00  , 1.5604487e+00  , 1.0000000e+00,   1.4011275e+00   ,1.4633193e+00  , 1.0000000e+00  , 1.4038012e+00 ,  1.3751333e+00  , 1.0000000e+00  , 1.4396985e+00  , 1.3073201e+00  , 1.0000000e+00 ,  1.4157853e+00  , 1.2177109e+00 ,  1.0000000e+00 ,  1.4340337e+00 ,  1.1906197e+00  , 2.0000000e+00  , 2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00  , 2.4192110e+00  , 2.5323105e+00 ,  2.4165282e+00  , 2.7397799e+00  , 2.7514617e+00 ,  2.9477917e+00,   2.8518032e+00 ,  2.6374583e+00  , 1.1700488e+00 ,  1.3450969e+00  , 1.3559311e+00 ,  1.1388275e+00 ,  1.4781074e+00 ,  1.4679126e+00  , 1.6246246e+00  , 1.6450216e+00 ,  1.6687890e+00 ,  1.5860370e+00 ,  1.3958501e+00 ,  1.7704266e+00  , 1.0000000e+00 ,  1.2102458e+00 ,  1.2957054e+00  , 5.4526974e-01 ,  6.6138415e-01 ,  7.2577018e-01  , 1.0000000e+00  , 1.2444336e+00  , 1.3073201e+00  , 1.0000000e+00   ,1.1570533e+00 ,  1.1906197e+00 ,  1.0000000e+00 ,  1.3578533e+00  , 1.4633193e+00 ,  1.0000000e+00 ,  1.4407532e+00  , 1.5801098e+00  , 9.9988492e-01  , 1.9999864e+00 ,  1.9999234e+00 ,  1.0000000e+00  , 4.9390396e-01 ,  2.5720969e-01 ,  3.9923633e-01 ,  9.9891775e-01 ,  1.0000000e+00 ,  1.0000000e+00  , 9.9927220e-01  , 1.0000000e+00 ,  1.0000000e+00 ,  9.9859944e-01  , 1.0000000e+00  , 1.0000000e+00  , 9.9894515e-01 ,  1.0000000e+00  , 1.0000000e+00 ,  9.9912740e-01  , 1.0000000e+00  , 1.0000000e+00  , 9.9927220e-01 ,  1.0000000e+00 ,  1.0000000e+00  , 9.9912740e-01 ,  1.0000000e+00  , 1.0000000e+00  , 9.9894515e-01 ,  1.0000000e+00  , 1.0000000e+00  , 9.9920635e-01 ,  1.0000000e+00  , 1.0000000e+00  , 9.9874687e-01  , 1.0000000e+00  , 1.0000000e+00  , 5.0000000e-01 ,  5.0000000e-01 ,  5.0000000e-01  , 5.0000000e-01  , 2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00,   2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00   ,5.0000000e-01  , 4.9807489e-01 ,  4.8148148e-01  , 4.7849462e-01  , 1.2187500e+00  , 1.5000000e+00  , 1.4784314e+00  , 1.2031319e+00 ,  1.2078431e+00  , 1.3803922e+00 ,  1.3686275e+00  , 1.2000000e+00,   9.9362084e-01  , 1.0000000e+00  , 1.0000000e+00,   5.4534429e-01 ,  5.4772256e-01  , 5.4772256e-01,   9.9362477e-01  , 1.0000000e+00 ,  1.0000000e+00 ,  9.9927220e-01  , 1.0000000e+00  , 1.0000000e+00 ,  9.9358974e-01 ,  1.0000000e+00  , 1.0000000e+00  , 9.9912740e-01  , 1.0000000e+00 ,  1.0000000e+00  , 2.4731098e+00  , 1.6654120e+00 ,  2.4731098e+00 ,  2.4731098e+00  , 4.0616221e+00  , 2.2488050e+00 ,  4.1592582e+00 ,  4.0616221e+00 ,  6.1951615e-04 ,  3.5110887e-04  , 6.1951615e-04 ,  6.1951615e-04 ,  1.2426266e+01  , 2.2652631e+00  , 1.3798116e+01 ,  1.2133712e+01   ,3.0288922e-03 ,  2.1391370e-03 ,  3.0288922e-03 ,  3.0288922e-03 ,  1.3815511e+01  , 4.5747341e+00 ,  1.3815511e+01  , 1.3815511e+01,  1.2993474e+00  , 1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00 ,  1.0000000e+00 ,  1.0000000e+00 ,  1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00 ,  1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00 ,  1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00 ,  1.0000000e+00   ,1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00 ,  1.0000000e+00 ,  1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00,   1.0000000e+00 ,  1.0000000e+00,   1.0000000e+00,   1.0000000e+00,   2.0000000e+00,   2.0000000e+00 ,  2.0000000e+00  , 2.0000000e+00 ,  2.0000000e+00  , 2.0000000e+00 ,  2.0000000e+00  , 2.0000000e+00  , 2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00 ,  2.0000000e+00 ,  1.2313725e+00 ,  1.4470588e+00  , 1.4470588e+00 ,  1.2196078e+00  , 1.2392157e+00 ,  1.4823529e+00 ,  1.4745098e+00 ,  1.2274510e+00  , 1.2470588e+00 ,  1.4901961e+00 ,  1.4862745e+00 ,  1.2000000e+00 ,  1.0000000e+00   ,1.0000000e+00   ,1.0000000e+00   ,5.4772256e-01   ,5.4772256e-01 ,  5.4772256e-01  , 1.0000000e+00 ,  1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00  , 1.0000000e+00 ,  1.0000000e+00  , 1.0000000e+00 ,  1.0000000e+00 ,  1.0000000e+00 ,  1.0000000e+00 ,  1.0000000e+00 ,  1.0000000e+00  , 1.0000000e+00 ,  2.0000000e+00  , 1.9999870e+00 ,  1.0000000e+00 ,  4.8924357e-01 ,  2.4411439e-01  , 6.9839780e-01]);

    if scaleFeatures:
        
        size = features.shape[0];

        for i in range(size):

            features[i] = features[i] - offsets[i];
            features[i] = features[i]/scales[i];

    return features;
