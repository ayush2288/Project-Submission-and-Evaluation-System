from django.db import models


class Sy_add_idea_no(models.Model):
    Add_sy_group_no = models.IntegerField()
    
    CHOICES_GUIDE = [
        ('0', 'None'),
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'C'),
        ('4', 'D'),
        ('5', 'E'),
    ]
    CHOICES_BRANCH = [
        ('0', 'NONE'),
        ('1', 'IT'),
        ('2', 'COMPS'),
        ('3', 'AIDS'),
        ('4', 'EXTC'),
    ]
    CHOICES_YEAR = [
        ('0', 'None'),
        ('1', '2023'),
        ('2', '2024'),
        ('3', '2025'),
        ('4', '2026'),
        ('5', '2027'),
        ('6', '2028'),
        ('7', '2029'),
        ('8', '2030'),
        ('9', '2031'),
        ('10', '2032'),
    ]

    sy_idea_1 = models.CharField(max_length=60)
    sy_idea_1_des = models.TextField(max_length=300)

    sy_idea_2 = models.CharField(max_length=60)
    sy_idea_2_des = models.TextField(max_length=300)
    
    sy_idea_3 = models.CharField(max_length=60)
    sy_idea_3_des = models.TextField(max_length=300)
    
    choices_guide = models.CharField(
        max_length=20,
        choices=CHOICES_GUIDE,
        default='0'
    )
    choices_branch = models.CharField(
        max_length=20,
        choices=CHOICES_BRANCH,
        default='0'
    )
    choices_year = models.CharField(
        max_length=20,
        choices=CHOICES_YEAR,
        default='0'
    )

    def get_grp_no(self):
        return self.Add_sy_group_no
    
    def get_sy_idea_1(self):
        return self.sy_idea_1
    
    def get_sy_idea_1_description(self):
        return self.sy_idea_1_des
    
    def get_sy_idea_2(self):
        return self.sy_idea_2
    
    def get_sy_idea_2_description(self):
        return self.sy_idea_2_des
    
    def get_sy_idea_3(self):
        return self.sy_idea_3
    
    def get_sy_idea_3_description(self):
        return self.sy_idea_3_des
    
    def get_choices_guide(self):
        return dict(self.CHOICES_GUIDE).get(self.choices_guide, 'Unknown')
    
    def get_choices_branch(self):
        return dict(self.CHOICES_BRANCH).get(self.choices_branch, 'Unknown')
    
    def get_choices_year(self):
        return dict(self.CHOICES_YEAR).get(self.choices_year, 'Unknown')

    def __str__(self):
        return (f'Group No: {self.Add_sy_group_no}, '
                f'Guide: {self.get_choices_guide()}, '
                f'Branch: {self.get_choices_branch()}, '
                f'Year: {self.get_choices_year()}')
    



class Sy_idea_no(models.Model):
    sy_name = models.CharField(max_length=100)
    sy_roll_no = models.IntegerField()
    sy_email = models.CharField(max_length=100,default='@somaiya.edu')
    sy_group_no = models.ForeignKey(Sy_add_idea_no, on_delete=models.CASCADE)
    def __str__(self):
        return f'Name : {self.sy_name}, Group No: {self.sy_group_no.Add_sy_group_no}, Branch: {self.sy_group_no.get_choices_branch()}, Guide: {self.sy_group_no.get_choices_guide()},Year: {self.sy_group_no.get_choices_year()}'


class final_idea(models.Model):
    final_title = models.ForeignKey(Sy_add_idea_no, on_delete=models.CASCADE)
    selected_idea = models.CharField(max_length=60)

    def __str__(self):
        return f' Selected Idea: {self.selected_idea} ,Group: {self.final_title.Add_sy_group_no}, Branch: {self.final_title.get_choices_branch()}'



CHOICES01 = [
    ('1', 'Student is Present'),
    ('0', 'Student is Absent'),
    ('2', 'The presentation has not been conducted yet')

]


CHOICES1 = [
   
    ('5', 'Cites substantial current quality literature(5)'),
    ('4', 'Cites reasonable quantity of current quality literature(4)'),
    ('3', 'Cites current literature(3)'),
    ('2', 'Does not cite any current quality literature(2)'),
    ('0', 'Assign zero marks.'),
]

