class FantasticBooks():
    # methods starting and ending in underscores (__init__, __len__, etc...) define behavour for particular syntax:
    # init defines what happens everytime 'FantasticBooks' is instatiated like FantasticBooks()
    # __len__ defines what happens when user calls len for that class only

    def __init__(self):
        self.title = 'The Fantastic Adventure'
        self.pages = [
            'It was the crack of dawn...',
            '...disaster strikes...',
            '...and they lived happily ever after'
        ]
        self.blurb = 'A high octane thriller'

    def __len__(self):
        return len(self.pages)    
    
    def __getitem__(self, idx):
        return self.pages[idx]
    
    def __str__(self) -> str:
        return self.title + ''.join(self.pages) + self.blurb



book = FantasticBooks()
print(len(book))
print(book)
book[2]