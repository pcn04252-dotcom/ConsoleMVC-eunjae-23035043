from src.model.task_repository import TaskRepository
from src.view.console_view import ConsoleView


class TaskController:
    def __init__(self, repository: TaskRepository, view: ConsoleView) -> None:
        self._repository = repository
        self._view = view

    def run(self) -> None:
        while True:
            self._view.show_menu()
            try:
                choice = self._view.prompt_choice()
                if choice == "1":
                    self._handle_add()
                elif choice == "2":
                    self._handle_list()
                elif choice == "3":
                    self._handle_toggle()
                elif choice == "4":
                    self._handle_delete()
                elif choice == "0":
                    break
                else:
                    self._view.show_error("올바른 메뉴 번호를 입력하세요.")
            except EOFError:
                break

    def _handle_add(self) -> None:
        title = self._view.prompt_title()
        try:
            task = self._repository.add(title)
            self._view.show_message(f"Task {task.id} 추가 완료.")
        except ValueError as exc:
            self._view.show_error(str(exc))

    def _handle_list(self) -> None:
        self._view.show_tasks(self._repository.list())

    def _handle_toggle(self) -> None:
        task_id = self._read_task_id()
        if task_id is None:
            return
        try:
            task = self._repository.toggle_done(task_id)
            self._view.show_message(f"Task {task.id} 완료 상태: {task.done}")
        except KeyError:
            self._view.show_error("존재하지 않는 Task ID입니다.")

    def _handle_delete(self) -> None:
        task_id = self._read_task_id()
        if task_id is None:
            return
        try:
            self._repository.delete(task_id)
            self._view.show_message(f"Task {task_id} 삭제 완료.")
        except KeyError:
            self._view.show_error("존재하지 않는 Task ID입니다.")

    def _read_task_id(self) -> int | None:
        try:
            return self._view.prompt_task_id()
        except ValueError:
            self._view.show_error("Task ID는 숫자로 입력해야 합니다.")
            return None