CHOICES2 = [
       
    ('5', 'Provides good understanding of literature cited(5)'),
    ('4', 'Provides understanding of literature cited(4)'),
    ('3', 'Exhibits poor understanding of literature cited(3)'),
    ('2', 'Very poor in understanding literature cited(2)'),
        ('0', 'Assign zero marks.'),
]

CHOICES3 = [
       
    ('10', 'Very good clarity about the subject matter'),
    ('8', 'Somewhat good clarity'),
    ('6', 'Not so good clarity'),
    ('4', 'Very poor'),
        ('0', 'Assign zero marks.'),
]

CHOICES4 = [
       
    ('3', 'Written in own, grammatically correct language'),
    ('2.4', 'Written in own language, has many grammatical errors'),
    ('1.8', 'Language not good'),
    ('1.2', 'Mostly copied'),
    ('0', 'Assign zero marks.'),
]

CHOICES5 = [
       
    ('2', 'Recommended format used'),
    ('1.4', 'Mostly in recommended format'),
    ('1.2', 'Many deviations from format'),
    ('0.8', 'No format'),
        ('0', 'Assign zero marks.'),
]

CHOICES6 = [
       
    ('3', 'Very good presentation'),
    ('2.4', 'Somewhat good presentation'),
    ('1.8', 'Messy presentation'),
    ('1.2', 'Very poor presentation'),
        ('0', 'Assign zero marks.'),
]

CHOICES7 = [
       
    ('2', 'Very good Communication Skill'),
    ('1.4', 'Good Communication Skill'),
    ('1.2', 'Poor Communication Skill'),
    ('0.8', 'Very poor Communication Skill'),
        ('0', 'Assign zero marks.'),
]

CHOICES8 = [
       
    ('10', 'International (Refereed) print Journal'),
    ('8', 'National (Refereed) print Journal'),
    ('6', 'International (Refereed) Conference'),
    ('4', 'National (Refereed) Conference and Online Journal'),
        ('0', 'Assign zero marks.'),
]

CHOICES9 = [
       
    ('2.5', 'Highly effective communication'),
    ('2.0', 'Good communication'),
    ('1.5', 'Adequate communication'),
    ('1.0', 'Ineffective communication'),
        ('0', 'Assign zero marks.'),
]

CHOICES10 = [
       
    ('2.5', 'Equal contribution from all members'),
    ('2.0', 'Good contribution from most members'),
    ('1.5', 'Uneven contribution'),
    ('1.0', 'Poor contribution from members'),
        ('0', 'Assign zero marks.'),
]

CHOICES11 = [
       
    ('2.5', 'Excellent coordination'),
    ('2.0', 'Good coordination'),
    ('1.5', 'Adequate coordination'),
    ('1.0', 'Poor coordination'),
        ('0', 'Assign zero marks.'),
]

CHOICES12 = [
    
    ('2.5', 'Excellent coordination'),
    ('2.0', 'Good coordination'),
    ('1.5', 'Adequate coordination'),
    ('1.0', 'Poor coordination'),
        ('0', 'Assign zero marks.'),
]




 

