## Azure App Service

```
az login

NAME=$RANDOM &&\
RGNAME=demo-$NAME

az group create --name $RGNAME --location westeurope
az webapp up -g $RGNAME --location westeurope --name demo$NAME --html

az webapp browse

az webapp log tail
OR
firefox https://demo$NAME.scm.azurewebsites.net/

az group delete -n $RGNAME
```