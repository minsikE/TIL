def trimmedMean(inList):
    """ 
        설명        :  절사평균 (최소 최댓값을 뺀 평균)
        파라미터    : inList (List)
        리턴값      :
    """
    # inList = [1,2,3,4]
    minValue = min(inList)
    maxValue = max(inList)

    inList.remove(minValue)
    inList.remove(maxValue)

    result = sum(inList) / len(inList)
    return result