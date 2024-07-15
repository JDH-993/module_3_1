def string_info(string):
    k = (len(string), string.upper(), string.lower())
    print(k)
    count_calls()


def is_contains(string, list_to_search):
    string = string.lower()
    k = 0
    for i in list_to_search:
        i = i.lower()
        if i == string:
            k = k + 1
        else:
            k = k + 0
    if k > 0:
        print(True)
    else:
        print(False)
    count_calls()


def count_calls():
    global calls
    calls = calls + 1


calls = 0
string_info(input())
string_info(input())
is_contains(input(), list(map(str, input().split())))
is_contains(input(), list(map(str, input().split())))
print(calls)
