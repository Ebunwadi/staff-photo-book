from app import create_app
from config.config import DevConfig
# from waitress import serve

app = create_app(DevConfig)

#run with 
if __name__ == "__main__":
    # serve(app, host='127.0.0.1', port='5000')
    app.run()