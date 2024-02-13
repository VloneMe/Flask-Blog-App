from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Corey schafer',
        'title': 'Blog post',
        'content': "First post Content",
        'date_posted': 'April 20, 2018'
    },{
        'author': 'John Doe',
        'title': 'Blog post',
        'content': "Second post Content",
        'date_posted': 'March 05, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")


if __name__ == '__main__':
    app.run(debug=True)
