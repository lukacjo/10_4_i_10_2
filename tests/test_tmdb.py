# BEZ PLIKU __init__.py wyskakuje-- ModuleNotFoundError: No module named 'main'
# to wstępne rozwiązanie
# do uzycia: pytest test_tmdb.py
import main, tmdb_client
from unittest.mock import Mock


def perform_api_test(monkeypatch, api_function, mock_input, expected_output):
    with monkeypatch.context() as m:
        requests_mock = Mock()
        response = requests_mock.return_value
        response.json.return_value = mock_input
        m.setattr("tmdb_client.requests.get", requests_mock)

        result = api_function(mock_input)

    assert result == expected_output


def test_get_single_movie(monkeypatch):
    mock_movie_data = ["Movie 1"]
    perform_api_test(
        monkeypatch, tmdb_client.get_single_movie, mock_movie_data, mock_movie_data
    )


def test_get_movie_images(monkeypatch):
    mock_image = ["Image 1"]
    perform_api_test(monkeypatch, tmdb_client.get_movie_images, mock_image, mock_image)


def test_get_single_movie_cast(monkeypatch):
    movie_id = 123
    mock_response = {"id": movie_id, "cast": [{"name": "Actor 1"}, {"name": "Actor 2"}]}

    mock = Mock()
    mock.return_value = mock_response
    monkeypatch.setattr(tmdb_client, "call_tmdb_api", mock)

    result = tmdb_client.get_single_movie_cast(movie_id, 2)

    assert result == mock_response["cast"]


def test_call_tmdb_api(monkeypatch):
    endpoint = "movie/123"
    mock_data = {"id": 123, "title": "Movie 1"}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_data
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    result = tmdb_client.call_tmdb_api(endpoint)

    assert result == mock_data


def test_get_poster_url():
    poster_api_path = "123123"
    size = "w500"
    expected_url = f"https://image.tmdb.org/t/p/{size}/{poster_api_path}"

    url = tmdb_client.get_poster_url(poster_api_path, size)

    assert url == expected_url


def test_get_movies(monkeypatch):
    how_many = 8
    list_type = "now_playing"
    mock_data = {
        "results": [{"id": i, "title": f"Movie {i}"} for i in range(1, how_many + 1)]
    }

    monkeypatch.setattr("tmdb_client.get_movies_list", lambda x: mock_data)

    movies = tmdb_client.get_movies(how_many, list_type)

    assert len(movies) == how_many


def test_get_movies_list(monkeypatch):
    list_type = "top_rated"
    mock_data = {"results": [{"id": 1, "title": "Movie 1"}]}

    monkeypatch.setattr("tmdb_client.call_tmdb_api", lambda x: mock_data)

    movies_list = tmdb_client.get_movies_list(list_type)

    assert movies_list == mock_data
