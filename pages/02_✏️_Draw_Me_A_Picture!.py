import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from streamlit_drawable_canvas import st_canvas

st.set_page_config(
    page_title="Draw/Send Picture!",
    page_icon="✏",
    layout="wide",
    initial_sidebar_state="expanded"
)

gbypytoys_em = st.secrets.emailvar
gbypytoys_em2 = st.secrets.emailvar2
pss = st.secrets.pssvar

st.title(":rainbow[Draw Settings]:")

drawing_mode = st.selectbox("Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform"))

stroke_width = st.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.color_picker("Stroke color hex: ")
bg_color = st.color_picker("Background color hex: ", '#81a88d')

realtime_update = st.checkbox("Update in realtime", True)

st.title("Canvas:")

canvas_result = st_canvas(fill_color="rgba(129,168,141,1.000)",
                          update_streamlit=realtime_update,
                          stroke_color=stroke_color,
                          background_color=bg_color,
                          drawing_mode=drawing_mode,
                          point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
                          key="canvas",
                          height=600,
                          width=1418)


def get_binary_file_downloader_html(file_path, file_label):
    with open(file_path, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'-> <a href="data:file/png;base64,{bin_str}" download="{file_label}.png">Download Image</a> <-'
    return href



if st.button("Download Image"):
    # Convert the drawn canvas to a PIL Image
    pil_image = Image.fromarray(canvas_result.image_data)

    # Save the PIL Image to a temporary file
    temp_file_path = "drawn_image.png"
    watermark_text = "Drawing Made With - g00bys-py-toys.streamlit.app/"
    draw = ImageDraw.Draw(pil_image)

    # Specify a small font size for the watermark
    font_size = 30
    font_color = "#d3d4d8"
    font = ImageFont.load_default()  # You can use any font file path or the default font
    text_width, text_height = draw.textsize(watermark_text, font)
    margin = 10  # Adjust the margin as needed
    draw.text((pil_image.width - text_width - margin, pil_image.height - text_height - margin), watermark_text,
              font=font, fill=font_color)
    pil_image.save(temp_file_path,  dpi=(600, 600))

    # Provide a download link
    st.markdown(get_binary_file_downloader_html(temp_file_path, 'Draw-g00by-A-Picture'), unsafe_allow_html=True)



if st.button("Send via Email"):
    pil_image = Image.fromarray(canvas_result.image_data)

    # Save the PIL Image to a temporary file
    temp_file_path = "drawn_image.png"
    watermark_text = "Drawing Made With - g00bys-py-toys.streamlit.app/"
    draw = ImageDraw.Draw(pil_image)


    font_size = 30
    font_color = "#d3d4d8"
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(watermark_text, font)
    margin = 10
    draw.text((pil_image.width - text_width - margin, pil_image.height - text_height - margin), watermark_text,
              font=font, fill=font_color)
    pil_image.save(temp_file_path, dpi=(600, 600))

    
    sender_email = gbypytoys_em
    receiver_email = gbypytoys_em2
    subject = "🚨📢 Someone Drew You A Picture!"
    body = "Check it out!"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(temp_file_path, 'rb') as f:
        img_data = f.read()
        image = MIMEImage(img_data, name="drawn_image.png")
        msg.attach(image)


    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, pss)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    st.success("Drawing sent successfully via email!")

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

