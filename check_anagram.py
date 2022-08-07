def check_anagram(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        print(True)
    else:
        print(False)

s1='abcdefghi'
s2='ihdefabc'
check_anagram(s1,s2)