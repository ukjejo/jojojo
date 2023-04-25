# 평균을  출력해주는 함수를 생성해보자
# 1. 인자 개수가 가변
# 2. 받아온 인자 값들을 원소 하나씩 출력
# 3. 각 원소들의 합계
#  3-1. 합계라는 변수 생성 - 0을 대입
#  3-2. 각 원소들의 값들은 합계에 추가
# 4. 합계 / 인자의 개수 -> 평균 리턴

def func_12(*_list):
    print(_list)
    result = 0
    for i in _list:
        result += i
    return result / len(_list)

# max(), min() 함수를 생성해보자.
# 1. 인자의 개수가 가변이다. -> *로 매개변수를 만들어줘야한다.
# 2. 각각의 항목들을 비교해서 가장 큰 숫자를 출력 -> return int형태
# 3. 예를 들어 4개의 항목의 데이터가 대입 
# 3-1. 첫째 항목과 둘째 항목을 비교해서 큰 값을 새로운 변수에 대입
# 3-2. 1번 과정에서 나온 값과 셋째 항목을 비교해서 큰 값을 다시 변수에 대입
# 3-3. 2번 과정에서 나온 값과 마지막 항목을 비교해서 큰 값을 다시 변수에 대입
# 3-4. 최종 변수의 값을 리턴

def custom_max(*_list):
    result = _list[0]
    #첫번째 원소를 출력
    #첫번째 원소와 두번째 원소의 값을 비교하여 큰 값 대입
    #if _list[0] > _list[1] :
    #    result = _list[0]
    #else:
    #    result = _list[1]
    #     if result < _list[1]:
    #         result = _list[1]
    # #result와 세번째 원소를 비교
    #if result > _list[2]:
    #    result = result
    #else:
    #    result = _list[2]
        # if result < list[2]:
        #     result = _list[2]
    # for i in range(1, len(_list), 1):
    #     if result < _list[i]:
    #         result = _list[i]
    # return result
    
    for i in _list:
        if result < i:
            result = i
    return result    
        