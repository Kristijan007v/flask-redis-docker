  File "C:\MY PROJECTS\flask-redis-docker\venv\lib\site-packages\flask\app.py", line 756, in update_template_context
    context.update(func())
  File "C:\MY PROJECTS\flask-redis-docker\app\app.py", line 9, in current_count
    count = get_count()
  File "C:\MY PROJECTS\flask-redis-docker\app\db.py", line 17, in get_count
    currentCount = str(r.get('count')).decode('utf-8')
AttributeError: 'str' object has no attribute 'decode'
127.0.0.1 - - [01/Apr/2022 00:53:22] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 -
127.0.0.1 - - [01/Apr/2022 00:53:22] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
127.0.0.1 - - [01/Apr/2022 00:53:22] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
127.0.0.1 - - [01/Apr/2022 00:53:22] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\db.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
127.0.0.1 - - [01/Apr/2022 00:53:32] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:34] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:34] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:43] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:43] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:43] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:43] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:53:46] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
127.0.0.1 - - [01/Apr/2022 00:56:26] "GET / HTTP/1.1" 500 -
Traceback (most recent call last):
  File "C:\MY PROJECTS\flask-redis-docker\app\app.py", line 27, in <module>
    def reset_counter():
  File "C:\MY PROJECTS\flask-redis-docker\venv\lib\site-packages\flask\scaffold.py", line 440, in decorator
    self.add_url_rule(rule, endpoint, f, **options)
  File "C:\MY PROJECTS\flask-redis-docker\venv\lib\site-packages\flask\scaffold.py", line 56, in wrapper_func
    return f(self, *args, **kwargs)
  File "C:\MY PROJECTS\flask-redis-docker\venv\lib\site-packages\flask\app.py", line 1083, in add_url_rule
    rule = self.url_rule_class(rule, methods=methods, **options)
  File "C:\MY PROJECTS\flask-redis-docker\venv\lib\site-packages\werkzeug\routing.py", line 703, in __init__
    raise ValueError("urls must start with a leading slash")
ValueError: urls must start with a leading slash
127.0.0.1 - - [01/Apr/2022 00:56:26] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 -
127.0.0.1 - - [01/Apr/2022 00:56:26] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
127.0.0.1 - - [01/Apr/2022 00:56:26] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
127.0.0.1 - - [01/Apr/2022 00:56:26] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
127.0.0.1 - - [01/Apr/2022 00:57:10] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:13] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 00:57:13] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:16] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 00:57:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:18] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:18] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:18] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:20] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:21] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 00:57:21] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:23] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:23] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 00:57:23] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:38] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 00:57:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:46] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:57:48] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 00:57:48] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
127.0.0.1 - - [01/Apr/2022 00:58:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:58:39] "GET /reset HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:59:37] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 00:59:46] "GET /about HTTP/1.1" 200 -
 * Detected change in 'C:\\MY PROJECTS\\flask-redis-docker\\app\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
127.0.0.1 - - [01/Apr/2022 01:00:10] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:13] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:13] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:13] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:13] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:13] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:15] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 01:00:15] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:18] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 01:00:18] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:00:59] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:01] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:09] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:09] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:09] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:11] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:11] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:13] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:14] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:01:16] "GET / HTTP/1.1" 200 -
(venv) PS C:\MY PROJECTS\flask-redis-docker\app> flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-998-582
127.0.0.1 - - [01/Apr/2022 01:02:42] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:44] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:46] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 01:02:46] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:52] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:02:55] "GET /reset HTTP/1.1" 302 -
127.0.0.1 - - [01/Apr/2022 01:02:55] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [01/Apr/2022 01:03:03] "GET / HTTP/1.1" 200 -
(venv) PS C:\MY PROJECTS\flask-redis-docker\app> cd ..
(venv) PS C:\MY PROJECTS\flask-redis-docker> pip install pipreqs
Collecting pipreqs
  Using cached pipreqs-0.4.11-py2.py3-none-any.whl (32 kB)
Collecting yarg
  Using cached yarg-0.1.9-py2.py3-none-any.whl (19 kB)
Collecting docopt
  Using cached docopt-0.6.2.tar.gz (25 kB)
  Preparing metadata (setup.py) ... done
Collecting requests
  Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.3-py3-none-any.whl (61 kB)
Collecting charset-normalizer~=2.0.0
  Using cached charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
Using legacy 'setup.py install' for docopt, since package 'wheel' is not installed.
Installing collected packages: docopt, certifi, urllib3, idna, charset-normalizer, requests, yarg, pipreqs
  Running setup.py install for docopt ... done
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.12 docopt-0.6.2 idna-3.3 pipreqs-0.4.11 requests-2.27.1 urllib3-1.26.9 yarg-0.1.9
(venv) PS C:\MY PROJECTS\flask-redis-docker> pipreqs
INFO: Successfully saved requirements file in C:\MY PROJECTS\flask-redis-docker\requirements.txt
(venv) PS C:\MY PROJECTS\flask-redis-docker> cd app
(venv) PS C:\MY PROJECTS\flask-redis-docker\app> pipreqs
INFO: Successfully saved requirements file in C:\MY PROJECTS\flask-redis-docker\app\requirements.txt
(venv) PS C:\MY PROJECTS\flask-redis-docker\app> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 0.2s (2/2) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 31B                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                0.1s 
 => => transferring context: 2B                                                                                                                  0.0s 
