def check_answer(user_answer, correct_answer):
    '''Tests if the user's answer is the same 
    as the correct answer, regardless of case 
    and blank space before and after the user response
    for example, if the answer is "Chicago" the
    "chicago" and "    chicago    " and "Chicago   " are all
    correct.'''

    if user_answer.strip().casefold() == correct_answer.strip().casefold():
        return True
    else:
        return False

