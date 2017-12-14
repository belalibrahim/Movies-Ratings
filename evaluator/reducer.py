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
    current_country = ""
    country_count = 0

    for line in sys.stdin:
        line = line.strip()
        movie_id, country = line.split("\t")
        if not last_movie_id:
            last_movie_id = movie_id
            current_country = country
            country_count = 1

        if movie_id == last_movie_id:
            if country != current_country:
                country_count = country_count + 1
                current_country = country
        else:
            _emit([last_movie_id, country_count])
            last_movie_id = movie_id
            current_country = country
            country_count = 1

    _emit([movie_id, country_count])


if __name__ == '__main__':
    reducer()
