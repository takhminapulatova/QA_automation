def test_total_price():
    price = 100
    tax = 10
    expected_total = 110

    actual_total = price + tax

    assert actual_total == expected_total
