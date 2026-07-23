import ollama
from bs4 import BeautifulSoup
import requests
import traceback
from IPython.display import Markdown, display
from rich.console import Console
from rich.markdown import Markdown


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}

def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]

def summarize(url):
    try:
        res_site = fetch_website_contents(url)
        res = ollama.chat(
            model="llama3.2:1b",
            messages = [
            {
                'role': 'user',
                'content': f'Summarize the following website content in a few sentences also look for about page to get the maximum information about this website {res_site}',
            },
            {
                'role': 'system',
                'content': 'you are a helpful assistant'
            }
            ],
            options={
                'temperature': 1.5,
                'seed': 2,
            }
        )
        return res['message']['content']
    except Exception as e:
        print(f"Error summarizing {url}: {e}")
        print(f"Error summarizing {url}: {traceback.format_exc()}")




# def generate_response():
#     response = ollama.chat(
#         model='llama3.2:1b',
#         messages=[
#             {
#                 'role': 'user',
#                 'content': 'Why is the sky blue? Give me a short answer.',
#             },
#             {
#                 'role': 'system',
#                 'content': 'you are a snarky helpful assistant'
#             }
#         ]
#     )
    
#     # Print the full response text
#     print(response['message']['content'])

if __name__ == "__main__":
    # generate_response()
    URL = "https://drprettypsy.com/"
    val = summarize(URL)
    console = Console()
    console.print(Markdown(val))
    # print(val)