import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}/images".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMDJhMzM0ZTFlZTlmZGMwMzYyZDc1YzFiNDJlZWUyMyIsInN1YiI6IjY1ZDA3OGE4MWQzMTQzMDE4NGI5ZDE0YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CdARUxHhe50RMwojcYxW_iU2FK3UBoYY12Y1uUkh-HI"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    poster_path = data["backdrops"][2]['file_path']
    # print(len(data["backdrops"]))
    full_path = "https://image.tmdb.org/t/p/w500"+poster_path
    return full_path

print(fetch_poster(19995))