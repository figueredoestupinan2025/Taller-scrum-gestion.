import json
from typing import List, Dict, Optional

class TaskManager:
    def __init__(self, storage_path: str = 'tareas.json'):
        self.storage_path = storage_path
        self.tasks: List[Dict] = []
        self._load()

    def _load(self):
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            self.tasks = []

    def _save(self):
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(t['id'] for t in self.tasks) + 1

    def list_tasks(self) -> List[Dict]:
        return list(self.tasks)

    def add_task(self, descripcion: str) -> Dict:
        descripcion = descripcion.strip()
        if not descripcion:
            raise ValueError('La descripcion no puede estar vacía')
        task = {'id': self._next_id(), 'descripcion': descripcion, 'completada': False}
        self.tasks.append(task)
        self._save()
        return task

    def complete_task(self, task_id: int) -> bool:
        t = next((x for x in self.tasks if x['id'] == task_id), None)
        if not t:
            return False
        if not t.get('completada'):
            t['completada'] = True
            self._save()
        return True

    def delete_task(self, task_id: int) -> bool:
        t = next((x for x in self.tasks if x['id'] == task_id), None)
        if not t:
            return False
        self.tasks.remove(t)
        self._save()
        return True

    def clear_completed(self) -> int:
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.get('completada')]
        self._save()
        return before - len(self.tasks)

    def export_json(self) -> str:
        return json.dumps(self.tasks, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Este módulo provee `TaskManager`. Importe y úselo desde un script CLI.')
