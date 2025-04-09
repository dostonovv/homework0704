from app import FreamWorkApp

app = FreamWorkApp()

@app.route("/home")
def home(request , response):
    response.text = "Home page assalomu alekum"

@app.route("/about1")
def about(request , response):
    response.text = "About page bu dasturni Zoirjon va Qahhor yozgan"

@app.route("/about2")
def about(request , response):
    response.text = "Bu Abduqahhor haqidagi page\nuning yoshi 16da \nboyi : 1,75"

@app.route("/u/id")
def get_info(request , response , id):
    response.text = f"Siz {id} idli user siz"
