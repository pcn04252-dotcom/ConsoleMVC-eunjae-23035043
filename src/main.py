import sys

from src.controller.task_controller import TaskController
from src.model.task_repository import TaskRepository
from src.view.console_view import ConsoleView


def main() -> None:
    # Windows 콘솔 기본 코드페이지(cp949)에서 한글이 깨지는 것을 방지
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")

    controller = TaskController(TaskRepository(), ConsoleView())
    controller.run()


if __name__ == "__main__":
    main()
