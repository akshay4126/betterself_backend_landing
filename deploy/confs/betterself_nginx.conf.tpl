server {
  server_name {{ host }};
  listen 80;
  listen 443 ssl;

  location ~ (/api/|/api-auth/|/admin/|/docs/) {
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

  location ^~ /static_backend/ {
    alias /home/ubuntu/betterself_backend/static/;
  }

  location /media {
    add_header "Access-Control-Allow-Origin" "$http_origin";
    add_header "Access-Control-Allow-Credentials" "true";
    root /home/ubuntu/betterself_backend/;
  }

  client_max_body_size 250M;

  ssl_certificate /etc/letsencrypt/live/{{ host }}/fullchain.pem; # managed by Certbot
  ssl_certificate_key /etc/letsencrypt/live/{{ host }}/privkey.pem; # managed by Certbot
  include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
  ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

  if ($scheme != "https") {
      return 301 https://$host$request_uri;
  } # managed by Certbot
}
