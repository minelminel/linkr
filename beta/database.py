
data = [
    {
        "id":"1",
        "name":"search engines",
        "children": [
        {
            "id":"1",
            "url":"http://www.google.com",
            "parent":"1",
        },
        {
            "id":"2",
            "url":"http://www.yahoo.com",
            "parent":"1",
        },
        {
            "id":"3",
            "url":"http://www.duckduckgo.com",
            "parent":"1",
        },
        ]
    },
    {
        "id":"2",
        "name":"online shopping",
        "children": [
        {
            "id":"4",
            "url":"http://www.amazon.com",
            "parent":"2",
        },
        {
            "id":"5",
            "url":"http://www.ebay.com",
            "parent":"2",
        },
        {
            "id":"6",
            "url":"http://www.target.com",
            "parent":"2",
        },
        ]
    }
]

def Database():
    return data
