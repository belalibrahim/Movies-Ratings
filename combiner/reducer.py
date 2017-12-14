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

    last_user_id = None
    current_country = "-"

    for line in sys.stdin:
        user_id, movie_id, country = _format_and_split(line)

        if not last_user_id or last_user_id != user_id:
            last_user_id = user_id
            current_country = country
        elif user_id == last_user_id:
            country = current_country

            _emit([movie_id, country])


if __name__ == '__main__':
    reducer()
