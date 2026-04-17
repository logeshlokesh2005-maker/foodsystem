pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build & Test') {
            steps {
                // 'bat' is for Windows command prompt
                bat 'python -m unittest test_delivery.py'
            }
        }
        stage('Docker Build') {
            steps {
                // This assumes Docker Desktop is installed and running
                bat 'docker build -t food-delivery-app .'
            }
        }
    }
}
