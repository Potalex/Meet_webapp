{"filter":false,"title":"settings.py","tooltip":"/playmonster/settings.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":126,"column":38},"end":{"row":126,"column":39},"action":"insert","lines":["p"],"id":27}],[{"start":{"row":126,"column":39},"end":{"row":126,"column":40},"action":"insert","lines":["l"],"id":28}],[{"start":{"row":126,"column":40},"end":{"row":126,"column":41},"action":"insert","lines":["a"],"id":29}],[{"start":{"row":126,"column":40},"end":{"row":126,"column":41},"action":"remove","lines":["a"],"id":33}],[{"start":{"row":126,"column":39},"end":{"row":126,"column":40},"action":"remove","lines":["l"],"id":34}],[{"start":{"row":126,"column":38},"end":{"row":126,"column":39},"action":"remove","lines":["p"],"id":35}],[{"start":{"row":126,"column":46},"end":{"row":127,"column":0},"action":"insert","lines":["",""],"id":36}],[{"start":{"row":127,"column":0},"end":{"row":130,"column":1},"action":"insert","lines":["STATICFILES_DIRS = (","    os.path.join(PROJECT_ROOT, 'static'),","    os.path.join(BASE_DIR, \"static\"),",")"],"id":37}],[{"start":{"row":126,"column":46},"end":{"row":127,"column":0},"action":"insert","lines":["",""],"id":38}],[{"start":{"row":127,"column":0},"end":{"row":128,"column":57},"action":"insert","lines":["","PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))"],"id":39}],[{"start":{"row":126,"column":46},"end":{"row":127,"column":0},"action":"remove","lines":["",""],"id":40}],[{"start":{"row":126,"column":0},"end":{"row":126,"column":46},"action":"remove","lines":["STATIC_ROOT = os.path.join(BASE_DIR, 'static')"],"id":41}],[{"start":{"row":125,"column":23},"end":{"row":126,"column":0},"action":"remove","lines":["",""],"id":42}],[{"start":{"row":127,"column":0},"end":{"row":128,"column":0},"action":"insert","lines":["",""],"id":43}],[{"start":{"row":127,"column":0},"end":{"row":127,"column":46},"action":"insert","lines":["STATIC_ROOT = os.path.join(BASE_DIR, 'static')"],"id":44}],[{"start":{"row":127,"column":34},"end":{"row":127,"column":35},"action":"remove","lines":["R"],"id":45}],[{"start":{"row":127,"column":33},"end":{"row":127,"column":34},"action":"remove","lines":["I"],"id":46}],[{"start":{"row":127,"column":32},"end":{"row":127,"column":33},"action":"remove","lines":["D"],"id":47}],[{"start":{"row":127,"column":31},"end":{"row":127,"column":32},"action":"remove","lines":["_"],"id":48}],[{"start":{"row":127,"column":30},"end":{"row":127,"column":31},"action":"remove","lines":["E"],"id":49}],[{"start":{"row":127,"column":29},"end":{"row":127,"column":30},"action":"remove","lines":["S"],"id":50}],[{"start":{"row":127,"column":28},"end":{"row":127,"column":29},"action":"remove","lines":["A"],"id":51}],[{"start":{"row":127,"column":27},"end":{"row":127,"column":28},"action":"remove","lines":["B"],"id":52}],[{"start":{"row":127,"column":27},"end":{"row":127,"column":28},"action":"insert","lines":["P"],"id":54}],[{"start":{"row":127,"column":28},"end":{"row":127,"column":29},"action":"insert","lines":["r"],"id":55}],[{"start":{"row":127,"column":29},"end":{"row":127,"column":30},"action":"insert","lines":["o"],"id":56}],[{"start":{"row":127,"column":29},"end":{"row":127,"column":30},"action":"remove","lines":["o"],"id":57}],[{"start":{"row":127,"column":28},"end":{"row":127,"column":29},"action":"remove","lines":["r"],"id":58}],[{"start":{"row":127,"column":27},"end":{"row":127,"column":28},"action":"remove","lines":["P"],"id":59}],[{"start":{"row":127,"column":27},"end":{"row":127,"column":28},"action":"insert","lines":["R"],"id":60}],[{"start":{"row":127,"column":28},"end":{"row":127,"column":29},"action":"insert","lines":["O"],"id":61}],[{"start":{"row":127,"column":28},"end":{"row":127,"column":29},"action":"remove","lines":["O"],"id":62}],[{"start":{"row":127,"column":27},"end":{"row":127,"column":28},"action":"remove","lines":["R"],"id":63}],[{"start":{"row":127,"column":27},"end":{"row":127,"column":28},"action":"insert","lines":["P"],"id":64}],[{"start":{"row":127,"column":28},"end":{"row":127,"column":29},"action":"insert","lines":["R"],"id":65}],[{"start":{"row":127,"column":29},"end":{"row":127,"column":30},"action":"insert","lines":["O"],"id":66}],[{"start":{"row":127,"column":27},"end":{"row":127,"column":30},"action":"remove","lines":["PRO"],"id":67},{"start":{"row":127,"column":27},"end":{"row":127,"column":39},"action":"insert","lines":["PROJECT_ROOT"]}],[{"start":{"row":125,"column":0},"end":{"row":131,"column":1},"action":"remove","lines":["STATIC_URL = '/static/'","PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))","STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')","STATICFILES_DIRS = (","    os.path.join(PROJECT_ROOT, 'static'),","    os.path.join(BASE_DIR, \"static\"),",")"],"id":68},{"start":{"row":125,"column":0},"end":{"row":143,"column":23},"action":"insert","lines":["PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))","","STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')","STATIC_URL = '/static/'","","# Extra places for collectstatic to find static files.","STATICFILES_DIRS = (","    os.path.join(PROJECT_ROOT, 'static'),","    os.path.join(BASE_DIR, \"static\"),",")","","# Simplified static file serving.","# https://warehouse.python.org/project/whitenoise/","","STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'","","# Honor the 'X-Forwarded-Proto' header for request.is_secure()","SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')","STATIC_URL = '/static/'"]}],[{"start":{"row":106,"column":0},"end":{"row":107,"column":0},"action":"insert","lines":["",""],"id":69}],[{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":70}],[{"start":{"row":108,"column":0},"end":{"row":110,"column":1},"action":"insert","lines":["AUTHENTICATION_BACKENDS = (","    ('django.contrib.auth.backends.ModelBackend'),",")"],"id":71}],[{"start":{"row":37,"column":34},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":72},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "],"id":74}],[{"start":{"row":37,"column":34},"end":{"row":38,"column":0},"action":"remove","lines":["",""],"id":75}],[{"start":{"row":87,"column":0},"end":{"row":88,"column":0},"action":"insert","lines":["",""],"id":76}],[{"start":{"row":88,"column":0},"end":{"row":93,"column":0},"action":"insert","lines":["# Update database configuration with $DATABASE_URL.","import dj_database_url","","db_from_env = dj_database_url.config(conn_max_age=500)","DATABASES['default'].update(db_from_env)",""],"id":77}],[{"start":{"row":34,"column":18},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":78},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":6},"action":"insert","lines":["''"],"id":79}],[{"start":{"row":35,"column":5},"end":{"row":35,"column":10},"action":"insert","lines":["boots"],"id":84}],[{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["r"],"id":85}],[{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["a"],"id":86}],[{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["p"],"id":87}],[{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["_"],"id":88}],[{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["a"],"id":89}],[{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["d"],"id":90}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["m"],"id":91}],[{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["i"],"id":92}],[{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["n"],"id":93}],[{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":[","],"id":94}],[{"start":{"row":35,"column":21},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":95},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":6},"action":"insert","lines":["''"],"id":96}],[{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":["m"],"id":97}],[{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":["a"],"id":98}],[{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"insert","lines":["r"],"id":99}],[{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["k"],"id":100}],[{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["d"],"id":101}],[{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":["o"],"id":102}],[{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":["w"],"id":103}],[{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":["n"],"id":104}],[{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["."],"id":105}],[{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"remove","lines":["."],"id":106}],[{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["."],"id":107}],[{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"remove","lines":["."],"id":108}],[{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":[","],"id":109}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":110}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["i"],"id":111}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["m"],"id":112}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"],"id":113}],[{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["o"],"id":114}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["r"],"id":115}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":5},"action":"remove","lines":["impor"],"id":116},{"start":{"row":13,"column":0},"end":{"row":13,"column":6},"action":"insert","lines":["import"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "],"id":117}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["a"],"id":118}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["a"],"id":119}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["m"],"id":120}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["a"],"id":121}],[{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["r"],"id":122}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["k"],"id":123}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["d"],"id":124}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["o"],"id":125}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["w"],"id":126}],[{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["n"],"id":127}],[{"start":{"row":45,"column":1},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":128}],[{"start":{"row":46,"column":0},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":129}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":39},"action":"insert","lines":["from django.conf import global_settings"],"id":130}],[{"start":{"row":47,"column":39},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":131}],[{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":132}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":35},"action":"insert","lines":["BOOTSTRAP_ADMIN_SIDEBAR_MENU = True"],"id":133}],[{"start":{"row":36,"column":21},"end":{"row":37,"column":15},"action":"remove","lines":["","    'markdown',"],"id":134}],[{"start":{"row":12,"column":9},"end":{"row":14,"column":0},"action":"remove","lines":["","import markdown",""],"id":135}],[{"start":{"row":33,"column":18},"end":{"row":34,"column":21},"action":"remove","lines":["","    'bootsrap_admin',"],"id":136}]]},"ace":{"folds":[],"scrolltop":646.9091148376465,"scrollleft":0,"selection":{"start":{"row":44,"column":0},"end":{"row":44,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":36,"state":"start","mode":"ace/mode/python"}},"timestamp":1493942733237,"hash":"e97610a39c36fc46dcc0d7322e902ad404e69ac5"}