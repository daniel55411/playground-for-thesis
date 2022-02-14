# playground-for-thesis
Playground for thesis


## Деплой

### k8s

Настройка Github:

Создаем oauth app и в callback прописываем: https://weather-service.local/oauth2/callback

Деплой:
```shell script
minikube start
minikube docker-env
docker build -f weather-service/Dockerfile weather-service -t weather-service
envsubst < deploy/k8s/oauth2-secrets.yml.tpl > deploy/k8s/oauth2-secrets.yml
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

Настройка Github:

Создаем oauth app и в callback прописываем: https://weather-service.local/oauth2/callback

Деплой:
```shell script
minikube start
minikube docker-env
docker build -f weather-service/Dockerfile weather-service -t weather-service
envsubst < deploy/k8s/oauth2-secrets.yml.tpl > deploy/k8s/oauth2-secrets.yml
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

### ansible

Настройка Github:

Создаем oauth app и в callback прописываем: http://127.0.0.1:8081/oauth2/callback

Запуск виртуальной машины:
```
limactl start ansible/vm/vm-1.yaml
```

Запуск локального registry:
```shell script
docker run -d -p 5000:5000 --restart always --name registry registry:2
```

Пуш в локальный регистри
```shell script
docker build -f weather-service/Dockerfile weather-service -t registry.local:5000/weather-service
docker push registry.local:5000/weather-service
```

Запуск ansible
```shell script
cd deploy/ansible/deploy
ansible-playbook -i inventory web.yml --extra-vars @secrets.yml
```
