class Class42:
    teacher :str= 'parrot'

def show_teacher_outcls(cls) -> None:
    print(f"teacher: {cls.teacher}")

def change_teacher_outcls(cls, teacher) -> None:
    cls.teacher = teacher

show_teacher_outcls(Class42)
change_teacher_outcls(Class42, 'penguin')
show_teacher_outcls(Class42)