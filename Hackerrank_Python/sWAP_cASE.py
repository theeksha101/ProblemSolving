def swap_case(s):
    swapped = ''
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            swapped += chr(ord(i) - 32)
        elif ord('A') <= ord(i) <= ord('Z'):
            swapped += chr(ord(i) + 32)
        else:
            swapped += i
    return swapped


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

    # BROTHER'S CODE

    # swapped = ""
    # for c in s:
    #     if ord('A') <= ord(c) <= ord('Z'):
    #         swapped += chr(ord(c) + 32)
    #         continue
    #     elif ord('a') <= ord(c) <= ord('z'):
    #         swapped += chr(ord(c) - 32)
    #         continue
    #     swapped += c
    #
    # return swapped
