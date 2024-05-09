import requests
import pandas as pd


def get_anime_data():
    anime_query = input('What anime are you interested in? ')
    response = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_query}&sfw")
    ani_data = 'data'
    ind = response.json()[ani_data]

    titles = []
    types = []
    ratings = []
    durations = []
    synopses = []

    for anime_info in ind:
        titles.append(anime_info['title_english'])
        types.append(anime_info['type'])
        ratings.append(anime_info['rating'])
        durations.append(anime_info['duration'])
        synopses.append(anime_info['synopsis'])

    anime_data = pd.DataFrame({
        'Title': titles,
        'Type': types,
        'Rating': ratings,
        'Duration': durations,
        'Synopsis': synopses
    })

    print(anime_data)
    anime_data.to_csv("Anime.csv", index=False)


def main():
    get_anime_data()


if __name__ == "__main__":
    main()
