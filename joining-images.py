img1 = cv2.imread('temp1.png')
img2 = cv2.imread('temp2.png')
img3 = cv2.imread('temp3.png')
result = cv2.hconcat([img1, img2, img3])
cv2.imwrite(path + 'basic-stats-comparison.png', result)

