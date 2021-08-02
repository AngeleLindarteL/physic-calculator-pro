from flask import Flask, render_template, request
from forms.tankForm import tankForm
from forms.fillForm import fillForm
from models.Tanque import Tanque
from models.Relleno import Relleno

app = Flask(__name__)
app.config['SECRET_KEY'] = '3nju1nxkjah2m3n5'


@app.route('/', methods=["GET","POST"])
def index():
    form = tankForm(request.form)
    fillform = fillForm(request.form)
    if request.method == "POST":
        obj = Tanque(form.diametro.data,form.alto.data,form.medida.data)
        fillObj = Relleno(fillform.nombre.data,fillform.cantidad.data,fillform.medidar.data,fillform.quest.data)
        print(fillObj.medida)
        return render_template('result.html',obj=obj, fillObj=fillObj)
    return render_template('index.html',form=form, fillform=fillform)