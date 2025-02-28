from flask import Flask,render_template , url_for

app = Flask(__name__)

posts = [
    {
        'author':'Tamanna ',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'May 21,2024'
    },
    {
         'author':'Azlan',
         'title':'Blog post 2',
         'content':'Second post content',
         'date_posted':'May 22,2024'
    }
]

@app.route("/")
def hello():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='About')

if __name__=="__main__":
    app.run(debug=True)


