import streamlit as st
import cv2 as cv



def denoise(img, n = 7, v = 21):
    dst = cv.fastNlMeansDenoisingColored(img,None,10,10,n,v)
    return dst










st.title('Computational Photography')

up_file = st.file_uploader("Choose a file", ['png','jpg'])

if up_file is not None:
    with open(up_file.name,'wb') as f:
        f.write(up_file.read())

    # OpenCv Read
    img = cv.imread(up_file.name)
    # img = cv.imread(up_file.name, cv.IMREAD_GRAYSCALE)
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    with st.container(border=True):
        st.header("Original Image")
        st.image(img, caption=" ")


    with st.container(border=True):
        st.header("Image Denoising")
        n = st.slider(" ", 1, 15, (7), step=2)
        v = st.slider(" ", 11, 31, (21), step=2)
        st.image(denoise(img, n, v) )


    # # Filter
    # with st.container(border=True):
        # col1,col2 = st.columns(2)
        
        # col1.header("Denoising")
        # v, n = col1.slider(" ", 1, 255, (127, 255))
        # col1.image(denoise(img) )

        # col2.header("Binary INV")
        # v, n = col2.slider(" ", 1, 255, (127, 255), key=1)
        # col2.image(thr_bin_inv(img, v, n))


    