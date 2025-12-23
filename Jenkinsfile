pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-demo-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                // Git automatically checks out code here
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // UPDATED: 'bat' is for Windows
                    bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    echo 'Running a quick test...'
                    // UPDATED: 'bat' commands
                    bat "docker run -d -p 5000:5000 --name test-container %IMAGE_NAME%:%BUILD_NUMBER%"
                    bat "timeout /t 5"
                    bat "curl localhost:5000"
                }
            }
        }
    }

    post {
        always {
            // UPDATED: Cleanup for Windows
            bat "docker stop test-container"
            bat "docker rm test-container"
        }
    }
}