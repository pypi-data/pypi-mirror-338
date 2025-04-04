from requests import get,post,Session
import base64,uuid,json,time
class Botgp:
    def __init__(self):
        pass
    
        
    def share_facebook_post_EAAGN(self,token, id_share,cookie,privacy='0'):
        try:
            """
            Share a post on Facebook using the Facebook Graph API.
            :param token: Facebook access token [EAAGNO...........]
            :param post_url: URL of the post to share
            :param privacy: Privacy setting for the post (default: SELF)
            Returns:
                Grapg api respone
            """
            he = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate',
                'connection': 'keep-alive',
                'content-length': '0',
                'cookie': cookie,
                'host': 'graph.facebook.com'
            }
            response = post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published={privacy}&access_token={token}', headers=he).json()
            if 'id' in response:
                return (True,response)
        except Exception as e:
            return (False,e)
    def comment_post_EAAGN(self,post_id='9000855519965854',message='ma4D1',token=None,cookes=None):
        try:
            """
            Comment on a post on Facebook using the Facebook Graph API.
            :param token: Facebook access token [EAAGNO...........]
            :param post_url: URL of the post to share
            :param privacy: Privacy setting for the post (default: SELF)
            Returns:
            Grapg api respone
            """
            if token and cookes :
                response=post(f"https://graph.facebook.com/{post_id}/comments/?message={message}&access_token={token}", headers = {"cookie":cookes}).json()
                if 'id' in response:
                    return (True,response)
        except Exception as e:
            return (False,e)


class EAAAAU(Botgp):
    def __init__(self):
        #--> Access Token (EAAU from b-graph login)
        pass
    def share_facebook_post_EAAAAU(self,token, post_url,privacy='SELF'):
        try:
            """
            Share a post on Facebook using the Facebook Graph API.
            :param token: Facebook access token [EAAAAUaZA8...........]
            :param post_url: URL of the post to share
            :param privacy: Privacy setting for the post (default: SELF)
            Returns:
                Grapg api respone
            """
            fb_url = 'https://graph.facebook.com/v13.0/me/feed'
            data = {'link': post_url, 'published': '0', 'privacy': '{"value":"%s"}'%(privacy), 'access_token': token}
            response = post(fb_url, data=data).json()
            if 'id' in response:
                return (True,response)
        except Exception as e:
            return (False,e)
        
    def follow_EAAAAU(self,terge_id=None,Token=None):
        """_summary_
        This a function to follow a user on Facebook using the Facebook Graph API.
         token after loging use graph api
        Args:
            terge_id (_type_, optional): _description_. Defaults to None.
            Token (_type_, optional): _description_. Defaults to None.
             #--> Access Token (EAAU from b-graph login)

        Returns:
            _type_: _description_
        """
        try:
            if terge_id and Token:
                response=post(f'https://graph.facebook.com/{terge_id}/subscribers?access_token={Token}').json()
                return True,response
        except Exception as e:
            return (False,e)
    def pgLike_EAAAAU(self,terge_id=None,Token=None):
        """_summary_
        This a function to page like a user on Facebook using the Facebook Graph API.
         token after loging use graph api
        Args:
            terge_id (_type_, optional): _description_. Defaults to None.
            Token (_type_, optional): _description_. Defaults to None.
             #--> Access Token (EAAU from b-graph login)
        Returns:
            _type_: _description_
        """
        try:
            if terge_id and Token:
                response=post(f'https://graph.facebook.com/{terge_id}/likes?access_token={Token}').json()
                return True,response
        except Exception as e:
            return (False,e)
    def post_reaction_EAAAAU(self,actor_id:str, post_id:str, react:str, token:str):
        r    = Session()
        var  = {"input":{"feedback_referrer":"native_newsfeed","tracking":[None],"feedback_id":str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8')),"client_mutation_id":str(uuid.uuid4()),"nectar_module":"newsfeed_ufi","feedback_source":"native_newsfeed","attribution_id_v2":"NewsFeedFragment,native_newsfeed,cold_start,1710331848.276,264071715,4748854339,,","feedback_reaction_id":react,"actor_id":actor_id,"action_timestamp":str(time.time())[:10]}}
        data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'id_ID','fb_api_req_friendly_name':'ViewerReactionsMutation','fb_api_caller_class':'graphservice','client_doc_id':'2857784093518205785115255697','variables':json.dumps(var),'fb_api_analytics_tags':["GraphServices"],'client_trace_id':str(uuid.uuid4())}
        pos  = r.post('https://graph.facebook.com/graphql', data=data).json()
        try:
            if react in str(pos):
                return(True,pos['data']['feedback_react']['feedback']['reactors']['count'])
               
            else: return(False,'React Failed!')
        except Exception: return(False,'React Failed!')
        
        
