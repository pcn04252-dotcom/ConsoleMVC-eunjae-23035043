# ConsoleMVC

콘솔 애플리케이션의 MVC(Model / View / Controller) 패키지 구조와 역할 분리를 검증하기 위한 PoC 프로젝트입니다.

- 언어: Python
- 상태: 구현 완료 (Task 관리 데모)
- 상세 계획: [`PLAN.md`](./PLAN.md), 세션 참고 문서: [`CLAUDE.md`](./CLAUDE.md)

## 실행 방법

```
python -m src.main
```

## 테스트 방법

```
pip install -r requirements-dev.txt
pytest
ruff check .
```

## 검증한 것

- View는 입출력(print/input)만 담당하고 비즈니스 로직을 갖지 않는다.
- Model은 순수 데이터/로직만 담당하고 입출력을 하지 않는다.
- Controller는 View와 Model을 조율만 하고, 직접 print/input을 호출하지 않는다.

Task(할 일) 추가 / 목록 조회 / 완료 토글 / 삭제 기능으로 위 경계를 데모한다.
