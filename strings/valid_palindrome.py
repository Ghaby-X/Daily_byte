def validPalindrom(a: str) -> bool :
    def pre_process(b: str) -> str:
        return filter(lambda p: p.isalnum(),b.lower())
        
    processed = ''.join(pre_process(a))

    print(processed == processed[::-1])

validPalindrom('level')
validPalindrom('algorithm')
validPalindrom('A man, a plan, a canal: Panama.')