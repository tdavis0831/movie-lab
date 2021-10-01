


"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/movies")
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)


@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route("/users", methods = ["POST"])
def register_user():
    """View all users."""

    email = request.form.get("email") 

    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash("Email exists already, plese try logging in")
    else:
        crud.create_user(email, password)
        flash("Account Created")

    return redirect("/")

@app.route('/rating', methods =["POST"])
def create_rating():
    
    user = crud.get_user_by_email(email)
    movie = crud.get_movie_by_id(movie_id)
    rating = request.args.get()
    crud.create_rating(user, movie, )
    def create_rating(user, movie, score):

    return render_template(movie_details.html)





@app.route('/login', methods =["POST"])
def login():
    email = request.form.get("email") 

    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if user and user.password ==password:
        session["user_id"] = user.email
        flash("You are logged in")
    else:
        flash("The email or password you entered was incorrect.")
    return redirect("/")




@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)
        return render_template("user_details.html", user=user)





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)



if __name__ == "__main__":
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0", debug=True)
