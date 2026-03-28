pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Código descargado correctamente desde GitHub.'
            }
        }
        
        stage('Preparar Entorno') {
            steps {
                echo 'Instalando dependencias (pytest)...'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest
                '''
            }
        }

        stage('Ejecutar Pruebas (pytest)') {
            steps {
                echo 'Corriendo las pruebas unitarias...'
                // Ejecutamos pytest y generamos un reporte XML que Jenkins entiende
                sh '''
                . venv/bin/activate
                pytest --junitxml=reporte_pruebas.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'reporte_pruebas.xml'
        }
        success {
            echo '¡Todas las pruebas pasaron! El código es seguro.'
        }
        failure {
            echo '¡ALERTA! Una prueba falló. Revisa los logs.'
        }
    }
}