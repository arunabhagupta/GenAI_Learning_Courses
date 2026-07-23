import ollama
from bs4 import BeautifulSoup
import requests
import traceback

def translate_song(system_prompt, user_prompt, song):
    try:
        res = ollama.chat(
            model="llama3.2:1b",
            messages = [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt + "\n\n" + song
                }
            ],
            options={
                "temperature": 0,
                "seed": 70,
            }
        )
        print(f"Content of Response: {res["message"]["content"]}")
    except Exception as e:
        print(f"Error translating song: {e}")
        print(f"Error translating song: {traceback.format_exc()}")

if __name__ == "__main__":
    system_prompt = "You are an AI translator who helps me with translating from any language to english."
    user_prompt = "help me translate this French song to english. Make sure to keep the orignial meaning intact."
    song = """On me dit que nos vies ne valent pas grand chose
    Elles passent en un instant comme fanent les roses
    On me dit que le temps qui glisse est un salaud
    Que de nos chagrins il s'en fait des manteaux
    Pourtant quelqu'un m'a dit
    Que tu m'aimais encore
    C'est quelqu'un qui m'a dit que tu m'aimais encore
    Serait-ce possible alors?
    On me dit que le destin se moque bien de nous
    Qu'il ne nous donne rien et qu'il nous promet tout
    Paraît que le bonheur est à portée de main
    Alors on tend la main et on se retrouve fou
    Pourtant quelqu'un m'a dit
    Que tu m'aimais encore
    C'est quelqu'un qui m'a dit que tu m'aimais encore
    Serait-ce possible alors?
    Serait-ce possible alors?
    Mais qui est-ce qui m'a dit que toujours tu m'aimais?
    Je ne me souviens plus c'était tard dans la nuit
    J'entends encore la voix, mais je ne vois plus les traits
    Il vous aime, c'est secret, lui dites pas que je vous l'ai dit
    Tu vois quelqu'un m'a dit
    Que tu m'aimais encore
    Me l'a-t-on vraiment dit
    Que tu m'aimais encore
    Serait-ce possible alors?
    On me dit que nos vies ne valent pas grand chose
    Elles passent en un instant comme fanent les roses
    On me dit que le temps qui glisse est un salaud
    Que de nos tristesses il s'en fait des manteaux
    Pourtant quelqu'un m'a dit
    Que tu m'aimais encore
    C'est quelqu'un qui m'a dit que tu m'aimais encore
    Serait-ce possible alors?"""

    translate_song(system_prompt, user_prompt, song)
