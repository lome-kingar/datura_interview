#!/usr/bin/env python3
import typing as tp
import re

import click


def _clean(s):
    return s.lower()


def iter_words(value) -> tp.Iterator[str]:
    for word in re.findall(r'\w+', value):
        yield _clean(word)


def word_count(value: str) -> dict[str, int]:
    ret = dict()
    for word in iter_words(value):
        if word in ret.keys():
            ret[word] += 1
        else:
            ret[word] = 1
    return ret


@click.command()
@click.argument('path', required=True, type=click.Path())
def word_count_command(path):
    try:
        with open(path, 'r') as f:
            res = word_count(f.read())
            print(res)
    except Exception as e:
        print(e)
        exit(2)


if __name__ == '__main__':
    word_count_command()
