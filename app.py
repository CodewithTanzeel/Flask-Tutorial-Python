from flask import Flask , render_template, url_for

app = Flask(__name__)

@app.route('/')#route handler
def index():# route function
    return render_template('index.html')#return pathway 

@app.route('/member.html')
def membership():
    return render_template('member.html')

if __name__ == "__main__":
   app.run(debug=True)



   