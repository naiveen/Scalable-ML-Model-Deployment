# Scalable ML Model Deployment
Steps:
# For serving from Docker

```bash
docker-compose up
```

# For serving from kubernetes

```bash
kubectl apply -f k8s
```

To start the service:

```bash
minikube service tfweb-load-balancer-service
```

# Test

  Server Url : http://127.0.0.1:8080/home
  
  Test Url : [https://tensorflow.org/images/blogs/serving/cat.jpg](https://tensorflow.org/images/blogs/serving/cat.jpg)

  #Running Kube Tests

  [locust](http://127.0.0.1:8089/)

  Stress Testing using locust

  ```bash
  locust
  ```
