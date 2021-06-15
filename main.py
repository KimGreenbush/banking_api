#run project from here
from src.app import app
import src.controllers.api_controllers

if __name__ == '__main__':
    app.run(debug=True)