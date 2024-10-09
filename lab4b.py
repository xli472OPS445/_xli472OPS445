#!/usr/bin/env python3

def join_lists(l1, l2):
    new_list1 = set(l1) | set(l2)
    return list(new_list1)

def match_lists(l1, l2):
    new_list2 = set(l1) & set(l2)
    return list(new_list2)

def diff_lists(l1, l2):
    new_list3 = set(l1) ^ set(l2)
    return list(new_list3)

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
