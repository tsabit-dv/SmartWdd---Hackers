from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    subprocess.Popen(["streamlit", "run", "streamlit_app.py"])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
