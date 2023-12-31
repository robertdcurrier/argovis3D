# Boilerplate for nginx with Let’s Encrypt on docker-compose


## Reference:
* https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71
* https://github.com/rappo-ai/nginx-certbot/tree/master
* https://blog.devgenius.io/how-to-dockerize-a-production-ready-django-application-django-nginx-uwsgi-a908d3e4d8f8


`init-letsencrypt.sh` fetches and ensures the renewal of a Let’s
Encrypt certificate for one or multiple domains in a docker-compose
setup with nginx.
This is useful when you need to set up nginx as a reverse proxy for an
application.

## Installation
1. Go into the nginx folder, and make an .env file based on the .env_template file. 

        cd nginx/
        cp .env_template .env

2. Modify .env file:

        vim .env

   - NGINX_DOMAIN_LIST - [REQUIRED] the list of domains for nginx (also used by letsencrypt); each domain name should be separated by a space; the first domain name will be taken as the primary domain unless NGINX_PRIMARY_DOMAIN env variable is also provided; defaults to "example.org www.example.org"
   - NGINX_PRIMARY_DOMAIN - [OPTIONAL] the primary domain name to use for certificate registration; defaults to "example.org"
   - NGINX_PROXY_PASS - [REQUIRED] the url to route all incoming requests on ports 80, 443; for example "http://localhost:8080" to forward all incoming to localhost:8080; defaults to "http://example.org"
   - LETSENCRYPT_EMAIL - [OPTIONAL] the email id to use for LetsEncrypt registration; defaults to ""
   - LETSENCRYPT_STAGING - [OPTIONAL] Set to 1 if you're testing your setup to avoid hitting request limits; defaults to 0

3. Make sure the script has execute permissions:

        chmod +x init-letsencrypt.sh

4. Run the init script:

        ./init-letsencrypt.sh

5. Go back to web_server folder, and run the docker compose command:

        cd ..
        docker compose up