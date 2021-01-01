node {

  // def label = "docker-${UUID.randomUUID().toString()}"

  //     podTemplate(label: label, yaml: """
  //     apiVersion: v1
  //     kind: Pod
  //     spec:
  //       containers:
  //       - name: docker
  //         image: docker:1.11
  //         command: ['cat']
  //         tty: true
  //         volumeMounts:
  //         - name: dockersock
  //           mountPath: /var/run/docker.sock
  //       volumes:
  //       - name: dockersock
  //         hostPath:
  //           path: /var/run/docker.sock
  //     """
  //       ) {

  //       def image = "jenkins/jnlp-slave"
  //       node(label) {
  //         stage('Build Docker image') {
  //           git 'https://github.com/jenkinsci/docker-jnlp-slave.git'
  //           container('docker') {
  //             sh "docker build -t ${image} ."
  //           }
  //         }
  //       }
  //     }

 
   def commit_id
   stage('Preparation') {
     checkout scm

   }
   stage('test') {
     def myTestContainer = docker.image('python:3.8-slim-buster')
     myTestContainer.pull()
     myTestContainer.inside {
       sh 'curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz'
       sh 'pip install -r requirements.txt'
       sh 'pytest   -n 4 --driver Remote  --port 31498  --capability browserName chrome -v --html=output/report.html'
     }
   }
}
