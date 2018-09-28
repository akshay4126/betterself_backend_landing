[program:{{ name }}]
command={{ command }}
directory=/home/ubuntu/betterself_backend
autostart=true
autorestart=true
killasgroup=true
user=ubuntu
redirect_stderr=false
stdout_logfile=/var/log/supervisor/{{ name }}.log
stderr_logfile=/var/log/supervisor/{{ name }}_errors.log