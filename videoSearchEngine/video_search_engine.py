# Packages that have to be installed are following
# pip install moviepy
# pip install SpeechRecognition


from moviepy.editor import VideoFileClip
import speech_recognition as sr

def convert_video_to_audio(src_video_path, dest_audio_path):
    """Converts a video file to an audio file."""
    try:
        video_clip = VideoFileClip(src_video_path)
        video_audio = video_clip.audio
        video_audio.write_audiofile(dest_audio_path)
        video_audio.close()
    except Exception as error:
        print(f"Conversion Error: {error}")
        exit()

def transcribe_audio_to_text(audio_file_path):
    """Transcribes audio to text using Google's Speech Recognition."""
    speech_recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source_audio:
        print("Transcribing audio to text, please wait...")
        try:
            recorded_audio = speech_recognizer.record(source_audio)
            transcription = speech_recognizer.recognize_google(recorded_audio)
            return transcription
        except Exception as error:
            print(f"Transcription Error: {error}")

def count_dialogue_occurrences(transcribed_text):
    """Counts occurrences of a specified dialogue in the transcribed text."""
    user_dialogue = input("Enter Dialogue: ")
    occurrence_count = transcribed_text.count(user_dialogue)
    if occurrence_count > 0:
        print(f"'{user_dialogue}' occurs {occurrence_count} times")
    else:
        print("Dialogue not found in the transcribed text.")


source_video = "video.mp4"
destination_audio = "converted_audio.wav"


convert_video_to_audio(source_video, destination_audio)
transcribed_text = transcribe_audio_to_text(destination_audio)
if transcribed_text:
    count_dialogue_occurrences(transcribed_text)
