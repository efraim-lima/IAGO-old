from re import I
from pytrends.request import TrendReq


def trends(search, timing, g):
    pytrends = TrendReq(hl='pt-BR', tz=360)

    kw_list = [f"{search}"]
    ime = {
        '5y':'today 5-y',
        '7d':'today 7-d'
    }
    
    geo = g
    timeframes = ['today 5-y', 'today 12-m', 'today 90-d'
                 'today 30-d', 'today 7-d', 'today 4-h ']
    print(timeframes[0])
    
    
    pytrends.build_payload(kw_list, 
                        cat=0, 
                        timeframe = f'{timeframes[0]}', 
                        geo='', 
                        gprop='')
    
    data = pytrends.interest_over_time()
    mean = round(data.mean(),2)
    kw = kw_list[0]
    minn = mean[kw]
    avg = round(data[kw][-52:].mean(),2)
    avg2 = round(data[kw][:52].mean(),2)
    trend = round(((avg/mean[kw])-1)*100,2)
    trend2 = round(((avg/avg2)-1)*100,2)
    print(data)
    print(mean)
    print(kw)
    print(minn)
    print(avg)
    print(trend)
    print(trend2)
    
    if mean[kw] > 75 and abs(trend)<=5:
        stability = 'Stable'
    elif mean[kw] > 75 and abs(trend) > 5:
        stability = 'Increasing'
    elif mean[kw] > 75 and abs(trend) < -5:
        stability = 'Decreasing'
    elif mean[kw] > 60 and abs(trend) <= 15:
        stability = 'Relatively Stable'
    elif mean[kw] > 60 and abs(trend) > 15:
        stability = 'Relatively Stable and Increasing'
    elif mean[kw] > 60 and abs(trend) > 15:
        stability = 'Relatively Stable and Decreasing'
    
    print(stability)
trends('pastel', 'today 7-d', 'BR')