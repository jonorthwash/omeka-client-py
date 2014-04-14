import httplib2
import urllib.request, urllib.parse, urllib.error
import mimetypes

class OmekaClient:
    
    def __init__(self, endpoint, key=None):
        self._endpoint = endpoint
        self._key = key
        self._http = httplib2.Http()
    
    def get(self, resource, id=None, query={}):
        return self._request("GET", resource, id=id, query=query)
    
    def post(self, resource, data, query={}, headers={}):
        return self._request("POST", resource, data=data, query=query, headers=headers)
    
    def put(self, resource, id, data, query={}):
        return self._request("PUT", resource, id, data=data, query=query)
    
    def delete(self, resource, id, query={}):
        return self._request("DELETE", resource, id, query=query)
    
    def post_file(self, data, filename, contents):
        """ data is JSON metadata, filename is a string, contents is file contents """
        BOUNDARY = '----------E19zNvXGzXaLvS5C'
        CRLF = '\r\n'
        headers = {'Content-Type': 'multipart/form-data; boundary=' + BOUNDARY}
        L = []
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="data"')
        L.append('')
        L.append(data)
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="file"; filename="%s"' % filename)
        #L.append(b'Content-Transfer-Encoding: base64')
        L.append('Content-Type: %s' % self.get_content_type(filename))
        L.append('')
        L.append(CRLF)
        #L.append(contents)
        #L.append('--' + BOUNDARY)
        
        #print(CRLF, '-', len(L))
        #print(CRLF.join(L))
        body = CRLF.join(L)
        body = bytes(body, encoding='utf-8')
        body += contents
        body += bytes(CRLF+'--'+BOUNDARY, encoding='utf-8')
        
        headers['content-length'] = str(len(body))
        headers['Connection'] = 'close'
        print(str(body))
        print(self.get_content_type(filename))
        #headers['charset'] = 'utf-8'
        query = {}
        return self.post("files", body, query, headers)
     
    def post_file_urllib2(self, fields, filename, contents):
        files = {'file': {'filename': filename, 'content': contents}}
        data, headers = formdata.encode_multipart(fields, files)
        request = urllib2.Request('http://httpbin.org/post', data=data, headers=headers)
        f = urllib2.urlopen(request)


    def get_content_type(self, filename):
        """ use mimetypes to detect type of file to be uploaded """
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

    def _request(self, method, resource, id=None, data=None, query=None, headers=None):
        url = self._endpoint + "/" + resource
        if id is not None:
            url += "/" + str(id)
        if self._key is not None:
            query["key"] = self._key
        url += "?" + urllib.parse.urlencode(query)
        resp, content = self._http.request(url, method, body=data, headers=headers)
        return resp, content
