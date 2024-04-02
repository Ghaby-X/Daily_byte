# This question is asked by Amazon. Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

# Ex: Given the following strings...

# s = "ABC#", t = "CD##AB", return true
# s = "como#pur#ter", t = "computer", return true
# s = "cof#dim#ng", t = "code", return false

def compare_strokes(s: str, t: str):
    
    def preprocess( strokes: str):
        stroke_array = []
        for i in strokes:
            if stroke_array and i == '#':
                stroke_array.pop()
                continue
            
            stroke_array.append(i)

        return stroke_array
    
    s_processed = preprocess(s)
    t_processed = preprocess(t)
    
    if s_processed == t_processed:
        print('true')
        return
    
    print('false')
    return

compare_strokes("ABC#", "CD##AB") # return true
compare_strokes("como#pur#ter", "computer") # return true
compare_strokes("cof#dim#ng", "code") # return false