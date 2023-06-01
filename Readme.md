Steps:

1.  docker build -t tfs .
2.  cd frontend
3.  docker build -t flaskweb .
4.  cd ../
5.  docker-compose up
**
  Server Url : http://127.0.0.1:8080/home
  Test Url : https://tensorflow.org/images/blogs/serving/cat.jpg
