# especializacao-pece-monografia
Repositório para armazenar os códigos utilizados na Monografia da Especialização em Engenharia de Dados e Big Data da Poli USP (PECE)


1. Create bucket

```
aws s3api create-bucket \
  --bucket credit-risk \
  --region us-east-1
```
<img width="985" height="542" alt="Captura de Tela 2025-07-28 às 11 30 51" src="https://github.com/user-attachments/assets/8e01f526-4dd5-4bda-8650-bf80f0e53d2e" />



2. Download file from https://www.kaggle.com/datasets/laotse/credit-risk-dataset?resource=download


<img width="956" height="422" alt="image" src="https://github.com/user-attachments/assets/ce5a972d-5164-4ba7-be4b-b732bd557bd5" />


3. Upload to bucket


<img width="766" height="413" alt="image" src="https://github.com/user-attachments/assets/0b6a86c7-bcb6-4f52-80c9-85c464b54168" />


4. Create Cloud9 for development propose:


```
aws cloud9 create-environment-ec2 \
  --name credit-risk-dev \
  --description "Ambiente Cloud9 para monografia: clusterização de clientes" \
  --instance-type t3.small \
  --subnet-id subnet-0b2a3b6908c2e9da0 \
  --automatic-stop-time-minutes 60 \
  --image-id amazonlinux-2-x86_64
```
<img width="1021" height="636" alt="Captura de Tela 2025-07-28 às 11 39 02" src="https://github.com/user-attachments/assets/bd178055-45c0-457e-83f2-1eccc6f7db6a" />
