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

// pipeline {
//     agent {
//         docker { image 'python:3.8-slim-buster' }
//     }

//     stages{

//       stage('test') {
//         steps{
//         checkout scm
//         sh 'pip install -r requirements.txt'
//         sh 'pytest   -n 4 --driver Remote  --port 31498  --capability browserName chrome -v --html=output/report.html'
//         }
//       }
//    }
// }


// define the docker containers we want here:
podTemplate(containers: [
    containerTemplate(name: 'git', image: 'alpine/git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'python', image: 'python:3.8-slim-buster', command: 'cat', ttyEnabled: true),
  ]
  )
{
    // automatically label the pod - see https://plugins.jenkins.io/kubernetes/ for more info
    node(POD_LABEL) {

        // clone a git repo that contains a gradle project
        stage('Clone git repository') {
            // run the following commands in the git container
            container('git') {
                sh 'git clone -b master https://github.com/navinislam/Python-Pytest-with-Pytest-Selenium.git'
                // show the cloned project files, just for info
                sh 'find .'
            }
        }

        // run the example gradle build
        stage('Python Build') {
            // insoide the gradle docker image now
            container('python') {
                    // run gradle build
                    sh 'cd Python-Pytest-with-Pytest-Selenium; pip install -r requirements.txt'
                    sh 'pytest -n 3 --driver Remote --capability browserName chrome '
                    // a little more info on the output
                    // sh 'ls -al springbootjenkinspipelinedemo/build/libs/'
                    // finally, archive the built application
                    // archiveArtifacts artifacts: 'springbootjenkinspipelinedemo/build/libs/**/*.jar', fingerprint: true
            }
        }

    }
}
