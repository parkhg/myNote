import http.client

url = "www.wku.ac.kr"
try:
    conn = http.client.HTTPConnection(url)
    print(conn)
    conn.request("HEAD", "/")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    if getattr(r1,'status') == 200:
        print('on')

except http.client.HTTPException:
    print("http Error : ", http.client.HTTPException)
except:
    print('Bad URL :', url)
