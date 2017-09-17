sudo docker run --expose=80 --expose=8001 --name dockerLinear -v `pwd`/paddle/linear:/data -d -p 8002:80 -e WITH_GPU=0 paddlepaddle/book:serve
