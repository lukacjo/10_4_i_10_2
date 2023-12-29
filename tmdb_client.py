import requests
import random
import os

api_token = os.environ.get(
    "TMDB_API_TOKEN",
    "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NmNhYWFlN2JkOTNlY2E2ZjVlNjM3MGY4ZjQ1YjAyMSIsInN1YiI6IjY0MzdkYjI3MWQ1Mzg2MDBmNDBmNDIwMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SU0oZNmYrcBAucNtzZdvolzCYkqUXdO_FuLZDb7hIgs",
)


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


"""def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    repsonse = requests.get(endpoint, headers=headers)
    repsonse.raise_for_status()
    return repsonse.json()"""


def call_tmdb_api(
    endpoint,
):  # to pozwala nie powielaćtego całego tekstu w reszcie, tylko odpowiedni endpoint i dużo kodu mniej do pisania
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    data = data["results"]
    random.shuffle(data)
    return data[:how_many]


"""def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()"""


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:how_many]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()
