A sample Backend for WeChat Server.

#Install Node.js
cd ~
curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install nodejs
sudo apt-get install build-essential
cd ~
vim hello.js
```
#!/usr/bin/env nodejs
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
}).listen(8080, 'localhost');
console.log('Server running at http://localhost:8080/');
```
sudo ufw allow 8080
chmod +x ./hello.js
./hello.js
curl http://localhost:8080

#Install PM2
sudo npm install -g pm2
pm2 start hello.js
pm2 startup systemd
sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u sammy --hp /home/sammy
pm2 stop app_name_or_id
pm2 restart app_name_or_id
pm2 list

# Install and start Nginx
sudo add-apt-repository ppa:nginx/stable
sudo apt-get install nginx
sudo /etc/init.d/nginx start

# Config Nginx
sudo vim /etc/nginx/sites-enabled/default
```
location / {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
```
sudo nginx -t
sudo systemctl restart nginx

# Demo
sudo mkdir /var/www
sudo mkdir /var/www/flaskserver
cd /var/www/flaskserver
pip install flask
vim wechatbackend.py
python wechatbackend.py



# Config uWSGI
vim /var/www/flaskserver/flaskserver.ini
sudo mkdir -p /var/log/uwsgi
sudo chown -R ubuntu:ubuntu /var/log/uwsgi
uwsgi --ini /var/www/flaskserver/flaskserver.ini

