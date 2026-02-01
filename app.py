from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from routes.chat_routes import chat_bp



app = Flask(__name__)
app.register_blueprint(chat_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5001,debug=True)