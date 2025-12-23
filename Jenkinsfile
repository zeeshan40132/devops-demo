pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-demo-app"
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

        stage('Unit Tests') {
            steps {
                script {
                    echo 'Running Python Unit Tests...'
                    // Run the container temporarily just to execute the test script
                    // --rm means "remove the container immediately after it finishes"
                    bat "docker run --rm %IMAGE_NAME%:%BUILD_NUMBER% python -m unittest test_app.py"
                }
            }
        }

        stage('Integration Test') {
            steps {
                script {
                    echo 'Deploying to Staging...'
                    // Start the container for the "Live" test
                    bat "docker run -d -p 5000:5000 --name test-container %IMAGE_NAME%:%BUILD_NUMBER%"
                    
                    // Give it time to boot
                    sleep(time: 5, unit: "SECONDS")
                    
                    // Verify it is actually serving traffic
                    bat "curl localhost:5000"
                }
            }
        }
    }

    post {
        always {
            // Cleanup
            bat "docker stop test-container"
            bat "docker rm test-container"
        }
    }
}