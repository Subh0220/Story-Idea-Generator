import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"))

def generate_story_idea(genre, theme, character):
    prompt = f"""
    Generate a creative story idea with the following:
    - Genre: {genre}
    - Theme: {theme}
    - Main Character: {character}
    The idea should be unique, engaging, and suitable for a short story or novel.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    
    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    genre = input("Enter a genre (e.g., fantasy, sci-fi, romance): ")
    theme = input("Enter a theme (e.g., friendship, survival, betrayal): ")
    character = input("Enter a main character type (e.g., detective, wizard, alien): ")

    idea = generate_story_idea(genre, theme, character)
    print("\n✨ Your Story Idea:")
    print(idea)