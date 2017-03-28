import datetime

# Store the next available is for all new notes
last_id = 0


class Note:
    ''' Represents a note in the notebook. Match against a string
        in searches and stores tag for each note. '''

    def __init__(self, memo, tags=''):
        ''' initialise a note with memo and optional tags.
            Automatically set the note's creation date and a unique id '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, ftr):
        return ftr in self.memo or ftr in self.tags


class Notebook:
    ''' Represents the notebook which is a collection of notes '''
    
    def __init__(self):
        self.notes = []
        
    def new_note(self, memo, tags=''):
        ''' Create a new note and add it to the notebook '''
        self.notes.append(Note(memo, tags=''))

    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        self._find_note(note_id).tags = tags
        
    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
    def search(self, ftr):
        return [note for note in self.notes if note.match(ftr)]


