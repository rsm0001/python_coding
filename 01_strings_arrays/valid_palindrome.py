import sys

# ============================================

def get_char(s, i):
    if (s[i].isalpha() or s[i].isdigit()):
        return s[i].lower()
    return None

def is_palindrome(s):
    l, r = 0, (len(s) - 1)
    while (l < r):
        cl = None
        while ((l < r) and (cl is None)):
            cl = get_char(s, l)
            l += 1 if (cl is None) else 0
        cr = None
        while ((l < r) and (cr is None)):
            cr = get_char(s, r)
            r -= 1 if (cr is None) else 0
        if (cl != cr):
            return False
        l += 1
        r -= 1
    return True

# ============================================

def main():
    print("-------------------------")
    s = input("Enter a string: ")
    print(f"{s} is a valid palindrome: <{is_palindrome(s)}>")
    print("-------------------------")
    return

# ============================================

if (__name__ == "__main__"):
    try:
        main()
    except:
        print(sys.exc_info())

# ============================================

#  Goal: get comfortable with variadic arguments — collecting an arbitrary number
#  of positional/keyword args, unpacking with */** at call sites, and forwarding
#  args through a wrapper.

#  Write a script arg_stats.py that:

#  1. Write a function describe(*args, **kwargs) that prints:
#    - The number of positional args and their values.
#    - The number of keyword args and their key/value pairs.
#  2. Write stats(*nums) that takes any number of numeric positional args and
#  returns (min, max, sum/len) as a tuple — reuse the tuple-unpacking idiom from
#  coord_stats.py for printing the result.
#  3. Write a generic logging wrapper logged(func, *args, **kwargs) that prints
#  the function name and the args/kwargs it's about to call func with, then calls
#  func(*args, **kwargs) and returns its result. Call stats through logged a
#  couple of times with different arg counts, so you're forwarding *args/**kwargs
#  through a second layer, not just consuming them.
#  4. Demonstrate unpacking at a call site: build a list of numbers and a dict of
#  keyword args separately, then call describe(*your_list, **your_dict) to show
#  */** unpack a collection into individual arguments — the flip side of
#  collecting them.
#  5. Bonus (optional): give stats a keyword-only argument (e.g. stats(*nums,
#  precision=2) — anything after *args in the signature is keyword-only) that
#  controls how many decimal places the average is rounded to, and explain why it
#  has to come after *nums rather than before.

#  Ping me when you've got a draft.

# ============================================

