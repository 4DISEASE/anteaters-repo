#import from __init__.py file
from bulkofproject import app, db

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True, port = 8080)