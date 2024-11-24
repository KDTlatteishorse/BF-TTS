import os
import platform
import subprocess
import sys
from openai import OpenAI

def generate_audio(text, output_folder="output"):
    """
    텍스트를 음성으로 변환하여 MP3 파일로 저장하는 함수.

    Parameters:
    - text (str): 음성으로 변환할 텍스트.
    - output_folder (str): 결과 MP3 파일을 저장할 폴더 경로.

    Returns:
    - str: 생성된 MP3 파일 경로.
    """
    # API 키 파일 읽기
    with open("api.txt", "r") as file:
        api_key = file.read().strip()

    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=api_key)

    # 출력 폴더 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 파일 이름 생성
    output_file = os.path.join(output_folder, "output.mp3")

    # OpenAI TTS API 호출
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova", # 남성 : alloy, echo, fable, onyx / 여성 : nova, shimmer
        input=text,
    )

    # 결과 저장
    response.stream_to_file(output_file)

    return output_file

def play_audio(file_path):
    """
    MP3 파일을 재생하는 함수.

    Parameters:
    - file_path (str): 재생할 MP3 파일 경로.
    """
    print("Playing audio...")
    if platform.system() == "Darwin":  # macOS
        subprocess.run(["afplay", file_path])
    elif platform.system() == "Linux":  # Linux
        subprocess.run(["mpg123", file_path])
    elif platform.system() == "Windows":  # Windows
        os.startfile(file_path)
    else:
        print("Audio playback is not supported on this system.")

if __name__ == "__main__":
    # 명령줄 인수로 텍스트 입력 받기
    if len(sys.argv) < 2:
        print("Usage: python generate_audio.py \"Your text here\"")
        sys.exit(1)

    input_text = sys.argv[1]  # 첫 번째 인수로 텍스트 받기
    output_path = generate_audio(input_text)

    # # 재생
    # play_audio(output_path)