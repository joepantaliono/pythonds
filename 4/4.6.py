from stack import Stack

def matching_par(str):
    """check matching parentheses using stack"""
    s = Stack()
    for c in str:
        if c == "(":
            s.push(c)
        else:
            if s.is_empty() == True:
                return False
            else:
                s.pop()
    return s.is_empty()
       


matching_par("((()))")  # true
matching_par("(()())") # true
matching_par("((())))")  # false