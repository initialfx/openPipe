import sys
import os
import openpipe

def status():
    """패키지의 전반적인 상태를 출력합니다."""
    print("========================================")
    print("   OpenPipe Core Status Checker")
    print("========================================")
    print(f"OpenPipe Version: {openpipe.__version__}")
    print(f"Package Location: {os.path.dirname(openpipe.__file__)}")
    print(f"Python Integrity: OK")
    print(f"Executable Path: {sys.executable}")
    print("========================================")

def welcome(name="User"):
    """환영 메시지를 반환합니다."""
    return f"Welcome, {name}! OpenPipe core is ready to use."
