import textwrap

def wrap(string, max_width):
    for i in range(0,len(string)-max_width,max_width):
        if (len(string)-max_width==i):
            break
        print(string[i:i+max_width])
        

    return string[i+max_width:]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
