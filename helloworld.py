from flask import Flask
#https://github.com/Neilaj/firstapp.git
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello PrabhuJI , you are the greatest."

if __name__ == '__main__':
	app.run(port=5000, debug=True)


	