#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import urllib
import urllib2

API_KEY = 'YOUR_RESTFUL_KEY'
API_URL = 'http://api.page2images.com/restfullink'

#api call status
API_CALL_STATUA_ERROR = 'error'
API_CALL_STATUA_PROCESSING = 'processing'
API_CALL_STATUA_FIHISHED = 'finished'

def call_p2i():
    # URL can be those formats: http://www.google.com
    # https://google.com google.com and www.google.com
    url = "http://www.google.com"

    # 0 - iPhone4, 1 - iPhone5, 2 - Android, 3 - WinPhone,
    # 4 - iPad, 5 - Android Pad, 6 - Desktop
    device = 0

    loop_flag = True
    TIMEOUT = 120 # timeout after 120 seconds

    start_time = time.time()
    timeout_flag = False

    while (loop_flag):
        # We need call the API until we get the screenshot or error message
        try:
            post_data = {
                "p2i_url": url,
                "p2i_key": API_KEY,
                "p2i_device": device
            }
            json_data = json.loads(urllib2.urlopen(API_URL, \
                    urllib.urlencode(post_data)).read())
            print json_data
            if(json_data['status'] == API_CALL_STATUA_ERROR):
                # do something to handle error
                loop_flag = False
                print ' '.join([str(json_data['errno']), json_data['msg']])
            elif(json_data['status'] == API_CALL_STATUA_FIHISHED):
                # do something with finished. For example, show this image
                print json_data['image_url']
                # Or you can download the image from our server
                loop_flag = False
            else: # API_CALL_STATUA_PROCESSING or Timeout
                if ((time.time() - start_time) > TIMEOUT):
                    loop_flag = False
                    # set the timeout flag. You can handle it later.
                    timeout_flag = True
                else:
                    time.sleep(3) # This only work on windows.
        except Exception, e:
            # Do whatever you think is right to handle the exception.
            loop_flag = False
            print 'Caught exception: %s' % str(e)

    if (timeout_flag):
        # handle the timeout event here
        print "Error: Timeout after %d seconds." % TIMEOUT

def call_p2i_with_callback():
    # URL can be those formats: http://www.google.com
    # https://google.com google.com and www.google.com
    url = "http://www.google.com";

    # 0 - iPhone4, 1 - iPhone5, 2 - Android, 3 - WinPhone,
    # 4 - iPad, 5 - Android Pad, 6 - Desktop
    device = 0

    # you can pass us any parameters you like. We will pass it back.
    # Please make sure http://your_server_domain/api_callback can handle our call
    callback_url = "http://your_server_domain/api_callback?image_id=your_unique_image_id_here"

    try:
        post_data = {
            "p2i_url": url,
            "p2i_key": API_KEY,
            "p2i_device": device,
            "p2i_callback": callback_url
        }
        urllib2.urlopen(API_URL, urllib.urlencode(post_data))
    except Exception, e:
    # Do whatever you think is right to handle the exception.
        print 'Caught exception: %s' % str(e)

# This function demo how to handle the callback request
def api_callback(request):
    if not ('image_id' in request.REQUEST and request.REQUEST['image_id']):
        """do anything you want about the unique image id. We suggest to
        use it to identify which url you send to us since you can send 1,000
        at one time."""
        pass

    if ('result' in request.REQUEST and request.REQUEST['result']):
        request_data = request.REQUEST['result']
        try:
            json_data = json.loads(request_data)
            if(json_data['status'] == API_CALL_STATUA_ERROR):
                # do something to handle error
                print ' '.join([str(json_data['errno']), json_data['msg']])
            elif(json_data['status'] == API_CALL_STATUA_FIHISHED):
                # do something with finished. For example, show this image
                print urllib2.unquote(json_data['image_url'])
                # Or you can download the image from our server
        except Exception, e:
            # Do whatever you think is right to handle the exception.
            print 'Caught exception: %s' % str(e)
    else:
        #Do whatever you think is right to handle the exception.
        print "Error: Empty"

if __name__ == '__main__':
    print 'call begin'
    call_p2i()
    call_p2i_with_callback()
    print 'call done'
