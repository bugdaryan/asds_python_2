import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from glob import glob


def run(pic_1, border):
    pic_1 = cv2.imread(pic_1)
    pic_1 = cv2.cvtColor(pic_1, cv2.COLOR_BGR2GRAY)


    ret, thresh = cv2.threshold(pic_1, 0, 255, cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)

    len(contours)
    area_countours = []
    area = []
    t=(thresh!=255).sum()*0.5
    for contour in contours:
        a= cv2.contourArea(contour)
        if a>t:
            area_countours.append(contour)
            area.append(a)


    idx = pd.DataFrame([area]).T.sort_values(0,ascending=False).head(2).index[border]
    c = [area_countours[idx]]



    mask = np.zeros_like(thresh)

    cv2.drawContours(image=mask, contours=c, contourIdx=-1, color=255, thickness=-1)
    for i in c:
        rect = cv2.boundingRect(i)
        cv2.rectangle(mask,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]), 0,20)

    cuted = thresh[rect[1]:rect[1]+rect[3],rect[0]: rect[0]+rect[2]]
    cuted = cuted[:int(cuted.shape[0]*0.2),:int(cuted.shape[1]*0.2)]


    cnts, hierarchy = cv2.findContours(image=cuted, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
    index_sort = sorted(range(len(cnts)), key=lambda i : cv2.contourArea(cnts[i]),reverse=True)

    len(cnts)


    mask = np.zeros_like(cuted)
    c=[cnts[index_sort[1]]]
    cv2.drawContours(image=mask, contours=c, contourIdx=-1, color=255, thickness=-1)
    rect = cv2.boundingRect(c[0])


    final = cuted[rect[1]:rect[1]+rect[3],rect[0]: rect[0]+rect[2]]
    invert = cv2.bitwise_not(final)
    gts = []
    name = []
    for i in glob("compare/*"):
        gt = cv2.imread(i)

        gt = cv2.cvtColor(gt, cv2.COLOR_BGR2GRAY)
        ret, thresh_gt = cv2.threshold(gt, 0, 255, cv2.THRESH_OTSU)
        gts.append(thresh_gt)
        name.append(i.split("/")[-1])



    first=0
    for i,j in zip(gts[::-1],name[::-1]):
        invert= cv2.resize(invert,(i.shape[1],i.shape[0]))
        diff_img = cv2.absdiff(invert, i)
        rank_diff = int(np.sum(diff_img)/255)
        if first == 0:
            sm = rank_diff
            first=1
            label = j
        if sm>rank_diff:
            sm = rank_diff
            label = j
    return sm, label


def main():
    path_b = []
    path_no_b = []
    with_border = 1
    without_border = 0
    for i in path_b:
        _, suit = run(i,with_border)
        print(f"{i}\nCard is {suit.split('.')[0]}\n")


    for i in path_no_b:
        _, suit = run(i,without_border)
        print(f"{i}\nCard is {suit.split('.')[0]}\n")


if __name__ =="__main__":
  main()
