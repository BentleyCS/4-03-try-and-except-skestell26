#No using the built in type check function
#https://www.w3schools.com/python/python_try_except.asp


def sum(arr: list):
    """
    Modify the function such that it returns the sum of all numbers within the given list.
    Ignores strings entirely, even if they represent numbers.
    :param arr:
    :return:
    """
    total = 0.0
    for num in arr:
        try:
            # Only allow int or float; raise TypeError for anything else
            if not isinstance(num, (int, float)):
                raise TypeError
            total += num
        except TypeError:
            # Ignore non-numeric values (strings, None, etc.)
            pass
    return total


def cleanData(rawData: list) -> list:
    cleaned = []
    for item in rawData:
        try:
            cleaned.append(float(item))
        except (ValueError, TypeError):
            pass
    return cleaned
    """
    modify the function such that it takes in a list as an argument will return a new list that
     contains only the valeus that can be typecast to a float.
    :param rawData:
    :return:
    """
    pass
def unreliableCalculator(divisors: list) -> list:
    results = []
    for value in divisors:
        try:
            results.append(100 / value)
        except Exception as e:
            results.append(type(e).__name__)
    return results
    """
    Modify the function such that it takes in a list as an argument and returns a new list where each
    index is 100 divided by the values from the input list.
    If division ever causes an error instead have the value be the type of error as a string.
    Example the list [100,50,25,"5"] as an argument would return [1, 2, 4, "TypeError"]
    :param divisors:
    :return:
    """
    pass


def upperAll(arr: list) -> None:
    """
    Uppercases all strings within the given list.
    Modifies the original list.
    """
    for i in range(len(arr)):
        if isinstance(arr[i], str):
            arr[i] = arr[i].upper()
    """
    Modiy the function such that is uppercases all strings within the given argument list.
    The string method .upper() turns all characters in as tirng uppercase.
    You should mpdify the original list not return a new list.
    :param arr:
    :return:
    """
    x = "hello"
    print(x)
    x = x.upper()
    print(x)


def firstItems(arr: list) -> list:
    result = []
    for item in arr:
        if isinstance(item, list):
            result.append(item[0])
        else:
            result.append(item)
    return result
    """
    Modify the function below such that given a list of values. Many of the list elements will be lists
    themselves. For any list element that is a list grab the first element from that list. If the list
    element is not a list then just grab the value itself.
    Create a new list of all the first indexes of inner lists or just values themselves.
    Example firstItems( [[1,2],[3,4],[5,6],[7,8]],9 ) == [1,3,5,7,9]
    :param arr:
    :return:
    """
    pass

