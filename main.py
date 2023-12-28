from flask import Flask, render_template, request
import tmdb_client, random

app = Flask(__name__)

@app.route("/")
def homepage():

    butts = ["top_rated", "now_playing","upcoming","popular"]
    current_list = request.args.get('list_type')
    if current_list not in butts:
        movies = tmdb_client.get_movies(how_many=8, list_type="popular")
    else:
        movies = tmdb_client.get_movies(how_many=8, list_type=current_list)
    
    
    return render_template("homepage.html", movies=movies, butts=butts, current_list=current_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id,16)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images["backdrops"])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)


if __name__ == "__main__": 
    app.run(debug=True, port=3000)

