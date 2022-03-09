from flask import Flask, flash, render_template, request
app = Flask(__name__)

@app.route("/WelcomeToSneakersByLou")
def welcome():
    return render_template('Welcome.html')


@app.route("/welcome")
def welcomeFunction():
    return render_template('Welcome.html')


@app.route("/restorations")
def restorationFunction():
    return render_template('restorations.html')


@app.route("/selling")
def sellingFunction():
    return render_template('selling.html')


@app.route("/contact")
def contactFunctions():
    return render_template('contactus.html')


    
if __name__ == "__main__":  
    app.run(debug=True)
