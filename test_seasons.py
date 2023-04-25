from seasons import check_birthday

def main():
    test_checkbirthday ()

def test_checkbirthday():
    assert check_birthday("2002-02-06") == ("2002", "02", "06")
    assert check_birthday("2002-02-06") == None

if __name__ == "__main__":
    main()