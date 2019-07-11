import json
from flask import Flask, render_template, request, url_for, jsonify

from dispatch import Dispatcher
from database import Database

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

buckets = [
    {"name":"my bucket 1",
    "id":"1",
    "active":False},
    {"name":"search engines",
    "id":"2",
    "active":False},
    {"name":"social media",
    "id":"3",
    "active":False},
    {"name":"videos",
    "id":"4",
    "active":False},
    {"name":"sports",
    "id":"5",
    "active":False},
]

links = [
    {"id":"1",
    "url":"https://www.google.com/",
    "parent":"1",
    "active":False},
    {"id":"2",
    "url":"https://www.twitter.com/",
    "parent":"2",
    "active":False},
    {"id":"3",
    "url":"https://www.ebay.com/",
    "parent":"3",
    "active":False},
    {"id":"4",
    "url":"https://www.facebook.com/",
    "parent":"4",
    "active":False},
]


# database2 = Database()
with open("sampleDatabase.json") as json_file:
    database2 = json.load(json_file)


def parse_view_args(args):
    """ arg :: request.args <ImmutableDict>
        return :: bucket <Int>
        return :: link <Int>
    """
    if "bucket" in args.keys() and "link" in args.keys():
        bucket, link = args["bucket"], args["link"]
    elif "bucket" in args.keys():
        bucket, link = args["bucket"], None
    elif "link" in args.keys():
        bucket, link = None, args["link"]
    else:
        bucket, link = None, None
    if bucket is not None and bucket.isdigit():
        bucket = int(bucket)
    else:
        bucket = None

    if link is not None and link.isdigit():
        link = int(link)
    else:
        link = None
    # print(f"[ parse_view_args() \n bucket: {bucket} \t link: {link} ]")
    return bucket, link



@app.route("/detail", methods=["GET","POST"])
def detail():
    if request.method == "POST":
        target, proceed = Dispatcher.create_url(request.form.get("txtbox", ""))
        print(target)
        if proceed:
            schema = Dispatcher(target).create_schema()
        else:
            schema = Dispatcher.defaults()
    else:
        schema = Dispatcher.defaults()
    return render_template("detail.html", schema=schema)



@app.route("/", methods=["GET"])
def index():
    """ parse request.args for bucket and link
    if either is present, retrieve data accordingly
    if either is present, set active attribute to True
    return schema """
    # initialize empty lists so we dont raise errors
    buckets = []
    links = []
    # get list of buckets
    buckets = database2
    # parse args
    bucket, link = parse_view_args(request.args)
    if bucket:  # retrieve child links, set bucket to active
        for each in buckets:
            if each["id"] == bucket:
                each["active"] = True
                links = each["children"]
            else:
                each["active"] = False
    else:
        for each in buckets:
            each["active"] = False
    if link:    # create preview schema, set link to active
        for each in links:
            if each["id"] == link:
                each["active"] = True
                schema = Dispatcher(each["url"]).create_schema()
            else:
                each["active"] = False
    else:
        for each in links:
            each["active"] = False
        schema = Dispatcher.defaults()
    return render_template("index.html", buckets=buckets, links=links, schema=schema)



@app.route("/dashboard")
def dashboard():
    """ ?bucket=<int>&link=<int>
    parse request.args for the 3 possibilities:
                        ['bucket'] && ['link']
                        ['bucket']
                        ['link']
                        None
    """
    bucket, link = parse_view_args(request.args)
    # query database for all assets by user
    if bucket:
        # retrieve children
        pass
    if link:
        # generate schema
        pass
    # if all(item is not None for item in [bucket, link]): pass
    # build schema, modify relevant ACTIVE values to True <boolean>
    assets = {"args":request.args,
            "bucket":bucket,
            "link":link}
    return jsonify(assets)



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


for each time that the user clicks a button the selection should be recorded
such that when the data is delivered the selection is active

each list should be comprised of single selection ribbons



"""
