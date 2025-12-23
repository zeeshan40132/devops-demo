pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-demo-app"
        // ADD THIS LINE BELOW:
        DOCKER_HOST = "tcp://127.0.0.1:2375"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    echo 'Running a quick test...'
                    bat "docker run -d -p 5000:5000 --name test-container %IMAGE_NAME%:%BUILD_NUMBER%"
                  sleep(time: 5, unit: "SECONDS")
                    bat "curl localhost:5000"
                }
            }
        }
    }

    post {
        always {
            bat "docker stop test-container"
            bat "docker rm test-container"
        }
    }
}