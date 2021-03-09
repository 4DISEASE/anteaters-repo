#imports
from bulkofproject import db

#database config
##create models for database
class maindb(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    song = db.Column(db.String)
    artist = db.Column(db.String)

    ##printable version of database
    def __repr__(self):
        return f"User('{self.username}', '{self.song}', '{self.artist}')"