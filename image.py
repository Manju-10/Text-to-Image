import requests
import streamlit as st
import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("https://wallpapercave.com/wp/wp6774809.jpg")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set custom title with HTML/CSS for blue glow effect on both text and icon
st.markdown(
    """
    <h1 style="text-align: center; color: #00BFFF; font-size: 50px;
    text-shadow: 0 0 10px #00BFFF;
    filter: brightness(1.5);">
    <img src="https://icon-library.com/images/ai-icon/ai-icon-7.jpg" alt="icon" 
    style="width:50px;height:50px;vertical-align:middle;margin-right:10px;
    filter: brightness(2);">
    Text to Image AI
    </h1>
    """,
    unsafe_allow_html=True
)


API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input('Enter Prompt'),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button('Generate'):
	st.image(image)
