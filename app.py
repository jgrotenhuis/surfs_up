from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world(df):
	return 'Hello world'

print(df)