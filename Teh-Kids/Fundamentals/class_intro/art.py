# creatingFlaskApp
from flask import Flask,redirect

app = Flask(__name__)





@app.route("/")
def index():
    return "Hello C4T4, this is homepage"
    
@app.route("/About-me")
def index_2():
    info = ("Hello my name is Phuc \n gender:Male \n Age:17 \n Hobbies: Sport")
    return info
@app.route("/Hello/<name>")
def index_3(name):

    user = {
        "huy" : {
            "name" : "Nguyen Quang huy",
            "age" : 29
        },
        "don" : {
            "name" : "Pham Quy Don",
            "age" : 23
        }
    }
    text = ""
    if name not in user:
        return "user not found"

    for info in user[name]:
        text += info
        text += ":"
        text += str(user[name][info])
        text += "</br>"
    return text
    
    
        

@app.route("/School")
def hello():
    return redirect("http://techkids.vn ", code=302)



if __name__ =="__main__":
    app.run(debug=True)