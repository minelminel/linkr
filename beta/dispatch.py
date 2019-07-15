import os
import json
import requests
from time import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup as BS4
from wrapt_timeout_decorator import timeout


class Dispatcher(object):
    """
    [Operation]
    get request => parse response => create schema

    [Usage]
    schema = Dispatcher(target).create_schema()
    >> schema = {
                'title': 'Google',
                'friendy': 'google.com',
                'status': 200,
                'target': 'http://google.com'
                }
    """
    def __init__(self, target):
    # target    :: url <string>
        self.target = target
    # response  :: <Response Object> || None
        self.response = self._get_request()
    # success   :: <boolean>
        self.success = self._status_code_ok()
    # friendly  :: <string>
        self.friendly = self._friendly_name()
    # title     :: <string>
        self.title = self._parse_title()
    # description     :: <string>
        self.description = self._parse_description()
    # favicon   ::  url <string> as image 
        self.favicon = os.path.join("https://", self.friendly, "favicon.ico")

    # internal method
    def _get_request(self):
        # @timeout(1, use_signals=False, timeout_exception=TimeoutError)
        def _request(arg):
            try:
                return requests.get(arg)
            except:
                pass
        try:
            return _request(self.target)
        except:
            pass

    # internal method
    def _friendly_name(self):
        return urlparse(self.target).netloc

    # internal method
    def _status_code_ok(self):
        success_codes = [200, 201, 202]
        if self.response and self.response.status_code in success_codes:
            return True
        else:
            return False

    # internal method
    def _is_html(self):
        if not self.success:
            return False
        content = self.response.headers.get("Content-Type", "")
        if "text/html" in content:
            return True
        else:
            return False

    # internal method
    def _parse_title(self):
        if self._is_html() and self.success:
            try:
                return BS4(self.response.content, "html.parser").title.string
            except:
                return ""
        else:
            return ""

    # internal method
    def _parse_description(self):
        if self._is_html() and self.success:
            try:
                return BS4(self.response.content, "html.parser").find('p').text
            except:
                return ""
        else:
            return ""

    # primary method
    def create_schema(self):
        return dict(title=self.title,
                    description=self.description,
                    favicon=self.favicon,
                    friendly=self.friendly,
                    status=self.response.status_code if self.success else 700,
                    target=self.target)

    @staticmethod
    def defaults():
        return dict(title="",
                    description="",
                    favicon="",
                    friendly="",
                    status=700,
                    target="")

    @staticmethod
    def create_url(target):
        if "http://" or "https://" in target:
            proceed = True
        else:
            target = "https://" + target
            proceed = True
        if "." not in target:
            proceed = False
        return target, proceed



if __name__ == "__main__":
    def main(target):
        from pprint import pprint

        print("[Class-based execution]")
        s1 = time()
        schema = Dispatcher(target).create_schema()
        pprint(schema)
        print(f"[time] {time() - s1} sec")

    targets = [
        "http://titan.dcs.bbk.ac.uk/~kikpef01/testpage.html",
        "https://discuss.atom.io/t/select-all-and-edit-all-at-once/25220",
        "https://www.youtube.com/watch?v=_M9yTG19PnE",
        "https://stackooverflow.com/questions/20562543/zoom-to-fit-pdf-embedded-in-html", # broken link
        "https://www.ifixit.com/Search?query=pop%20socket&doctype=product&c-doctype_namespace=product",
    ]
    for target in targets:
        print("/"*20)
        main(target)
