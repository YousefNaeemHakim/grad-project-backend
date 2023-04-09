## Nginx

Nginx is a high-performance web server and reverse proxy server that can be used to handle HTTP, HTTPS, and other protocols. It is widely used for its scalability, flexibility, and performance. In this learning summary, we will go from zero to hero in Nginx by covering the following topics:

1. Installing and configuring Nginx
2. Serving static content with Nginx
3. Configuring Nginx as a reverse proxy server
4. Implementing SSL/TLS with Nginx
5. Configuring load balancing with Nginx

## Installing and Configuring Nginx

To install Nginx on Ubuntu, you can use the following command:

```bash
sudo apt-get update
sudo apt-get install nginx
```

To start Nginx, use the following command:

```bash
sudo systemctl start nginx
```

To configure Nginx, you can edit the `/etc/nginx/nginx.conf` file. Here's an example configuration that listens on port 80 and serves content from the `/var/www/html` directory:

```nginx
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
  worker_connections 768;
}

http {
  sendfile on;
  tcp_nopush on;
  tcp_nodelay on;
  keepalive_timeout 65;
  types_hash_max_size 2048;

  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;

  gzip on;
  gzip_disable "msie6";

  server {
    listen 80;
    server_name localhost;

    root /var/www/html;
    index index.html;
  }
}
```

## Serving Static Content with Nginx

To serve static content with Nginx, you can place your content in the `/var/www/html` directory (or any other directory that you specify in your configuration). Here's an example HTML file that you can use:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Welcome to my website!</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
```

To serve this file, restart Nginx using the following command:

```bash
sudo systemctl restart nginx
```

You can now access your website by visiting `http://localhost` in your web browser.

## Configuring Nginx as a Reverse Proxy Server

To configure Nginx as a reverse proxy server, you can use the `proxy_pass` directive in your configuration. Here's an example configuration that proxies requests to a Node.js application running on port 3000:

```nginx
server {
  listen 80;
  server_name myapp.com;

  location / {
    proxy_pass http://localhost:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }
}
```

## Setting up SSL/TLS with Nginx

```nginx
server {
  listen 80;
  server_name myapp.com;
  return 301 https://$server_name$request_uri;
}

server {
  listen 443 ssl;
  server_name myapp.com;

  ssl_certificate /etc/letsencrypt/live/myapp.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/myapp.com/privkey.pem;

  location / {
    proxy_pass http://localhost:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }
}
```

## Configuring Load Balancing with Nginx

```nginx
upstream myapp {
  server localhost:3000;
  server localhost:3001;
  server localhost:3002;
}

server {
  listen 80;
  server_name myapp.com;

  location / {
    proxy_pass http://myapp;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }
}
```

## Conclusion

By following this learning summary, you should now have a good understanding of how to install, configure, and use Nginx for serving web content, reverse proxying, implementing SSL/TLS, and load balancing. Keep in mind that this is just an introduction to Nginx, and there are many more advanced topics to explore, such as caching, rate limiting, and more.