class FinalMarksEvaluation(models.Model):
    final_marks_evaluation = models.ForeignKey(final_idea, on_delete=models.CASCADE)
    final_marks_student = models.ForeignKey(Sy_idea_no, on_delete=models.CASCADE)

    # Fields for P1 Marks Evaluation
    num01 = models.CharField(max_length=60, choices=CHOICES01, default='2')
    num1 = models.CharField(max_length=60, choices=CHOICES1, default='0')
    num2 = models.CharField(max_length=60, choices=CHOICES2, default='0')
    num21 = models.CharField(max_length=60, choices=CHOICES3, default='0')
    num31 = models.CharField(max_length=60, choices=CHOICES4, default='0')
    num32 = models.CharField(max_length=60, choices=CHOICES5, default='0')
    num33 = models.CharField(max_length=60, choices=CHOICES6, default='0')
    num34 = models.CharField(max_length=60, choices=CHOICES7, default='0')
    num41 = models.CharField(max_length=60, choices=CHOICES8, default='0')
    num51 = models.CharField(max_length=60, choices=CHOICES9, default='0')
    num52 = models.CharField(max_length=60, choices=CHOICES10, default='0')
    num53 = models.CharField(max_length=60, choices=CHOICES11, default='0')
    num54 = models.CharField(max_length=60, choices=CHOICES12, default='0')


    # Fields for P2 Marks Evaluation
    p2_num01 = models.CharField(max_length=60, choices=CHOICES01, default='2')
    p2_num1 = models.CharField(max_length=60, choices=CHOICES1, default='0')
    p2_num2 = models.CharField(max_length=60, choices=CHOICES2, default='0')
    p2_num21 = models.CharField(max_length=60, choices=CHOICES3, default='0')
    p2_num31 = models.CharField(max_length=60, choices=CHOICES4, default='0')
    p2_num32 = models.CharField(max_length=60, choices=CHOICES5, default='0')
    p2_num33 = models.CharField(max_length=60, choices=CHOICES6, default='0')
    p2_num34 = models.CharField(max_length=60, choices=CHOICES7, default='0')
    p2_num41 = models.CharField(max_length=60, choices=CHOICES8, default='0')
    p2_num51 = models.CharField(max_length=60, choices=CHOICES9, default='0')
    p2_num52 = models.CharField(max_length=60, choices=CHOICES10, default='0')
    p2_num53 = models.CharField(max_length=60, choices=CHOICES11, default='0')
    p2_num54 = models.CharField(max_length=60, choices=CHOICES12, default='0')


    # Fields for P3 Marks Evaluation
    p3_num01 = models.CharField(max_length=60, choices=CHOICES01, default='2')
    p3_num1 = models.CharField(max_length=60, choices=CHOICES1, default='0')
    p3_num2 = models.CharField(max_length=60, choices=CHOICES2, default='0')
    p3_num21 = models.CharField(max_length=60, choices=CHOICES3, default='0')
    p3_num31 = models.CharField(max_length=60, choices=CHOICES4, default='0')
    p3_num32 = models.CharField(max_length=60, choices=CHOICES5, default='0')
    p3_num33 = models.CharField(max_length=60, choices=CHOICES6, default='0')
    p3_num34 = models.CharField(max_length=60, choices=CHOICES7, default='0')
    p3_num41 = models.CharField(max_length=60, choices=CHOICES8, default='0')
    p3_num51 = models.CharField(max_length=60, choices=CHOICES9, default='0')
    p3_num52 = models.CharField(max_length=60, choices=CHOICES10, default='0')
    p3_num53 = models.CharField(max_length=60, choices=CHOICES11, default='0')
    p3_num54 = models.CharField(max_length=60, choices=CHOICES12, default='0')


    # Fields for P4 Marks Evaluation
    p4_num01 = models.CharField(max_length=60, choices=CHOICES01, default='2')
    p4_num1 = models.CharField(max_length=60, choices=CHOICES1, default='0')
    p4_num2 = models.CharField(max_length=60, choices=CHOICES2, default='0')
    p4_num21 = models.CharField(max_length=60, choices=CHOICES3, default='0')
    p4_num31 = models.CharField(max_length=60, choices=CHOICES4, default='0')
    p4_num32 = models.CharField(max_length=60, choices=CHOICES5, default='0')
    p4_num33 = models.CharField(max_length=60, choices=CHOICES6, default='0')
    p4_num34 = models.CharField(max_length=60, choices=CHOICES7, default='0')
    p4_num41 = models.CharField(max_length=60, choices=CHOICES8, default='0')
    p4_num51 = models.CharField(max_length=60, choices=CHOICES9, default='0')
    p4_num52 = models.CharField(max_length=60, choices=CHOICES10, default='0')
    p4_num53 = models.CharField(max_length=60, choices=CHOICES11, default='0')
    p4_num54 = models.CharField(max_length=60, choices=CHOICES12, default='0')


    oral_practical = models.IntegerField(default=0)
    def return_final_idea_des(self):
        selected_idea = self.final_marks_evaluation.selected_idea
        final_title = self.final_marks_evaluation.final_title

        if not selected_idea or not final_title:
            return "No description available."

        # Mapping selected idea to corresponding descriptions
        if selected_idea == final_title.sy_idea_1:
            return final_title.get_sy_idea_1_description()
        elif selected_idea == final_title.sy_idea_2:
            return final_title.get_sy_idea_2_description()
        elif selected_idea == final_title.sy_idea_3:
            return final_title.get_sy_idea_3_description()

        return "No description available."




    
    def total_marks(self):
        return float(self.num1) + float(self.num2) + float(self.num21) + float(self.num31) + float(self.num32) + float(self.num33) + float(self.num34) + float(self.num41) +float(self.num51) + float(self.num52) + float(self.num53) + float(self.num54)
    
    def p2_total_marks(self):
        return float(self.p2_num1) + float(self.p2_num2) + float(self.p2_num21) + float(self.p2_num31) + float(self.p2_num32) + float(self.p2_num33) + float(self.p2_num34) + float(self.p2_num41) +float(self.p2_num51) + float(self.p2_num52) + float(self.p2_num53) + float(self.p2_num54)
    
    def p3_total_marks(self):
        return float(self.p3_num1) + float(self.p3_num2) + float(self.p3_num21) + float(self.p3_num31) + float(self.p3_num32) + float(self.p3_num33) + float(self.p3_num34) + float(self.p3_num41) +float(self.p3_num51) + float(self.p3_num52) + float(self.p3_num53) + float(self.p3_num54)
    
    def p4_total_marks(self):
        return float(self.p4_num1) + float(self.p4_num2) + float(self.p4_num21) + float(self.p4_num31) + float(self.p4_num32) + float(self.p4_num33) + float(self.p4_num34) + float(self.p4_num41) +float(self.p4_num51) + float(self.p4_num52) + float(self.p4_num53) + float(self.p4_num54)
    def avg_marks(self):
        avg = self.total_marks() + self.p2_total_marks() + self.p3_total_marks() + self.p4_total_marks()
        return round(avg/4,2)


