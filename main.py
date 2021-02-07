from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'key1':'data1',
        'key2':'data2',
        'key3':'data3',
        'key4':'data4'
    },
    {
        'key1': 'data5',
        'key2': 'data6',
        'key3': 'data7',
        'key4': 'data8'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
