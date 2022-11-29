pipeline {
  agent {  dockerfile { filename 'Dockerfile.build' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python main.py'
      }   
    }
  }
}
