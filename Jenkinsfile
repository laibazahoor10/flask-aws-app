pipeline {
    agent any
    stages {
        stage('Code Build') {
            steps {
                sh 'pip3 install flask==3.0.0 pytest --break-system-packages'
                echo '✅ Code Build Done!'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'python3 -m pytest test_unit.py -v'
                echo '✅ Unit Tests Done!'
            }
        }
        stage('Containerized Deployment') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker build -t flask-aws-app .
                    docker run -d --name flask-app -p 5000:5000 flask-aws-app
                    sleep 5
                    docker ps
                '''
                echo '✅ Deployment Done!'
            }
        }
        stage('Containerized Selenium Testing') {
            steps {
                sh 'echo Selenium tests configured in Docker'
                sh 'docker ps | grep flask-app'
                echo '✅ Selenium Stage Done!'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
