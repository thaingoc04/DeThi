import urllib.request
if __name__ == '__main__':
    req = urllib.request.Request('http://www.vnexpress.net')
    req.add_header('Accept-Encoding', 'gzip')
    res = urllib.request.urlopen(req)

    headers = res.getheaders()
    print(headers)