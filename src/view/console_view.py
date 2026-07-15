class ConsoleView:
    def show_menu(self) -> None:
        print("=" * 40)
        print("Task 관리 콘솔")
        print("=" * 40)
        print("[1] 추가  [2] 목록  [3] 완료 토글  [4] 삭제  [0] 종료")

    def prompt_choice(self) -> str:
        return input("선택 > ").strip()

    def prompt_title(self) -> str:
        return input("제목 > ").strip()

    def prompt_task_id(self) -> int:
        return int(input("Task ID > ").strip())

    def show_tasks(self, tasks: list) -> None:
        if not tasks:
            print("등록된 Task가 없습니다.")
            return
        print(f"{'ID':<4}{'완료':<6}{'제목'}")
        for task in tasks:
            mark = "V" if task.done else " "
            print(f"{task.id:<4}[{mark}]   {task.title}")

    def show_message(self, message: str) -> None:
        print(message)

    def show_error(self, message: str) -> None:
        print(f"오류: {message}")
