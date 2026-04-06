import os
import re

class Project:
    """프로젝트 및 샷 관리를 위한 핵심 클래스"""
    
    def __init__(self, name, root_path):
        self.name = name
        self.root_path = root_path

    def get_project_dir(self):
        """프로젝트 루트 경로 반환"""
        return os.path.normpath(self.root_path)

    def __repr__(self):
        return f"<Project: {self.name} ({self.root_path})>"

def get_shot_info(path):
    """
    파일 경로에서 샷 이름과 버전 정보를 추출합니다.
    예: 'C:/Project/SK_010_v001.hip' -> {'shot': 'SK_010', 'version': 1}
    """
    filename = os.path.basename(path)
    
    # 샷 및 버전 정규식 패턴 (단순 예시)
    match = re.search(r"([A-Z0-9_]+)_v(\d+)", filename, re.IGNORECASE)
    
    if match:
        return {
            "shot": match.group(1),
            "version": int(match.group(2))
        }
    return None

def test_production_logic():
    """핵심 로직 테스트 함수"""
    print("--- Testing Core Production Logic ---")
    prj = Project("Demo_Show", "C:/HOU/Dev/Projects")
    print(prj)
    
    sample_path = "C:/HOU/Dev/Projects/OpenPipe/shot_AS_010_v005.nk"
    info = get_shot_info(sample_path)
    print(f"Path Analysis: {info}")
