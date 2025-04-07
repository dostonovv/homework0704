from app import FreamWorkApp

app = FreamWorkApp()

@app.route("/home")
def home(request , response):
    response.text = "Home page assalomu alekum"

@app.route("/about")
def about(request , response):
    response.text = "About page bu dasturni Zoirjon va Qahhor yozgan"