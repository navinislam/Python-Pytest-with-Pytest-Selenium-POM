// node {

 
//    def commit_id
//    stage('Preparation') {
//      checkout scm

//    }
//    stage('test') {
//      def myTestContainer = docker.image('python:3.8-slim-buster')
//      myTestContainer.pull()
//      myTestContainer.inside {
//        sh 'curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
//   && tar xzvf docker-17.04.0-ce.tgz \
//   && mv docker/docker /usr/local/bin \
//   && rm -r docker docker-17.04.0-ce.tgz'
//        sh 'pip install -r requirements.txt'
//        sh 'pytest   -n 4 --driver Remote  --port 31498  --capability browserName chrome -v --html=output/report.html'
//      }
//    }
// }

pipeline {
    agent {
        docker { image 'python:3.8-slim-buster' }
    }

   def commit_id
   stage('Preparation') {
     checkout scm

   }
    stage('test') {
       sh 'pip install -r requirements.txt'
       sh 'pytest   -n 4 --driver Remote  --port 31498  --capability browserName chrome -v --html=output/report.html'
     }
   }
