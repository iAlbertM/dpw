
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world! ')
        # Tommy's grade
        t = Transcript()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        self.response.write("Tommy's final grade: " + str(t.final_grade) + " ")

        # Sally's grade
        s = Transcript()
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 75
        self.response.write("Sally's final grade: " + str(s.final_grade)
       + " ")

class Transcript(object):
    def __init__(self):
        self.grade1 = 0
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0

    @property
    def final_grade(self):
        # calculate final grade
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5
        return self.__final_grade


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
