# EXA--CF
\huge#####################README########################### 

EC2
ingreseamos al EC2 paraa crear una instancia con Imágenes de máquina de Amazon (AMI) Amazon Linux 2023
con tipo de instancia t.3 small
creamos par de claves 
en configuración de red damos click al botón EDITAR y habilitamos los puertos:
- SSH - 20
- HTTP - 80
- TCP PERSONALIZADO - 5000
hecho todo esto lanzamos la instancia

CLOUD 9
creamos un entorno con tipo de instancia
- t3.small (2 GiB RAM + 2 vCPU)
  y en configuración de red elegir
- Secure Shell (SSH)
luego damos click en crear

VINCULAR EL COUD9 CON LA EC2
para vincular el Cloud9 con la EC2 ejecutamos los siguientes comandos

- touch clave.pem
- chmod 600 clave.pem
- nano clave.pem 
- ssh -i ec2-user@ip_del_EC2

una ves dentro del EC2 ejecutamos el comando 
- ssh-keygen -t ed25519 -C "your_email_@example.com"
- presionamos 3 veces ENTER
  y nos dirigimos al directorio .ssh para visualizar las claves publicas
  ejectuamos el comando
  - cat id_ed25519.pub
    y copiamos la clave publica para generar la key en el github

  una vez genereda la KEY ejecutamos el comando dentro del EC2
- git clone git@github.com:c40s7r31r3/EXA--CF.git (coigo ssh del repositorio)
  una vez clonado el repositorio comenzamos a trabajar en nuestra aplicación

REQUISITOS TECNICOS INSTALAR LAS SIGUIENTES LIBRERIAS
python, pip, flask, flask-testing, 

sudo yum update  

sudo yum install git -y ( para instalar git hub en el EC2)

sudo yum install nodejs

sudo yum install python3

sudo yum install python3 pip

pip install flask

pip install Flask-Testing

python3 -m pip install flake8

DESCRIPCIÓN DEL USO DE ARCHIVOS

app.py : es el que llama al formulario.html y al formulario.html
formulario.html : es el que muestra el formulario para rellenar con los datos que queramos
resultado.html : muestra el resultado del calculo de lso salarios del empleado y del gerente

ejecutamos el comando python3 app.py

para poder ver nuestra aplicación buscamos la IP de nuestro EC2 seguido de :5000 

