sudo docker run --name docker-sentiment -v `pwd`/paddle/sentiment:/data -d -p 8001:80 -e WITH_GPU=0 paddlepaddle/book:serve
