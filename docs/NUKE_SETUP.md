# 누크 셋업 가이드 (Nuke Path)

누크는 `NUKE_PATH` 환경 변수를 사용하여 시작 시 자동으로 리소스를 읽어올 수 있습니다.

## 1. 개요 (Overview)
누크가 실행될 때 `nuke/` 폴더 내의 `init.py`와 `menu.py`가 자동으로 실행되어 OpenPipe 환경을 초기화하고 커스텀 메뉴를 추가합니다.

## 2. 환경 변수 등록 (Environment Variable)
시스템 환경 변수 `NUKE_PATH`에 `OpenPipe` 프로젝트 내의 `nuke/` 폴더 경로를 추가해야 합니다.

### 설정 예시 (Windows 기준)
- `NUKE_PATH`: `C:\HOU\Dev\OpenPipe\nuke`

### 수동 등록 (Powershell 가이드)
```powershell
[System.Environment]::SetEnvironmentVariable("NUKE_PATH", "C:\HOU\Dev\OpenPipe\nuke", "User")
```

## 3. PYTHONPATH 추가
파이썬 모듈을 읽어오기 위해 `src/` 폴더도 `PYTHONPATH`에 추가해야 합니다.
- `PYTHONPATH`: `C:\HOU\Dev\OpenPipe\src`

## 4. 작동 원리
- **`init.py`**: 누크 시작 시 Gizmos 경로와 전용 파이썬 라이브러리 경로를 플러그인 패스(`nuke.pluginAddPath`)에 추가합니다.
- **`menu.py`**: 상단 메뉴바에 `OpenPipe` 탭을 생성하고 메뉴 항목을 등록합니다.

## 5. 모듈 임포트 연습 (Sample Practice)
누크 실행 후 스크립트 에디터(`Script Editor`)에서 아래 코드를 실행해보세요.

```python
# 1. 메인 패키지 확인
import openpipe
print(openpipe.__version__)

# 2. 누크 전용 샘플 모듈 임포트
from openpipe.nuke import sample
sample.test_nuke()

# 3. 블러 노드 자동 생성 및 설정하기
blur = sample.create_blur_node()
print(f"새로운 블러 노드가 생성되었습니다: {blur.name()}")
```

## 6. Troubleshooting
- `pluginAddPath` 확인: 누크에서 `nuke.pluginPath()`를 실행하여 `OpenPipe` 경로가 포함되어 있는지 확인하십시오.
- `menu.py` 미실행: `init.py`에서 에러가 발생하면 `menu.py`가 실행되지 않을 수 있습니다. `Script Editor` 창의 에러 메시지를 확인하세요.
