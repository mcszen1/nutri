import base64
import streamlit as st
import os
import tempfile
import requests, uuid, json
from openai import OpenAI
import json

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def save_uploaded_file(uploaded_file_content):
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file_content)
    return "temp_image.jpg"



    # Clean up the temporary file
    os.remove(temp_file.name)


def analyze_image_with_openai(image):
    # This function will send a request to OpenAI's GPT-4 Vision API to analyze the image.
    # The 'image' parameter can be a URL or base64-encoded data.
    # Here we provide a mock-up of the API call with placeholder response handling.

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Identifique alimentos e ingredientes nesta imagem e sugira uma receita para utilizá-los"},
                    {"type": "image_url", "image_url": image},
                ],
            }
        ],
        max_tokens=300,
    )
    description_content = response.choices[0].message.content
    print(description_content)
    
 
     
    return description_content

def main():
    st.image("logonutri2.jpg",use_column_width="False")
    st.title("NUTRI RECEITAS")
    st.write('ASSISTENTE DE IDENTIFICAÇÃO E DESCRIÇÃO DE IMAGENS')
    st.write('Use uma imagem de arquivo ou tire uma foto com sua câmera')
    option = st.radio('Escolha a origem da sua imagem:',('Arquivo', 'Camera'))
    if option=="Arquivo":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            temp_path1 = save_uploaded_file(uploaded_file.read())
    
            st.image(temp_path1, caption="Image fornecida", use_column_width=True)

            if uploaded_file is not None:
                # Convert the file to an image URL or base64-encoded string as required by OpenAI API
                image_data = uploaded_file.getvalue()
                image_url = "data:image/jpg;base64," + base64.b64encode(image_data).decode()
        
                # Analyze the image with OpenAI's GPT-4 Vision API
                description = analyze_image_with_openai(image_url)
                #st.spinner('Analisando sua imagem ... Aguarde !')
                            
                # Display the description and translated text
                st.write("Sugestão: ", description)
        
                
   
                
    if option=='Camera':
        picture = st.camera_input("Tire uma foto")

        if picture:
            temp_path = save_uploaded_file(picture.read())
            st.image(temp_path, caption="Foto tirada", use_column_width=True)
    
   
            if picture is not None:
                # Convert the file to an image URL or base64-encoded string as required by OpenAI API
                image_data = picture.getvalue()
                image_url = "data:image/jpg;base64," + base64.b64encode(image_data).decode()
        
                # Analyze the image with OpenAI's GPT-4 Vision API
                description = analyze_image_with_openai(image_url)
                #st.spinner('Analisando sua imagem ... Aguarde !')
                
           
                # Display the description and translated text
                st.write("Sugestão: ", description)
          
if __name__ == '__main__':
    main()               
               
