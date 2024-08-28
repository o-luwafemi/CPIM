import streamlit as st
import cv2 as cv



def thr_bin(img, v=127, n=255):
    ret,thresh = cv.threshold(img, v, n, cv.THRESH_BINARY)
    return thresh

def thr_bin_inv(img, v=127, n=255):
    ret,thresh = cv.threshold(img,v,n,cv.THRESH_BINARY_INV)
    return thresh

def thr_trunc(img, v=127, n=255):
    ret,thresh = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    return thresh

def thr_2zero(img, v=127, n=255):
    ret,thresh = cv.threshold(img, v, n, cv.THRESH_TOZERO)
    return thresh

def thr_2zero_inv(img, v=127, n=255):
    ret,thresh = cv.threshold(img, v, n, cv.THRESH_TOZERO_INV)
    return thresh



def thr_mean(img, n=11, v=2):
    img = cv.medianBlur(img,5)
    thresh = cv.adaptiveThreshold(
        img, 255, 
        cv.ADAPTIVE_THRESH_MEAN_C, 
        cv.THRESH_BINARY, n, v
        )
    return thresh


def thr_gua(img, n=11, v=2):
    img = cv.medianBlur(img,5)
    thresh = cv.adaptiveThreshold(
        img,255,
        cv.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv.THRESH_BINARY, n, v
        )
    return thresh





st.title('Image Thresholding')

up_file = st.file_uploader("Choose a file", ['png','jpg'])

if up_file is not None:
    with open(up_file.name,'wb') as f:
        f.write(up_file.read())

    # OpenCv Read
    img = cv.imread(up_file.name)
    img = cv.imread(up_file.name, cv.IMREAD_GRAYSCALE)
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    with st.container(border=True):
        st.header("Original Image")
        st.image(img, caption=" ")


    # Filter
    with st.container(border=True):
        col1,col2 = st.columns(2)
        
        col1.header("Binary")
        v, n = col1.slider(" ", 1, 255, (127, 255))
        col1.image(thr_bin(img, v, n) )

        col2.header("Binary INV")
        v, n = col2.slider(" ", 1, 255, (127, 255), key=1)
        col2.image(thr_bin_inv(img, v, n))


    # Filter
    with st.container(border=True):
        col1,col2 = st.columns(2)
        
        col1.header("To Zero")
        v, n = col1.slider(" ", 1, 255, (127, 255), key=2)
        col1.image(thr_2zero(img, v, n), clamp=True )

        col2.header("To Zero INV")
        v, n = col2.slider(" ", 1, 255, (127, 255), key=3)
        col2.image(thr_2zero_inv(img, v, n), clamp=True)


    # Filter
    with st.container(border=True):
        col1,col2 = st.columns(2)
        
        col1.header("Adaptive Mean")
        n = col1.slider(" Block Size", 3, 51, (11), step=2, key=4)
        v = col1.slider("Constant ", 1, 21, (2), key=5)
        col1.image(thr_mean(img, n, v))

        col2.header("Adaptive Gaussian")
        n = col2.slider(" Block Size", 3, 51, (11), step=2, key=6)
        v = col2.slider("Constant ", 1, 21, (2), key=7)
        col2.image(thr_gua(img, n, v), clamp=True)