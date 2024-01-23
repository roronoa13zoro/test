from flask import *
#追加------------
import sukii
#------------------

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
    
#変更&追加-----------------------
@app.route("/nittei")
def nittei():
	return render_template('nittei.html')

@app.route("/skiing", methods=['GET','POST'])
def skiing():
	if request.method == 'GET':
		return render_template('skiing.html')
	elif request.method == 'POST':
		lift1 = request.form['lift1']
		wear1 = request.form['wear1']
		chose1 = request.form['chose1']
		change1 = request.form['change1']
		lift2 = request.form['lift2']
		wear2 = request.form['wear2']
		chose2 = request.form['chose2']
		change2 = request.form['change2']
		result = sukii.client(lift1, wear1, chose1, change1, lift2, wear2, chose2, change2)
		return render_template('skiing.html', lift1 = result[0], wear1 = result[1], chose1 = result[2], change1 = result[3], lift2 = result[4], wear2 = result[5], chose2 = result[6], change2 = result[7], money = result[8])
		#pas = request.form['pas']
		#result = sukii(id, pas)
		#if len(result) == 2:
		#	return render_template('skiing.html', id=result[0],pas=result[1])
		#else:
		#	return render_template('calc.html',error=result)
@app.route("/Rebuilding", methods=['GET','POST'])
def Rebuilding():
	return render_template('calc.html')

@app.route("/rentalcar", methods=['GET','POST'])
def rentalcar():
	return render_template('calc.html')
#-------------------------------------
	

if __name__ == '__main__':
    app.run(port=5555,host="0.0.0.0")