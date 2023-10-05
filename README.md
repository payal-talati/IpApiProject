# IpApiProject

Description -
It is a command line interface (CLI) program for the Mac or Linux shell that queries the IPStack API(You will need to sign up for a free
API key to do this assignment) and obtains the lattitude and longitude of an IP address and print on stdout.

This project contains -
1) Dockerfile
2) getipinfo/__main__.py

To clone -
git clone   https://github.com/payal-talati/IpApiProject.git

To run this on Linux -
1) cd to dir IpApiProject or where you have Dockerfile and getipinfo files
2) Create Docker by
   >docker build -t `<image name>`  .
3) Run docker in interactive mode by
   >docker run -it --entrypoint /bin/bash `<image that you created in previous cmd>`
4) you need to create .env file in your docker /app dir
5) .env file should contain your IPStack access key as per below.
   >echo access_key=`<your key>` >.env
6) Run script
   root@a8b4ed6a80d6:/app# python3 getipinfo --ip `<ip address you want to query>`
7) exit docker




