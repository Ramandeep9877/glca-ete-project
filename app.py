# here we install flask to use its some functionality into our project

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template('home.html')



if __name__=='__main__':
    app.run()


# the above code for creation of our application(app and if code) the code we write between this 2 becouse we want code in a running statement
