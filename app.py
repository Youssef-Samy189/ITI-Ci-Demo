from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    print ("Hello ITI ^.^")
    return "Nice to meet you"

if __name__ == "__main__" :
        app.run()
