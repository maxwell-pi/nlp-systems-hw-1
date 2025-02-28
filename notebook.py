import json

class Notebook:
    def __init__(self, history_fname='history.json'):
        self.history_fname = history_fname
        self.notes_dict = {}
        try:
            self._load()
            print('History loaded successfully.')
        except FileNotFoundError:
            print('Failed to load history; starting anew.')
        except json.JSONDecodeError:
            print('History is corrupted; starting anew.')

    def __len__(self):
        return len(self.notes_dict)
    
    def __getitem__(self, title):
        if title in self.notes_dict:
            return self.notes_dict[title]
        else:
            raise KeyError(f'No note named {title}.')
        
    def __setitem__(self, title, body):
        if title in self.notes_dict:
            raise ValueError(f'A note named "{title}" already exists, and it\'s not my problem to deal with updates.')
        self.notes_dict[title] = body
        self._save()
        
    def __iter__(self):
        yield from self.notes_dict

    def __contains__(self, title):
        return title in self.notes_dict
    
    def items(self):
        yield from self.notes_dict.items()
    
    def find(self, term):
        return [title for title, body in self.notes_dict.items() if term in body]
    
    def _save(self):
        with open(self.history_fname, 'w') as f:
            json.dump(self.notes_dict, f)

    def _load(self):
        with open(self.history_fname) as f:
            self.notes_dict = json.load(f)
    
