# Text Wrap 

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width = max_width)
    wrap_list = wrapper.wrap(text = string)
    l = len(wrap_list)
    for line in range(l-1):
        print(wrap_list[line])
    return wrap_list[l-1]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)