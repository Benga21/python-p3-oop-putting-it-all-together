#!/usr/bin/env python3

import pytest
from lib.shoe import Shoe
import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand, size, and color passed to __init__, and values can be set to new instance.'''
        stan_smith = Shoe("Adidas", 9, "White")
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9
        assert stan_smith.color == "White"

    def test_requires_int_size(self):
        '''raises ValueError if size is not an integer.'''
        with pytest.raises(ValueError, match="size must be an integer"):
            Shoe("Adidas", "not an integer", "White")

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9, "White")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Your shoe is as good as new!\n"
    
    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and sets it to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9, "White")
        stan_smith.cobble()
        assert stan_smith.condition == "New"
