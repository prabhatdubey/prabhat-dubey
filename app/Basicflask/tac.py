from flask import Flask,redirect,url_for, render_template
app=Flask(__name__)

@app.route('/')
def index():
    name='Prabhat is awesome'
    mylist=[12,14,20,45]
    mytuple=(10,20,30,40,50)
    mydict={'1':'Prabhat','2':'Adarsh','3':'Alfeen',}
    return render_template('tmp.html',name=name,mylist=mylist,mytuple=mytuple,mydict=mydict)

if __name__=='__main__':
    app.run(debug=True)
