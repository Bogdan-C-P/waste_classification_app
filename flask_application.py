from flask import Flask,flash, url_for, request, render_template, redirect, jsonify
from flask_jsglue import JSGlue # this is use for url_for() working inside javascript which is help us to navigate the url
import load_model
import os
from werkzeug.utils import secure_filename
from load_model import classify_waste
UPLOAD_FOLDER = 'static/uploads/'




ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

application = Flask(__name__)

application.secret_key = "secret key"
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# JSGlue is use for url_for() working inside javascript which is help us to navigate the url
jsglue = JSGlue() # create a object of JsGlue
jsglue.init_app(application) # and assign the app as a init app to the instance of JsGlue

load_model.load_artifacts()
#home page
@application.route("/")
def home():
    return render_template('upload.html')


@application.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		x,y= classify_waste(os.path.join(application.config['UPLOAD_FOLDER'], filename))
		flash(f"Your image has been classified as: {str(x)}",category='1')
		flash(f"{str(y)}",category='2')
		#os.remove(os.path.join(application.config['UPLOAD_FOLDER'], filename))
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)



@application.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
if __name__ == "__main__":
    application.run()