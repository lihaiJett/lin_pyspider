from urllib import parse

endPageLink = "http://www.baidu.com?i=5"
bits = list(parse.urlparse(endPageLink))
qs = parse.parse_qs(bits[4])  # 注意value是一个list
pageCount = int(qs['i'][0])
qs['i'] = ["3"]
bits[4] = parse.urlencode(qs, True)
url = parse.urlunparse(bits)
for i in range(1, pageCount+1):
    qs['page'] = [str(i)]
    bits[4] = parse.urlencode(qs, True)
    url = parse.urlunparse(bits)
    print(url)