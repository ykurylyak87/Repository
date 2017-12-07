# inside the .split module use symbol how to split (',' '.' ' ' etc.)
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

# .pop(0) goes to the beginning    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

# .pop(0) goes to the end   
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Taken in a full sentence and retuns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

##### Instruction #####
# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> sentence
# 'All good things come to those who wait.'
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> sorted_sentence = ex25.sort_sentence(sentence)
# >>> sorted_sentence
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
    
# You can avoid typing "ex25." at the beginning
# of everyting if you import the module like thise instead:
# >>> from ex25 import *
# Then you can run the commands like this:
# print break_words(sentence)

