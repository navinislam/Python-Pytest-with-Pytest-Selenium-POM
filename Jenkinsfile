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
            
            checkout scm
            // run the following commands in the git container
            // container('git') {
            //     sh 'git clone -b master https://github.com/navinislam/Python-Pytest-with-Pytest-Selenium.git'
            //     // show the cloned project files, just for info
            //     sh 'find .'
            // }
        }

        // run the example gradle build
        stage('Python Build') {
            // insoide the gradle docker image now
            container('python') {
                    // run gradle build
                    sh 'cd Python-Pytest-with-Pytest-Selenium; pip install -r requirements.txt'
                    sh ' pytest -n 4 --driver Remote --capability browserName chrome -vv --selenium-host 192.168.64.5 --selenium-port 30044 --html=output/report.html --self-contained-html'
                    // a little more info on the output
                    // sh 'ls -al Python-Pytest-with-Pytest-Selenium/output'
                    // finally, archive the built application
                    // archiveArtifacts artifacts: 'output', fingerprint: true
                    archiveArtifacts artifacts: 'output/**', followSymlinks: false,  allowEmptyArchive: true                   
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '../test1/output/', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: ''])        
                
            }

        }
    }
}
