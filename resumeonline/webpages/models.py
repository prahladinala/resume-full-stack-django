from pydoc import describe
from ssl import create_default_context
from django.db import models

# Create your models here.


# class Settings(models.Model):
#     theme_color = models.CharField(max_length=100, default='#BD5D38')
#     theme_color_dark = models.CharField(max_length=100, default='#BD5D38')


class About(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/profile/')
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    describe_yourself = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Experience(models.Model):
    role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    from_month = models.CharField(max_length=50)
    to_month = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role + ' at ' + self.company_name


class Education(models.Model):
    degree_chocies = (
        ('B.Sc', 'B.Sc'),
        ('M.Sc', 'M.Sc'),
        ('B.A', 'B.A'),
        ('M.A', 'M.A'),
        ('B.Com', 'B.Com'),
        ('M.Com', 'M.Com'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('B.Arch', 'B.Arch'),
        ('M.Arch', 'M.Arch'),
        ('B.Ams', 'B.Ams'),
        ('M.Ams', 'M.Ams'),
        ('B.Pharma', 'B.Pharma'),
        ('M.Pharma', 'M.Pharma'),
        ('B.Sc.Engg', 'B.Sc.Engg'),
        ('M.Sc.Engg', 'M.Sc.Engg'),
        ('B.Sc.Engg', 'B.Sc.Engg'),
    )
    branch_choices = (
        ('Computers Science Engineering(CSE)',
         'Computers Science Engineering(CSE)'),
        ('Electronics and Communication(ECE)',
         'Electronics and Communication(ECE)'),
        ('Electrical and Electronics(EEE)',
         'Electrical and Electronics(EEE)'),
        ('ME', 'ME'),
        ('CE', 'CE'),
        ('CIVIL ENGINEERING', 'CIVIL ENGINEERING'),
        ('MECH ENGINEERING', 'MECH ENGINEERING'),
        ('PHYSICS', 'PHYSICS'),
        ('CHEMISTRY', 'CHEMISTRY'),
        ('MATHEMATICS', 'MATHEMATICS'),
        ('PHYSICAL', 'PHYSICAL'),
        ('BIOLOGY', 'BIOLOGY'),
        ('MUSIC', 'MUSIC'),
        ('PHILOSOPHY', 'PHILOSOPHY'),
        ('SOCIAL', 'SOCIAL'),
        ('COMPUTER', 'COMPUTER'),
        ('ENGLISH', 'ENGLISH'),
        ('HISTORY', 'HISTORY'),
        ('GEOGRAPHY', 'GEOGRAPHY'),
        ('ARTS', 'ARTS'),
        ('SCIENCE', 'SCIENCE'),
        ('OTHERS', 'OTHERS'),
    )
    college_name = models.CharField(max_length=100)
    degree = models.CharField(choices=degree_chocies, max_length=100)
    branch = models.CharField(choices=branch_choices, max_length=100)
    GPA = models.CharField(max_length=10)
    from_month = models.CharField(max_length=50)
    to_month = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.college_name + ' - ' + self.degree


class Awards(models.Model):
    award_name = models.CharField(max_length=100)
    awarded_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.award_name


class Skill(models.Model):
    skill_level_choices = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )
    skill_name_choices = (
        ('fab fa-java', 'Java'),
        ('fab fa-python', 'Python'),
        ('fab fa-php', 'PHP'),
        ('fab fa-html5', 'HTML'),
        ('fab fa-css3-alt', 'CSS'),
        ('fab fa-js-square', 'JavaScript'),
        ('fab fa-bootstrap', 'Bootstrap'),
        ('fab fa-angular', 'Angular'),
        ('fab fa-react', 'React'),
        ('fab fa-node-js', 'Node'),
        ('fab fa-aws', 'AWS'),
        ('fab fa-git', 'Git'),
        ('fab fa-github', 'GitHub'),
        ('fab fa-gitlab', 'GitLab'),
        ('fab fa-bitbucket', 'BitBucket'),
        ('fab fa-sass', 'Sass'),
        ('fab fa-less', 'LESS'),
        ('fab fa-wordpress', 'WordPress'),
        ('fab fa-gulp', 'Gulp'),
        ('fab fa-grunt', 'Grunt'),
        ('fab fa-npm', 'NPM'),
        ('fab fa-jekyll', 'Jekyll'),
        ('fab fa-digital-ocean', 'Digital Ocean'),
        ('fab fa-docker', 'Docker'),
        ('fab fa-figma', 'Figma'),
        ('fab fa-jenkins', 'Jenkins'),
        ('fab fa-jira', 'Jira'),
        ('fab fa-joomla', 'Joomla'),
        ('fab fa-laravel', 'Laravel'),
        ('fab fa-linode', 'Linode'),
        ('fab fa-linux', 'Linux'),
        ('fab fa-markdown', 'Markdown'),
        ('fas fa-unity', 'Unity'),
    )
    skill_name = models.CharField(choices=skill_name_choices, max_length=100)
    skill_level = models.CharField(choices=skill_level_choices, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill_name


class Workflow(models.Model):
    workflow_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.workflow_name


class Interests(models.Model):
    interests_name = models.CharField(max_length=100)
    interests_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.interests_name
