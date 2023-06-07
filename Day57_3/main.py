from flask import Flask, render_template
import requests
from post import Post

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
objs = []
for resp in response:
    new_obj = Post(resp["id"],resp["title"],resp["subtitle"],resp["body"])
    objs.append(new_obj)

# for obj in objs:
#     print(obj.title)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", objs=objs)

@app.route("/blog/<int:post_id>")
def blogp(post_id):
    return render_template("post.html", objs=objs, post_id=post_id)

if __name__ == "__main__":
    app.run(debug=True)
