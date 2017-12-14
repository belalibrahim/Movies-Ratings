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


def mapper():

    for line in sys.stdin:
        movie_id = "-"
        country = "-"

        splits = _format_and_split(line)

        if len(splits) == 5:
            user_id = splits[0]
            country = splits[4]
        else:
            user_id = splits[1]
            movie_id = splits[2]

        _emit([user_id, movie_id, country])


if __name__ == '__main__':
    mapper()
