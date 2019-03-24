from app import create_app

app = create_app()

from app.tasks.reptile import synchronization

a = synchronization.delay()

print(a.wait())
print(a.result)
