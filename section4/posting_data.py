import requests as r

# resp = r.post(
#     "https://www.httpbin.org/post",
#     data={"key1": "value1", "key2": "a value with spaces and an apostrophe ' "},
# )

resp = r.post(
    "https://www.httpbin.org/post",
    json={"key1": "value1", "key2": "a value with spaces and an apostrophe ' "},
)
resp.json()

print(resp.request.body)
