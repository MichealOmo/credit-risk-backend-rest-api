pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        sh """
          docker-compose build
        """
      }
    }
    stage("remove-old") {
      steps {
        sh """
          docker-compose stop fast-api || true
        """
      }
    }
    stage("run") {
      steps {
        sh """
          // docker-compose run --rm fast-api
          docker-compose up
        """
      }
    }

  }
}