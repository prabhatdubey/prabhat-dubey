from flask import Flask,redirect,url_for, render_template
app=Flask(__name__)

@app.route('/index')
def index():
    user={'username':'Danell'}
    posts=[
        {
            'author':{'username':'Danell'},
            'body':'Prabhat is awesome'
            },
        {
            'author':{'username':'Amar'},
            'body':'Prabhat is the best'
            }
        ]
    return render_template('index.html',user=user,posts=posts)

if __name__=='__main__':
    app.run(debug=True)
