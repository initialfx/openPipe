def test_hou():
    """후디니용 테스트 함수"""
    print("✅ [OpenPipe] Houdini Module imported successfully!")

def get_nodes_count():
    """현재 씬의 전체 노드 개수를 반환합니다 (실제 후디니 환경에서 작동)"""
    try:
        import hou
        return len(hou.node("/").allSubChildren())
    except ImportError:
        print("⚠️ Warning: Houdini module 'hou' not found. Returning a mock count.")
        return 42
