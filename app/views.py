from app import app
from flask import render_template, url_for


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cat')
def cat():
    cat_image_url = url_for('static', filename='images/cat.jpg')
    return render_template('cat.html', cat_image_url=cat_image_url)

@app.route('/dog')
def dog():   
    dog_image_url = url_for('static', filename='images/dog.jpg')
    return render_template('dog.html', dog_image_url=dog_image_url)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
