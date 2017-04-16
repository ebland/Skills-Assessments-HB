    #"""
    #"""Part 2: Classes and Init Methods""" """Part 2: Classes and Init Methods"""

# 1. What are the three main design advantages that object orientation
#    can provide? Explain each concept.

# ANSWER://

# The following 3 main design advantages that object orientation presents is through 
# abstraction/encapsulation, inheritance, and polymorphism.

#     1) In encapsulation, sensitive tampering of values can be 
#        eliminated with objects having the ability to hide certain parts of 
#        themselves from programmers.
#          -Abstraction refers to the act of representing essential features without
#           including the background details or explanations.
#          -Storing data and functions in a single unit(class) is encapsulation.

#     2) Inheritance is the process by which objects can acquire the properties of 
#        objects of other classes. Inheritance provides reusability, like, adding 
#        additional features to an existing class without modifying it in supporting 
#        legacy code and other tasks. (Polymorphism is extensively used in 
#        implementing inheritance)

#     3) Polymorphism means the ability to take more than one form. An operation may
#        exhibit different behaviors in different instances. The behavior depends on 
#        the data types used in the operation. 

# NOTE:// Due to larger applications being complex and challenging to code, object
#         orientation forces programmers to plan and implement preventative/intensive
#         planning process phases before beginning and having all design concepts
#         already integrated to assure a solid foundation which will present less 
#         errors down the road. Another beneficial characteristic of utilizing 
#         object orientation is that once a program reaches a certain size, the 
#         applications are easier to maintain and build upon in comparison with 
#         applications that are non object oriented ones.

# 2. What is a class?

# ANSWER:// "class object is a parent of all of its instance objects"-liz

# A class is a way of organizing and producing objects with similar attributes 
# and methods. (ex. dictionary)
#    Class objects support two kinds of operations: 
#     -attribute references 
#     -instantiation

# 3. What is an instance attribute?

# ANSWER://

# An instance attribute is a variable defined in a class, in which each object
# of the class has a separate copy, or instance. Instance attributes have notation 
# of data unique to each instance and class variables, mentioned in the question/answer 
# "2. What is a class?" above, are for attributes/methods shared by all instances
# of the class.

# 4. What is a method?

# ANSWER://

# A method is a function that takes a class instance as its first parameter. 
#     -Methods are members of classes and are bound or unbound.

#     1) Bound methods belong to instances of a class.
#     2) Unbound methods are called inside of a class instead of inside an instance.

# 5. What is an instance in object orientation?

# ANSWER://

# An instance in object orientation has to be aware of it's parent,(+properties)
# so you have to pass the method that refers to the parent class as "self".

# 6. How is a class attribute different than an instance attribute?
#    Give an example of when you might use each.

# ANSWER://

# Class attributes are same for all instances of class whereas instance attributes
# is particular for each instance. Also, instance attributes are for data specificied
# for each instance, and class attributes are used by all instances of the class."""


#"""EXAMPLES PARTS 2 THROUGH 5""" """BELOW""""""EXAMPLES PARTS 2 THROUGH 5"""

# Parts 2 through 5:
# Create your classes and class methods

#"""6. Give an example of when you might use each, a class attribute and an 
#instance attribute"""

########################
#EXAMPLE USING "A"

# class attributes syntax= A.__dict__:
# class A:
#    class_attribute = 10
#    def class_method(self):
#         self.instance_attribute = 'I am instance attribute'
# print A.__dict__
# #{'__module__': '__main__', 'class_method': <function class_method at 0x10978ab18>, 'class_attribute': 10, '__doc__': None}
# #########################

# # instance attributes as A().__dict__:
# a = A() 
# a.class_method()
# print a.__dict__
# {'instance_attribute': 'I am instance attribute'}

#Class attribute will be available to all the functions in the class 
#AND the instance attribute is available to the function for that instance of
#the object.
#"""######### MY EXAMPLE #########"""

#""" #1 CLASS OBJECT ##########"""
import datetime

class Person:

        def __init__(self, name, birthday, address, phone_number, email_address):
            self.name = name
            self.birthday = birthday
            self.address = address
            self.phone_number = phone_number
            self.email_address = email_address

        def age(self):
            today = datetime.date.today()
            age = today.year - self.birthday.year

            if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
                age -= 1

            return age

