from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx', 'pptx', 'txt'}

# Example subjects. Modify as needed.
SUBJECTS = [
    'Mathematik',
    'Deutsch',
    'Englisch',
    'Physik',
    'Chemie'
]

# Ensure upload directories exist for each subject
for subject in SUBJECTS:
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], subject), exist_ok=True)

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form.get('subject')
        file = request.files.get('file')
        if subject in SUBJECTS and file and allowed_file(file.filename):
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], subject, file.filename)
            file.save(save_path)
            return redirect(url_for('index'))
    return render_template('index.html', subjects=SUBJECTS)

if __name__ == '__main__':
    app.run(debug=True)
