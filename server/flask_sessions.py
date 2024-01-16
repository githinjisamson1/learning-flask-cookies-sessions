from flask import Flask, session, make_response
from flask_session import Session

app = Flask(__name__)

# data is not stored forever/permanently
app.config["SESSION_PERMANENT"] = False

# data is stored as files
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# code below remains the same
@app.route("/")
def home():
    response = make_response("<h1>Session set</h1>")
    session["username"] = "John"
    return response

@app.route("/get")
def get_username():
    username = session.get("username", None)
    return f"Username is {username}"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
    

# !data is stored in server => secure
# no need for secret key
# if the ID is tampered with, server knows that data is tampered with by the user