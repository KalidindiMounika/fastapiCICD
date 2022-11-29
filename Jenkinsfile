pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'ab586125-4b2d-4ffe-93e4-0b4e41663633', url: 'https://github.com/KalidindiMounika/fastapiCICD.git']]])
            }
        }
        stage('build') {
            steps {
                git branch: 'main', credentialsId: 'ab586125-4b2d-4ffe-93e4-0b4e41663633', url: 'https://github.com/KalidindiMounika/fastapiCICD.git'
                bat 'python main.py'
            }
        
    }
}
