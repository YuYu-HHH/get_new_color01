
import numpy as np
from scipy import interpolate
import numpy as np

from get_score import get_Data, getHueProbFeatures, getColorSpaces, getPlaneFeatures


class allFeatures():
    def __init__(self):
        self.chsvCol = [];
        self.chsvSortedCol = [];
        self.chsvDiff = [];
        self.chsvSortedDiff = [];
        self.chsvMean = [];
        self.chsvStdDev = [];
        self.chsvMedian = [];
        self.chsvMax = [];
        self.chsvMin = [];
        self.chsvMaxMinDiff = [];
        self.chsvPlane = [];

        self.labCol = [];
        self.labSortedCol = [];
        self.labDiff = [];
        self.labSortedDiff1 = [];
        self.labMean = [];
        self.labStdDev = [];
        self.labMedian = [];
        self.labMax = [];
        self.labMin = [];
        self.labMaxMinDiff = [];
        self.labPlane = [];

        self.hsvCol = [];
        self.hsvSortedCol = [];
        self.hsvDiff = [];
        self.hsvSortedDiff = [];
        self.hsvMean = [];
        self.hsvStdDev = [];
        self.hsvMedian = [];
        self.hsvMax = [];
        self.hsvMin = [];
        self.hsvMaxMinDiff = [];
        self.hsvHueProb = [];

        self.rgbCol = [];
        self.rgbSortedCol = [];
        self.rgbDiff = [];
        self.rgbSortedDiff = [];
        self.rgbMean = [];
        self.rgbStdDev = [];
        self.rgbMedian = [];
        self.rgbMax = [];
        self.rgbMin = [];
        self.rgbMaxMinDiff = [];
        self.rgbPlane = [];

        self.resultchsv = [];
        self.resultrgb = [];
        self.resulthsv = [];
        self.resultlab = [];
allFeatures = allFeatures();
featureNames = [];


