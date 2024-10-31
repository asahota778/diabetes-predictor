##### Testing functions ####
import sys
import os
import pandas as pd
import numpy as np
import datetime
from geopy.distance import geodesic

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#Importing functions from hw4
from hw4 import count_simba,get_day_month_year,compute_distance,sum_general_int_list

# Test 1)
# Testing count_simba

def test_count_simba():
    # Test 1: Mixed case of "Simba"
    assert count_simba(["SIMBA is NO king", "simba", "that is not sim?ba, that Simba#$"]) == 3

    # Test 2: Empty list
    assert count_simba([]) == 0

    # Test 3: Large input with one instance of "Simba"
    assert count_simba(["Hakuna matata"] * 1000 + ["Simba"]) == 1

    # Test 4: List with special characters and multiples "Simba"
    assert count_simba(["Simba!!", "simba", "Simba's land"]) == 3

#Test 2)
#Testing get_day_month_year

def test_get_day_month_year():
    # Test 1: Empty list input
    dates = []
    expected_df = pd.DataFrame(columns=['day', 'month', 'year'])
    pd.testing.assert_frame_equal(get_day_month_year(dates), expected_df, check_dtype=False)
    
    # Test 2: List with a single date
    dates = [datetime.date(2021, 5, 15)]
    expected_df = pd.DataFrame({
        'day': [15],
        'month': [5],
        'year': [2021]
    })
    pd.testing.assert_frame_equal(get_day_month_year(dates), expected_df, check_dtype=False)

    # Test 3: List with dates from different centuries
    dates = [datetime.date(1800, 1, 1), datetime.date(2023, 6, 25)]
    expected_df = pd.DataFrame({
        'day': [1, 25],
        'month': [1, 6],
        'year': [1800, 2023]
    })
    pd.testing.assert_frame_equal(get_day_month_year(dates), expected_df, check_dtype=False)


#Test 3)
#Testing compute_distance

def test_compute_distance():
    # Test 1: Empty list
    coords = []
    expected_distances = []
    assert compute_distance(coords) == expected_distances

    # Test 2: Single pair of coordinates
    coords = [((0, 0), (0, 1))]
    expected_distances = [geodesic((0, 0), (0, 1)).kilometers]
    assert compute_distance(coords) == expected_distances

    # Test 3: Coordinates with zero distance
    coords = [((51.5, -0.1), (51.5, -0.1))]
    expected_distances = [0.0]  # Expecting zero distance
    assert compute_distance(coords) == expected_distances
    
    # Test 4: Different hemispheres
    coords = [((37.7749, -122.4194), (-33.8688, 151.2093))]
    expected_distances = [geodesic((37.7749, -122.4194), (-33.8688, 151.2093)).kilometers]
    assert compute_distance(coords) == expected_distances


#Test 4)
def test_sum_general_int_list():
    # Test 1: Complex nested list
    nested_list = [[6], 4, 5, [1, [4], [3, 5, [7, 8]], 10]]
    expected_sum = 53
    assert sum_general_int_list(nested_list) == expected_sum

    # Test 3: Empty list
    nested_list = []
    expected_sum = 0
    assert sum_general_int_list(nested_list) == expected_sum

    # Test 4: List with only integers
    nested_list = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_sum = 36
    assert sum_general_int_list(nested_list) == expected_sum

    # Test 5: List with deep nesting
    nested_list = [[[[[1]]]], 2, [[[3]], 4]]
    expected_sum = 10
    assert sum_general_int_list(nested_list) == expected_sum

    # Test 6: List with single integer
    nested_list = [68]
    expected_sum = 68
    assert sum_general_int_list(nested_list) == expected_sum
