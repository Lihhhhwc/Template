"""Main module."""

def greeting(mood=None) -> None:
    """
    greeting(mood): Print a greeting depending on the mood.

    Parameters
    ----------
    mood : str, optional
           The mood of the greeting.

    """

    if mood is None:
        greeting = "Hallo!"

    elif mood == "sad":
        greeting = "How are you? I'm sad."

    elif mood == "good":
        greeting = "Hi, what's up?"

    elif moood == "formal":
        greeting = "Good day, how are you today?"

    else:
        greeting == "I did not get that."

    print(greeting)

    return(greeting)


