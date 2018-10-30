from flask import render_template, session, redirect, url_for
from app import app
from .forms import NameForm

@app.route('/',methods=['Get','POST'])
@app.route('/index',methods=['Get','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        form.name.data=''
    return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session('name'))

