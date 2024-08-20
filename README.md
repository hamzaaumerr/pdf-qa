# Chat with PDF

Welcome to the **Chat with PDF** project! This application allows users to upload a PDF document, ask questions related to its content, and receive accurate answers. Built using Python and Streamlit, the app provides an intuitive interface for interacting with PDF content through natural language queries.

## Overview

The Chat with PDF app enables users to upload a PDF file and ask questions about its content. The application uses advanced natural language processing powered by Cohere to deliver precise answers. With an easy-to-use interface, users can engage with their documents in a conversational manner.

## Features

- **PDF Upload**: Upload your PDF document directly through the app's sidebar.
- **Question & Answer**: Ask questions related to the PDF content and get accurate responses.
- **Streamlit Integration**: Built with Streamlit, the app features a responsive and clean user interface.
- **Cohere API Integration**: Leverages Cohere's powerful language models to process and understand PDF content.

## Demo

You can try the live demo of the app here: [Chat with PDF on Streamlit](#)

## Getting Started

To run this application locally, follow the instructions below:

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Cohere API Key

### Installation

1. Clone the repository:

    ```bash
    git clone #
    cd Chat_with_PDF
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain your Cohere API key [here](https://dashboard.cohere.com/) and enter it in the Streamlit sidebar.

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

### Usage

- Open the app in your browser at `http://localhost:8501`.
- Upload your PDF file using the upload button in the sidebar.
- Enter your questions in the input box provided.
- Click the "Ask" button to receive responses based on the PDF content.

## Getting a Cohere API Key

To use this app, you will need a Cohere API key. You can obtain your key by following the instructions [here](https://dashboard.cohere.com/).
