from flask import Flask, render_template
import models

app = Flask(__name__)

@app.route("/")
def index():
	procedures = models.Procedure.query.limit(100).all()
	return render_template('home.html', procedures=procedures)

@app.route("/drg")
def list_drg():
	drg = models.DRG.query.limit(100).all()
	return render_template('drg_list.html', drg=drg)

@app.route("/drg/<int:drg_id>")
def show_provider_by_drg(drg_id):
	procedure = models.Procedure.query.filter(models.Procedure.DRG_Id == drg_id)
	return render_template('procedure.html', procedure=procedure[0])

@app.route('/procedure/<int:procedure_id>')
def show_procedure(procedure_id):
	procedures = models.Procedure.query.filter(models.Procedure.id == procedure_id)
	return render_template('procedure_list.html', procedure=procedures)

@app.route('/provider/<int:provider_id>')
def show_provider(provider_id):
	provider = models.Provider.query.filter(models.Provider.Provider_Id == provider_id)
	return render_template('provider.html', provider=provider[0])

if __name__ == "__main__":
    app.debug = True
    app.run()
