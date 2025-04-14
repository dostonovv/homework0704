from app import FrameWorkApp
import json

app = FrameWorkApp()


def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)

    return users


def load_view():

    with open("view.json", "r") as file:
        data = json.load(file)

    return data


cnt = load_view()


@app.route("/home")
def home(request, response):
    global cnt
    cnt["home"] += 1
    with open("view.json", "w") as file:
        json.dump(cnt, file)
    response.text = f"Home pagedan uyquli salom! -> Korichlar soni: {cnt['home']}"


@app.route("/about")
def about(request, response):
    global cnt
    cnt["about"] += 1
    with open("view.json", "w") as file:
        json.dump(cnt, file)
    response.text = f"About pagedan Azizxonga salom! -> Korishlar soni: {cnt['about']} "


sntp = load_users()


@app.route("/u/{id}")
def get_info(request, response, id):
    global sntp
    users = load_users()
    user = users.get(id, "Bunday user yo'q!")

    sntp[id]["int"] += 1
    with open("users.json", "w") as file:
        json.dump(sntp, file)

    response.text = json.dumps(user)