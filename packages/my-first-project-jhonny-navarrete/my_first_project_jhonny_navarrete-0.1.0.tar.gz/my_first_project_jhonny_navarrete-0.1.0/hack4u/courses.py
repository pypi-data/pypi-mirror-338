class Course:

    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self):
        return f"{self.name}[{self.duration} horas] ({self.link})"


courses = [
            Course("Introduccion a Linux", 15, "www.google.com.ve"),
            Course("Personalizacion de Linux", 3, "www.google.com.co"),
            Course("Introduccion al Hacking", 53, "www.google.com.mx")
]

def list_courses():
    for course in courses:
       print(course)


def search_course_by_name(text):
    for course in courses:
        if course.name == text:
            return course
    return None














