# /api-bridge/app.py
from app import app
from app.config import PORT, DEBUG

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG, port=PORT)
