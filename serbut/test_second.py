import pytest

def test_failing():
    r = (1, 2, 3)
    excpected = (3, 2, 1)
    assert r != excpected

@pytest.mark.smoke
def test_failing2():
    assert (1, 2, 3) == (1, 2, 3)

def test_dict():    
    f1 = dict(name='serbut', desc='desc')
    f2 = dict(name='sebut', desc='desc')
    assert f1 != f2

@pytest.mark.smoke
@pytest.mark.regression
def test_except_failed():
    s = 1/0
    assert s is True

@pytest.mark.smoke
def test_except_passes():
    with pytest.raises(ZeroDivisionError):
        1/0

@pytest.mark.regression
def test_except_failed_2():
    with pytest.raises(ZeroDivisionError):
        raise Exception("My bad")
        1/0

def test_to_run():
    assert 1 == 1

@pytest.mark.skip(reason='misunderstood the API')
def test_to_skip():
    assert 1 == 0

@pytest.mark.xfail(reason='misunderstood the API')
def test_fail():
    assert 1 == 0


@pytest.fixture(scope='session')
def user_yield():
    print("setup user")
    # db.create_user
    yield 43
    print("remove user")
    # db.remove_user

@pytest.mark.fix
def test_user_age(user_yield):
    """Use fixture return value in a test."""
    assert user_yield == 43



@pytest.mark.fix
def test_user_name(user_yield):
    """Use fixture return value in a test."""
    assert user_yield == 44
