import os, sys
sys.path.insert(0, os.getcwd())


from app import app

if __name__ == '__main__':
    app.run(debug=True, port='3000')