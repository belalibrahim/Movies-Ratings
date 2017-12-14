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

    last_movie_id = None
    current_movie = "-"

    for line in sys.stdin:
        movie_id, ratings, movie_title = _format_and_split(line)

        if not last_movie_id or last_movie_id != movie_id:
            last_movie_id = movie_id
            current_movie = movie_title
        elif movie_id == last_movie_id:
            movie_title = current_movie

            _emit([movie_title, ratings])


if __name__ == '__main__':
    reducer()
