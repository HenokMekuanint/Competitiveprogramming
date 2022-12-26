if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) # This is a map.
    tuple_data = tuple(integer_list) # This is tuple
    # Now hash value of this tuple
    print(hash(tuple_data))
