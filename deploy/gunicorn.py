import multiprocessing

bind = '127.0.0.1:8000'
workers = multiprocessing.cpu_count() * 2
user = 'ubuntu'
max_requests = 500
threads = 1
proc_name = 'betterself_backend'
env = 'LANG="en_US.utf8"'
