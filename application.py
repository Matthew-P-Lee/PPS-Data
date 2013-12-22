from flask import Flask, render_template

import models


app = Flask(__name__)

@app.route("/")
def index():
	p = Procedure()
	txt = p.GetProcedures()
	return render_template('home.html', name=txt)

if __name__ == "__main__":
    app.debug = True
    app.run()
