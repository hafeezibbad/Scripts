def title_case(title, minor_words=""):
    capt= " ".join([(word[0].upper()+word[1:].lower())
                      if word not in minor_words.lower().split(" ") else (word.lower())
                      for word in title.lower().split(" ")])
    return capt[0].upper()+capt[1:]
    
print title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
print title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
print title_case('the quick brown fox')
