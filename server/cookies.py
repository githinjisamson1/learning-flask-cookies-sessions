from flask import Flask, make_response, request

app = Flask(__name__)

# read a cookie
@app.route("/")
def home():
    theme = request.cookies.get("theme")
    return f"Theme is {theme}"

# set a cookie
@app.route("/cookie")
def cookie():
    response = make_response("<h1>Cookie set</h1>")
    response.set_cookie("theme", "dark")
    return response

if __name__ == "__main__":
    app.run(port=5555, debug=True)
    
    
# !data is stored in browser => insecure
# !Cookie is in text format, user can modify
# !hence cannot store sensitive information using cookies
# browser makes request
# server sends response with Set-Cookie: theme=dark in response headers
# browser makes subsequent request with Cookie attached
# server looks up the Cookie: theme=dark hence persist previous context