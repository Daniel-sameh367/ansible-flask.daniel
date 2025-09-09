pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Daniel-sameh367/ansible-flask.daniel.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test Backend') {
            steps {
                sh 'curl -f http://localhost:5004 || exit 1'
            }
        }

        stage('Test Frontend') {
            steps {
                sh 'curl -f http://localhost:3000 || exit 1'
            }
        }
    }
}

