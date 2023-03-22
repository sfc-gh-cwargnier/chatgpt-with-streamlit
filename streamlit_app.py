import openai
import streamlit as st

st.set_page_config(page_title="ChatGPT API with Stream option", page_icon="🎈")

api = st.secrets["api_secret"]

col1, col2, col3 = st.columns([0.45, 0.25, 0.8])

with col2:
    st.image("chatgpt_logo.png")

with col1:
    st.title("Stream:red[_GPT_]")

code = """

    openai.api_key = api
    # Checking if Run button is clicked
    if st.button("Let's go!"):
        # Creating an empty box to display the response
        res_box = st.empty()
        # Creating an empty list to store the response
        report = []
        # Generating response using OpenAI's GPT-3 model
        for response in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{prompt}"}],
            temperature=0,
            stream=True,
        ):
            # Checking if response contains content
            if "content" in response["choices"][0]["delta"]:
                # Appending response to the report list
                report.append(response["choices"][0]["delta"]["content"])
                # Joining all the responses and removing any new line characters
                result = "".join(report).strip()
                result = result.replace("", "")
                # Displaying the response in a markdown format
                res_box.markdown(f":black[{result}]")
    
    """

with st.expander("Show code"):
    st.code(code, language="python")

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.title("")
st.sidebar.markdown("""---""")
st.sidebar.info(
    """
    😎 This code uses `stream=True` to generate ChatGPT responses incrementally, allowing users to receive partial responses while the model is still working on the full response. 
    
    This is a great way to give the user a sense of progress, and to make the app feel more responsive!

"""
)
st.sidebar.markdown("""---""")

prompt = st.text_area(
    "👇 Ask me anything:",
    value="Write a poem about Streamlit in the style of Eminem.",
    placeholder="What's on your mind?",
    height=150,
)

if api:
    openai.api_key = api
    # Checking if Run button is clicked
    if st.button("Let's go!"):
        # Creating an empty box to display the response
        res_box = st.empty()
        # Creating an empty list to store the response
        report = []
        # Generating response using OpenAI's GPT-3 model
        for response in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{prompt}"}],
            temperature=0,
            stream=True,
        ):
            # Checking if response contains content
            if "content" in response["choices"][0]["delta"]:
                # Appending response to the report list
                report.append(response["choices"][0]["delta"]["content"])
                # Joining all the responses and removing any new line characters
                result = "".join(report).strip()
                result = result.replace("", "")
                # Displaying the response in a markdown format
                res_box.markdown(f":black[{result}]")
