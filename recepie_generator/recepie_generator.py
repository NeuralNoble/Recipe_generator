from online_module import  *
from apikey import apikey

st.title('Recepie Generator')

client = setup_apikey(apikey)

output_format = ("""
                    <h1> Fun Title of recipe </h1>
                    <h1> Table of Contents</h1> <li> links of content </li>
                    <h1> Introduction </h1><p> dish introduction</p>
                    <h1> Country of Origin </h1><p> Country of Origin</p>
                    <h1> Ingredients </h1><li>Ingredients list </li>
                    <h1> Cooking Steps</h1><li>Cooking Steps list </li>
                    <h1> FAQ </h1><p>question answers</p>
                 """)

recipe = st.text_input("Enter your recipe name")
image_prompt = recipe + "realistic ,cinematic"

if st.button('Generate a recipe'):
    with st.spinner('Generating recipe...'):
        image = generate_image_openai(client,recipe)
        st.image(image,caption=recipe,use_column_width=True)

    with st.spinner('Generarting recipe..'):
        text_area_placeholder = st.markdown("", unsafe_allow_html=True)
        prompt = f" Create a detailed cooking recipe for the dish named {recipe}." \
                 f" Include preparation steps and cooking tips." \
                 f" Follow the following format {output_format}"
        generate_text_openai(client,prompt,text_area_placeholder,html=True)



