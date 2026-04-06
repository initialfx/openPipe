# 범용 CLI 툴 사용 가이드 (OpenPipe CLI)

`OpenPipe` 프로젝트는 특정 DCC(Houdini, Nuke) 환경이 없더라도 터미널에서 작동하는 범용 CLI(Command Line Interface) 도구를 제공합니다.

## 1. 전제 조건 (Prerequisites)
- **Python 3.12+** 버전 권장
- `pip`를 사용한 프로젝트 설치 과정이 필요합니다.

## 2. 설치 방법 (Installation)
프로젝트 루트(`C:/HOU/Dev/OpenPipe`)에서 `editable mode`로 설치합니다.

```sh
cd c:/HOU/Dev/OpenPipe
pip install -e .
```

### 왜 Editable Mode(-e)인가요?
- 소스 코드를 수정할 때마다 매번 `pip install`을 다시 실행할 필요 없이, 수정사항이 즉시 반영됩니다.

## 3. 기본 명령어 및 실행 (CLI Command List)
설치 후 터미널(Command Prompt 또는 PowerShell)에서 아래 명령어를 실행할 수 있습니다.

| 명령어 | 기능 요약 | 예시 코드 (`src/openpipe/cli/`) |
| :--- | :--- | :--- |
| `hello` | 기본적인 인사말 출력 | `openpipe.cli.hello:main` |
| `foo` | 추가적인 로직 테스트용 | `openpipe.cli.foo:main` |

### 명령어 추가 방법 (Step-by-Step)
1. `src/openpipe/core/` 하위에 실제 기능 로직을 작성합니다.
2. `src/openpipe/cli/` 하위에 명령줄에서 실행할 파이썬 스크립트를 작성합니다.
3. `pyproject.toml` 파일의 `[project.scripts]` 섹션에 명령어 이름을 등록합니다.
   ```toml
   [project.scripts]
   my-new-cmd = "openpipe.cli.new_cmd:main"
   ```
4. `pip install -e .`를 다시 실행하면 새로운 명령어를 터미널에서 사용할 수 있습니다.

## 4. 환경 변수 수동 설정 (Path Setup)
명령어 설치 외에도 파이썬이 어디서나 `openpipe` 패키지를 찾을 수 있도록 `PYTHONPATH` 설정을 추가하는 것을 권장합니다.

- **Windows**: `setx PYTHONPATH "C:\HOU\Dev\OpenPipe\src;%PYTHONPATH%"`
- **Linux/macOS**: `export PYTHONPATH=$PWD/src:$PYTHONPATH`

## 5. 참고 문서 (References)
- [Houdini 환경 설정 가이드](./HOUDINI_SETUP.md)
- [Nuke 환경 설정 가이드](./NUKE_SETUP.md)
- [Houdini/Nuke 임포트 연습](./HOUDINI_SETUP.md#4-모듈-임포트-연습-sample-practice)
