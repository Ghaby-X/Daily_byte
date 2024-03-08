def string_reverse( a: str) -> str:
    reverse = ''
    for i in range(0, len(a)):
        reverse = a[i] + reverse
    print(reverse)

string_reverse('cat')
string_reverse('The Daily Byte')
string_reverse('civic')
