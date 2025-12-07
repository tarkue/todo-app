import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_all_endpoints():
    """
    Комплексный тест всех эндпоинтов tasks:
    1. Создать 5 задач
    2. Получить их по ID
    3. Получить все задачи
    4. Обновить каждую задачу отдельно (статус, описание, заголовок - каждый в отдельном запросе)
    5. Проверить обновления
    6. Удалить все задачи
    7. Проверить, что они удалены
    """
    async with AsyncClient(base_url="http://localhost:5000") as client:
        # Шаг 1: Создать 5 задач
        created_tasks = []
        task_data = [
            {"title": "Задача 1", "description": "Описание задачи 1"},
            {"title": "Задача 2", "description": "Описание задачи 2"},
            {"title": "Задача 3", "description": None},
            {"title": "Задача 4", "description": "Описание задачи 4"},
            {"title": "Задача 5", "description": "Описание задачи 5"},
        ]
        
        for task in task_data:
            response = await client.post("/tasks/", json=task)
            assert response.status_code == 201, f"Ошибка создания задачи: {response.text}"
            created_task = response.json()
            assert "id" in created_task
            assert created_task["title"] == task["title"]
            assert created_task["description"] == task["description"]
            assert created_task["status"] == "in progress"
            created_tasks.append(created_task)
        
        assert len(created_tasks) == 5, "Должно быть создано 5 задач"
        
        # Шаг 2: Получить задачи по ID
        task_ids = [task["id"] for task in created_tasks]
        for task_id in task_ids:
            response = await client.get(f"/tasks/{task_id}")
            assert response.status_code == 200, f"Ошибка получения задачи по ID: {response.text}"
            task = response.json()
            assert task["id"] == task_id
            assert "title" in task
            assert "status" in task
        
        # Шаг 3: Получить все задачи
        response = await client.get("/tasks/")
        assert response.status_code == 200, f"Ошибка получения всех задач: {response.text}"
        all_tasks = response.json()
        assert len(all_tasks) >= 5, "Должно быть минимум 5 задач"
        
        # Проверяем, что все созданные задачи присутствуют
        all_task_ids = [task["id"] for task in all_tasks]
        for task_id in task_ids:
            assert task_id in all_task_ids, f"Задача {task_id} не найдена в списке всех задач"
        
        # Шаг 4: Обновить каждую задачу отдельно
        # Обновление 1: Обновить заголовок первой задачи
        first_task_id = task_ids[0]
        response = await client.patch(
            f"/tasks/{first_task_id}",
            json={"title": "Обновленный заголовок 1"}
        )
        assert response.status_code == 200, f"Ошибка обновления заголовка: {response.text}"
        updated_task = response.json()
        assert updated_task["title"] == "Обновленный заголовок 1"
        assert updated_task["id"] == first_task_id
        
        # Обновление 2: Обновить описание первой задачи
        response = await client.patch(
            f"/tasks/{first_task_id}",
            json={"description": "Обновленное описание 1"}
        )
        assert response.status_code == 200, f"Ошибка обновления описания: {response.text}"
        updated_task = response.json()
        assert updated_task["description"] == "Обновленное описание 1"
        
        # Обновление 3: Обновить статус первой задачи
        response = await client.patch(
            f"/tasks/{first_task_id}",
            json={"status": "completed"}
        )
        assert response.status_code == 200, f"Ошибка обновления статуса: {response.text}"
        updated_task = response.json()
        assert updated_task["status"] == "completed"
        
        # Обновление 4: Обновить заголовок второй задачи
        second_task_id = task_ids[1]
        response = await client.patch(
            f"/tasks/{second_task_id}",
            json={"title": "Обновленный заголовок 2"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["title"] == "Обновленный заголовок 2"
        
        # Обновление 5: Обновить описание второй задачи
        response = await client.patch(
            f"/tasks/{second_task_id}",
            json={"description": "Обновленное описание 2"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["description"] == "Обновленное описание 2"
        
        # Обновление 6: Обновить статус второй задачи
        response = await client.patch(
            f"/tasks/{second_task_id}",
            json={"status": "completed"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["status"] == "completed"
        
        # Обновление 7: Обновить заголовок третьей задачи
        third_task_id = task_ids[2]
        response = await client.patch(
            f"/tasks/{third_task_id}",
            json={"title": "Обновленный заголовок 3"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["title"] == "Обновленный заголовок 3"
        
        # Обновление 8: Обновить описание третьей задачи
        response = await client.patch(
            f"/tasks/{third_task_id}",
            json={"description": "Обновленное описание 3"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["description"] == "Обновленное описание 3"
        
        # Обновление 9: Обновить статус третьей задачи
        response = await client.patch(
            f"/tasks/{third_task_id}",
            json={"status": "completed"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["status"] == "completed"
        
        # Обновление 10: Обновить заголовок четвертой задачи
        fourth_task_id = task_ids[3]
        response = await client.patch(
            f"/tasks/{fourth_task_id}",
            json={"title": "Обновленный заголовок 4"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["title"] == "Обновленный заголовок 4"
        
        # Обновление 11: Обновить описание четвертой задачи
        response = await client.patch(
            f"/tasks/{fourth_task_id}",
            json={"description": "Обновленное описание 4"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["description"] == "Обновленное описание 4"
        
        # Обновление 12: Обновить статус четвертой задачи
        response = await client.patch(
            f"/tasks/{fourth_task_id}",
            json={"status": "completed"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["status"] == "completed"
        
        # Обновление 13: Обновить заголовок пятой задачи
        fifth_task_id = task_ids[4]
        response = await client.patch(
            f"/tasks/{fifth_task_id}",
            json={"title": "Обновленный заголовок 5"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["title"] == "Обновленный заголовок 5"
        
        # Обновление 14: Обновить описание пятой задачи
        response = await client.patch(
            f"/tasks/{fifth_task_id}",
            json={"description": "Обновленное описание 5"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["description"] == "Обновленное описание 5"
        
        # Обновление 15: Обновить статус пятой задачи
        response = await client.patch(
            f"/tasks/{fifth_task_id}",
            json={"status": "completed"}
        )
        assert response.status_code == 200
        updated_task = response.json()
        assert updated_task["status"] == "completed"
        
        # Шаг 5: Проверить обновления
        # Проверяем первую задачу
        response = await client.get(f"/tasks/{first_task_id}")
        assert response.status_code == 200
        task = response.json()
        assert task["title"] == "Обновленный заголовок 1"
        assert task["description"] == "Обновленное описание 1"
        assert task["status"] == "completed"
        
        # Проверяем вторую задачу
        response = await client.get(f"/tasks/{second_task_id}")
        assert response.status_code == 200
        task = response.json()
        assert task["title"] == "Обновленный заголовок 2"
        assert task["description"] == "Обновленное описание 2"
        assert task["status"] == "completed"
        
        # Проверяем третью задачу
        response = await client.get(f"/tasks/{third_task_id}")
        assert response.status_code == 200
        task = response.json()
        assert task["title"] == "Обновленный заголовок 3"
        assert task["description"] == "Обновленное описание 3"
        assert task["status"] == "completed"
        
        # Проверяем четвертую задачу
        response = await client.get(f"/tasks/{fourth_task_id}")
        assert response.status_code == 200
        task = response.json()
        assert task["title"] == "Обновленный заголовок 4"
        assert task["description"] == "Обновленное описание 4"
        assert task["status"] == "completed"
        
        # Проверяем пятую задачу
        response = await client.get(f"/tasks/{fifth_task_id}")
        assert response.status_code == 200
        task = response.json()
        assert task["title"] == "Обновленный заголовок 5"
        assert task["description"] == "Обновленное описание 5"
        assert task["status"] == "completed"
        
        # Шаг 6: Удалить все задачи
        for task_id in task_ids:
            response = await client.delete(f"/tasks/{task_id}")
            assert response.status_code == 200, f"Ошибка удаления задачи {task_id}: {response.text}"
            deleted_task = response.json()
            assert deleted_task["id"] == task_id
        
        # Шаг 7: Проверить, что задачи удалены
        # Проверяем, что задачи не найдены по ID
        for task_id in task_ids:
            response = await client.get(f"/tasks/{task_id}")
            assert response.status_code == 422, f"Задача {task_id} должна быть удалена, но найдена"
        
        # Проверяем, что задачи отсутствуют в списке всех задач
        response = await client.get("/tasks/")
        assert response.status_code == 200
        all_tasks_after_delete = response.json()
        remaining_task_ids = [task["id"] for task in all_tasks_after_delete]
        for task_id in task_ids:
            assert task_id not in remaining_task_ids, f"Задача {task_id} не должна присутствовать в списке после удаления"
        
        print("✅ Все тесты пройдены успешно!")

