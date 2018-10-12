server {
  server_name betterself.today;
  listen 80;
  listen 443 ssl;

  location ~ (/api/|/api-auth/|/admin/|/sitemap.xml) {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Url-Scheme $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_pass http://127.0.0.1:8000;
  }

  location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Url-Scheme $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_pass http://127.0.0.1:8080;
  }

  location /robots.txt {
    alias /home/ubuntu/betterself_backend/static/robots-prod.txt;
  }

  location ^~ /static_backend/ {
    alias /home/ubuntu/betterself_backend/static/;
  }

  location /media {
    add_header "Access-Control-Allow-Origin" "$http_origin";
    add_header "Access-Control-Allow-Credentials" "true";
    root /home/ubuntu/betterself_backend/;
  }

  client_max_body_size 250M;

  ssl_certificate /etc/letsencrypt/live/betterself.today/fullchain.pem; # managed by Certbot
  ssl_certificate_key /etc/letsencrypt/live/betterself.today/privkey.pem; # managed by Certbot
  include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
  ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

  if ($scheme != "https") {
      return 301 https://$host$request_uri;
  } # managed by Certbot
}

# Redirects

server {
    server_name www.betterself.today;
    listen 80;
    return 301 https://betterself.today$request_uri;
}

server {
    server_name www.betterself.today;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/www.betterself.today/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.betterself.today/privkey.pem; # managed by Certbot
    return 301 https://betterself.today$request_uri;
}

server {
    server_name betterself.app;
    listen 80;
    return 301 https://betterself.today$request_uri;
}

server {
    server_name betterself.app;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/betterself.app/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/betterself.app/privkey.pem; # managed by Certbot
    return 301 https://betterself.today$request_uri;
}

server {
    server_name www.betterself.app;
    listen 80;
    return 301 https://betterself.today$request_uri;
}

server {
    server_name www.betterself.app;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/www.betterself.app/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.betterself.app/privkey.pem; # managed by Certbot
    return 301 https://betterself.today$request_uri;
}
