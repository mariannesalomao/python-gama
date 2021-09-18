pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '5eb39cf3-5dfd-4714-9df7-757a6fa612d7', url: 'https://github.com/mariannesalomao/python-gama.git']]])
      }
    }

    stage('Build') {
      steps {
        git branch: 'main', credentialsId: '5eb39cf3-5dfd-4714-9df7-757a6fa612d7', url: 'https://github.com/mariannesalomao/python-gama.git'
      }
    }

    stage('Test') {
      steps {
        echo 'The job has been tested'
      }
    }

    stage('Production') {
      steps {
        echo 'The job has been put in production'
      }
    }
  }
}