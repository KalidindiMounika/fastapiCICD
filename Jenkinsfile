pipeline {
    agent any
    
    stages {
         stage('Building Docker Image') {
            steps {
                script {
                    dockerImage = docker.build "${python-flask}:${latest}"
              }
            }
        }
    }  