class GroupEvaluation(models.Model):
    CHOICES1 = [
        ('5', 'Cites substantial current quality literature(5)'),
        ('4', 'Cites reasonable quantity of current quality literature(4)'),
        ('3', 'Cites current literature(3)'),
        ('2', 'Does not cite any current quality literature(2)'),
    ]
    
    CHOICES2 = [
        ('5', 'Provides good understanding of literature cited(5)'),
        ('4', 'Provides understanding of literature cited(4)'),
        ('3', 'Exhibits poor understanding of literature cited(3)'),
        ('2', 'Very poor in understanding literature cited(2)'),
    ]

    CHOICES3 = [
        ('10', 'Very good clarity about the subject matter'),
        ('8', 'Somewhat good clarity'),
        ('6', 'Not so good clarity'),
        ('4', 'Very poor'),
    ]

    CHOICES4 = [
        ('3', 'Written in own, grammatically correct language'),
        ('2.4', 'Written in own language, has many grammatical errors'),
        ('1.8', 'Language not good'),
        ('1.2', 'Mostly copied'),
    ]
    
    CHOICES5 = [
        ('2', 'Recommended format used'),
        ('1.4', 'Mostly in recommended format'),
        ('1.2', 'Many deviations from format'),
        ('0.8', 'No format'),
    ]
    
    CHOICES6 = [
        ('3', 'Very good presentation'),
        ('2.4', 'Somewhat good presentation'),
        ('1.8', 'Messy presentation'),
        ('1.2', 'Very poor presentation'),
    ]
    
    CHOICES7 = [
        ('2', 'Very good Communication Skill'),
        ('1.4', 'Good Communication Skill'),
        ('1.2', 'Poor Communication Skill'),
        ('0.8', 'Very poor Communication Skill'),
    ]

    CHOICES8 = [
        ('10', 'International (Refereed) print Journal'),
        ('8', 'National (Refereed) print Journal'),
        ('6', 'International (Refereed) Conference'),
        ('4', 'National (Refereed) Conference and Online Journal'),
    ]

    CHOICES9 = [
        ('2.5', 'Highly effective communication'),
        ('2.0', 'Good communication'),
        ('1.5', 'Adequate communication'),
        ('1.0', 'Ineffective communication'),
    ]

    CHOICES10 = [
        ('2.5', 'Equal contribution from all members'),
        ('2.0', 'Good contribution from most members'),
        ('1.5', 'Uneven contribution'),
        ('1.0', 'Poor contribution from members'),
    ]

    CHOICES11 = [
        ('2.5', 'Excellent coordination'),
        ('2.0', 'Good coordination'),
        ('1.5', 'Adequate coordination'),
        ('1.0', 'Poor coordination'),
    ]

    CHOICES12 = [
        ('2.5', 'Excellent coordination'),
        ('2.0', 'Good coordination'),
        ('1.5', 'Adequate coordination'),
        ('1.0', 'Poor coordination'),
    ]

    CHOICES13 = [
        ('None', 'None'),
        ('IT', 'IT'),
        ('COMPS', 'COMPS'),
        ('AIDS', 'AIDS'),
        ('EXTC', 'EXTC'),
    ]

    group_name = models.CharField(max_length=255, null=True)
    roll_no = models.IntegerField()
    sy_idea_no = models.ForeignKey(Sy_idea_no, on_delete=models.CASCADE, null=True, blank=True)
    
    num01 = models.CharField(
        max_length=7,
        choices=CHOICES13,
        default='None',
        blank=True
    )

    group_year = models.CharField(max_length=4, null=True)
    
    num1 = models.CharField(
        max_length=1,
        choices=CHOICES1,
        default='2'
    )
    
    num2 = models.CharField(
        max_length=1,
        choices=CHOICES2,
        default='2'
    )
    
    num21 = models.CharField(
        max_length=2,
        choices=CHOICES3,
        default='4'
    )
    
    num31 = models.CharField(
        max_length=3,
        choices=CHOICES4,
        default='4'
    )
    
    num32 = models.CharField(
        max_length=3,
        choices=CHOICES5,
        default='4'
    )
    
    num33 = models.CharField(
        max_length=3,
        choices=CHOICES6,
        default='4'
    )
    
    num34 = models.CharField(
        max_length=3,
        choices=CHOICES7,
        default='4'
    )
    
    num41 = models.CharField(
        max_length=2,
        choices=CHOICES8,
        default='4'
    )
    
    num51 = models.CharField(
        max_length=3,
        choices=CHOICES9,
        default='4'
    )
    
    num52 = models.CharField(
        max_length=3,
        choices=CHOICES10,
        default='4'
    )
    
    num53 = models.CharField(
        max_length=3,
        choices=CHOICES11,
        default='4'
    )
    
    num54 = models.CharField(
        max_length=3,
        choices=CHOICES12,
        default='4'
    )

    oral_practical = models.IntegerField(default=0)
    
    def eval1_total(self):
        return float(self.num1) + float(self.num2)
    
    def eval2_total(self):
        return float(self.num21)
    
    def eval3_total(self):
        return float(self.num31) + float(self.num32) + float(self.num33) + float(self.num34)
    
    def eval4_total(self):
        return float(self.num41)
    
    def eval5_total(self):
        return float(self.num51) + float(self.num52) + float(self.num53) + float(self.num54)

    def calculate_teamwork(self):
        total = (self.eval1_total() + self.eval2_total() + self.eval3_total() + self.eval4_total() + self.eval5_total())
        return total / 5



