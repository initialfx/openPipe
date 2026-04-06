"""Core OpenPipe Production Modules"""
from .prod import Project, get_shot_info, test_production_logic

def get_project_name():
    """기본 프로젝트 이름 반환"""
    return "OpenPipe"

def say_hello():
    """간단한 인사말 반환"""
    return "Hello from OpenPipe core!"
