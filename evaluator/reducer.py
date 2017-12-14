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


def reducer():

    last_movie = None
    rating_count = 0

    for line in sys.stdin:
        movie, rating = _format_and_split(line)
        if not last_movie:
            last_movie = movie
            rating_count = 1

        if movie == last_movie:
                rating_count = rating_count + 1
        else:
            _emit([last_movie, rating_count])
            last_movie = movie
            rating_count = 1

    _emit([movie, rating_count])


if __name__ == '__main__':
    reducer()
