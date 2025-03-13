nums = [1,[2,3],[4,[5,6],7],8]  # -> [1,2,3,4,5,6,7,8]

def unpacking(List, result=None):
    """ Функция распаковывает список """
    if result is None:
        result = []
    for element in List:
        if type(element) == list:
            unpacking(element, result)
        else: result.append(element)
    return result
if __name__=="__main__":
    print(unpacking(nums))
