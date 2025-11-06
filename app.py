from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5500))
    app.run(debug=True)