import json
import os
from tareas_core import TaskManager


def test_add_complete_delete(tmp_path):
    path = tmp_path / 'tareas_test.json'
    tm = TaskManager(str(path))

    # inicialmente vacío
    assert tm.list_tasks() == []

    # agregar
    t1 = tm.add_task('Primera tarea')
    assert t1['id'] == 1
    assert t1['descripcion'] == 'Primera tarea'
    assert t1['completada'] is False

    t2 = tm.add_task('Segunda tarea')
    assert t2['id'] == 2

    # listar
    tasks = tm.list_tasks()
    assert len(tasks) == 2

    # completar
    assert tm.complete_task(1) is True
    tasks = tm.list_tasks()
    assert any(t['id'] == 1 and t['completada'] for t in tasks)

    # eliminar
    assert tm.delete_task(2) is True
    tasks = tm.list_tasks()
    assert len(tasks) == 1

    # persistencia
    # crear nueva instancia desde el mismo archivo
    tm2 = TaskManager(str(path))
    tasks2 = tm2.list_tasks()
    assert len(tasks2) == 1
    assert tasks2[0]['id'] == 1

    # limpiar completadas
    removed = tm2.clear_completed()
    assert removed == 1
    assert tm2.list_tasks() == []


def test_add_empty_description(tmp_path):
    path = tmp_path / 'tareas_test2.json'
    tm = TaskManager(str(path))
    try:
        tm.add_task('   ')
        assert False, 'should have raised ValueError'
    except ValueError:
        pass
