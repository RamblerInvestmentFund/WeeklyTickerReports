import pandas as pd
import finviz as fv
import re

TICKER = 'MSFT'
# Format ticker news
news = fv.get_news(TICKER)


story1_date=news[0][0]
story1_short=news[0][1]
story1_link=news[0][2]

story2_date=news[1][0]
story2_short=news[1][1]
story2_link=news[1][2]

story3_date=news[2][0]
story3_short=news[2][1]
story3_link=news[2][2]

story4_date=news[3][0]
story4_short=news[3][1]
story4_link=news[3][2]

story5_date=news[3][0]
story5_short=news[3][1]
story5_link=news[3][2]

print(story1_short)
print(story2_short)
print(story3_short)
print(story4_short)
print(story5_short)