failed to solve with frontend dockerfile.v0: failed to create LLB definition: the Dockerfile cannot be empty
(venv) PS C:\MY PROJECTS\flask-redis-docker\app> deactivate
PS C:\MY PROJECTS\flask-redis-docker\app> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 0.1s (2/2) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 29B                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                0.0s 
 => => transferring context: 2B                                                                                                                  0.0s 
failed to solve with frontend dockerfile.v0: failed to create LLB definition: the Dockerfile cannot be empty
PS C:\MY PROJECTS\flask-redis-docker\app> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 0.1s (2/2) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 29B                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                0.0s 
 => => transferring context: 2B                                                                                                                  0.0s 
failed to solve with frontend dockerfile.v0: failed to create LLB definition: the Dockerfile cannot be empty
PS C:\MY PROJECTS\flask-redis-docker\app> cd ..
PS C:\MY PROJECTS\flask-redis-docker> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 0.1s (2/2) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 29B                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                0.1s 
 => => transferring context: 44B                                                                                                                 0.0s 
failed to solve with frontend dockerfile.v0: failed to create LLB definition: the Dockerfile cannot be empty
PS C:\MY PROJECTS\flask-redis-docker> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 7.2s (13/15)
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 303B                                                                                                             0.0s 
 => [internal] load .dockerignore                                                                                                                0.1s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       2.5s 
 => [auth] docker/dockerfile:pull token for registry-1.docker.io                                                                                 0.0s
 => docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                         2.0s
 => => resolve docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                             0.0s 
 => => sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff 2.00kB / 2.00kB                                                   0.0s
 => => sha256:0fd968d6b87118e5c321970e04567ad319a583d3ff7ea88fb57015f14fbeeaa7 528B / 528B                                                       0.0s 
 => => sha256:c45593c04fe618ad08c8f3e6cdd0d6d42c7e1dd8e103adb6c88bed6fe6c5d2c6 2.37kB / 2.37kB                                                   0.0s
 => => sha256:96cc9c4d9b06a8798ac4c21bd88d4a32f3737594d10cd176ac4f2549bea93c71 9.93MB / 9.93MB                                                   1.7s 
 => => extracting sha256:96cc9c4d9b06a8798ac4c21bd88d4a32f3737594d10cd176ac4f2549bea93c71                                                        0.2s 
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => [internal] load .dockerignore                                                                                                                0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        1.9s 
 => [auth] library/python:pull token for registry-1.docker.io                                                                                    0.0s 
 => [internal] load build context                                                                                                                0.4s 
 => => transferring context: 9.46MB                                                                                                              0.4s 
 => CANCELED [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023         0.4s 
 => => resolve docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s 
 => => sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023 1.86kB / 1.86kB                                                   0.0s 
 => => sha256:ceec3171247ccc8202523d89de726323c7f1b364b5e36910a9aa8f93caeece79 1.37kB / 1.37kB                                                   0.0s 
 => => sha256:da8c3561d9c1194a917a226328e1d68871fc1517a016cb282e15a41ee72424e9 7.56kB / 7.56kB                                                   0.0s 
 => => sha256:f003217c5aaebdfee0b9a448fbabd995e5f0159f5b231460c0ecc21baf171953 0B / 27.15MB                                                      0.4s 
 => => sha256:89f192ed04782b15b45c31ce33d4fd7f8a80041ff0cfa31c95e7cd750fc396f7 0B / 2.78MB                                                       0.4s 
 => => sha256:39e7b7dc56b7a621e7cc3599b145a8535ad965602abf6ccbeafb34d38e67ab32 0B / 11.29MB                                                      0.4s 
 => CACHED [2/5] WORKDIR /app                                                                                                                    0.0s 
 => ERROR [3/5] COPY requirements.txt requirements.txt                                                                                           0.0s 
------
 > [3/5] COPY requirements.txt requirements.txt:
------
failed to compute cache key: "/requirements.txt" not found: not found
PS C:\MY PROJECTS\flask-redis-docker> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 19.0s (14/14) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 32B                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                0.1s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       0.7s 
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load .dockerignore                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        0.3s 
 => [internal] load build context                                                                                                                0.3s
 => => transferring context: 161.68kB                                                                                                            0.2s
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                 11.1s 
 => => resolve docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s 
 => => sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023 1.86kB / 1.86kB                                                   0.0s 
 => => sha256:ceec3171247ccc8202523d89de726323c7f1b364b5e36910a9aa8f93caeece79 1.37kB / 1.37kB                                                   0.0s 
 => => sha256:da8c3561d9c1194a917a226328e1d68871fc1517a016cb282e15a41ee72424e9 7.56kB / 7.56kB                                                   0.0s 
 => => sha256:f003217c5aaebdfee0b9a448fbabd995e5f0159f5b231460c0ecc21baf171953 27.15MB / 27.15MB                                                 9.1s 
 => => sha256:89f192ed04782b15b45c31ce33d4fd7f8a80041ff0cfa31c95e7cd750fc396f7 2.78MB / 2.78MB                                                   1.3s 
 => => sha256:39e7b7dc56b7a621e7cc3599b145a8535ad965602abf6ccbeafb34d38e67ab32 11.29MB / 11.29MB                                                 8.8s 
 => => sha256:d931cd7e647a12910eb509471d193ce6f19fb1f261b8632face8dad9749404c3 235B / 235B                                                       1.7s 
 => => sha256:0372c15f94026a2184cb24894401ff9e832ab7840e2e792cd98c448f19a39266 3.17MB / 3.17MB                                                   4.0s 
 => => extracting sha256:f003217c5aaebdfee0b9a448fbabd995e5f0159f5b231460c0ecc21baf171953                                                        0.8s 
 => => extracting sha256:89f192ed04782b15b45c31ce33d4fd7f8a80041ff0cfa31c95e7cd750fc396f7                                                        0.1s 
 => => extracting sha256:39e7b7dc56b7a621e7cc3599b145a8535ad965602abf6ccbeafb34d38e67ab32                                                        0.3s 
 => => extracting sha256:d931cd7e647a12910eb509471d193ce6f19fb1f261b8632face8dad9749404c3                                                        0.0s 
 => => extracting sha256:0372c15f94026a2184cb24894401ff9e832ab7840e2e792cd98c448f19a39266                                                        0.2s 
 => [2/5] WORKDIR /app                                                                                                                           0.2s 
 => [3/5] COPY requirements.txt requirements.txt                                                                                                 0.1s 
 => [4/5] RUN pip3 install -r requirements.txt                                                                                                   5.6s 
 => [5/5] COPY . .                                                                                                                               0.2s 
 => exporting to image                                                                                                                           0.2s 
 => => exporting layers                                                                                                                          0.2s 
 => => writing image sha256:2046c51bb77756730407299cfc6b0f2b268d26aa091ef78a17175264078ee575                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 3.4s (14/14) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 300B                                                                                                             0.0s 
 => [internal] load .dockerignore                                                                                                                0.1s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       1.5s 
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        0.7s 
 => [internal] load build context                                                                                                                0.3s
 => => transferring context: 162.78kB                                                                                                            0.3s
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s 
 => CACHED [2/5] WORKDIR /app                                                                                                                    0.0s 
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                                                          0.0s 
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                                            0.0s 
 => [5/5] COPY . .                                                                                                                               0.2s 
 => exporting to image                                                                                                                           0.2s 
 => => exporting layers                                                                                                                          0.2s 
 => => writing image sha256:b893a59c388fe18143fae5dd64f56bda5ae555ef94e2389de1479c2240f2d280                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker> docker build -t kristijan007v/flask-redis:v1.0 . 
[+] Building 2.6s (14/14) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 32B                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                0.0s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       0.8s 
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        0.7s 
 => [internal] load build context                                                                                                                0.3s
 => => transferring context: 162.51kB                                                                                                            0.3s
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s 
 => CACHED [2/5] WORKDIR /app                                                                                                                    0.0s 
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                                                          0.0s 
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                                            0.0s 
 => [5/5] COPY . .                                                                                                                               0.2s 
 => exporting to image                                                                                                                           0.2s 
 => => exporting layers                                                                                                                          0.2s 
 => => writing image sha256:331685300a31bafe43d7557b3754a57e76f914fa93f721d43576926e934b7fc8                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 3.2s (14/14) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 277B                                                                                                             0.0s 
 => [internal] load .dockerignore                                                                                                                0.0s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       1.5s 
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load .dockerignore                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        0.7s 
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s
 => [internal] load build context                                                                                                                0.3s
 => => transferring context: 162.75kB                                                                                                            0.3s 
 => CACHED [2/5] WORKDIR /app                                                                                                                    0.0s 
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                                                          0.0s 
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                                            0.0s 
 => [5/5] COPY . .                                                                                                                               0.2s 
 => exporting to image                                                                                                                           0.2s 
 => => exporting layers                                                                                                                          0.2s 
 => => writing image sha256:f5c0ec790bd0db69a415134c91bd424493af000c6942b677c65f1f5de49fa259                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 3.5s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => => transferring dockerfile: 271B                                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                0.0s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       1.5s 
 => [auth] docker/dockerfile:pull token for registry-1.docker.io                                                                                 0.0s
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load .dockerignore                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        0.9s 
 => [auth] library/python:pull token for registry-1.docker.io                                                                                    0.0s
 => [internal] load build context                                                                                                                0.3s 
 => => transferring context: 161.89kB                                                                                                            0.3s 
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s 
 => CACHED [2/5] WORKDIR /app                                                                                                                    0.0s 
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                                                          0.0s 
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                                            0.0s 
 => [5/5] COPY . .                                                                                                                               0.2s 
 => exporting to image                                                                                                                           0.2s 
 => => exporting layers                                                                                                                          0.2s 
 => => writing image sha256:9e06f7b7e300beb118c8835d5e23a8e06c1d7b7bde98350b5a68cc00644ef222                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker> cd app
PS C:\MY PROJECTS\flask-redis-docker\app> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 8.1s (14/14) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.1s
 => => transferring dockerfile: 275B                                                                                                             0.0s 
 => [internal] load .dockerignore                                                                                                                0.1s 
 => => transferring context: 51B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       0.8s 
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load .dockerignore                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        0.7s 
 => [internal] load build context                                                                                                                0.1s
 => => transferring context: 2.83kB                                                                                                              0.0s
 => CACHED [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023           0.0s 
 => [2/5] WORKDIR /python-docker                                                                                                                 0.1s 
 => [3/5] COPY requirements.txt requirements.txt                                                                                                 0.1s 
 => [4/5] RUN pip3 install -r requirements.txt                                                                                                   5.8s 
 => [5/5] COPY . .                                                                                                                               0.1s 
 => exporting to image                                                                                                                           0.2s 
 => => exporting layers                                                                                                                          0.2s 
 => => writing image sha256:067f5249749cac6b4e143c47d564bc2442745bd6c26cf1c741516a8d57855e78                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker\app> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 2.0s (14/14) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 290B                                                                                                             0.0s 
 => [internal] load .dockerignore                                                                                                                0.1s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       0.7s 
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load .dockerignore                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        0.7s 
 => [internal] load build context                                                                                                                0.0s
 => => transferring context: 550B                                                                                                                0.0s
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s 
 => CACHED [2/5] WORKDIR /python-docker                                                                                                          0.0s 
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                                                          0.0s 
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                                            0.0s 
 => [5/5] COPY . .                                                                                                                               0.1s 
 => exporting to image                                                                                                                           0.1s 
 => => exporting layers                                                                                                                          0.1s 
 => => writing image sha256:0ade43779e09a525f56ded282f21d60fdfbed9e131c4e8399f4139f18d9d1303                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker\app> cd ..
PS C:\MY PROJECTS\flask-redis-docker> docker compose-up
docker: 'compose-up' is not a docker command.
See 'docker --help'
PS C:\MY PROJECTS\flask-redis-docker> docker compose up
Top-level object must be a mapping
PS C:\MY PROJECTS\flask-redis-docker> cd app
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
Top-level object must be a mapping
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Running 7/7
 - redis Pulled                                                                                                                                 12.7s 
   - 40e059520d19 Pull complete                                                                                                                  1.4s
   - 9801e2773878 Pull complete                                                                                                                  1.5s 
   - 8a19c93db723 Pull complete                                                                                                                  1.6s 
   - ffaef02f5447 Pull complete                                                                                                                  8.5s 
   - 1b609b4c7a67 Pull complete                                                                                                                  8.6s 
   - ee96e1297c38 Pull complete                                                                                                                  8.6s 
[+] Running 3/3
 - Network app_default    Created                                                                                                                0.9s 
 - Container app-redis-1  Created                                                                                                                0.6s
 - Container app-web-1    Created                                                                                                                0.1s 
Attaching to app-redis-1, app-web-1
app-redis-1  | 1:C 31 Mar 2022 23:25:44.194 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
app-redis-1  | 1:C 31 Mar 2022 23:25:44.194 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
app-redis-1  | 1:C 31 Mar 2022 23:25:44.194 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
app-redis-1  | 1:M 31 Mar 2022 23:25:44.195 * monotonic clock: POSIX clock_gettime
app-redis-1  | 1:M 31 Mar 2022 23:25:44.195 * Running mode=standalone, port=6379.
app-redis-1  | 1:M 31 Mar 2022 23:25:44.195 # Server initialized
app-redis-1  | 1:M 31 Mar 2022 23:25:44.195 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.  
app-redis-1  | 1:M 31 Mar 2022 23:25:44.196 * Ready to accept connections
app-web-1    |  * Environment: production
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |    Use a production WSGI server instead.
app-web-1    |  * Debug mode: off
app-web-1    |  * Running on all addresses (0.0.0.0)
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |  * Running on http://127.0.0.1:5000
app-web-1    |  * Running on http://172.18.0.2:5000 (Press CTRL+C to quit)
app-web-1    | [2022-03-31 23:25:48,490] ERROR in app: Exception on / [GET]
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 614, in connect
app-web-1    |     sock = self.retry.call_with_retry(
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/retry.py", line 45, in call_with_retry
app-web-1    |     return do()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 615, in <lambda>
app-web-1    |     lambda: self._connect(), lambda error: self.disconnect(error)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 680, in _connect
app-web-1    |     raise err
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 668, in _connect
app-web-1    |     sock.connect(socket_address)
app-web-1    | ConnectionRefusedError: [Errno 111] Connection refused
app-web-1    |
app-web-1    | During handling of the above exception, another exception occurred:
app-web-1    |
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2077, in wsgi_app
app-web-1    |     response = self.full_dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1525, in full_dispatch_request
app-web-1    |     rv = self.handle_user_exception(e)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1523, in full_dispatch_request
app-web-1    |     rv = self.dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1509, in dispatch_request
app-web-1    |     return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
app-web-1    |   File "/python-docker/app.py", line 19, in index
app-web-1    |     count()
app-web-1    |   File "/python-docker/db.py", line 14, in count
app-web-1    |     r.incr('count')
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/commands/core.py", line 1719, in incrby
app-web-1    |     return self.execute_command("INCRBY", name, amount)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/client.py", line 1192, in execute_command
app-web-1    |     conn = self.connection or pool.get_connection(command_name, **options)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 1386, in get_connection
app-web-1    |     connection.connect()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 620, in connect
app-web-1    |     raise ConnectionError(self._error_message(e))
app-web-1    | redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:25:48] "GET / HTTP/1.1" 500 -
Gracefully stopping... (press Ctrl+C again to force)
[+] Running 2/2
 - Container app-web-1    Stopped                                                                                                               11.6s 
 - Container app-redis-1  Stopped                                                                                                                1.5s 
canceled
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Running 2/2
 - Container app-web-1    Created                                                                                                                0.0s 
 - Container app-redis-1  Recreated                                                                                                              0.2s 
Attaching to app-redis-1, app-web-1
Error response from daemon: driver failed programming external connectivity on endpoint app-redis-1 (77d0598f065bc73edc10b53686cf88b977db26cc5eece5c52fb8de5b14604c17): Bind for 0.0.0.0:6379 failed: port is already allocated
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Running 1/0
 - Container app-web-1  Running                                                                                                                  0.0s 
Attaching to app-redis-1, app-web-1
app-redis-1  | 1:C 31 Mar 2022 23:27:11.873 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
app-redis-1  | 1:C 31 Mar 2022 23:27:11.873 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
app-redis-1  | 1:C 31 Mar 2022 23:27:11.873 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
app-redis-1  | 1:M 31 Mar 2022 23:27:11.873 * monotonic clock: POSIX clock_gettime
app-redis-1  | 1:M 31 Mar 2022 23:27:11.873 * Running mode=standalone, port=6379.
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 # Server initialized
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.  
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 * Loading RDB produced by version 6.2.6
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 * RDB age 37 seconds
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 * RDB memory usage when created 0.77 Mb
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 # Done loading RDB, keys loaded: 0, keys expired: 0.
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 * DB loaded from disk: 0.000 seconds
app-redis-1  | 1:M 31 Mar 2022 23:27:11.874 * Ready to accept connections
app-web-1    | [2022-03-31 23:27:18,607] ERROR in app: Exception on / [GET]
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 614, in connect
app-web-1    |     sock = self.retry.call_with_retry(
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/retry.py", line 45, in call_with_retry
app-web-1    |     return do()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 615, in <lambda>
app-web-1    |     lambda: self._connect(), lambda error: self.disconnect(error)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 680, in _connect
app-web-1    |     raise err
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 668, in _connect
app-web-1    |     sock.connect(socket_address)
app-web-1    | ConnectionRefusedError: [Errno 111] Connection refused
app-web-1    |
app-web-1    | During handling of the above exception, another exception occurred:
app-web-1    |
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2077, in wsgi_app
app-web-1    |     response = self.full_dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1525, in full_dispatch_request
app-web-1    |     rv = self.handle_user_exception(e)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1523, in full_dispatch_request
app-web-1    |     rv = self.dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1509, in dispatch_request
app-web-1    |     return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
app-web-1    |   File "/python-docker/app.py", line 19, in index
app-web-1    |     count()
app-web-1    |   File "/python-docker/db.py", line 14, in count
app-web-1    |     r.incr('count')
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/commands/core.py", line 1719, in incrby
app-web-1    |     return self.execute_command("INCRBY", name, amount)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/client.py", line 1192, in execute_command
app-web-1    |     conn = self.connection or pool.get_connection(command_name, **options)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 1386, in get_connection
app-web-1    |     connection.connect()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 620, in connect
app-web-1    |     raise ConnectionError(self._error_message(e))
app-web-1    | redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:27:18] "GET / HTTP/1.1" 500 -
Gracefully stopping... (press Ctrl+C again to force)
[+] Running 2/2
 - Container app-web-1    Stopped                                                                                                               13.6s 
 - Container app-redis-1  Stopped                                                                                                                3.7s 
canceled
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Running 2/2
 - Container app-web-1    Created                                                                                                                0.0s 
 - Container app-redis-1  Recreated                                                                                                              2.0s 
Attaching to app-redis-1, app-web-1
app-web-1    |  * Environment: production
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |    Use a production WSGI server instead.
app-web-1    |  * Debug mode: off
app-web-1    |  * Running on all addresses (0.0.0.0)
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |  * Running on http://127.0.0.1:5000
app-web-1    |  * Running on http://172.18.0.2:5000 (Press CTRL+C to quit)
app-redis-1  | 1:C 31 Mar 2022 23:29:13.186 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
app-redis-1  | 1:C 31 Mar 2022 23:29:13.186 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
app-redis-1  | 1:C 31 Mar 2022 23:29:13.186 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
app-redis-1  | 1:M 31 Mar 2022 23:29:13.186 * monotonic clock: POSIX clock_gettime
app-redis-1  | 1:M 31 Mar 2022 23:29:13.187 * Running mode=standalone, port=6379.
app-redis-1  | 1:M 31 Mar 2022 23:29:13.187 # Server initialized
app-redis-1  | 1:M 31 Mar 2022 23:29:13.187 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.  
app-redis-1  | 1:M 31 Mar 2022 23:29:13.188 * Loading RDB produced by version 6.2.6
app-redis-1  | 1:M 31 Mar 2022 23:29:13.188 * RDB age 39 seconds
app-redis-1  | 1:M 31 Mar 2022 23:29:13.188 * RDB memory usage when created 0.77 Mb
app-redis-1  | 1:M 31 Mar 2022 23:29:13.188 # Done loading RDB, keys loaded: 0, keys expired: 0.
app-redis-1  | 1:M 31 Mar 2022 23:29:13.188 * DB loaded from disk: 0.000 seconds
app-redis-1  | 1:M 31 Mar 2022 23:29:13.188 * Ready to accept connections
app-web-1    | [2022-03-31 23:29:19,121] ERROR in app: Exception on / [GET]
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 614, in connect
app-web-1    |     sock = self.retry.call_with_retry(
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/retry.py", line 45, in call_with_retry
app-web-1    |     return do()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 615, in <lambda>
app-web-1    |     lambda: self._connect(), lambda error: self.disconnect(error)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 680, in _connect
app-web-1    |     raise err
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 668, in _connect
app-web-1    |     sock.connect(socket_address)
app-web-1    | ConnectionRefusedError: [Errno 111] Connection refused
app-web-1    |
app-web-1    | During handling of the above exception, another exception occurred:
app-web-1    |
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2077, in wsgi_app
app-web-1    |     response = self.full_dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1525, in full_dispatch_request
app-web-1    |     rv = self.handle_user_exception(e)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1523, in full_dispatch_request
app-web-1    |     rv = self.dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1509, in dispatch_request
app-web-1    |     return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
app-web-1    |   File "/python-docker/app.py", line 19, in index
app-web-1    |     count()
app-web-1    |   File "/python-docker/db.py", line 14, in count
app-web-1    |     r.incr('count')
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/commands/core.py", line 1719, in incrby
app-web-1    |     return self.execute_command("INCRBY", name, amount)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/client.py", line 1192, in execute_command
app-web-1    |     conn = self.connection or pool.get_connection(command_name, **options)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 1386, in get_connection
app-web-1    |     connection.connect()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 620, in connect
app-web-1    |     raise ConnectionError(self._error_message(e))
app-web-1    | redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:29:19] "GET / HTTP/1.1" 500 -
app-web-1    | [2022-03-31 23:29:20,119] ERROR in app: Exception on / [GET]
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 614, in connect
app-web-1    |     sock = self.retry.call_with_retry(
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/retry.py", line 45, in call_with_retry
app-web-1    |     return do()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 615, in <lambda>
app-web-1    |     lambda: self._connect(), lambda error: self.disconnect(error)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 680, in _connect
app-web-1    |     raise err
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 668, in _connect
app-web-1    |     sock.connect(socket_address)
app-web-1    | ConnectionRefusedError: [Errno 111] Connection refused
app-web-1    |
app-web-1    | During handling of the above exception, another exception occurred:
app-web-1    |
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2077, in wsgi_app
app-web-1    |     response = self.full_dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1525, in full_dispatch_request
app-web-1    |     rv = self.handle_user_exception(e)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1523, in full_dispatch_request
app-web-1    |     rv = self.dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1509, in dispatch_request
app-web-1    |     return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
app-web-1    |   File "/python-docker/app.py", line 19, in index
app-web-1    |     count()
app-web-1    |   File "/python-docker/db.py", line 14, in count
app-web-1    |     r.incr('count')
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/commands/core.py", line 1719, in incrby
app-web-1    |     return self.execute_command("INCRBY", name, amount)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/client.py", line 1192, in execute_command
app-web-1    |     conn = self.connection or pool.get_connection(command_name, **options)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 1386, in get_connection
app-web-1    |     connection.connect()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 620, in connect
app-web-1    |     raise ConnectionError(self._error_message(e))
app-web-1    | redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:29:20] "GET / HTTP/1.1" 500 -
app-web-1    | [2022-03-31 23:29:20,455] ERROR in app: Exception on / [GET]
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 614, in connect
app-web-1    |     sock = self.retry.call_with_retry(
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/retry.py", line 45, in call_with_retry
app-web-1    |     return do()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 615, in <lambda>
app-web-1    |     lambda: self._connect(), lambda error: self.disconnect(error)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 680, in _connect
app-web-1    |     raise err
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 668, in _connect
app-web-1    |     sock.connect(socket_address)
app-web-1    | ConnectionRefusedError: [Errno 111] Connection refused
app-web-1    |
app-web-1    | During handling of the above exception, another exception occurred:
app-web-1    |
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2077, in wsgi_app
app-web-1    |     response = self.full_dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1525, in full_dispatch_request
app-web-1    |     rv = self.handle_user_exception(e)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1523, in full_dispatch_request
app-web-1    |     rv = self.dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1509, in dispatch_request
app-web-1    |     return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
app-web-1    |   File "/python-docker/app.py", line 19, in index
app-web-1    |     count()
app-web-1    |   File "/python-docker/db.py", line 14, in count
app-web-1    |     r.incr('count')
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/commands/core.py", line 1719, in incrby
app-web-1    |     return self.execute_command("INCRBY", name, amount)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/client.py", line 1192, in execute_command
app-web-1    |     conn = self.connection or pool.get_connection(command_name, **options)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 1386, in get_connection
app-web-1    |     connection.connect()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 620, in connect
app-web-1    |     raise ConnectionError(self._error_message(e))
app-web-1    | redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:29:20] "GET / HTTP/1.1" 500 -
Gracefully stopping... (press Ctrl+C again to force)
[+] Running 2/2
 - Container app-web-1    Stopped                                                                                                               11.7s 
 - Container app-redis-1  Stopped                                                                                                                1.6s 
canceled
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Running 2/2
 - Container app-web-1    Created                                                                                                                0.0s 
 - Container app-redis-1  Recreated                                                                                                              0.2s 
Attaching to app-redis-1, app-web-1
app-redis-1  | 1:C 31 Mar 2022 23:29:51.987 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
app-redis-1  | 1:C 31 Mar 2022 23:29:51.987 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
app-redis-1  | 1:C 31 Mar 2022 23:29:51.987 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 * monotonic clock: POSIX clock_gettime
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 * Running mode=standalone, port=6379.
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 # Server initialized
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.  
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 * Loading RDB produced by version 6.2.6
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 * RDB age 16 seconds
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 * RDB memory usage when created 0.77 Mb
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 # Done loading RDB, keys loaded: 0, keys expired: 0.
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 * DB loaded from disk: 0.000 seconds
app-redis-1  | 1:M 31 Mar 2022 23:29:51.988 * Ready to accept connections
app-web-1    |  * Environment: production
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |    Use a production WSGI server instead.
app-web-1    |  * Debug mode: off
app-web-1    |  * Running on all addresses (0.0.0.0)
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |  * Running on http://127.0.0.1:5000
app-web-1    |  * Running on http://172.18.0.3:5000 (Press CTRL+C to quit)
app-web-1    | [2022-03-31 23:29:59,186] ERROR in app: Exception on / [GET]
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 614, in connect
app-web-1    |     sock = self.retry.call_with_retry(
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/retry.py", line 45, in call_with_retry
app-web-1    |     return do()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 615, in <lambda>
app-web-1    |     lambda: self._connect(), lambda error: self.disconnect(error)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 680, in _connect
app-web-1    |     raise err
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 668, in _connect
app-web-1    |     sock.connect(socket_address)
app-web-1    | ConnectionRefusedError: [Errno 111] Connection refused
app-web-1    |
app-web-1    | During handling of the above exception, another exception occurred:
app-web-1    |
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2077, in wsgi_app
app-web-1    |     response = self.full_dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1525, in full_dispatch_request
app-web-1    |     rv = self.handle_user_exception(e)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1523, in full_dispatch_request
app-web-1    |     rv = self.dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1509, in dispatch_request
app-web-1    |     return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
app-web-1    |   File "/python-docker/app.py", line 19, in index
app-web-1    |     count()
app-web-1    |   File "/python-docker/db.py", line 14, in count
app-web-1    |     r.incr('count')
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/commands/core.py", line 1719, in incrby
app-web-1    |     return self.execute_command("INCRBY", name, amount)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/client.py", line 1192, in execute_command
app-web-1    |     conn = self.connection or pool.get_connection(command_name, **options)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 1386, in get_connection
app-web-1    |     connection.connect()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 620, in connect
app-web-1    |     raise ConnectionError(self._error_message(e))
app-web-1    | redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:29:59] "GET / HTTP/1.1" 500 -
Gracefully stopping... (press Ctrl+C again to force)
[+] Running 2/2
 - Container app-web-1    Stopped                                                                                                               13.1s 
 - Container app-redis-1  Stopped                                                                                                                3.1s 
canceled
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Running 2/2
 - Container app-redis-1  Created                                                                                                                0.0s 
 - Container app-web-1    Recreated                                                                                                              0.2s 
Attaching to app-redis-1, app-web-1
app-redis-1  | 1:C 31 Mar 2022 23:33:11.505 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
app-redis-1  | 1:C 31 Mar 2022 23:33:11.505 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
app-redis-1  | 1:C 31 Mar 2022 23:33:11.505 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
app-redis-1  | 1:M 31 Mar 2022 23:33:11.505 * monotonic clock: POSIX clock_gettime
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 * Running mode=standalone, port=6379.
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 # Server initialized
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.  
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 * Loading RDB produced by version 6.2.6
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 * RDB age 20 seconds
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 * RDB memory usage when created 0.79 Mb
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 # Done loading RDB, keys loaded: 0, keys expired: 0.
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 * DB loaded from disk: 0.000 seconds
app-redis-1  | 1:M 31 Mar 2022 23:33:11.506 * Ready to accept connections
app-web-1    |  * Environment: production
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |    Use a production WSGI server instead.
app-web-1    |  * Debug mode: off
app-web-1    |  * Running on all addresses (0.0.0.0)
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |  * Running on http://127.0.0.1:5000
app-web-1    |  * Running on http://172.18.0.3:5000 (Press CTRL+C to quit)
app-web-1    | [2022-03-31 23:33:14,838] ERROR in app: Exception on / [GET]
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 614, in connect
app-web-1    |     sock = self.retry.call_with_retry(
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/retry.py", line 45, in call_with_retry
app-web-1    |     return do()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 615, in <lambda>
app-web-1    |     lambda: self._connect(), lambda error: self.disconnect(error)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 680, in _connect
app-web-1    |     raise err
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 668, in _connect
app-web-1    |     sock.connect(socket_address)
app-web-1    | ConnectionRefusedError: [Errno 111] Connection refused
app-web-1    |
app-web-1    | During handling of the above exception, another exception occurred:
app-web-1    |
app-web-1    | Traceback (most recent call last):
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2077, in wsgi_app
app-web-1    |     response = self.full_dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1525, in full_dispatch_request
app-web-1    |     rv = self.handle_user_exception(e)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1523, in full_dispatch_request
app-web-1    |     rv = self.dispatch_request()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1509, in dispatch_request
app-web-1    |     return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
app-web-1    |   File "/python-docker/app.py", line 19, in index
app-web-1    |     count()
app-web-1    |   File "/python-docker/db.py", line 14, in count
app-web-1    |     r.incr('count')
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/commands/core.py", line 1719, in incrby
app-web-1    |     return self.execute_command("INCRBY", name, amount)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/client.py", line 1192, in execute_command
app-web-1    |     conn = self.connection or pool.get_connection(command_name, **options)
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 1386, in get_connection
app-web-1    |     connection.connect()
app-web-1    |   File "/usr/local/lib/python3.8/site-packages/redis/connection.py", line 620, in connect
app-web-1    |     raise ConnectionError(self._error_message(e))
app-web-1    | redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:33:14] "GET / HTTP/1.1" 500 -
Gracefully stopping... (press Ctrl+C again to force)
[+] Running 2/2
 - Container app-redis-1  Stopped                                                                                                                0.7s 
 - Container app-web-1    Stopped                                                                                                               10.6s 
canceled
PS C:\MY PROJECTS\flask-redis-docker\app> docker build -t kristijan007v/flask-redis:v1.0 .
[+] Building 3.2s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 32B                                                                                                              0.0s 
 => [internal] load .dockerignore                                                                                                                0.0s 
 => => transferring context: 34B                                                                                                                 0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                       1.6s 
 => [auth] docker/dockerfile:pull token for registry-1.docker.io                                                                                 0.0s
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:178c4e4a93795b9365dbf6cf10da8fcf517fcb4a17f1943a775c0f548e9fc2ff                  0.0s
 => [internal] load .dockerignore                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                        1.1s 
 => [auth] library/python:pull token for registry-1.docker.io                                                                                    0.0s
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:be583dd9bff379065b9b591e8e4cf441730dbb4609f6654b7a8a6cb6e921c023                  0.0s 
 => [internal] load build context                                                                                                                0.0s 
 => => transferring context: 831B                                                                                                                0.0s 
 => CACHED [2/5] WORKDIR /python-docker                                                                                                          0.0s 
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                                                          0.0s 
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                                            0.0s 
 => [5/5] COPY . .                                                                                                                               0.1s 
 => exporting to image                                                                                                                           0.1s 
 => => exporting layers                                                                                                                          0.1s 
 => => writing image sha256:afeb1d88a9d213a8553d875bfe7508f7bfabfed5adb1245ec66ca8d396fcb0ae                                                     0.0s 
 => => naming to docker.io/kristijan007v/flask-redis:v1.0                                                                                        0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Building 0.0s (0/0)
unable to prepare context: path "afeb1d88a9d2" not found
PS C:\MY PROJECTS\flask-redis-docker\app> docker compose up
[+] Running 2/2
 - Container app-web-1    Recreated                                                                                                              0.2s 
 - Container app-redis-1  Recreated                                                                                                              0.2s 
Attaching to app-redis-1, app-web-1
app-redis-1  | 1:C 31 Mar 2022 23:36:10.335 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
app-redis-1  | 1:C 31 Mar 2022 23:36:10.335 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
app-redis-1  | 1:C 31 Mar 2022 23:36:10.335 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
app-redis-1  | 1:M 31 Mar 2022 23:36:10.335 * monotonic clock: POSIX clock_gettime
app-redis-1  | 1:M 31 Mar 2022 23:36:10.335 * Running mode=standalone, port=6379.
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 # Server initialized
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.  
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 * Loading RDB produced by version 6.2.6
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 * RDB age 107 seconds
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 * RDB memory usage when created 0.77 Mb
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 # Done loading RDB, keys loaded: 0, keys expired: 0.
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 * DB loaded from disk: 0.000 seconds
app-redis-1  | 1:M 31 Mar 2022 23:36:10.336 * Ready to accept connections
app-web-1    |  * Environment: production
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |    Use a production WSGI server instead.
app-web-1    |  * Debug mode: off
app-web-1    |  * Running on all addresses (0.0.0.0)
app-web-1    |    WARNING: This is a development server. Do not use it in a production deployment.
app-web-1    |  * Running on http://127.0.0.1:5000
app-web-1    |  * Running on http://172.18.0.3:5000 (Press CTRL+C to quit)
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:36:13] "GET / HTTP/1.1" 200 -
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:36:21] "GET / HTTP/1.1" 200 -
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:37:14] "GET / HTTP/1.1" 200 -
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:37:14] "GET / HTTP/1.1" 200 -
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:37:14] "GET / HTTP/1.1" 200 -
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:37:15] "GET /reset HTTP/1.1" 302 -
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:37:15] "GET /about HTTP/1.1" 200 -
app-web-1    | 172.18.0.1 - - [31/Mar/2022 23:37:16] "GET / HTTP/1.1" 200 -
Gracefully stopping... (press Ctrl+C again to force)
[+] Running 2/2
 - Container app-redis-1  Stopped                                                                                                                3.5s 
 - Container app-web-1    Stopped                                                                                                               13.7s 
canceled
PS C:\MY PROJECTS\flask-redis-docker\app>