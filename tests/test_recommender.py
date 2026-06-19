import sys
sys.path.append('.')

from src.recommender import recommend_movies

def test_inception():
    results = recommend_movies("Inception")
    assert len(results) == 3
    print(" Test 1 Passed: Inception returns 3 recommendations")

def test_invalid_movie():
    result = recommend_movies("Batman")
    assert "not found" in result
    print(" Test 2 Passed: Invalid movie handled correctly")

def test_titanic():
    results = recommend_movies("Titanic")
    assert len(results) == 3
    print("Test 3 Passed: Titanic returns 3 recommendations")

# Run all tests
test_inception()
test_invalid_movie()
test_titanic()

print("\n All tests passed!")