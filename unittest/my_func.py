def odd_ox(num):
    if type(num) is not int:
        return "정수를 입력하세요"
    else:    
        if num%2 == 0:
            return True
        else:
            return False

def mean_n(list_n):
    if len(list_n) == 0:
        return "빈 리스트"
    else:
        return sum(list_n)/len(list_n)

def max_m(list_m):
    if len(list_m) == 0:
        return "빈 리스트"
    else:
        return max(list_m)

def min_l(list_l):
    if len(list_l) == 0:
        return "빈 리스트"
    else:
        return min(list_l)