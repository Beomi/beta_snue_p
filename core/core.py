import requests
import json


def _check_if_student(user_id, user_pw):
    payload = {
        'usr_id': str(user_id),
        'usr_pwd': str(user_pw)
    }
    with requests.Session() as s:
        auth = s.post('http://lms.snue.ac.kr/ilos/lo/login.acl', data=payload)
        if ('Expires' in auth.headers['Set-Cookie']) and ('Domain=snue.ac.kr' in auth.headers['Set-Cookie']):
            result = True
        else:
            result = False
        return result


class PubSub(object):
    """
    Very simple Pub/Sub pattern wrapper
    using simplified Redis Pub/Sub functionality.
    Usage (publisher)::
        import redis
        r = redis.Redis()
        q = PubSub(r, "channel")
        q.publish("test data")
    Usage (listener)::
        import redis
        r = redis.Redis()
        q = PubSub(r, "channel")
        def handler(data):
            print "Data received: %r" % data
        q.subscribe(handler)
    """
    def __init__(self, redis, channel="default"):
        self.redis = redis
        self.channel = channel

    def publish(self, data):
        self.redis.publish(self.channel, json.dumps(data))

    def subscribe(self, handler):
        redis = self.redis.pubsub()
        redis.subscribe(self.channel)

        for data_raw in redis.listen():
            if data_raw['type'] != "message":
                continue

            data = json.loads(data_raw["data"])
            handler(data)