def createFeatures(data):
    np.seterr(invalid='ignore')
    use2 = 0;
    x = get_Data.get_KulerX();
    hueProbs = get_Data.get_HueProb();
    y = [];
    u = [];
    for i in range(0, 361):
        i = i / 360;
        u.append(i);
    y.append(u);

    y = np.array(y);
    y = y.T;
    x = x.T;
    x.sort();
    x = x.T;

    tck = interpolate.splrep(x, y)
    mapping = tck;

    numThemes = 1;
    num1 = 15;
    num2 = 12;
    num3 = 3;
    labs = np.zeros([numThemes, num1]);
    color = np.zeros([numThemes, num1]);
    #sortedCol = np.zeros([numThemes, num1]);
    sortedColchsv = np.zeros([numThemes, num1]);
    sortedColhsv = np.zeros([numThemes, num1]);
    sortedColrgb = np.zeros([numThemes, num1]);
    sortedCollab = np.zeros([numThemes, num1]);

    diff = np.zeros([numThemes, num2]);
    sortedDiffchsv = np.zeros([numThemes, num2]);
    sortedDifflab = np.zeros([numThemes, num2]);
    sortedDiffhsv = np.zeros([numThemes, num2]);
    sortedDiffrgb = np.zeros([numThemes, num2]);

    meanschsv = np.zeros([numThemes, num3]);
    meanslab = np.zeros([numThemes, num3]);
    meanshsv = np.zeros([numThemes, num3]);
    meansrgb = np.zeros([numThemes, num3]);

    stddevschsv = np.zeros([numThemes, num3]);
    stddevshsv = np.zeros([numThemes, num3]);
    stddevsrgb = np.zeros([numThemes, num3]);
    stddevslab = np.zeros([numThemes, num3]);

    medianschsv = np.zeros([numThemes, num3]);
    medianshsv = np.zeros([numThemes, num3]);
    mediansrgb = np.zeros([numThemes, num3]);
    medianslab = np.zeros([numThemes, num3]);

    minschsv = np.zeros([numThemes, num3]);
    minshsv = np.zeros([numThemes, num3]);
    minsrgb = np.zeros([numThemes, num3]);
    minslab = np.zeros([numThemes, num3]);

    maxschsv = np.zeros([numThemes, num3]);
    maxshsv = np.zeros([numThemes, num3]);
    maxsrgb = np.zeros([numThemes, num3]);
    maxslab = np.zeros([numThemes, num3]);

    maxMinDiffchsv = np.zeros([numThemes, num3]);
    maxMinDiffhsv = np.zeros([numThemes, num3]);
    maxMinDiffrgb = np.zeros([numThemes, num3]);
    maxMinDifflab = np.zeros([numThemes, num3]);

    planechsv = np.zeros([numThemes, 7]);
    planelab = np.zeros([numThemes, 7]);
    planergb = np.zeros([numThemes, 7]);
    planelab = np.zeros([numThemes, 7]);

    satValThresh = 0.2;

    rand35 = np.random.rand(3, 5)
    hueFeatures = getHueProbFeatures.getHueProbFeatures(rand35, satValThresh, hueProbs);

    hueProbFeatures = -99 * np.ones([numThemes, len(hueFeatures)]);

    for c in range(1,5):
        if c == 1:
            name = 'chsv';
        else:
            if c == 2:
                name = 'lab';
            else:
                if c == 3:
                    name = 'rgb';
                else:
                    if c == 4:
                        name = 'hsv';

        for i in range(1):

            rgb = data;
            rgb = np.array(rgb);
            numColors = 5;
            rgb = rgb[:, 0:numColors];
            # rgbs[i,1:(3*numColors)]=rgb;
            hsv, lab, chsv = getColorSpaces.getColorSpaces(rgb, mapping);
            lab = np.transpose(lab);
            # print(lab);
            hsv = np.array(hsv)
            hsv = np.transpose(hsv)
            # chsv = chsv / 255;

            # lab = lab/255;
            hsv = hsv / 255;

            rgb = rgb / 255;
            # labs[i,0:(3*numColors)]=lab;
            labs = lab.reshape(1, 15);
            chsvs = []
            for o in range(3):
                chsvs.append(chsv[o][0])
            chsv = np.array(chsvs);

            if name == 'chsv':
                col = chsv;
            if name == 'lab':
                col = lab;
            if name == 'rgb':
                col = rgb;
            if name == 'hsv':
                col = hsv;
            color = col.reshape((1, 15), order='F');
            if name == 'hsv':
                hueProbFeatures[i] = getHueProbFeatures.getHueProbFeatures(hsv, satValThresh, hueProbs);

            diffs = np.zeros([3, numColors - 1]);

            for j in range(1,5):
                if name == 'hsv':
                    hsv1 = [hsv[1, j - 1:j+1]];
                    hsv2 = [hsv[2, j - 1:j+1]];
                    hsv_use = [];
                    for k in range(len(hsv1)):
                        hsv_use.append(hsv1[k]);
                    for k in range(len(hsv2)):
                        hsv_use.append(hsv2[k])
                    hsv_use = np.array(hsv_use);
                    hsv_use = hsv_use.reshape(1,4);
                    minSatVal = min(hsv_use[0]);
                    if minSatVal >= satValThresh:
                        pts = sorted([col[0, j], col[0, j - 1]]);
                        pts = np.array(pts);
                        diffs[0, j - 1] = min((pts[1] - pts[0]), (1 - (pts[1] - pts[0])));
                else:
                    diffs[0,j-1]=col[0,j]-col[0,j-1];
                diffs[1, j - 1] = col[1, j] - col[1, j - 1];
                diffs[2, j - 1] = col[2, j] - col[2, j - 1];
            diff2 = np.array([diffs[0, :], diffs[1, :], diffs[2, :]]);
            diff = diff2.reshape(1, 12);
            numDiffs = numColors - 1;

            if name == 'chsv':

                sortedDiffchsv[i, 0:numDiffs] = sorted((diffs[0, :].tolist()), reverse=True);
                sortedDiffchsv[i, (numDiffs):2 * numDiffs] = sorted(diffs[1, :].tolist(), reverse=True);
                sortedDiffchsv[i, (2 * numDiffs):3 * numDiffs] = sorted(diffs[2, :].tolist(), reverse=True);

                col = np.transpose(col);
                mean1 = [np.mean(col[:, 0]), np.mean(col[:, 1]), np.mean(col[:, 2])];
                mean1 = np.array(mean1);
                meanschsv[i, :] = mean1;

                stds = [np.std(col[:, 0], ddof=1), np.std(col[:, 1], ddof=1), np.std(col[:, 2], ddof=1)];
                stddevschsv[i, :] = np.array(stds);

                medianss = [np.median(col[:, 0]), np.median(col[:, 1]), np.median(col[:, 2])];
                medianschsv[i, :] = np.array(medianss);

                min_col = [];
                max_col = [];
                for k in range(3):
                    col_use = col[:, k];
                    a = min(col_use);
                    b = max(col_use);
                    min_col.append(a);
                    max_col.append(b);

                min_col = np.array(min_col);
                max_col = np.array(max_col);

                minschsv[i, :] = min_col;
                maxschsv[i, :] = max_col;

                maxMinDiffchsv[i, :] = maxschsv[i, :] - minschsv[i, :];

                col = np.transpose(col);
                planechsv[i, 0:3], planechsv[i, 3:6], planemean, planechsv[i, 6] = getPlaneFeatures.getPlaneFeatures(col);

                x = col[2, :];
                x = x.tolist();
                B = sorted(x);

                sortIdx = sorted(range(len(x)), key=lambda k: x[k], reverse=False)
                col = col[:, sortIdx];
                col = np.array(col);
                sortedColchsv = col.reshape((1, 15), order='F');

            if name == 'lab':

                sortedDifflab[i, 0:numDiffs] = sorted((diffs[0, :].tolist()), reverse=True);
                sortedDifflab[i, (numDiffs):2 * numDiffs] = sorted(diffs[1, :].tolist(), reverse=True);
                sortedDifflab[i, (2 * numDiffs):3 * numDiffs] = sorted(diffs[2, :].tolist(), reverse=True);

                col = np.transpose(col);
                mean1 = [np.mean(col[:, 0]), np.mean(col[:, 1]), np.mean(col[:, 2])];
                mean1 = np.array(mean1);
                meanslab[i, :] = mean1;

                stds = [np.std(col[:, 0], ddof=1), np.std(col[:, 1], ddof=1), np.std(col[:, 2], ddof=1)];
                stddevslab[i, :] = np.array(stds);

                medianss = [np.median(col[:, 0]), np.median(col[:, 1]), np.median(col[:, 2])];
                medianslab[i, :] = np.array(medianss);

                min_col = [];
                max_col = [];
                for k in range(3):
                    col_use = col[:, k];
                    a = min(col_use);
                    b = max(col_use);
                    min_col.append(a);
                    max_col.append(b);

                min_col = np.array(min_col);
                max_col = np.array(max_col);

                minslab[i, :] = min_col;
                maxslab[i, :] = max_col;

                maxMinDifflab[i, :] = maxslab[i, :] - minslab[i, :];

                col = np.transpose(col);
                planelab[i, 0:3], planelab[i, 3:6], planemean, planelab[i, 6] = getPlaneFeatures.getPlaneFeatures(col);

                x = col[2, :];
                x = x.tolist();
                B = sorted(x);

                sortIdx = sorted(range(len(x)), key=lambda k: x[k], reverse=False)
                col = col[:, sortIdx];
                col = np.array(col);
                sortedCollab = col.reshape((1, 15), order='F');
            if name == 'hsv':

                sortedDiffhsv[i, 0:numDiffs] = sorted((diffs[0, :].tolist()), reverse=True);
                sortedDiffhsv[i, (numDiffs):2 * numDiffs] = sorted(diffs[1, :].tolist(), reverse=True);
                sortedDiffhsv[i, (2 * numDiffs):3 * numDiffs] = sorted(diffs[2, :].tolist(), reverse=True);

                col = np.transpose(col);
                mean1 = [np.mean(col[:, 0]), np.mean(col[:, 1]), np.mean(col[:, 2])];
                mean1 = np.array(mean1);
                meanshsv[i, :] = mean1;

                stds = [np.std(col[:, 0], ddof=1), np.std(col[:, 1], ddof=1), np.std(col[:, 2], ddof=1)];
                stddevshsv[i, :] = np.array(stds);

                medianss = [np.median(col[:, 0]), np.median(col[:, 1]), np.median(col[:, 2])];
                medianshsv[i, :] = np.array(medianss);

                min_col = [];
                max_col = [];
                for k in range(3):
                    col_use = col[:, k];
                    a = min(col_use);
                    b = max(col_use);
                    min_col.append(a);
                    max_col.append(b);

                min_col = np.array(min_col);
                max_col = np.array(max_col);

                minshsv[i, :] = min_col;
                maxshsv[i, :] = max_col;

                maxMinDiffhsv[i, :] = maxshsv[i, :] - minshsv[i, :];

                col = np.transpose(col);
                x = col[2, :];
                x = x.tolist();
                B = sorted(x);

                sortIdx = sorted(range(len(x)), key=lambda k: x[k], reverse=False)
                col = col[:, sortIdx];
                col = np.array(col);

                sortedColhsv = col.reshape((1, 15), order='F');

            if name == 'rgb':

                sortedDiffrgb[i, 0:numDiffs] = sorted((diffs[0, :].tolist()), reverse=True);
                sortedDiffrgb[i, (numDiffs):2 * numDiffs] = sorted(diffs[1, :].tolist(), reverse=True);
                sortedDiffrgb[i, (2 * numDiffs):3 * numDiffs] = sorted(diffs[2, :].tolist(), reverse=True);

                col = np.transpose(col);
                mean1 = [np.mean(col[:, 0]), np.mean(col[:, 1]), np.mean(col[:, 2])];
                mean1 = np.array(mean1);
                meansrgb[i, :] = mean1;

                stds = [np.std(col[:, 0], ddof=1), np.std(col[:, 1], ddof=1), np.std(col[:, 2], ddof=1)];
                stddevsrgb[i, :] = np.array(stds);

                medianss = [np.median(col[:, 0]), np.median(col[:, 1]), np.median(col[:, 2])];
                mediansrgb[i, :] = np.array(medianss);

                min_col = [];
                max_col = [];
                for k in range(3):
                    col_use = col[:, k];
                    a = min(col_use);
                    b = max(col_use);
                    min_col.append(a);
                    max_col.append(b);

                min_col = np.array(min_col);
                max_col = np.array(max_col);

                minsrgb[i, :] = min_col;
                maxsrgb[i, :] = max_col;

                maxMinDiffrgb[i, :] = maxsrgb[i, :] - minsrgb[i, :];

                col = np.transpose(col);
                planergb[i, 0:3], planergb[i, 3:6], planemean, planergb[i, 6] = getPlaneFeatures.getPlaneFeatures(col);


                x = col[2, :];
                x = x.tolist();
                B = sorted(x);

                sortIdx = sorted(range(len(x)), key=lambda k: x[k], reverse=False)
                col = col[:, sortIdx];
                col = np.array(col);
                sortedColrgb = col.reshape((1, 15), order='F');

            if name == 'chsv':

                allFeatures.chsvCol = color;
                allFeatures.chsvSortedCol = sortedColchsv;

                allFeatures.chsvDiff = diff;
                allFeatures.chsvSortedDiff = sortedDiffchsv;

                allFeatures.chsvMean = meanschsv;
                allFeatures.chsvStdDev = stddevschsv;
                allFeatures.chsvMedian = medianschsv;
                allFeatures.chsvMax = maxschsv;
                allFeatures.chsvMin = minschsv;
                allFeatures.chsvMaxMinDiff = maxMinDiffchsv;
                allFeatures.chsvPlane = planechsv;
            if name == 'lab':

                allFeatures.labCol = color;
                allFeatures.labSortedCol = sortedCollab;
                allFeatures.labDiff = diff;
                allFeatures.labSortedDiff1 = sortedDifflab;
                allFeatures.labMean = meanslab;
                allFeatures.labStdDev = stddevslab;
                allFeatures.labMedian = medianslab;
                allFeatures.labMax = maxslab;
                allFeatures.labMin = minslab;
                allFeatures.labMaxMinDiff = maxMinDifflab;
                allFeatures.labPlane = planelab;
            if name == 'rgb':

                allFeatures.rgbCol = color;
                allFeatures.rgbSortedCol = sortedColrgb;

                allFeatures.rgbDiff = diff;
                allFeatures.rgbSortedDiff = sortedDiffrgb;

                allFeatures.rgbMean = meansrgb;
                allFeatures.rgbStdDev = stddevsrgb;
                allFeatures.rgbMedian = mediansrgb;
                allFeatures.rgbMax = maxsrgb;
                allFeatures.rgbMin = minsrgb;
                allFeatures.rgbMaxMinDiff = maxMinDiffrgb;
                allFeatures.rgbPlane = planergb;
            if name == 'hsv':

                allFeatures.hsvCol = color;
                allFeatures.hsvSortedCol = sortedColhsv;

                allFeatures.hsvDiff = diff;
                allFeatures.hsvSortedDiff = sortedDiffhsv;

                allFeatures.hsvMean = meanshsv;
                allFeatures.hsvStdDev = stddevshsv;
                allFeatures.hsvMedian = medianshsv;
                allFeatures.hsvMax = maxshsv;
                allFeatures.hsvMin = minshsv;
                allFeatures.hsvMaxMinDiff = maxMinDiffhsv;
                size = hueProbFeatures.shape[1];
                for i in range(1, size):
                    hueProbFeatures[(hueProbFeatures[:, i] == -99), i] = max(hueProbFeatures[:, i]) + 0.0001;
                allFeatures.hsvHueProb = hueProbFeatures;

    return allFeatures, numThemes, rgb, labs;



