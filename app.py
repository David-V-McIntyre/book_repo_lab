from flask import Flask. render_template

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def home():
    return render_template('index.html')