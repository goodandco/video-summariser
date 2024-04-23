import re
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

client = OpenAI()
# video_id = "X31-atKcF4E" # baumeister books
# video_id = "kCre83853TM" # Ray Kurzweil & Geoff Hinton Debate the Future of AI
description = "In this episode, recorded during the 2024 Abundance360 Summit, Ray, Geoffrey, and Peter debate whether AI will become sentient, what consciousness constitutes, and if AI should have rights."
# video_id = "PVXQUItNEDQ" # Ray Kurzweil in TED about neocortex
# description = "You are a video transcript analyzer. Description of the video: Two hundred million years ago, our mammal ancestors developed a new brain feature: the neocortex. This stamp-sized piece of tissue (wrapped around a brain the size of a walnut) is the key to what humanity has become. Now, futurist Ray Kurzweil suggests, we should get ready for the next big leap in brain power, as we tap into the computing power in the cloud."
languages = ['en']
# video_id = "VdwEvn1G89I"
# description = "Приєднуйтесь до нашої подорожі, щоб дізнатися про легенди та досягнення Стенфордського університету. Від становлення до сучасності — ми дізнаємося про визначні моменти його історії, видатних випускників та першовідкривачів, які змінили світ."
# languages = ['uk']
url = "https://www.youtube.com/watch?v=kCre83853TM"


def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        transcript = ""
        for line in transcript_list:
            transcript += line['text'] + " "
        return transcript
    except Exception as e:
        print("An error occurred:", e)
        return None


def extract_video_id(url: str) -> str:
    data = re.findall(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if data:
        return data[0]
    return ""


def get_summary_by_transcript(transcript: str, provider: str) -> str:


def get_summary_by_transcript_chat_gpt(transcript: str) -> str:
    response = completion = client.chat.completions.create(
        model="davinci-002",
        messages=[
            {"role": "system", "content": description, },
            {"role": "user", "content": 'Make a summary of that video transcript ' + transcript, },
        ]
    )

    return response.choices[0].text.strip()


def get_summary_by_transcript_gemini(transcript: str) -> str:


def run(url):
    video_id = extract_video_id(url)
    print(video_id)
    transcript = get_transcript(video_id)
    if transcript:
        print("Transcript:")
        print(transcript)
        # response = completion = client.chat.completions.create(
        #     model="davinci-002",
        #     messages=[
        #         {"role": "system", "content": description, },
        #         {"role": "user", "content": 'Make a summary of that video transcript', },
        #     ]
        # )
        #
        # print(response.choices[0].text.strip())
    else:
        print("Failed to retrieve transcript.")


run(url)
