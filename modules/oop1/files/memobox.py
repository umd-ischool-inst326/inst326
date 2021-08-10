class Memobox:
    """ A mechanism for users to communicate with each other.
    
    Attributes:
        name (str): the user's name.
        contacts (dict of str: Memobox): the people the user
            communicates with and their Memobox objects. Each key is the
            name of a contact; each value is that contact's Memobox.
        memos (list of (tuple of str, str)): unread memos received
            by the user. Each memo is a tuple consisting of a sender
            and a memo string.
    """
    def __init__(self, name):
        """ Initialize new Memobox object.
        
        Side effects:
           Sets attributes name, contacts, and memos.
        """
        self.name = name
        self.contacts = dict()
        self.memos = list()
    
    def add_contact(self, contact):
        """ Add contact to contacts.
        
        Args:
            contact (Memobox): Memobox of a contact to add.
        
        Side effects:
            Modifies contacts attribute.
        """
        self.contacts[contact.name] = contact
    
    def receive_memo(self, sender, memo):
        """ Receive a memo.
        
        Args:
            sender (Memobox): the sender of the memo.
            memo (str): the memo that was received.
        
        Side effects:
            Modifies memos attribute.
        """
        self.memos.append((sender.name, memo))
    
    def send_memo(self, recipient, memo):
        """ Send a memo.
        
        Args:
            recipient (str): the intended recipeint of the memo.
            memo (str): the memo to send.
        
        Side effects:
            Invokes recipient's receive_memo() method.
        
        Raises:
            ValueError: recipient is not listed in contacts.
        """
        if recipient not in self.contacts:
            raise ValueError(f"recipient {recipient} not in contacts")
        self.contacts[recipient].receive_memo(self, memo)
    
    def read_memos(self):
        """ Display all memos and clear memo queue.
        
        Side effects:
            Modifies memos attribute.
            Writes to stdout.
        """
        if len(self.memos) > 0:
            for sender, memo in self.memos:
                print(f"memo from {sender}: {memo}")
            self.memos = list()
        else:
            print("No new memos")
