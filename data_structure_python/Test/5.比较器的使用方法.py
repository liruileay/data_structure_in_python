class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        # repr表示打印对象的时候打印sm必须有返回值
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10), ]
# key表示按照什么进行比较里面传一个函数
# 这个函数要接收一个参数并且有一个返回值作为sorted排序的依据
sorted(student_objects, key=lambda student: student.name)

print(student_objects)
