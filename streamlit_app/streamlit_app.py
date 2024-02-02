import streamlit as st
import requests


API_URL = "https://api-inference.huggingface.co/models/Feluda/pegasus-samsum"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()



def main():
    st.title('Chat Summarizer')
    st.sidebar.markdown("""
    ### How to use the Chat Summarizer :speech_balloon:

    1. **Choose your input method** :point_down:
        - *Paste text directly* into the text area
        - *Upload a text file* with your chat content
    2. **Enter or upload your text** :clipboard:
        - If you chose to paste the text, enter it in the text area below
        - If you chose to upload a file, click on 'Browse files' and select the text file from your device
    3. **Click 'Summarize'** :rocket:
        - Get a concise summary of your text
    """)

    upload_option = st.selectbox('How would you like to provide the text?', ('Paste text', 'Upload file'))
    text = ''
    if upload_option == 'Paste text':
        text = st.text_area('Enter your text here')
    else:
        uploaded_file = st.file_uploader("Choose a text file", type="txt")
        if uploaded_file is not None:
            text = uploaded_file.read().decode()

    if st.button('Summarize'):
        if text:
            with st.spinner('Summarizing...'):
                try:
                    output = query({
                        "inputs": text,
                        "options": {
                            "wait_for_model": True
                        }
                    })
                    summary = output[0]['generated_text']
                    st.subheader('Summary')
                    st.write(summary)

                except:
                    st.error('Error: Something went wrong. Please try again later.')
        else:
            st.error('Error: Please enter some text or upload a file before summarizing.')

if __name__ == "__main__":
    main()
