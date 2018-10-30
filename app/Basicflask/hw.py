from flask import Flask,redirect,url_for, render_template
app=Flask(__name__)

@app.route('/')
def index():
    name=',Prabhat'
    name1='Prabhat is awesome.'
    name2='Prabhat is the best.'
    return render_template('tmp.html',name=name,name1=name1,name2=name2)

if __name__=='__main__':
    app.run(debug=True)

