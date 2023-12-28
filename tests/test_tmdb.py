# BEZ PLIKU __init__.py wyskakuje-- ModuleNotFoundError: No module named 'main'
# to wstępne rozwiązanie
# do uzycia: pytest test_tmdb.py
import main, tmdb_client
from unittest.mock import Mock
def test_get_poster_url_uses_default_size():
    #przygotowanie dancyh
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    #porównanie wyników
    assert expected_default_size in poster_url
    #assert poster_url == "https://image.tmdb.org/t/p/s342/some-poster-path"
    
def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies(how_many=8, list_type="popular")
    assert movies_list is not None
    
def some_function_to_mock():
    raise Exception("Original was called")

def test_mocking(monkeypatch):#to i to poprzednie chyba niepotrzebne tylko takie przykłady nie ma to związku z zadaniem
    my_mock = Mock()
    my_mock.return_value = 2
    monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
    result = some_function_to_mock()
    assert result == 2
    #394
    
def test_get_movies_list(monkeypatch):
    #lista którą bedzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']
    
    requests_mock = Mock()
    # wynik wywoołania zapytania do API
    response = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list    
    
    
    
    #te dwa na dole chyba muszą być w tmdb_client.py. dodałem je tam
"""def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"        
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")"""
    
def test_get_single_movie(monkeypatch):
    mock_movie_id = ['Movie 1']
    
    requests_mock = Mock()
    # wynik wywoołania zapytania do API
    response = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movie_id
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    
    movie_id = tmdb_client.get_single_movie(mock_movie_id)
    assert movie_id == mock_movie_id    

def test_get_movie_images(monkeypatch):
    mock_image = ['Movie 1']
    
    requests_mock = Mock()
    # wynik wywoołania zapytania do API
    response = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_image
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    
    image = tmdb_client.get_movie_images(mock_image)
    assert image == mock_image

