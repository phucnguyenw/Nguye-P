from flask import Flask,render_template,redirect
import mLab
from modules.movie import Movie
app = Flask(__name__)

mLab.connect()

@app.route("/")
def index():
    movie_list = Movie.objects()
    first_movie = movie_list[0]
    return render_template("index.html",movie=first_movie)
if __name__=="__main__":
    app.run(debug=True)