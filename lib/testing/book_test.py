#!/usr/bin/env python3

from lib.book import Book
import io
import sys

class TestBook:
    '''Book in book.py'''

    def test_has_title_and_page_count_and_year(self):
        '''has the title, page_count, and year_published passed to __init__, and values can be set to new instance.'''
        book = Book("And Then There Were None", 272, 1939)
        assert book.title == "And Then There Were None"
        assert book.page_count == 272
        assert book.year_published == 1939

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Book("And Then There Were None", "two hundred seventy-two", 1939)
        except ValueError:
            pass
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called.'''
        book = Book("The World According to Garp", 69, 1978)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"

    # Add any additional tests if needed, for example:
    # def test_invalid_year_published(self):
    #     '''Handle invalid year_published values if necessary.'''

