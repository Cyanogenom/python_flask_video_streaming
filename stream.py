from flask import Flask
from flask import stream_with_context, request, Response

app = Flask(__name__)

@app.route("/")
def main():
	return "stream route: /stream"

@app.route('/stream')
def streamed_response():
	def generate():
		print('gen')
		with open('film2.mov', 'rb') as file:
			print('open')
			yield file.read()
	print('stream')
	return Response(stream_with_context(generate()))

if __name__ == "__main__":
	app.run()