# TY:



class Ty_idea_no(models.Model):
    ty_idea = models.CharField(max_length=250)
    ty_grp_no = models.IntegerField()

    def __str__(self):
        return f"{self.ty_idea} - {self.ty_grp_no}"

class GroupEvaluation_ty(models.Model):
# Substantial current and good quality literature (10)
    CHOICES1 = [
        ('5', 'Cites substantial current quality literature(5)'),
        ('4', 'Cites reasonable quantity of current quality literature(4)'),
        ('3', 'Cites current literature(3)'),
        ('2', 'Does not cite any current quality literature(2)'),
    ]
   
    CHOICES2 = [
        ('5', 'Provides good understanding of literature cited(5)'),
        ('4', 'Provides understanding of literature cited(4)'),
        ('3', 'Exhibits poor understanding of literature cited(3)'),
        ('2', 'Very poor in understanding literature cited(2)'),
    ]
 # Answering Questions Posed by Examiner (10)
    CHOICES3 = [
        ('10', 'Very good clarity about the subject matter'),
        ('8', 'Somewhat good clarity'),
        ('6', 'Not so good clarity'),
        ('4', 'Very poor'),
    ]
# Presentation skills(10)
    CHOICES4 = [
        ('4', 'Written in own, grammatically correct language'),
        ('3.2', 'Written in own language, has many grammatical errors'),
        ('2.4', 'Language not good'),
        ('1.6', 'Mostly copied'),
    ]
    
    CHOICES5 = [
        ('4', 'Very good presentation'),
        ('3.2', 'Somewhat good presentation'),
        ('2.4', 'Messy presentation'),
        ('1.6', 'Very poor presentation'),
    ]

    CHOICES6 = [
        ('2', 'Recommended format used'),
        ('1.6', 'Mostly in recommended format'),
        ('1.2', 'Many deviations from format'),
        ('0.8', 'No format'),
    ]

    # Communication skills(10)
    CHOICES7 = [
        ('10', 'Very good Communication Skill'),
        ('8', 'Good Communication Skill'),
        ('6', 'Poor Communication Skill'),
        ('4', 'Very poor Communication Skill'),
    ]

