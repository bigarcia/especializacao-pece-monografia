# especializacao-pece-monografia
Repositório para armazenar os códigos utilizados na Monografia da Especialização em Engenharia de Dados e Big Data da Poli USP (PECE)

## Configuração dos serviços da AWS:
1. Cria um bucket

```
aws s3api create-bucket \
  --bucket credit-risk \
  --region us-east-1
```
<img width="985" height="542" alt="Captura de Tela 2025-07-28 às 11 30 51" src="https://github.com/user-attachments/assets/8e01f526-4dd5-4bda-8650-bf80f0e53d2e" />

 

 2. Download arquivo do site do Kaggle: https://www.kaggle.com/datasets/laotse/credit-risk-dataset?resource=download


<img width="956" height="422" alt="image" src="https://github.com/user-attachments/assets/ce5a972d-5164-4ba7-be4b-b732bd557bd5" />


3. Upload do arquivo pro bucket


<img width="1062" height="498" alt="image" src="https://github.com/user-attachments/assets/51995bda-090c-43d0-aeee-76d82c060e8d" />


4. Cria Cloud9 como ambiente de desevolvimento/teste :
Utilizaremos o Cloud9 para testar o desenvolvimento e uso de recursos da AWS.

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

4.1. Atualize pacotes e instale Java (requisito do Spark)

```
sudo yum update -y
```

<img width="680" height="560" alt="image" src="https://github.com/user-attachments/assets/f2410b08-8f36-4611-8baa-5d5e836fe34e" />

```
sudo yum install java-11-amazon-corretto -y
```
<img width="838" height="577" alt="image" src="https://github.com/user-attachments/assets/bdcf1828-2214-4a33-929f-5abe94554c05" />


4.2. Configure variável de ambiente para Java

```
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```
<img width="711" height="57" alt="image" src="https://github.com/user-attachments/assets/d26eab3f-353b-4bbd-98fd-52b350e84c1e" />


4.3. Instale todas bibliotecas necessárias:

```
pip install -r requirements.txt

```
<img width="1039" height="482" alt="image" src="https://github.com/user-attachments/assets/23e08187-f6fb-47e1-889d-88bfa35a464d" />



<img width="637" height="213" alt="image" src="https://github.com/user-attachments/assets/87c660dd-405e-4be9-b8b6-939e5f869304" />

4.4 Instale o conector Hadoop AWS
Crie uma pasta para os JARs:

```
mkdir -p ~/jars
cd ~/jars
```

<img width="318" height="39" alt="image" src="https://github.com/user-attachments/assets/69000c66-e5b8-4472-9f0b-98bb6a568598" />

Baixe os dois arquivos JARs:

```
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
```

<img width="863" height="185" alt="image" src="https://github.com/user-attachments/assets/bc08b7f0-95ec-4d80-99ee-d3682d9938f4" />

```
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.375/aws-java-sdk-bundle-1.12.375.jar
```

<img width="898" height="230" alt="image" src="https://github.com/user-attachments/assets/cd3b7343-3bf8-4488-9deb-46d96ae0c7ce" />

4.5 Certificar que as credenciais estão funcionando:

```
aws sts get-caller-identity
```

## Desenvolvimento

Google Colab: https://colab.research.google.com/drive/1SGQZ_alVqHL72KlAceTER31iEvBM-2Q7#scrollTo=5R-t9lfd4ICs

Os códigos testados no Cloud9 se encontram nesse repositório
