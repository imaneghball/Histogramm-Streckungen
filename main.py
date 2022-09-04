import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("lenagray.jpg",0)
def findMinMaxMat(mat):
    min=255
    max=0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j]>max:
                max=mat[i,j]
            if mat[i,j]<min:
                min=mat[i,j]
    return (min,max)
def LimitHistogram(img):
    (Imin,Imax)=findMinMaxMat(img)
    (Omin,Omax)=(90,180)
    outImage = np.zeros((img.shape),dtype="uint8")
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            outImage[i,j]=((((Omax-Omin)/(Imax-Imin))*(img[i,j]-Imin))+Omin)
    return outImage
def HistogrammStreckungen1(img):
    (Imin, Imax) = findMinMaxMat(img)
    outImage = np.zeros((img.shape), dtype="uint8")
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j]<Imin:
                outImage[i,j]=0
            elif img[i,j]>Imax:
                outImage[i,j]=255
            else:
                outImage[i,j]=round(255*((img[i,j]-Imin)/(Imax-Imin)))
    return outImage
def HistogrammStreckungen2(img):
    (Imin, Imax) = findMinMaxMat(img)
    (Omin, Omax) = (0,255)
    outImage = np.zeros((img.shape), dtype="uint8")
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            outImage[i, j] = ((((Omax - Omin) / (Imax - Imin)) * (img[i, j] - Imin)) + Omin)
    return outImage
def showHistogram(img):
    hist=cv2.calcHist([img], [0], None, [256], [0, 255])
    return hist
img2=LimitHistogram(img)
plt.figure()
plt.subplot(321),plt.imshow(img2,"gray"),plt.title("Orginal"),
plt.xticks([]),plt.yticks([])
plt.subplot(322),plt.plot(showHistogram(img2)),plt.title("Histogram Orginal")
plt.subplot(323),plt.imshow(HistogrammStreckungen1(img2),"gray"),plt.title("Strckung 1"),
plt.xticks([]),plt.yticks([])
plt.subplot(324),plt.plot(showHistogram(HistogrammStreckungen1(img))),plt.title("Histogram Strekung 1")
plt.subplot(325),plt.imshow(HistogrammStreckungen2(img2),"gray"),plt.title("Strckung 2"),
plt.xticks([]),plt.yticks([])
plt.subplot(326),plt.plot(showHistogram(HistogrammStreckungen2(img))),plt.title("Histogram Strekung 2")
plt.show()