# Quality of Research Paper (10)
    CHOICES8 = [
        ('10', 'International (Refereed) print Journal'),
        ('8', 'National (Refereed) print Journal'),
        ('6', 'International (Refereed) Conference'),
        ('4', 'National (Refereed) Conference and Online Journal'),
    ]

# Teamwork and Collaboration (10)
    CHOICES9 = [
        ('10', 'Highly effective communication and Equal contribution from all members'),
        ('8', 'Good communication and good contribution from most members'),
        ('6', 'Adequate communication and uneven contribution'),
        ('4', 'Ineffective communication and poor contribution from members'),
    ]

    # Documentation and Reporting (10)

    CHOICES10 = [
        ('10', 'Very clear, concise, well organized and logical'),
        ('8', 'Mostly clear, concise and organized'),
        ('6', 'Somewhat clear, concise and organized'),
        ('4', 'Lacks clarity and conciseness and Poorly organized.'),
    ]


    CHOICES11 = [
        ('None', 'None'),
        ('IT', 'IT'),
        ('COMPS', 'COMPS'),
        ('AIDS', 'AIDS'),
        ('EXTC', 'EXTC'),
    ]
    
    group_name = models.CharField(max_length=255, null=True)
    roll_no = models.IntegerField(default=0)
    ty_idea_no = models.ForeignKey(Ty_idea_no, on_delete=models.CASCADE, null=True, blank=True)
    
   
    # branch
    num01 = models.CharField(
        max_length=7,
        choices=CHOICES11,
        default='None'
    )

    group_year = models.CharField(max_length=4, null=True)

    # Substantial current and good quality literature (10)
    num1 = models.CharField(
        max_length=1,
        choices=CHOICES1,
        default='None'
    )
    
    num2 = models.CharField(
        max_length=1,
        choices=CHOICES2,
        default='2'
    )
    
