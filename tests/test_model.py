import pytest

from src.model.task_repository import TaskRepository


def test_add_creates_task_with_incrementing_id():
    repo = TaskRepository()
    first = repo.add("첫 번째 할 일")
    second = repo.add("두 번째 할 일")
    assert first.id == 1
    assert second.id == 2
    assert first.done is False


def test_add_rejects_blank_title():
    repo = TaskRepository()
    with pytest.raises(ValueError):
        repo.add("   ")


def test_list_returns_all_added_tasks():
    repo = TaskRepository()
    repo.add("a")
    repo.add("b")
    assert [task.title for task in repo.list()] == ["a", "b"]


def test_toggle_done_flips_status():
    repo = TaskRepository()
    task = repo.add("a")
    assert repo.toggle_done(task.id).done is True
    assert repo.toggle_done(task.id).done is False


def test_toggle_done_missing_id_raises_key_error():
    repo = TaskRepository()
    with pytest.raises(KeyError):
        repo.toggle_done(999)


def test_delete_removes_task():
    repo = TaskRepository()
    task = repo.add("a")
    repo.delete(task.id)
    assert repo.list() == []


def test_delete_missing_id_raises_key_error():
    repo = TaskRepository()
    with pytest.raises(KeyError):
        repo.delete(999)
