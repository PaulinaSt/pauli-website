from flaskblog import app #will import from init file

if __name__ == '__main__': #this conditional is only true if we run the scrit directly
    app.run(debug=True)