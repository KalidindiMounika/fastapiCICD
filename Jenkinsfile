pipeline {
  agent none
  stages {
    stage('build') {
      steps {
        bat 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        bat 'python main.py'
      }   
    }
  }
}
