class Students:
    Institute_name = 'Ferilion_Labs'
    def __init__(self,trainer_name,age,experience):
        self.name = trainer_name
        self.age  = age
        self.exp = experience
        self.course = None
        self.batch = None
        self.mobile = None

    def course_details(self,coursename,batch,mob_no):
        self.course = coursename
        self.batch  = batch
        self.mobile = mob_no

    def phase_details(self,phase1,phase2,phase3):
        self.phase1=phase1
        self.phase2=phase2
        self.phase3=phase3

    def trainers_details(self):
        return f"Trainer name is {self.name} , age is {self.age} and experience is {self.exp} "

    def Course_details(self):
        return f"course name is {self.course} , Batch Number is {self.batch} and Mobile number is {self.mobile} \n"

s1=Students('Harish',25,'1.3y')
s2=Students('Babu',24,'1y')
s3=Students('Krishna',23,'9M')


u1=Students('unknown',0,0)
u1.course_details('Python','B42',7997476016)

u2=Students('unknown',0,0)
u2.course_details("DE","B42",8106929707)

u3=Students('unknown',0,0)
u3.course_details('Java','B42',7032864628)

print(s1.trainers_details())
print(u1.Course_details())

print(s2.trainers_details())

print(u2.Course_details())

print(s3.trainers_details())

print(u3.Course_details())
