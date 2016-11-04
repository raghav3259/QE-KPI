"""This code collects lthe test logs from jenkins and
   stroes those test logs into elasticsearch"""

import requests
from requests.auth import HTTPBasicAuth
import json
from githubMapping import githubMapping
from elasticsearch import Elasticsearch


class GithubManager(object):

    """This is the main class for xunit."""

    def __init__(self, job_url, user, password):
        """constructor, for collecting project credentials.
           Project: github repo name, user: your user_name for github
           password: you password for github, job_url: Github url,
           """
        self.job_url = job_url
        self.user = user
        self.password = password
        self.es = Elasticsearch()

        requests.put("http://localhost:9200/" + self.user,
                     data=json.dumps(githubMapping))

    # def post_github_report(self):

    #	response_json = self.call_github(job_url + '/api/json')
    #	self.index_contributors()

    # def index_assignees(self):
        # Initialize a request
    #    print '*************'
    #    u = requests.get('https://github.com/repos/:owner/:repo/assignees')
    #    print u

    def call_github(self):
        """
        connects to github by passing github url, username and password
        """
        r = requests.get(self.job_url, auth=HTTPBasicAuth(self.user, self.password))
        if(r.ok):
            print 'success'

    # index_assignees('self')
