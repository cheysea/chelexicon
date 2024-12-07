def pass_note(do_you_love_me: str) -> str:
    """
   Pass a classmate a note that asks if they love you.

   :param do_you_love_me: Check yeees or noooooooo!
   :type do_you_love_me: str
   :raise `docs.example_docstrings.LoveError`: Raised if you checked 'no'.
   :return: A heartwarming message
   :rtype: str

   >>> pass_note('yes')
   Awww, I love you, tew!! ^~^
    """
    if isinstance(do_you_love_me, str):
        if do_you_love_me.lower() == 'yes':
            return "Awww, I love you, tew!! ^~^"
        elif do_you_love_me.lower() == 'no':
            return "But, senpai whyyyyy :((!"
        else:
            return "Well, okay, but thats a confusing response."
    else:
        raise LoveError("Uh, nvm. I dont know what to do with that answer.", None)

class LoveError(Exception):
    """
    Raised when I cant understand your answer.
    """
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors

check_box = pass_note('no')
print(check_box)