import streamlit as st
from PIL import Image
from typing import Tuple
import os
import base64
from gradio_client import Client, file
import pyvista as pv
import streamlit as st
from stpyvista import stpyvista

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()



def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def save_uploaded_file(uploaded_file):

    if not os.path.exists("uploaded_files"):
        os.makedirs("uploaded_files")
    
    file_path = os.path.join("uploaded_files", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path


set_background(r"C:\Users\user\OneDrive\Рабочий стол\Фото\Сочи2023-20230809T090702Z-001\Сочи2023\IMG_5456.JPG")


st.write("""
# 3D reconstruction
""")

uploaded_file = st.file_uploader("Выберите изображение", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)


client = Client("pengHTYX/Era3D_MV_demo")

def pil_resize(image: Image.Image, 
               base_width: int = 300) -> Image.Image:
    
    wpercent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((base_width, hsize), Image.Resampling.LANCZOS)
    return image



def stable_picture(uploaded_file) -> Tuple:
    
    if uploaded_file is not None:

        result = client.predict(
		single_image=file(file_path),
		guidance_scale=3,
		steps=30,
		seed=600,
		crop_size=420,
		chk_group=["Write Results"],
		api_name="/partial_1"
)
    return result


def show_stable_picture(arr_picture: Tuple) -> None:

    for arr in arr_picture:
        cols = st.columns(6)
        for j in range(len(arr)):
            image_path = arr[j]['image']
            image = Image.open(image_path)
            with cols[j]:    
                image = pil_resize(image, 200)
                st.image(image, caption=f"Photo {j}")


def show_3d_model():
    plotter = pv.Plotter(window_size=[400, 400])

## Create a mesh with a cube
    mesh = pv.Cube()

    ## Add some scalar field associated to the mesh
    mesh["my_scalar"] = mesh.points[:, 2] * mesh.points[:, 0]

    ## Add mesh to the plotter
    plotter.add_mesh(mesh, scalars="my_scalar", cmap="bwr")

    ## Final touches
    plotter.view_isometric()
    plotter.add_scalar_bar()
    plotter.background_color = "white"

    ## Pass a key to avoid re-rendering at each page change
    stpyvista(plotter, key="pv_cube")

    
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = pil_resize(image, 200)
    st.image(image, caption='Загруженное изображение')

show_created_pic = st.button("Pic to 3D")
if show_created_pic:
    new_pic = stable_picture(image)
    show_stable_picture(new_pic)
    show_3d_model()
