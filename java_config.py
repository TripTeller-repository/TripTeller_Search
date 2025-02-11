import jpype
from konlpy.jvm import init_jvm

def configure_java():
    if not jpype.isJVMStarted():
        try:
            init_jvm()
            print("JVM started successfully")
        except Exception as e:
            raise RuntimeError(f"JVM 시작 실패: {str(e)}")
    else:
        print("JVM is already started")