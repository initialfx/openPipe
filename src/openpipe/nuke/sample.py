def test_nuke():
    """누크용 테스트 함수"""
    print("✅ [OpenPipe] Nuke Module imported successfully!")

def create_blur_node():
    """새로운 블러 노드를 생성하고 반환합니다 (실제 누크 환경에서 작동)"""
    try:
        import nuke
        blur = nuke.createNode("Blur")
        blur["size"].setValue(10)
        return blur
    except ImportError:
        print("⚠️ Warning: Nuke module 'nuke' not found. Returning a mock node object.")
        class MockNode:
            def name(self): return "MockBlur1"
        return MockNode()
