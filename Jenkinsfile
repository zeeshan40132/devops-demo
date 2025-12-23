pipeline {
    agent any

    environment {
        // Name of the image we will build
        IMAGE_NAME = "my-demo-app"
    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins automatically checks out code from git here
                echo 'Checking out code...'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // This command uses the Docker daemon on your host
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    echo 'Running a quick test...'
                    // Run the container briefly to check it works, then remove it
                    sh "docker run -d -p 5000:5000 --name test-container ${IMAGE_NAME}:${BUILD_NUMBER}"
                    sh "sleep 5" // wait for boot
                    sh "curl localhost:5000" // prove it replies
                }
            }
        }
    }

    post {
        always {
            // Cleanup: Stop and remove the container so the next build doesn't fail
            sh "docker stop test-container || true"
            sh "docker rm test-container || true"
        }
    }
}