# Transcryber: Voicemail Transcription App

## Project Overview

This project aims to create an Android application that transcribes voicemails and other audio files using the Assembly AI API. The backend is a Python-based web service that handles the transcription, and the frontend will be a native Android application.

This document provides instructions for a coding assistant to continue development and build the Android `.apk`.

## Backend Setup and Usage

The backend is a Flask web application that exposes an API for transcribing audio files.

### Prerequisites

- Python 3.x
- `pip` for installing packages

### Installation

1.  Clone the repository.
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

1.  Start the Flask application:
    ```bash
    python app.py
    ```
2.  The server will start on `http://127.0.0.1:5000`.

### API Endpoint

-   **`POST /transcribe`**
    -   **Description:** Transcribes an audio file.
    -   **Request:** `multipart/form-data` with a single field named `file` containing the audio file.
    -   **Example using `curl`:**
        ```bash
        curl -X POST -F "file=@/path/to/your/audio.wav" http://127.0.0.1:5000/transcribe
        ```
    -   **Success Response (200):**
        ```json
        {
          "transcription": "This is the transcribed text..."
        }
        ```
    -   **Error Response (400, 500):**
        ```json
        {
          "error": "Error message..."
        }
        ```

## Android App Development Roadmap for Coding Assistant

This section outlines the steps to build the Android `.apk`.

### Recommended Technologies

*   **Language:** Kotlin (the modern standard for Android development).
*   **Architecture:** Model-View-ViewModel (MVVM) is recommended for a clean separation of concerns. Use Android Architecture Components like `ViewModel`, `LiveData`, and `Room`.
*   **Networking:** Use a library like `Retrofit` or `OkHttp` to communicate with the backend API.
*   **UI:** Use Jetpack Compose for building the user interface. It's a modern and declarative way to build UIs in Android.
*   **Permissions:** The app will need permissions for `RECORD_AUDIO`, `READ_EXTERNAL_STORAGE`, and potentially others related to accessing voicemails.

### Development Steps

1.  **Set up the Android Studio Project:**
    *   Create a new Android Studio project.
    *   Select "Empty Compose Activity" as the template.
    *   Choose Kotlin as the language.

2.  **Implement the User Interface (UI):**
    *   Design and build the main screen using Jetpack Compose. This screen should display a list of voicemails and their transcriptions.
    *   Create a button or menu option to allow users to select and transcribe other audio files.

3.  **Implement the Networking Layer:**
    *   Use Retrofit to create a service that communicates with the backend's `/transcribe` endpoint.
    *   Implement the logic to upload audio files from the device to the backend.

4.  **Integrate Voicemail Access:**
    *   **This is the most challenging part.** Accessing voicemails directly is restricted in modern Android versions for security reasons. You will need to investigate the `VoicemailContract` API and potentially use other methods to access voicemail data if the standard API is not sufficient on the target device (Samsung Galaxy S25).
    *   Implement a service that runs in the background to detect new voicemails and trigger transcription.

5.  **Handle Audio File Transcription:**
    *   Implement a file picker to allow users to select audio files from their device, Google Drive, and OneDrive.
    *   For Google Drive and OneDrive, you will need to integrate their respective SDKs for authentication and file access.

6.  **Implement Local Database (Optional but Recommended):**
    *   Use the `Room` persistence library to store transcriptions locally. This will allow the app to work offline and reduce the number of API calls.

7.  **Handle Permissions:**
    *   Implement the necessary logic to request permissions from the user at runtime.

8.  **Build and Test:**
    *   Build the `.apk` file.
    *   Thoroughly test the application on a physical device or an emulator that matches the target device's specifications.

By following these instructions, you should be able to seamlessly continue the development of the Transcryber Android application.
