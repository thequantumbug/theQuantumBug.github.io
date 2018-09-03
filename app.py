from flask import Flask, redirect,render_template,url_for
app = Flask(__name__)

posts =[
  {
     'author':'x',
     'title':'why we are still miles away from artificial human mind ',
     'content':'gs',
     'date_posted':'April 20,2018'
  },
{
 'author':'ME',
 'title':'basic problems with the present state of quantum computers',
 'content':'gs1',
 'date_posted':'April 21,2018'
}

]
@app.route('/')
@app.route("/home")
def home():
    return render_template('index.html',posts=posts)
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
   app.run(debug ='true')
