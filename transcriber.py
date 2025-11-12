import os
import argparse
import requests

ASSEMBLY_AI_API_KEY = "0a1960b702ce461ebbf863100cf4d162"
UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"

def transcribe_audio(file_path):
    """Transcribes an audio file using the Assembly AI API."""
    headers = {"authorization": ASSEMBLY_AI_API_KEY}
    with open(file_path, "rb") as f:
        response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=f)
    upload_url = response.json()["upload_url"]
    transcript_request = {"audio_url": upload_url}
    transcript_response = requests.post(
        TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers
    )
    transcript_id = transcript_response.json()["id"]
    polling_endpoint = f"{TRANSCRIPTION_ENDPOINT}/{transcript_id}"
    while True:
        polling_response = requests.get(polling_endpoint, headers=headers)
        status = polling_response.json()["status"]
        if status == "completed":
            return polling_response.json()["text"]
        elif status == "error":
            raise Exception(f"Transcription failed: {polling_response.json()['error']}")

def get_audio_from_source(source):
    """Downloads an audio file from a given source."""
    if source.startswith("file://"):
        return source[7:]
    elif source.startswith("gdrive://"):
        print("Google Drive support is not yet implemented.")
        return None
    elif source.startswith("onedrive://"):
        print("OneDrive support is not yet implemented.")
        return None
    else:
        # Assume it's a local file path
        return source

def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Transcribe an audio file.")
    parser.add_argument("source", help="The source of the audio file to transcribe (local path, gdrive://, onedrive://).")
    args = parser.parse_args()
    file_path = get_audio_from_source(args.source)
    if file_path:
        transcription = transcribe_audio(file_path)
        print(transcription)

if __name__ == "__main__":
    main()
