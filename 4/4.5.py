def rev_string(my_str):
    """Write a function rev_string(my_str) that uses a stack to reverse the characters in a string."""
    my_str = list(my_str)
    answer = []
    count = 0
    while count < len(my_str):
        answer.append(my_str.pop())
    answer = ''.join(answer)
    return answer

print(rev_string("cat")) #tac
print(rev_string("dog")) #god
print(rev_string("pumpkin")) #nikpmup
print(rev_string("candle")) #eldnac