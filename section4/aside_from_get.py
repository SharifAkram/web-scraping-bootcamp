# httpbin

import requests as r

print(r.delete("https://www.httpbin.org/delete").json())

print(r.patch("https://www.httpbin.org/patch").json())

print(r.put("https://www.httpbin.org/put").json())

print(r.post("https://www.httpbin.org/post").json())
