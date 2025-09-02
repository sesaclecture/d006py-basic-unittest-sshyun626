from my_func import odd_ox, mean_n, max_m, min_l

def test_odd_ox():
    assert False == odd_ox(7)
    assert True == odd_ox(-2)
    assert False == odd_ox(-12871241)
    assert False == odd_ox(13)
    assert True == odd_ox(0)
    assert False == odd_ox(1)

def test_mean_n():
    assert 2.5 == mean_n([1,2,3,4])
    assert 15.75 == mean_n([22,42,12,12,0,12,24,2])
    assert 8.5 == mean_n([1,2,3,34,5,6])
    assert "빈 리스트" == mean_n([])

def test_max_m():
    assert 4 == max_m([1,2,3,4])
    assert 42 == max_m([22,42,12,12,0,12,24,2])
    assert 34 == max_m([1,2,3,34,5,6])
    assert "빈 리스트" == max_m([])

def test_min_l():
    assert 1 == min_l([1,2,3,4])
    assert 0 == min_l([22,42,12,12,0,12,24,2])
    assert 1 == min_l([1,2,3,34,5,6])
    assert "빈 리스트" == min_l([])    
