# api structure

/localhost:5000/dashboard?username={{ username }}%bucket={{ bucket }}&link={{ link }}
/localhost:5000/dashboard?username=michael&bucket=1&link=4

the request is made to the page for all the buckets owned by the user
if a bucket is specified by the user, ONLY the links associated with THAT bucket is returned
if a bucket is specified by the user, set the buckets's `active` attribute to `True`
if a bucket is specified by the user, display the children links
if a link is specified by the user, set the parent bucket'a `active` attribute to `True`
if a link is specified by the user, create the schema for the link detail



GET request with verification done at 2 levels: session['logged_in'], csrf_token
read the url to configure the page view

[1] verify credentials

[2] parse request

[3] handle request

[4] return response
