import jpype
import os

def configure_java():
    # JAVA_HOME 환경 변수 설정 (JVM 경로를 명시적으로 지정)
    java_home = r"C:\Program Files (x86)\Common Files\Oracle\Java\java8path\java.exe"  # 설치된 Java 경로
    os.environ['JAVA_HOME'] = java_home
    
    # JVM 경로를 명시적으로 지정
    jvm_path = os.path.join(java_home, "jre", "bin", "server", "jvm.dll")
    jpype.startJVM(jvm_path)  # JVM 시작