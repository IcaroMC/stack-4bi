# GitOps using ArgoCD

### install
```sh
brew install helm
brew install argocd
```

### repos
```sh
helm repo add argo https://argoproj.github.io/argo-helm
```

### build
```sh
terraform init
terraform apply
```

### configure [manual]
```sh
kubectl patch svc argocd-server -n gitops -p '{"spec": {"type": "LoadBalancer"}}'
kubectl get svc argocd-server -n gitops
kubectl -n gitops get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo


argocd login "192.168.40.40" --username admin --password "dEmlJCEGEfRDmxg-" --insecure
argocd login "192.168.1.50" --username admin --password "33Pox6vGhrlSHlmn" --insecure
argocd cluster add ""

kubectl apply -f git-repo-conf.yaml -n gitops
```
