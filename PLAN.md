# PLAN: ConsoleMVC

> 이 문서는 구현이 진행됨에 따라 갱신되는 living document입니다. 실제 구현 중 발견된 이슈나 구조 변경 사항을 반영해 계속 업데이트합니다.

## 1. 목적

콘솔 애플리케이션에서 Model / View / Controller의 패키지 구조와 역할 분리가 실제로 성립하는지 검증하는 PoC.
반도체 시료 시스템 도메인과 무관하게, 가장 단순한 도메인(할 일 목록)으로 MVC 경계만 순수하게 검증한다.

## 2. 검증 대상 (PoC로 증명할 것)

- View는 입출력(print/input)만 담당하고 비즈니스 로직을 갖지 않는다.
- Model은 순수 데이터/로직만 담당하고 입출력을 하지 않는다.
- Controller는 View와 Model을 조율만 하고, 직접 print/input을 호출하지 않는다.

## 3. 데모 도메인: Task(할 일) 목록

MVC 경계를 보여주기 위한 최소 도메인. 필드: `id`, `title`, `done`.

## 4. 폴더 구조

```
src/
  model/       # Task, TaskRepository (순수 로직, in-memory)
  view/        # ConsoleView (메뉴 출력/입력/렌더링)
  controller/  # TaskController (메뉴 루프, Model-View 조율)
  main.py      # 조립 및 실행 진입점
tests/
  test_model.py
```

## 5. 구현 단계

- [ ] 1단계 - `model`: `Task` dataclass, `TaskRepository`(add/list/toggle_done/delete) 구현. I/O 코드 없음.
- [ ] 2단계 - `view`: `ConsoleView` 구현 (메뉴 출력, 입력 수집, 목록/결과 렌더링). Model을 import하지 않음.
- [ ] 3단계 - `controller`: `TaskController` 구현. 메뉴 루프에서 View로부터 입력을 받아 Model 메서드 호출 후 결과를 View로 전달.
- [ ] 4단계 - `main.py`: Model/View/Controller 조립 및 실행.
- [ ] 5단계 - `tests/test_model.py`: Model 단위 테스트 (pytest, I/O 없이 순수 로직만 검증).

## 6. 완료 기준 (Definition of Done)

- `python -m src.main` 실행 시 메뉴 루프가 정상 동작한다.
- 추가 / 목록 조회 / 완료 토글 / 삭제 4개 기능이 모두 동작한다.
- `src/model/` 코드에 `print`/`input` 호출이 없다.
- `src/view/` 코드에 `model` 모듈 import가 없다 (Controller를 거쳐서만 데이터가 오간다).
- `src/controller/` 코드에 직접적인 `print`/`input` 호출이 없다 (View 메서드 호출로만 I/O 수행).
- `pytest` 전체 통과.

## 7. 미결정/추후 논의 사항

- (없음, 발견 시 추가)
