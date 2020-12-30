node {
   def commit_id
   stage('Preparation') {
     checkout scm

   }
   stage('test') {
     def myTestContainer = docker.image('python:3.8-slim-buster')
     myTestContainer.pull()
     myTestContainer.inside {
       sh 'pip install -r requirements.txt'
       sh 'pytest   -n 4 --driver Remote  --port 31498  --capability browserName chrome -v --html=output/report.html'
     }
   }
}
