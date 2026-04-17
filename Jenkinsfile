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
                sh 'python3 -m unittest test_delivery.py'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t food-delivery-app .'
            }
        }
    }
}
