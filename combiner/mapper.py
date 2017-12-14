#!/usr/bin/env python
import sys


def _format_and_split(line, separator=','):
    # remove leading and trailing whitespace and split on separator
    return _skip_quoted(line.strip().split(separator))


def _emit(elements, separator='\t'):
    # convert all list items to string
    # by applying function str to all list items using function map
    elements_as_string = map(str, elements)
    # concatenation all list items by separator to one string
    output_string = separator.join(elements_as_string)
    print(output_string)


def _skip_quoted(line):

    if line[1][0] == '"':
        i = 1
        while line[i][-1] != '"':
            line[i] += ',' + line[i+1]
            line.remove(line[i+1])

    return line


def mapper():

    for line in sys.stdin:
        movie_title = "-"
        user_id = "-"
        ratings = "-"

        splits = _format_and_split(line)

        if len(splits) == 3:
            movie_id = splits[0]
            movie_title = splits[1]
        else:
            movie_id = splits[1]
            user_id = splits[0]
            ratings = splits[2]

        _emit([movie_id, ratings, movie_title])


if __name__ == '__main__':
    mapper()