person = Person(
    "Elizabeth Bland",
    datetime.date(1979, 10, 11), 
    "1326 Larkin St",
    "501-580-7383",
    "elizabethblands@gmail.com")

print(person.name)
print(person.email_address)
print(person.age())

#""" a)Instance attribute adding privacy to the person age information"""

def age(person):
        if hasattr(self, "_age"):
            return self._age

        today = datetime.date.today()

        age = today.year - self.birthday.year

        if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1

        person._age = age
        return age
#######by adding "_"...this will "hide" and provide an instance of privacy
#      so that the age of the person cannot be accessed directly in this instance.

#""" b)Class attributes provide default attribute values to your instance:)"""

class Person:
        dead_or_alive = False

        def dead_not_alive(self):
            self.dead_or_alive = True

#"""##########################################"""


#"""Part 2: Classes and Init Methods""" """Part 2: Classes and Init Methods"""


class Student(object):
        """1. Student"""
#     #{'first_name': 'Jasmine',
#       'last_name': 'Debugger',
#       'address': '0101 Computer Street'}

#      {'first_name': 'Jaqui',
#       'last_name': 'Console',
#       'address': '888 Binary Ave'}
    def __init__(self, first_name, last_name, address):
        """Init student class properties"""

        self.first_name = first_name
        self.last_name =   last_name
        self.address =       address

        #"""?????????????????????????"""
    # def __repr__(self):
    # return self.__str__() 
class Question(object):
        """Question"""
#     {'question': 'What is the capital of Alberta?',
#      'correct_answer': 'Edmonton'}

#     {'question': 'Who is the author of Python?',
#      'correct_answer': 'Guido Van Rossum'}
    def __init__(self, question, correct_answer):
        """Initialize question"""

        self.question=question
        self.correct_answer=correct_answer

    def ask_and_evaluate(self):
        """Prompt user for an answer to the question and return True/False"""

        user_answer=raw_input(self.question + " > ")
        return user_answer==self.correct_answer

         #"""?????????????????????????"""
    # def __repr__(self):
    # return self.__str__() 
#"""Part 3: Methods"""
class Exam(object):
        """Exam"""
#         {'name':'Midterm',
#          'questions': [

#         {'question':'What is the capital of Alberta?',
#          'correct_answer': 'Edmonton'},

#         {'question': 'Who is the author of Python?',
#          'correct_answer': 'Guido Van Rossum' }

#   ]
# }

#         {'name':'Final',
#          'questions': [

#         {'question':"Who is Ubermelon's competition?",
#          'correct_answer': 'Sqysh'},

#         {'question': "What is Balloonicorn's favorite color?",
#          'correct_answer': 'Sparkles'}

#   ]
# }
    def __init__(self, name):
        """Init exam"""
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Make a question for the exam and add to list of questions"""
        # Instantiate Question + append to list of Question objects
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """Administer all of the exam's questions and return score"""
        score = 0
        # Loop through objects (Question) call ask_and_evaluate() for object
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score+=1
        return score

        # """?????????????????????????"""
    # def __repr__(self):
    # return self.__str__()
#"""Part 4: Create an actual exam!"""

    def take_test(exam, student):
        """Administer the exam for a student and assign score to student"""
        
        student.score=exam.administer()
        return student.score

def example(exam_name, student_first_name, student_last_name, student_address):
        example_exam = Exam(exam_name)
        example_exam.add_question("What is the capital of Alberta?", "Edmonton")
        example_exam.add_question("Who is the author of Python?", "Guido Van Rossum")
        example_exam.add_question("What is Balloonicorn's favorite color?", "Sparkles")
        example_student = Student(student_first_name, student_last_name, student_address)
        print take_test(example_exam, example_student)


#"""Part 5: Inheritance"""


class Quiz(Exam):
        """Quiz
        Quiz is pass/fail
        Pass if at least half of the questions are answered correctly
        """

    def administer(self):
        """Administer all of the quiz's questions and returns True/False for Pass/Fail"""

        if super(Quiz, self).administer() < (len(self.questions)/2):
            return False
        else:
            return True


    



