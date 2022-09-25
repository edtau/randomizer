string = "test string123456"
lst = []

new_string = ""
    digits = ""
    for letter in string:
      if letter.isdigit():
        digits = digits + letter
      else:
        lst.append(letter)
    random.shuffle(lst)
    for letter in lst:
        new_string = new_string + letter
    if len(digits) > 0:
        new_string = new_string + str(digits)
    return f'{string} --> {new_string}'
