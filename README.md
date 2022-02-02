# playground-for-thesis
Playground for thesis


## Деплой

### k8s

Деплой:
```shell script
minikube start
minikube docker-env
docker build -f weather-service/Dockerfile weather-service -t weather-service
kubectl apply -f deploy/k8s/oauth2-proxy.yml,deploy/k8s/weather-service.yml,deploy/k8s/oauth2-ingress.yml,deploy/k8s/service-ingress.yml
```

Туннелирование:
```shell script
echo "127.0.0.1 weather-service.local" >> /etc/hosts
minikube tunnel
curl https://weather-service.local/admin/temperature
```

Отчистка:
```shell script
kubectl delete ing --all
kubectl delete all --all
```

### helm chart

Деплой:
```shell script
minikube start
minikube docker-env
docker build -f weather-service/Dockerfile weather-service -t weather-service
helm upgrade -i --atomic -f deploy/helm/generic/values.yaml app deploy/helm/generic
````

Туннелирование:
```shell script
echo "127.0.0.1 weather-service.local" >> /etc/hosts
minikube tunnel
curl https://weather-service.local/admin/temperature
```

Отчистка:
```shell script
kubectl delete ing --all
kubectl delete all --all
```