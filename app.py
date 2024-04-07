from flask import Flask, render_template, request
import pdfkit
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe" # this needs to be changed
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    gender = request.form['gender']

    # Generate the dynamic HTML page
    html = render_template('dynamic_page.html', name=name, email=email, age=age, gender=gender)

    # Convert the HTML to a PDF file
    pdfkit.from_string(html, 'output.pdf', configuration=config)

    return 'Registration successful! PDF generated.'

if __name__ == '__main__':
    app.run(debug=True)