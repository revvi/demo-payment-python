## demo-payment-python

Setup
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Development mode
```
export FLASK_ENV=development
```

Production mode
```
export FLASK_ENV=production
```

Run
```
python3 -m flask run
```

## Docker
Build
```
docker build -t python-docker .
```
Run
```
# run in terminal mode until ctrl+c
docker run -p 5000:5000 python-docker

# run in detached mode
docker run -d -p 5000:5000 python-docker

curl localhost:5000
```

Run in an EC2 Instance
```
sudo yum -y update
sudo yum -y install docker
sudo usermod -aG docker ec2-user
sudo service docker start

# <dockerimage> is using USER/REPO:TAG based in docker hub image format
docker run -d -p 80:5000 --name python-docker <dockerimage>
```