def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = {'id': 793723, 'cast': [{'adult': False, 'gender': 1, 'id': 18182, 'known_for_department': 'Acting', 'name': 'Olga Kurylenko', 'original_name': 'Olga Kurylenko', 'popularity': 11.477, 'profile_path': '/q0QXFRg5bSnaLjbvhamfclt0eId.jpg', 'cast_id': 1, 'character': 'Klara', 'credit_id': '601d1be1fb3f610041cdfdef', 'order': 0}, {'adult': False, 'gender': 1, 'id': 1431070, 'known_for_department': 'Acting', 'name': 'Marilyn Lima', 'original_name': 'Marilyn Lima', 'popularity': 4.338, 'profile_path': '/o3lYJpFWLJ6NAvVx6pzFr3dRrMM.jpg', 'cast_id': 3, 'character': 'Tania', 'credit_id': '601d1bf2aafebd003de62634', 'order': 1}, {'adult': False, 'gender': 0, 'id': 1671403, 'known_for_department': 'Acting', 'name': 'Michel Nabokoff', 'original_name': 'Michel Nabokoff', 'popularity': 1.563, 'profile_path': '/eOVfFjiWVgaV6cidbSUzH6kXxCZ.jpg', 'cast_id': 10, 'character': 'Leonid Kadnikov', 'credit_id': '602a69df8258fc003e9cd93e', 'order': 2}, {'adult': False, 'gender': 0, 'id': 102517, 'known_for_department': 'Acting', 'name': 'Martin Swabey', 'original_name': 'Martin Swabey', 'popularity': 1.62, 'profile_path': '/gBV5ElUGdHEIt1LZBdiAHaaIhR9.jpg', 'cast_id': 14, 'character': 'Lieutenant Eric Jaubert', 'credit_id': '6042a7e45258ae00453e4a29', 'order': 3}, {'adult': False, 'gender': 0, 'id': 1778568, 'known_for_department': 'Acting', 'name': 'Carole Weyers', 'original_name': 'Carole Weyers', 'popularity': 1.157, 'profile_path': '/x0AMwBYXFv2XkLPnp8rNDYoIpLc.jpg', 'cast_id': 15, 'character': 'Capitaine Catherine Muller', 'credit_id': '6042a80cd18572002ae63c0c', 'order': 4}, {'adult': False, 'gender': 0, 'id': 2965552, 'known_for_department': 'Acting', 'name': 'Andrey Gorlenko', 'original_name': 'Andrey Gorlenko', 'popularity': 1.532, 'profile_path': '/sAg4uptBeXDahtksUlT9dJMb9JM.jpg', 'cast_id': 4, 'character': 'Yvan Kadnikov', 'credit_id': '601d1c0bbb1057003d9fae3d', 'order': 5}, {'adult': False, 'gender': 0, 'id': 586193, 'known_for_department': 'Acting', 'name': 'Antonia Malinova', 'original_name': 'Antonia Malinova', 'popularity': 2.359, 'profile_path': '/eYfsNxJXyyMm85Tb6ntjfZOqhH7.jpg', 'cast_id': 16, 'character': 'Maria Kovalev', 'credit_id': '6042a8421108a80077838c08', 'order': 6}, {'adult': False, 'gender': 2, 'id': 2707004, 'known_for_department': 'Acting', 'name': 'Gabriel Almaer', 'original_name': 'Gabriel Almaer', 'popularity': 0.828, 'profile_path': '/ht7ixpjz0Kg46pGxpWcuJSXbxkr.jpg', 'cast_id': 17, 'character': 'Armurier', 'credit_id': '6042a87bc4ad59002a468dcc', 'order': 7}, {'adult': False, 'gender': 0, 'id': 2608223, 'known_for_department': 'Acting', 'name': 'Blaise Afonso', 'original_name': 'Blaise Afonso', 'popularity': 1.095, 'profile_path': '/jFDHB8TaAC5uav8yAnmGQA8WYjM.jpg', 'cast_id': 18, 'character': 'Soldat opération Sentinelle', 'credit_id': '6042a8aa6cf3d5002bc6b9b6', 'order': 8}, {'adult': False, 'gender': 2, 'id': 1556117, 'known_for_department': 'Acting', 'name': 'Guillaume Duhesme', 'original_name': 'Guillaume Duhesme', 'popularity': 0.6, 'profile_path': '/3rfCjVGZBr4eYzwlPsE1XF9m1Zk.jpg', 'cast_id': 2, 'character': 'Lieutenant Colonel', 'credit_id': '601d1be913a320003da59c69', 'order': 9}, {'adult': False, 'gender': 2, 'id': 1826552, 'known_for_department': 'Acting', 'name': 'Michel Biel', 'original_name': 'Michel Biel', 'popularity': 1.53, 'profile_path': '/ergeo2Drf1L5MkZOve9j2BowKPP.jpg', 'cast_id': 19, 'character': 'Aurélien', 'credit_id': '6042a8e327ff990045637933', 'order': 10}, {'adult': False, 'gender': 0, 'id': 1525450, 'known_for_department': 'Acting', 'name': 'Mustapha Makhada', 'original_name': 'Mustapha Makhada', 'popularity': 0.98, 'profile_path': None, 'cast_id': 20, 'character': 'Père syrien', 'credit_id': '6042a90c1108a80024d3863e', 'order': 11}, {'adult': False, 'gender': 0, 'id': 2999923, 'known_for_department': 'Acting', 'name': 'Salmane Taydi', 'original_name': 'Salmane Taydi', 'popularity': 0.6, 'profile_path': None, 'cast_id': 21, 'character': 'Fils syrien', 'credit_id': '6042a92299c964005a8b33d2', 'order': 12}, {'adult': False, 'gender': 2, 'id': 236905, 'known_for_department': 'Acting', 'name': 'Erico Salamone', 'original_name': 'Erico Salamone', 'popularity': 0.716, 'profile_path': '/nSUUnH7moMM00YRsNuG6PW8uuqG.jpg', 'cast_id': 22, 'character': 'Patron du Millenium', 'credit_id': '6042a9596cf3d5007059a8d2', 'order': 13}, {'adult': False, 'gender': 0, 'id': 2999925, 'known_for_department': 'Acting', 'name': 'Mikael Cassoli', 'original_name': 'Mikael Cassoli', 'popularity': 0.6, 'profile_path': None, 'cast_id': 23, 'character': 'Dealer', 'credit_id': '6042a9881108a80024d386c4', 'order': 14}, {'adult': False, 'gender': 2, 'id': 1186221, 'known_for_department': 'Writing', 'name': 'Olivier Massart', 'original_name': 'Olivier Massart', 'popularity': 1.214, 'profile_path': '/aR9SHZw0UwVzlHdZEO6nc9yykjE.jpg', 'cast_id': 24, 'character': 'Médecin de Tania', 'credit_id': '6042a9a85b2f47005a22807a', 'order': 15}, {'adult': False, 'gender': 0, 'id': 2999926, 'known_for_department': 'Acting', 'name': 'Doriane Pasquale', 'original_name': 'Doriane Pasquale', 'popularity': 0.6, 'profile_path': None, 'cast_id': 25, 'character': 'Jeune femme plage', 'credit_id': '6042a9cc50733c006fc0bcf0', 'order': 16}, {'adult': False, 'gender': 2, 'id': 54626, 'known_for_department': 'Acting', 'name': 'Alain Eloy', 'original_name': 'Alain Eloy', 'popularity': 1.292, 'profile_path': '/ugmjldocu7iMKJVFMxmvRO8Xygn.jpg', 'cast_id': 26, 'character': 'Médecin militaire', 'credit_id': '6042a9f8d1857200585118ca', 'order': 17}, {'adult': False, 'gender': 0, 'id': 2999927, 'known_for_department': 'Acting', 'name': 'Sarah Al Sayed Obeid', 'original_name': 'Sarah Al Sayed Obeid', 'popularity': 0.6, 'profile_path': None, 'cast_id': 27, 'character': 'Mère syrienne', 'credit_id': '6042aa3472c13e005b3a92a9', 'order': 18}, {'adult': False, 'gender': 1, 'id': 1366229, 'known_for_department': 'Acting', 'name': 'Stéphanie Pareja', 'original_name': 'Stéphanie Pareja', 'popularity': 0.6, 'profile_path': None, 'cast_id': 28, 'character': "Responsable du bar de l'hôtel", 'credit_id': '6042aa6384f249005a51ea35', 'order': 19}, {'adult': False, 'gender': 0, 'id': 2999928, 'known_for_department': 'Acting', 'name': 'Marine Duvivier', 'original_name': 'Marine Duvivier', 'popularity': 0.6, 'profile_path': None, 'cast_id': 29, 'character': 'Jeune femme boîte de nuit', 'credit_id': '6042aa80d1857200585119ab', 'order': 20}, {'adult': False, 'gender': 0, 'id': 1189101, 'known_for_department': 'Acting', 'name': 'Eric Castex', 'original_name': 'Eric Castex', 'popularity': 0.6, 'profile_path': None, 'cast_id': 30, 'character': 'Équipier de Catherine Muller', 'credit_id': '6042aa9fa35c8e005ab979a3', 'order': 21}, {'adult': False, 'gender': 0, 'id': 2999929, 'known_for_department': 'Acting', 'name': 'Grigory Collomb', 'original_name': 'Grigory Collomb', 'popularity': 0.6, 'profile_path': None, 'cast_id': 31, 'character': 'Garde du corps de Leonid', 'credit_id': '6042aacb99c964006ef86232', 'order': 22}, {'adult': False, 'gender': 0, 'id': 2999930, 'known_for_department': 'Acting', 'name': 'Baptiste Leclercq', 'original_name': 'Baptiste Leclercq', 'popularity': 0.6, 'profile_path': None, 'cast_id': 32, 'character': 'Soldat français', 'credit_id': '6042ab1c8813e4002aec94d7', 'order': 23}, {'adult': False, 'gender': 0, 'id': 2999931, 'known_for_department': 'Acting', 'name': 'Mélissa Humler', 'original_name': 'Mélissa Humler', 'popularity': 0.6, 'profile_path': None, 'cast_id': 33, 'character': 'Fausse médecin', 'credit_id': '6042ab3cc4ad59002a46906c', 'order': 24}], 'crew': [{'adult': False, 'gender': 1, 'id': 66869, 'known_for_department': 'Editing', 'name': 'Soline Guyonneau', 'original_name': 'Soline Guyonneau', 'popularity': 0.6, 'profile_path': None, 'credit_id': '60370625afa1b00041a759ba', 'department': 'Editing', 'job': 'Editor'}, {'adult': False, 'gender': 2, 'id': 84439, 'known_for_department': 'Directing', 'name': 'Julien Leclercq', 'original_name': 'Julien Leclercq', 'popularity': 1.681, 'profile_path': '/xP2OPVSMg2S19A1KzECnaqswqh8.jpg', 'credit_id': '601d1c3513a320003ca540f9', 'department': 'Directing', 'job': 'Director'}, {'adult': False, 'gender': 2, 'id': 84439, 'known_for_department': 'Directing', 'name': 'Julien Leclercq', 'original_name': 'Julien Leclercq', 'popularity': 1.681, 'profile_path': '/xP2OPVSMg2S19A1KzECnaqswqh8.jpg', 'credit_id': '601d1c71aede5900402b285b', 'department': 'Production', 'job': 'Producer'}, {'adult': False, 'gender': 2, 'id': 84439, 'known_for_department': 'Directing', 'name': 'Julien Leclercq', 'original_name': 'Julien Leclercq', 'popularity': 1.681, 'profile_path': '/xP2OPVSMg2S19A1KzECnaqswqh8.jpg', 'credit_id': '601d1c431108a8003dc4dfcd', 'department': 'Writing', 'job': 'Writer'}, {'adult': False, 'gender': 0, 'id': 581267, 'known_for_department': 'Acting', 'name': 'Matthieu Serveau', 'original_name': 'Matthieu Serveau', 'popularity': 0.828, 'profile_path': None, 'credit_id': '601d1c528a88b2003dba323b', 'department': 'Writing', 'job': 'Writer'}, {'adult': False, 'gender': 1, 'id': 1163450, 'known_for_department': 'Costume & Make-Up', 'name': 'Emmanuelle Youchnovski', 'original_name': 'Emmanuelle Youchnovski', 'popularity': 0.6, 'profile_path': '/pjLbPFpJEDOmO6U3E3LgQiYGAuK.jpg', 'credit_id': '60370663223e2000400496aa', 'department': 'Costume & Make-Up', 'job': 'Costume Design'}, {'adult': False, 'gender': 2, 'id': 1398142, 'known_for_department': 'Production', 'name': 'Julien Madon', 'original_name': 'Julien Madon', 'popularity': 0.98, 'profile_path': '/dPgD3WOORtJROP2GqiyxUT02AWy.jpg', 'credit_id': '601d1c63b97442003e2b5ce6', 'department': 'Production', 'job': 'Producer'}, {'adult': False, 'gender': 2, 'id': 1759596, 'known_for_department': 'Camera', 'name': 'Brecht Goyvaerts', 'original_name': 'Brecht Goyvaerts', 'popularity': 0.6, 'profile_path': None, 'credit_id': '60370592d132d6003fa37372', 'department': 'Camera', 'job': 'Director of Photography'}]}
   #jeszcze to ogarnąć
    
    requests_mock = Mock()
    # wynik wywoołania zapytania do API
    response = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    
    single_movie_cast = tmdb_client.get_single_movie_cast( movie_id=1, how_many=7)
    assert single_movie_cast == mock_movie_cast['cast'][:7]