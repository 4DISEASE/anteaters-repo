#import from __init__.py file
from bulkofproject import app

if __name__ == '__main__':
    app.run(debug = True, port = 8080)