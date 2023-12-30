import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import base64
from streamlit_drawable_canvas import st_canvas

st.set_page_config(
    page_title="Draw Me A Picture!",
    page_icon="✏",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Draw Me A Picture!")

canvas_result = st_canvas(background_color="rgba(129,168,141,1.000)",
                          fill_color="rgba(129,168,141,1.000)",
                          height=600,
                          width=1418)


def get_binary_file_downloader_html(file_path, file_label):
    with open(file_path, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:file/png;base64,{bin_str}" download="{file_label}.png">Download Image</a>'
    return href

    drawing_mode = st.selectbox("Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform"))
    
    stroke_width = st.slider("Stroke width: ", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.slider("Point display radius: ", 1, 25, 3)
    stroke_color = st.color_picker("Stroke color hex: ")
    bg_color = st.color_picker("Background color hex: ", "#eee")
    bg_image = st.file_uploader("Background image:", type=["png", "jpg"])
    
    realtime_update = st.checkbox("Update in realtime", True)


# Add a download button
if st.button("Download Image"):
    # Convert the drawn canvas to a PIL Image
    pil_image = Image.fromarray(canvas_result.image_data)

    # Save the PIL Image to a temporary file
    temp_file_path = "drawn_image.png"
    watermark_text = "g00bys Py Toys - Made On Streamlit"
    draw = ImageDraw.Draw(pil_image)

    # Specify a small font size for the watermark
    font_size = 35
    font_color = "#d3d4d8"
    font = ImageFont.load_default()  # You can use any font file path or the default font
    text_width, text_height = draw.textsize(watermark_text, font)
    margin = 10  # Adjust the margin as needed
    draw.text((pil_image.width - text_width - margin, pil_image.height - text_height - margin), watermark_text,
              font=font, fill=font_color)
    pil_image.save(temp_file_path,  dpi=(600, 600))

    # Provide a download link
    st.markdown(get_binary_file_downloader_html(temp_file_path, 'Draw_g00by_A_Picture'), unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-testid=stButton] > button {
    background-color: #81A88D;
    color:#ffffff;
    }
    [data-testid=stAppViewContainer]{
    background-color: #81A88D;
    }
    [data-testid=stHeader]{
    background-color: #81A88D;
    }
    [data-testid=stSidebar] {
    background-color: #D3D4D8;
    }
    [data-testid=stButton] > button:hover {
    background-color: #A2A475;
    border-color:#ffffff;
    color:#ffffff;
    }
    [data-testid=stButton] > button:focus:not(:active) {
    background-color: #A2A475;
    border-color:#ffffff;
    color:#ffffff;
    }
    </style>""", unsafe_allow_html=True)

