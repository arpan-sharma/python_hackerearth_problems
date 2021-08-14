if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))

    list_arrr = list(arr)

    max_in_list = max(list_arrr)
    pop_list_item = list_arrr.remove(max_in_list)

    while True:
        if max_in_list in list_arrr:
            pop_list_item = list_arrr.remove(max_in_list)
        else:
            break
    second_runnner_up_is = max(list_arrr)
    print(second_runnner_up_is)

