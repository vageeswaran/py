import difflib
a = raw_input()
b = raw_input()
seq=difflib.SequenceMatcher(a=a.lower(), b=b.lower())
if seq.ratio() >0.75:
        print b


