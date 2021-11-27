from flask import Flask
from views import views 
#start flask website
app = Flask(__name__)
#register prefix
app.register_blueprint(views, url_prefix="/views")
#run the program with debug and port 8000 instead of standard 5000
if __name__ == "__main__":
    app.run(debug=True, port=8000)

