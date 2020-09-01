from flask import Flask, render_template, request, redirect
import csv 

app = Flask(__name__)


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/')
def home():
	return render_template('./index.html')


def write_to_file(data):
	with open('./database.txt', mode = 'a') as file:
		email = data['email']
		subject = data['subject']
		message = data['message']
		# file.write('ffff')
		tra = file.write('\n{}, {}, {}'.format(email, subject, message))
		print(tra)

def write_to_csv(data):
	with open('database.csv', 'a') as file2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(file2, delimiter="," , quotechar = "|",quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		write_to_csv(data)
		return redirect('thankyou.html')

	else:
		return "something wrong"
