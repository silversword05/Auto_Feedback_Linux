import cv2
import numpy as np
def break_captcha(img1):
    try:
        from PIL import Image
    except ImportError:
        import Image
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

    img=cv2.imread(img1,cv2.IMREAD_GRAYSCALE)

    ret,img = cv2.threshold(img,40,255,cv2.THRESH_BINARY_INV)
    mask= np.zeros(img.shape)
    # cv2.imshow("thresh",img)
    # print(img.shape)

    indexV=45
    if(img[45][4]==255 and img[45][7]==255):
        indexV=47

    indexH=10
    if(img[4][10]==255 and img[7][10]==255):
        indexH=8

    for i in range(img.shape[0]): #removing horizontal lines
        if(img[i][indexH]==255):
            for j in range(img.shape[1]):
                img[i][j]=0
                mask[i][j]=255

    for j in range(img.shape[1]): #removing vertical lines
        if(img[indexV][j]==255):
            for i in range(img.shape[0]):
                img[i][j]=0
                mask[i][j]=255

    img_copy = img.copy()
    kernel = np.ones((3,3),np.uint8)
    #kernel[0][0]=kernel[0][2]=kernel[2][0]=kernel[2][2]=0
    img = cv2.dilate(img,kernel,iterations = 1)

    img_subs =cv2.bitwise_and (mask,mask,mask=img - img_copy)
    img_final = img_copy + img_subs
    ret,img_final = cv2.threshold(img_final,40,255,cv2.THRESH_BINARY_INV)

    # cv2.imshow('Image_Copy',img_copy)
    # cv2.imshow('Image',img)
    # cv2.imshow('Mask',mask)
    # cv2.imshow('dilate',img_subs)
    # cv2.imshow('Image Final',img_final)
    return pytesseract.image_to_string(img_final)
    cv2.waitKey(0)