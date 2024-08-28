import numpy as np
import cv2 as cv
import streamlit as st



def laplacian(img):
    laplacian = cv.Laplacian(img,cv.CV_64F)
    return laplacian

def sobelx(img, n=5):
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=n)
    return sobelx

def sobely(img, n=5): 
    sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=n)
    return sobely


st.title('Image Gradients')

up_file = st.file_uploader("Choose a file", ['png','jpg'])

if up_file is not None:
    with open(up_file.name,'wb') as f:
        f.write(up_file.read())

    # OpenCv Read
    img = cv.imread(up_file.name)
    img = cv.imread(up_file.name, cv.IMREAD_GRAYSCALE)


    with st.container(border=True):
        st.header("Original Image")
        st.image(img, caption=" ")


    # Filter
    with st.container(border=True):
        col1,col2 = st.columns(2)
        
        col1.header("Sobel X")
        value = col1.slider(" ", 1, 31, (5), step=2)
        col1.image(sobelx(img, value), clamp=True,)

        col2.header("Sobel Y")
        value = col2.slider(" ", 1, 31, (5), step=2, key=1)
        col2.image(sobely(img, value), clamp=True)


    # Filter
    with st.container(border=True):
        col1,col2 = st.columns(2)
        
        col1.header("Laplacian")
        value = col1.slider(" ", 1, 10, key=2, disabled=True)
        col1.image(laplacian(img), clamp=True)