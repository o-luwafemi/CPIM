import streamlit as st
import cv2 as cv
import numpy as np



def filter2d(img, n=5):
    kernel = np.ones((n,n),np.float32)/25
    dst = cv.filter2D(img,-1,kernel)
    return dst

def blur(img, n=5):
    blur = cv.blur(img,(n,n))
    return blur

def gau_blur(img, n=5):
    blur = cv.GaussianBlur(img,(n,n),0)
    return blur

def medianBlur(img, n=5):
    median = cv.medianBlur(img,n)
    return median

def biFilter(img, n=8):
    blur = cv.bilateralFilter(img,n,75,75)
    return blur


st.title('Image Smoothing')

up_file = st.file_uploader("Choose a file", ['png','jpg'])


if up_file is not None:
    with open(up_file.name,'wb') as f:
        f.write(up_file.read())

    # OpenCv Read
    img = cv.imread(up_file.name)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    with st.container(border=True):
        st.header("Original Image")
        st.image(up_file, caption=" ")


    ## Filter
    with st.container(border=True):
        col1,col2 = st.columns(2)
        
        col1.header("2D Filter")
        value = col1.slider(" ", 1, 10, (5))
        col1.image(filter2d(img, value))

        col2.header("Bilateral Filter")
        value = col2.slider(" ", 1, 50, (8), key=1)
        col2.image(biFilter(img, value))

    
    
    ## Blur
    with st.container(border=True):
        col1,col2 = st.columns(2)

        col1.header("Blur")
        value = col1.slider(" ", 1, 50, (5), key=2)
        col1.image(blur(img, value))

        col2.header("Gaussian Blur")
        value = col2.slider(" ", 1, 51, (5), step=2, key=3)
        col2.image(gau_blur(img, value))



    


