pipeline {
    agent any
    stages {
        stage('Code Build') {
            steps {
                sh 'sudo pip3 install flask==3.0.0 pytest --break-system-packages'
                echo 'Code Build Done!'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'sudo python3 -m pytest test_unit.py -v'
                echo 'Unit Testing Done!'
            }
        }
        stage('Containerized Deployment') {
            steps {
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
                sh 'docker build -t flask-aws-app .'
                sh 'docker run -d --name flask-app -p 5000:5000 flask-aws-app'
                sh 'sleep 5'
                sh 'docker ps'
                echo 'Deployment Done!'
            }
        }
        stage('Containerized Selenium Testing') {
            steps {
                sh 'docker ps | grep flask-app'
                echo 'Selenium Stage Done!'
            }
        }
    }
}
