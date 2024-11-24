# BF-TTS
Text-to-Speech Models

---
## OpenAI TTS: 텍스트를 음성으로 변환

- OpenAI TTS API를 사용하여 텍스트를 음성으로 변환하고, 결과를 MP3 파일로 저장하는 Python 스크립트를 제공합

- 생성된 MP3 파일은 `output` 폴더에 저장되며, 생성 후 자동으로 재생

### 주요 기능

- OpenAI TTS API를 사용하여 텍스트를 MP3 파일로 변환

- 변환된 음성 파일을 지정된 디렉터리에 저장

### 사전 요구사항

- Python 3.7 이상

- 루트 디렉터리에 `api.txt` 파일로 저장된 OpenAI API 키

- 필수 Python 패키지(아래 설치 방법 참고)

### 설치 방법

1. 저장소를 클론

```bash
git clone https://github.com/yourusername/OpenAI-TTS.git
   cd OpenAI-TTS
```

2. 필요한 패키지를 설치

```bash
pip install -r requirements.txt
```

3. 루트 디렉터리에 api.txt 파일을 생성하고 OpenAI API 키를 추가
```bash
your_openai_api_key_here
```

### 사용방법

- 다음 명령어를 터미널에 입력하여 텍스트를 음성으로 변환

```bash
python openai-tts.py "변환할 텍스트 입력"
```

- 예제

```bash
pyhon openai-tts.py "모델 테스트"
```

- 출력

    - 생성된 MP3 파일은 output 폴더에 저장

### 파일 구조

```plaintext
OpenAI-TTS/
├── api.txt               # OpenAI API 키 파일
├── openai-tts.py         # 텍스트 음성 변환을 수행하는 메인 스크립트
├── output/               # 생성된 MP3 파일이 저장되는 디렉터리
├── requirements.txt      # 필요한 Python 패키지
└── README.md             # 문서 파일
```

### 문제 해결

1. API 키 관련 오류
    - api.txt 파일이 올바르게 작성되었는지 확인
    - OpenAI API 키가 정확한지 확인