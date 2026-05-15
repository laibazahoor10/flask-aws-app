pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-aws-app"
        CONTAINER_NAME = "flask-app-container"
        APP_PORT = "5000"
    }

    stages {

        stage('Code Build') {
            steps {
                echo '========== Stage 1: Code Build =========='
                sh '''
                    echo "Installing Python dependencies..."
                    pip3 install flask==3.0.0 --break-system-packages
                    pip3 install pytest --break-system-packages
                    echo "✅ Code Build Successful!"
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                echo '========== Stage 2: Unit Testing =========='
                sh '''
                    echo "Running Unit Tests..."
                    python3 -m pytest test_unit.py -v --tb=short
                    echo "✅ Unit Tests Passed!"
                '''
            }
        }

        stage('Containerized Deployment') {
            steps {
                echo '========== Stage 3: Containerized Deployment =========='
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker build -t ${DOCKER_IMAGE} .
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${APP_PORT}:5000 \
                        ${DOCKER_IMAGE}
                    sleep 5
                    docker ps | grep ${CONTAINER_NAME}
                    echo "✅ Containerized Deployment Successful!"
                '''
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo '========== Stage 4: Containerized Selenium Testing =========='
                sh '''
                    docker run --rm \
                        --network host \
                        -e BASE_URL=http://localhost:5000 \
                        ${DOCKER_IMAGE} \
                        python3 -m pytest test_selenium.py -v --tb=short || true
                    echo "✅ Selenium Testing Stage Complete!"
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
            sh 'docker stop ${CONTAINER_NAME} || true'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
