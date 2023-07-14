import requests
import json

class MetaGraphAPI():
    access_token = ''
    client_id = ''
    client_secret = ''
    api_version = ''
    base_url = ''
    fb_page_id = ''
    dev_insta_id = ''
    dev_insta_username = ''
    
    def __init__(self, LONG_LIVED_TOKEN,CLIENT_ID,CLIENT_SECRET,BASE_URL,API_VERSION,FB_PAGE_ID,DEV_INSTA_ID,DEV_INSTA_USERNAME):
        self.access_token = LONG_LIVED_TOKEN
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.api_version = API_VERSION
        self.base_url = str(BASE_URL) + str(self.api_version) + '/'
        self.fb_page_id = FB_PAGE_ID
        self.dev_insta_id = DEV_INSTA_ID
        self.dev_insta_username = DEV_INSTA_USERNAME
    
    
    def makeApiCall(self, url, endpointParams, debug ='no'):

        data = requests.get(url, endpointParams)
        response = dict()
        response['url'] = url
        response['endpoint_params'] = endpointParams
        response['endpoint_params_pretty'] = json.dumps(endpointParams,indent=4)
        response['json_data'] = json.loads(data.content)
        response['json_data_pretty'] = json.dumps(response['json_data'],indent=4)
        if ('yes'== debug):
            self.displayApiCallData(response)
        return response

    def displayApiCallData(self, response):
            print(response['url'])
            print(response['endpoint_params_pretty'])
            print(response['json_data_pretty'])


    def getUserInfo(self,username, debug='no'):
        endpointParams = dict()
        endpointParams['fields'] = "business_discovery.username(" + username + "){username,name,id,biography,profile_picture_url,follows_count,followers_count,media_count,media{id,caption,media_type,comments_count,like_count,media_url,permalink,timestamp}}"
        endpointParams['access_token'] = self.access_token
        url = str(self.base_url) + str(self.dev_insta_id) + '/'
        return self.makeApiCall(url, endpointParams, debug)
    
    def getLatestUserMediaID(self, username):
        response = self.getUserInfo(username)
        latest_media_id = response['json_data']['business_discovery']['media']['data'][0]['id']
        return latest_media_id
    
    def getMediaInsights(self, media_id, access_token = '', debug='no'):
        endpointParams = dict()
        endpointParams['metric'] = 'engagement,impressions,reach,saved,video_views'
        if (access_token == ''):
            endpointParams['access_token'] = self.access_token
        else: 
            endpointParams['access_token'] = access_token
            
        url = self.base_url + str(media_id) + '/insights'

        return self.makeApiCall(url, endpointParams, debug)        
    