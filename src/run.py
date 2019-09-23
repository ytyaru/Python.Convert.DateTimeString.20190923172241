import pytz
from DateTimeString import DateTimeString

cnv = DateTimeString()
for test_case in ([
    '2019-09-22T18:00:00+09:00', # RFC3339 (ISO-8601)
    '2019/09/22 18:00:00+09:00', # スラッシュやスペースでもOK
    '2019/09/22 18:00:00.123456+09:00', # 秒未満があっても無視する
    '2019-09-22T09:00:00Z',
    'Mon, 23 Sep 2019 15:00:00 +0900', # RFC1123
    '2019-12-31 12:34:56',
#    'AAAAABBBBBB',
]): 
    dt = cnv.convert(test_case)
    print(type(dt))
    print(dt.tzinfo)
#    utc = dt.astimezone(pytz.timezone('UTC')) # UTC時刻に変換
    utc = cnv.convert_utc(test_case)
    print(utc) 
    print(utc.strftime('%Y-%m-%dT%H:%M:%SZ')) # +00:00でなくZ

