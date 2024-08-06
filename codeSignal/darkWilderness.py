def growingPlant(upSpeed,downSpeed,desireHeight):
    # upSpeed : increase height fixed amount
    # downSpped : decrease height per every night
    # return days to reacht the " desiredHeight "
    day = 1
    while upSpeed*day - downSpeed*(day-1) < desireHeight :
        day +=1
    return day

print(growingPlant(100,10,910))