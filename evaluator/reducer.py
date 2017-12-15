#!/usr/bin/env python
import sys


def _format_and_split(line, separator='\t'):
    # remove leading and trailing whitespace and split on separator
    return line.strip().split(separator)


def _emit(elements, separator='\t'):
    # convert all list items to string
    # by applying function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print(output_string)


def calculations(rating_sum, rating_count, key=4):
    if key == 1:
        return rating_count
    elif key == 2:
        return rating_sum
    elif key == 3:
        return rating_sum / rating_count
    elif key == 4:
        avg = rating_sum / rating_count
        if avg > 4:
            return 'Wonderful Movie', str(avg)
        elif avg > 2.5:
            return 'Good Movie', str(avg)
        elif avg > 1:
            return 'Boring Movie', str(avg)
        else:
            return 'Bad Movie', str(avg)


def reducer():

    last_movie = None
    rating_count = 0
    rating_sum = 0

    for line in sys.stdin:
        movie, rating = _format_and_split(line)
        if not last_movie:
            last_movie = movie

        if movie == last_movie:
            rating_sum = rating_sum + float(rating)
            rating_count = rating_count + 1
        else:
            calc = calculations(rating_sum, rating_count)
            _emit([last_movie, calc])
            rating_sum = 0
            last_movie = movie
            rating_sum = rating_sum + float(rating)
            rating_count = 1

    calc = calculations(rating_sum, rating_count)
    _emit([movie, calc])


if __name__ == '__main__':
    reducer()