# Answering Questions Posed by Examiner (10)
    num21 = models.CharField(
        max_length=2,
        choices=CHOICES3,
        default='4'
    )
    # Presentation skills(10)
    num31 = models.CharField(
        max_length=3,
        choices=CHOICES4,
        default='4'
    )
    
    num32 = models.CharField(
        max_length=3,
        choices=CHOICES5,
        default='4'
    )
    
    num33 = models.CharField(
        max_length=3,
        choices=CHOICES6,
        default='2'
    )
    

    
    num41 = models.CharField(
        max_length=2,
        choices=CHOICES7,
        default='4'
    )
    
    num51 = models.CharField(
        max_length=3,
        choices=CHOICES8,
        default='4'
    )
    
    num61 = models.CharField(
        max_length=3,
        choices=CHOICES9,
        default='4'
    )

    num71= models.CharField(
        max_length=3,
        choices=CHOICES10,
        default='4'
    )
    
    oral_practical = models.IntegerField(default=0)
    
    def eval1_total(self):
        return float(self.num1) + float(self.num2)
    
    def eval2_total(self):
        return int(self.num21)
    
    def eval3_total(self):
        return float(self.num31) + float(self.num32) + float(self.num33) 
    
    def eval4_total(self):
        return float(self.num41)
    
    def eval5_total(self):
        return float(self.num51) 
    
    def eval6_total(self):
        return float(self.num61) 
    
    def eval7_total(self):
        return float(self.num71) 

    def calculate_teamwork(self):
        total = (self.eval1_total() + self.eval2_total() + self.eval3_total() + self.eval4_total() + self.eval5_total() + self.eval6_total() + self.eval7_total())
        ans =  total / 7
        return round(ans , 2)








# LY:

class GroupEvaluation_ly(models.Model):
# Substantial current and good quality literature (10)
    CHOICES1 = [
        ('5', 'Cites substantial current quality literature(5)'),
        ('4', 'Cites reasonable quantity of current quality literature(4)'),
        ('3', 'Cites current literature(3)'),
        ('2', 'Does not cite any current quality literature(2)'),
    ]
   
    CHOICES2 = [
        ('5', 'Provides good understanding of literature cited(5)'),
        ('4', 'Provides understanding of literature cited(4)'),
        ('3', 'Exhibits poor understanding of literature cited(3)'),
        ('2', 'Very poor in understanding literature cited(2)'),
    ]
 # Answering Questions Posed by Examiner (10)
    CHOICES3 = [
        ('10', 'Very good clarity about the subject matter'),
        ('8', 'Somewhat good clarity'),
        ('6', 'Not so good clarity'),
        ('4', 'Very poor'),
    ]
    
# Presentation skills(10)
    CHOICES4 = [
        ('4', 'Written in own, grammatically correct language'),
        ('3.2', 'Written in own language, has many grammatical errors'),
        ('2.4', 'Language not good'),
        ('1.6', 'Mostly copied'),
    ]
    
    CHOICES5 = [
        ('4', 'Very good presentation'),
        ('3.2', 'Somewhat good presentation'),
        ('2.4', 'Messy presentation'),
        ('1.6', 'Very poor presentation'),
    ]

    CHOICES6 = [
        ('2', 'Recommended format used'),
        ('1.6', 'Mostly in recommended format'),
        ('1.2', 'Many deviations from format'),
        ('0.8', 'No format'),
    ]

    # Communication skills(10)
    CHOICES7 = [
        ('10', 'Very good Communication Skill'),
        ('8', 'Good Communication Skill'),
        ('6', 'Poor Communication Skill'),
        ('4', 'Very poor Communication Skill'),
    ]

# Quality of Research Paper (10)
    CHOICES8 = [
        ('10', 'International (Refereed) print Journal'),
        ('8', 'National (Refereed) print Journal'),
        ('6', 'International (Refereed) Conference'),
        ('4', 'National (Refereed) Conference and Online Journal'),
    ]

