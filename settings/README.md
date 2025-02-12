# KONLPY 설치 과정 (Windows)

## 1. Java 설치
- [Java 다운로드 페이지](https://www.oracle.com/java/technologies/downloads/?er=221886)로 이동하여 Java 11 LTS 버전을 다운로드
- 설치 후, 운영체제에 맞게 Java를 설치

## 2. JAVA_HOME 설정 (시스템 환경 변수 설정)
1. 윈도우 + S 로 '시스템 환경변수 편집' 검색 
2. 또는 윈도우 + S 로 '고급 시스템 보기' - '시스템 속성'
3. 시스템 속성 창에서 `환경 변수` 버튼을 클릭
4. 시스템 변수 목록에서 `JAVA_HOME` 을 만들고, 그 값에 Java 설치 경로(예: `C:\Program Files\Java\jdk-11`)를 입력
    ![Image](https://github.com/user-attachments/assets/3fd1e821-0383-41c8-8296-30a6a5bc9c07)
5. 시스템 변수 목록에서 `path` 을 찾고 `%JAVA_HOME%bin` 입력
    ![Image](https://github.com/user-attachments/assets/0e0b687f-4bcb-4af3-abff-102c4268fbef)
6. 결과
- 환경 변수 적용을 위해 컴퓨터 재부팅이 필요할 수 있음. 혹시 안 되면 일단 재부팅해보면 될 수 있음.
- `where java`와 `java -version`을 입력했을 때 결과가 나와야 함.
    ![Image](https://github.com/user-attachments/assets/158b1ae6-326d-4769-9019-3168a5b7eb0b)

## 3. JPYPE1 설치
- [JPYPE1 PyPI 페이지](https://pypi.org/project/jpype1/#modal-lose)에서 사용하는 Python 버전과 시스템에 맞는 `.whl` 파일을 다운로드
- 예를 들어, `Python 3.10` 윈도우 64비트 시스템에서 사용할 파일은 `JPYPE1-1.5.2-CP310-CP310-WIN_AMD64.WHL`
- 터미널을 열고, 다운로드한 `.whl` 파일이 있는 경로로 이동한 뒤 아래 명령어로 설치
```
pip install 경로\JPYPE1-1.5.2-CP310-CP310-WIN_AMD64.WHL
```

## 4. KONLPY 설치
- Java와 JPYPE1 설치가 완료되면, 다음 명령어로 KONLPY를 설치
```
pip install konlpy
```

### 참고) AttributeError: Java Package 'kr.lucypark.okt' is not valid
[KONLPY GitHub 이슈 페이지](https://github.com/konlpy/konlpy/issues/401)

### 참고) java.config() 수동 설정하니 에러남.
```
import jpype
import os
from konlpy import utils

def configure_java():
    if not jpype.isJVMStarted():
        # JAVA_HOME 확인
        java_home = os.environ.get('JAVA_HOME')
        if not java_home:
            raise EnvironmentError("JAVA_HOME 환경 변수가 설정되지 않았습니다.")
        
        # JVM 경로 후보들
        jvm_paths = [
            os.path.join(java_home, "bin", "server", "jvm.dll"),
            os.path.join(java_home, "jre", "bin", "server", "jvm.dll"),
            os.path.join(java_home, "lib", "server", "jvm.dll"),
            os.path.join(java_home, "bin", "client", "jvm.dll")
        ]
        
        # JVM 찾기
        jvm_path = None
        for path in jvm_paths:
            if os.path.exists(path):
                jvm_path = path
                break
        
        if not jvm_path:
            raise FileNotFoundError(f"jvm.dll을 찾을 수 없습니다. JAVA_HOME: {java_home}")
        
        # KoNLPy Class path 설정
        javadir = '%s%sjava' % (utils.installpath, os.sep)
        classpath = os.path.join(javadir, "open-korean-text-2.1.0.jar")
        
        # JVM 시작
        try:
            jpype.startJVM(jvm_path, 
                        "-Djava.class.path=" + classpath,
                        "-Dfile.encoding=UTF8",
                        convertStrings=True)
            print(f"******JVM started successfully at: {jvm_path}")
            print(f"******Classpath: {classpath}")
        except Exception as e:
            raise RuntimeError(f"JVM 시작 실패: {str(e)}")
    else:
        print("JVM is already started")

if __name__ == "__main__":
    configure_java()

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
```