from src.model.task import Task


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str) -> Task:
        if not title.strip():
            raise ValueError("제목은 비어 있을 수 없습니다.")
        task = Task(id=self._next_id, title=title)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list(self) -> list[Task]:
        return list(self._tasks.values())

    def toggle_done(self, task_id: int) -> Task:
        task = self._tasks[task_id]
        task.done = not task.done
        return task

    def delete(self, task_id: int) -> None:
        del self._tasks[task_id]
