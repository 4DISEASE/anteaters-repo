from bulkofproject.models import maindb

def query(key):
    #empty list
    list = []

    #query database
    dbdict = maindb.query.all()
    #create dictionary for every user
    for entry in dbdict:
        entry = {'user':entry.username, 'song':entry.song, 'artist':entry.artist}
        #add dictionary to dict list
        list.append(entry)

    #turn list into dictionary
    dictionary = {key:list}
    return dictionary

def filter(dictionary, key, category, filter):
    #turn dictionary into a list
    dblist = dictionary[key]
    #empty list
    filtered = []

    #filter list
    for entry in dblist:
        if entry[category] == filter:
            filtered.append(entry)

    #make dictionary of new list
    filterdict = {key:filtered}
    return filterdict
