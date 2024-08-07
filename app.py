import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="Oneiric Occasions", page_icon="🤠", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load assets
lottie_coding = load_lottieurl("https://lottie.host/4a25035a-b065-4a03-a856-435e9e880299/A30VZPmIMn.json")
# image1 = Image.open(r"C:\Users\Andy\Desktop\New folder (2)\Python Project\images\img1.JPG")
# image2 = Image.open(r"C:\Users\Andy\Desktop\New folder (2)\Python Project\images\img2.JPG")

# Header section
with st.container():
    st.subheader("Oneiric Occasions")
    st.title("A Photography Page")
    st.write("Contact for more information")

# Additional content (optional)
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Sony Alpha 6100")
      #  st.write("49, 32")
    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# # Projects
# with st.container():
#     st.write("---")
#     st.header("Beautiful Views")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#          st.image(image2)
#     with text_column:
#         st.subheader("Amazing Sunrise")
#         st.write("From some of the great places in the world")
    
        
#another project
# with st.container():
#     st.write("---")
    
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(image1)
#     with text_column:
#         st.subheader("Beautiful Sunset")
#         st.write("From some of the great places in the world")

# --Contact
with st.container():
    st.write("---")
    st.header("Looking for photoshoot? Shoot me an email!!!")
    st.write("oneiricoccasions@gmail.com")





# # # # # #contact_form
contact_form = """
<form action="https://formsubmit.co/oneiricoccasions@gmail.com" method="post">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name"  placeholder="your name"required>
      <input type="email" name="email" placeholder="your email" required>
      <input type="text" name="message"  placeholder="your message here"required>
      <button type="submit">send</button>
</form>
"""


left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html = True)
with right_column:
    st.empty()


