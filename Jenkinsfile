pipeline {
  agent any
  stages {
    stage('printmessage') {
      steps {
        echo 'Hi we are in Blue Ocean'
      }
    }

    stage('execution') {
      steps {
        sh 'python helloworld.py -m "hello this executed" '
      }
    }

  }
}