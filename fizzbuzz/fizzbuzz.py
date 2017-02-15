def fizzbuzz(number):
    string = ''

    if number%3 == 0:
        string += 'Fizz'

    if number%5 == 0:
        string += 'buzz'

    return string
