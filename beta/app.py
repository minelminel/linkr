from flask import Flask, render_template, request, url_for

from dispatch import Dispatcher

app = Flask(__name__)


database = [
    {
    "id":"1",
    "name":"my bucket 1",
    "children":[
            {
                "id":"1",
                "name":"Facebook Link",
                "url":"https://www.facebook.com",
                "parent":"1",
            },
            {
                "id":"2",
                "name":"Google Link",
                "url":"https://www.google.com",
                "parent":"1",
            },
            {
                "id":"3",
                "name":"Ebay Link",
                "url":"https://www.ebay.com",
                "parent":"1",
            },
        ]
    },
    {
    "id":"2",
    "name":"my bucket 2",
    "children":[
            {
                "id":"4",
                "name":"Google Link",
                "url":"https://www.google.com",
                "parent":"2",
            },
            {
                "id":"5",
                "name":"Youtube Link",
                "url":"https://www.youtube.com",
                "parent":"2",
            },
        ]
    },
]


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        print(request.__dict__)
        target = request.form["txtbox"]
        print(target)
        schema = Dispatcher(target).create_schema()
    else:
        schema = Dispatcher.defaults()
    return render_template("index.html", schema=schema, database=database)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)




"""
when the user visits the dashboard page, all the buckets belonging to the user are loaded.
for each item in the list of bucket, a button is generated in the leftmost panel.
the middle panel showing the links contained in each bucket, and the preview panel, are empty.
when the user clicks a bucket button, all the links corresponding to that bucket are loaded
    and displayed in the middle panel. the rightmost panel is still empty.
when the user clicks a link, a detailed view is shown in the rightmost panel.


[action] user visits the dashboard page
[backend] all buckets owned by the user are retrieved
[frontend] all buckets are displayed in the bucket panel

[action] user clicks a bucket
[backend] bucket id is passed along and all children are retrieved
[frontend] all children links are displayed

[action] user clicks a link
[backend] link id is passed along and schema is generated
[frontend] schema is displayed in the detail panel

[action]
[backend]
[frontend]

[action]
[backend]
[frontend]

[action]
[backend]
[frontend]

[action]
[backend]
[frontend]
"""
