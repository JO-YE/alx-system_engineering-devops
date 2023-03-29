# 0x0C. Web server

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests
### DNS
-	What DNS stands for
-	What is DNS main role
### DNS Record Types
- A
- CNAME
- TXT
- MX

# Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You can’t use systemctl for restarting a process

# Links
- https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works
- https://en.wikipedia.org/wiki/Nginx
- https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04
- https://intranet.alxswe.com/concepts/110
- https://landingi.com/help/domains-vs-subdomains/
- https://www.tutorialspoint.com/http/http_methods.htm
- https://moz.com/learn/seo/redirection
- https://en.wikipedia.org/wiki/HTTP_404
- https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/

| Filename | Description |
| -------- | ----------- |
| [0. Transfer a file to your server](https://github.com/JO-YE/alx-system_engineering-devops/blob/master/0x0C-web_server/0-transfer_file) | Write a Bash script that transfers a file from our client to a serve Accepts 4 parameters. The path to the file to be transferred. The IP of the server we want to transfer the file to. The username scp connects with. The path to the SSH private key that scp uses|
| [1. Install nginx web server](https://github.com/JO-YE/alx-system_engineering-devops/blob/master/0x0C-web_server/1-install_nginx_web_server) | Web servers are the piece of software generating and serving HTML pages, let’s install one!. Install nginx on your web-01. Nginx should be listening on port 80. When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World! |
| [2. Setup a domain name](https://github.com/JO-YE/alx-system_engineering-devops/blob/master/0x0C-web_server/2-setup_a_domain_name) | create and provide your domain name gotten for .TECT Domains |
| [3. Redirection](https://github.com/JO-YE/alx-system_engineering-devops/blob/master/0x0C-web_server/3-redirection) | Configure your Nginx server so that `/redirect_me` is redirecting to another page. The redirection must be a “301 Moved Permanently” |
| [4. Not found page 404](https://github.com/JO-YE/alx-system_engineering-devops/blob/master/0x0C-web_server/4-not_found_page_404) | Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page. The page must return an HTTP 404 error code |
| [5. Install Nginx web server `(w/ Puppet)`](https://github.com/JO-YE/alx-system_engineering-devops/blob/master/0x0C-web_server/7-puppet_install_nginx_web_server.pp) | Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me. |
