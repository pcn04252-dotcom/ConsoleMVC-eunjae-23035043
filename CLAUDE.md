# CLAUDE.md

> 이 문서는 구현이 진행됨에 따라 갱신되는 living document입니다. 새 세션에서 이 repo를 열었을 때 아래 내용만으로 작업을 이어갈 수 있어야 합니다.

## 프로젝트 개요

콘솔 애플리케이션의 MVC(Model / View / Controller) 구조 분리를 검증하는 PoC. 상세 계획은 `PLAN.md` 참고.

## 기술 스택

- Python 3.x (표준 라이브러리만 사용, 외부 의존성 없음)
- 테스트: `pytest`

## 폴더 구조

```
src/model/       # 순수 도메인 로직 (I/O 금지)
src/view/        # 콘솔 입출력 전담 (비즈니스 로직 금지, model import 금지)
src/controller/  # Model-View 조율 (직접 print/input 금지)
src/main.py      # 진입점
tests/           # Model 단위 테스트
```

## 실행 방법

```
python -m src.main
```

## 테스트 방법

```
pytest
```

## 코드 컨벤션 / MVC 경계 규칙

- **Model**: `print`/`input` 사용 금지. 순수 함수/메서드로만 구성.
- **View**: `model` 패키지를 직접 import하지 않는다. 렌더링과 입력 수집만 담당.
- **Controller**: 직접 `print`/`input`을 호출하지 않고 View의 메서드를 통해서만 I/O를 수행한다.
- 타입 힌트를 사용한다.
- 주석은 WHY가 비자명한 경우에만 한 줄로 작성한다 (WHAT을 설명하는 주석 금지).

## 주의사항

- 이 repo는 PoC이므로 반도체 시료 도메인과 무관한 임의 도메인(Task)을 사용한다. 도메인 자체보다 MVC 경계 검증이 목적이다.
- Windows 콘솔 기본 코드페이지(cp949)에서 한글 출력이 깨지는 문제가 있어, `main.py`에서 `sys.stdout.reconfigure(encoding="utf-8")` / `sys.stdin.reconfigure(encoding="utf-8")`로 고정한다. 이 패턴은 콘솔 출력이 있는 다른 repo(특히 SampleOrderSystem)에도 동일하게 적용해야 한다.
