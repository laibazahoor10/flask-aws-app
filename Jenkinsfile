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
                    pip3 install -r requirements.txt
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
                    echo "Stopping existing container if running..."
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true

                    echo "Building Docker image..."
                    docker build -t ${DOCKER_IMAGE} .

                    echo "Running Docker container..."
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${APP_PORT}:5000 \
                        ${DOCKER_IMAGE}

                    echo "Waiting for app to start..."
                    sleep 10

                    echo "Checking if container is running..."
                    docker ps | grep ${CONTAINER_NAME}

                    echo "✅ Containerized Deployment Successful!"
                '''
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo '========== Stage 4: Containerized Selenium Testing =========='
                sh '''
                    echo "Installing Selenium and Chrome dependencies..."
                    pip3 install selenium==4.15.2

                    echo "Running Selenium Tests against deployed container..."
                    python3 -m pytest test_selenium.py -v --tb=short

                    echo "✅ Selenium Tests Passed!"
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline completed successfully! All 4 stages passed!'
        }
        failure {
            echo '❌ Pipeline failed! Check the logs above for errors.'
            sh '''
                echo "Cleaning up containers..."
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
            '''
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
