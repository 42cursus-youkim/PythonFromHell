class Class42:
    name : str
    likes : str
    teacher :str = 'parrot'

def run_student(obj) -> None:
    print(f"{obj.name} is running!")

bear = Class42()
bear.name="bear"
bear.likes="fish"

print(f"[studen {bear.name}]")
print(f"likes: {bear.likes}")
run_student(bear)
print(f"teacher: {bear.teacher}")