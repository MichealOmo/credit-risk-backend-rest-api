pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t credit-risk-backend-rest-api-image:latest .
        """
      }
    }
    stage("remove-old") {
      steps {
        sh """
          docker rm -f credit-risk-backend-rest-api || true
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run -d --name credit-risk-backend-rest-api credit-risk-backend-rest-api-image:latest
        """
      }
    }
  }
}