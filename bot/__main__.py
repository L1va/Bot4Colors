import os
import redis

from bot.web import app


if __name__ == '__main__':
    PORT = os.environ.get('PORT', 8000)
    
    #memcache_url = os.environ.get('MEMCACHED_URL', '127.0.0.1:11211')
    #mc_client = memcache.Client([memcache_url], debug=0)
    
    app.run(port=PORT, debug=True)