# Teamwork and Collaboration (10)
    CHOICES9 = [
        ('10', 'Highly effective communication and Equal contribution from all members'),
        ('8', 'Good communication and good contribution from most members'),
        ('6', 'Adequate communication and uneven contribution'),
        ('4', 'Ineffective communication and poor contribution from members'),
    ]

    # Documentation and Reporting (10)
    CHOICES10 = [
        ('10', 'Very clear, concise, well organized and logical'),
        ('8', 'Mostly clear, concise and organized'),
        ('6', 'Somewhat clear, concise and organized'),
        ('4', 'Lacks clarity and conciseness and Poorly organized.'),
    ]

    # Originality (10)
    CHOICES11 = [
        ('10', 'Highly innovative and original'),
        ('8', 'Some innovation and originality'),
        ('6', 'Minimal innovation and originality'),
        ('4', 'Lacks innovation and originality.'),
    ]

    # Creativity (10)
    CHOICES12 = [
        ('10', 'Demonstrates exceptional creativity'),
        ('8', 'Shows good creativity'),
        ('6', 'Demonstrates average creativity'),
        ('4', 'Lacks creativity'),
    ]

    # Design and Technical Feasibility (10)
    CHOICES13 = [
        ('10', 'Design is highly effective and it is highly feasible and practical'),
        ('8', 'Design is mostly effective and technically feasible and practical'),
        ('6', 'Design is somewhat effective and feasibility is questionable'),
        ('4', 'Design is ineffective and neither feasible nor practical'),
    ]


    CHOICES14 = [
        ('None', 'None'),
        ('IT', 'IT'),
        ('COMPS', 'COMPS'),
        ('AIDS', 'AIDS'),
        ('EXTC', 'EXTC'),
    ]
    

    group_no = models.IntegerField(unique=True)
    group_name = models.CharField(max_length=255, null=True)
    group_idea = models.CharField(max_length=255, null=True)
    
    # branch
    num01 = models.CharField(
        max_length=7,
        choices=CHOICES14,
        default='None'
    )

    group_year = models.CharField(max_length=4, null=True)

    # Substantial current and good quality literature (10)
    num1 = models.CharField(
        max_length=1,
        choices=CHOICES1,
        default='None'
    )
    
    num2 = models.CharField(
        max_length=1,
        choices=CHOICES2,
        default='2'
    )
    
# Answering Questions Posed by Examiner (10)
    num21 = models.CharField(
        max_length=2,
        choices=CHOICES3,
        default='4'
    )

    # Presentation skills(10)
    num31 = models.CharField(
        max_length=3,
        choices=CHOICES4,
        default='4'
    )
    
    num32 = models.CharField(
        max_length=3,
        choices=CHOICES5,
        default='4'
    )
    
    num33 = models.CharField(
        max_length=3,
        choices=CHOICES6,
        default='2'
    )

    # Communication skills(10)
    num41 = models.CharField(
        max_length=2,
        choices=CHOICES7,
        default='4'
    )

 # Quality of Research Paper (10)
    num51 = models.CharField(
        max_length=3,
        choices=CHOICES8,
        default='4'
    )
    
# Teamwork and Collaboration (10) 
    num61 = models.CharField(
        max_length=3,
        choices=CHOICES9,
        default='4'
    )

# Documentation and Reporting (10) 
    num71= models.CharField(
        max_length=3,
        choices=CHOICES10,
        default='4'
    )

# Originality
    num81= models.CharField(
        max_length=3,
        choices=CHOICES11,
        default='4'
    )

# Creativity
    num91= models.CharField(
        max_length=3,
        choices=CHOICES12,
        default='4'
    )

    # Design and Technical Feasibility
    num101= models.CharField(
        max_length=3,
        choices=CHOICES13,
        default='4'
    )
    
    oral_practical = models.IntegerField(default=0)
    
    def eval1_total(self):
        return float(self.num1) + float(self.num2)
    
    def eval2_total(self):
        return int(self.num21)
    
    def eval3_total(self):
        return float(self.num31) + float(self.num32) + float(self.num33) 
    
    def eval4_total(self):
        return float(self.num41)
    
    def eval5_total(self):
        return float(self.num51) 
    
    def eval6_total(self):
        return float(self.num61) 
    
    def eval7_total(self):
        return float(self.num71) 
    
    def eval8_total(self):
        return float(self.num81) 
    
    def eval9_total(self):
        return float(self.num91) 
    
    def eval10_total(self):
        return float(self.num101) 

    def calculate_teamwork(self):
        total = (self.eval1_total() + self.eval2_total() 
                 + self.eval3_total() + self.eval4_total() 
                 + self.eval5_total() + self.eval6_total() 
                 + self.eval7_total()  + self.eval8_total() 
                 + self.eval9_total()+ + self.eval10_total())
        ans =  total / 10
        return round(ans , 2)
