# AI Coding Assistant

This project is a voice-powered AI coding assistant that can execute commands on your local machine. It uses Google's Gemini Pro language model, LangChain for building the application logic, and OpenAI's TTS for voice output.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Pip (Python package installer)
- A microphone

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/alokdangre/My_Cursor.git
    cd My_Cursor
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**

    Create a `.env` file in the root of the project and add your API keys:

    ```
    GOOGLE_GEMINI_API="YOUR_GOOGLE_GEMINI_API_KEY"
    MIC_DEVICE_INDEX=0 # Optional: Change if you have multiple microphones
    ```

    You can find your `MIC_DEVICE_INDEX` by running the following Python code:
    ```python
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microphone with name \"{name}\" found for `Microphone(device_index={index})`")
    ```

## Usage

To run the application, execute the following command from the root of the project:

```bash
python -m app.main
```

The application will then start listening for your voice commands.

## Features

-   **Voice-powered:** Interact with the assistant using your voice.
-   **Command execution:** The assistant can execute shell commands on your machine.
-   **AI-powered:** Uses Google's Gemini Pro model to understand and respond to your requests.
-   **Extensible:** Built with LangChain, making it easy to add new tools and functionality.

## Dependencies

The project uses the following major dependencies:

-   `langchain`
-   `langgraph`
-   `google-generativeai`
-   `openai`
-   `speechrecognition`
-   `python-dotenv`

A full list of dependencies can be found in the `requirements.txt` file.
