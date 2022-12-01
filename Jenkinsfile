pipeline {
    agent any
    
    stages {
         stage('Building Docker Image') {
            steps {
                git branch: 'main', credentialsId: 'ab586125-4b2d-4ffe-93e4-0b4e41663633', url: 'https://github.com/KalidindiMounika/fastapiCICD.git'
                script {
                    dockerImage = docker.build("python-flask:latest")
                        }
                   }
                                       } 
        stage('Test') {
            steps {
                script {
                        docker.run("-p 3000:3000 python-flask:latest")
                        }
                 }
                    }
        
        
           }  
           }
