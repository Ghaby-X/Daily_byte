#Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
#Note: neither binary string will contain leading 0s unless the string itself is 0

#Ex: Given the following binary strings...

#"100" + "1", return "101"
#"11" + "1", return "100"
#"1" + "0", return  "1"

def add_binary(s1 : str, s2: str) -> None:
    answer = ''

    s1_cur = len(s1) - 1
    s2_cur = len(s2) - 1

    carry='0'

    while s1_cur >= 0 or s2_cur >= 0 or carry != '0':
        s1_var = s1[s1_cur] if int(s1_cur) >= 0 else '0'
        s2_var = s2[s2_cur] if int(s2_cur) >= 0 else '0'

        sum = int(s1_var) + int(s2_var) + int(carry)
        carry = str(sum // 2)
        
        answer = ('0' + answer) if sum >= 2 else (str(sum) + answer)


        s1_cur = s1_cur - 1
        s2_cur = s2_cur - 1
        
        # # Debug-tests
        # print(f's1_var is {s1_var}')
        # print(f's2_var is { s2_var }')
        # print(f'carry is { carry }')
        # print(f'sum is { sum }')
        # print(f'answer: { answer }')
    print(int(answer))

add_binary('100', '1')
add_binary('11', '1')
add_binary('1', '0')


#custom tests
add_binary("1101", "100") # answer 10001