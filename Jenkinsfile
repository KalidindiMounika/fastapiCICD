pipeline {
    agent any
    
    stages {
         stage('Building Docker Image') {
            steps {
                git branch: 'main', credentialsId: 'ab586125-4b2d-4ffe-93e4-0b4e41663633', url: 'https://github.com/KalidindiMounika/fastapiCICD.git'
                script {
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker" build -t python-flask:latest .'
                        }
                   }
        }
	 stage('Test') {
            steps {
                script {
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker" run -d -p 3000:3000 python-flask:latest'
                        }
                   }
        }
    }  
	
}

