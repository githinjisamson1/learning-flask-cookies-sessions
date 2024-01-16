from flask import Flask, session, make_response

app = Flask(__name__)

app.secret_key = "qwertyasdfghzxcvbnm"

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
    

# !data is actuallly stored in browser => insecure
# browser makes request
# server generates an id to be key for user data(value) and stores in session store
# server sends response with Set-Cookie: session=qwertyasdfgzxc in response headers
# browser makes subsequent request with Cookie: session=qwertyasdfgzxc attached
# server looks up the Cookie hence persist previous context by using the id