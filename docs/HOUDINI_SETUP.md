# 후디니 셋업 가이드 (Houdini Package)

Houdini 17.5 이상부터는 `houdini.env` 대신 JSON 방식의 **Package** 파일을 사용하여 환경 변수와 플러그인을 관리합니다.

## 1. 전제 조건 (Prerequisites)
- `OpenPipe`를 로컬에 클론 또는 다운로드한 상태여야 합니다.
- 경로 예시: `C:/HOU/Dev/OpenPipe`

## 2. Package 파일 생성 (`OpenPipe.json`)
아래 경로 중 하나에 `OpenPipe.json` 파일을 생성합니다.

- **Windows**: `Documents/houdiniX.Y/packages`
- **Linux**: `~/houdiniX.Y/packages`
- **macOS**: `~/Library/Preferences/houdini/X.Y/packages`

### JSON 내용 (복사해서 경로만 수정하세요)
> [!IMPORTANT]
> `PYTHONPATH` 설정 시 프로젝트 루트 아래의 **`src`** 폴더까지만 등록해야 합니다. (`src/openpipe`로 등록하면 작동하지 않습니다!)

```json
{
    "env": [
        {
            "OPENPIPE_ROOT": "C:/HOU/Dev/OpenPipe",
            "PYTHONPATH": "$OPENPIPE_ROOT/src",
            "HOUDINI_PATH": "$OPENPIPE_ROOT/hou"
        }
    ]
}
```

## 3. 작동 원리 및 패키지 구조
- **`PYTHONPATH`**: `src/` 폴더를 등록하면, 파이썬이 그 안의 `openpipe/` 폴더를 하나의 **패키지**로 인식합니다.
- **구조도**:
  ```text
  C:/HOU/Dev/OpenPipe/src/
  └── openpipe/         <-- 이 폴더가 'import openpipe' 대상입니다.
      ├── __init__.py   <-- 이것이 존재하므로 openpipe.py 파일은 필요 없습니다.
      ├── core/
      └── hou/
  ```

- **`HOUDINI_PATH`**: `hou/` 폴더를 등록하여 후디니가 HDA, Shelf, 시작 스크립트(`hou/scripts/123.py`)를 읽도록 합니다.

## 4. 모듈 임포트 연습 (Sample Practice)
후디니 실행 후 파이썬 쉘에서 아래 코드를 실행해보세요.

```python
# 1. 메인 패키지 확인
import openpipe
print(openpipe.__version__)

# 2. 후디니 전용 샘플 모듈 임포트
from openpipe.hou import sample
sample.test_hou()

# 3. 현재 씬의 노드 개수 세기
count = sample.get_nodes_count()
print(f"현재 씬에는 {count}개의 노드가 있습니다.")
```

## 5. Troubleshooting
- `ImportError`: `OPENPIPE_ROOT` 경로가 슬래시(`/`)로 되어있는지, 실제 파일 경로와 일치하는지 확인하십시오.
- `hou` 폴더가 안 읽힘: `HOUDINI_PATH` 설정 후 후디니를 **재시작**해야 합니다.
