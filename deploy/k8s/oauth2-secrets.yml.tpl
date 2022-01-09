# envsubst < deploy/k8s/oauth2-secrets.yml.tpl > deploy/k8s/oauth2-secrets.yml

apiVersion: v1
kind: Secret
metadata:
  name: oauth2-secret
type: Opaque
stringData:
  client-secret: ${CLIENT_SECRET}
  cookie-secret: ${COOKIE_SECRET}
