from django.db import models

# Create your models here.
class User(models.Model):
    "用户"
    username=models.IntegerField(verbose_name="账号",unique=True)
    password=models.CharField(verbose_name="密码",max_length=65)
    collage_choice={
        (1,"人文与新媒体学院"),
        (2,"外国语学院"),
        (3,"艺术学院"),
        (4,"教育与体育学院"),
        (5,"经济与管理学院"),
        (6,"法学院"),
        (7,"马克思主义学院"),
        (8,"信息与数学学院"),
        (9,"物理与光电工程学院"),
        (10,"化学与环境工程学院"),
        (11,"生命科学学院"),
        (12,"机械工程学院"),
        (13,"电子信息学院"),
        (14,"计算机科学学院"),
        (15,"城市建设学院"),
        (16,"资源与环境学院"),
        (17,"地球物理与石油资源学院"),
        (18,"地球科学学院"),
        (19,"石油工程学院"),
        (20,"农学院"),
        (21,"园艺园林学院"),
        (22,"动物科学学院"),
        (23,"医学部"),
        (24,"第一临床医学院"),
        (25,"第二临床医学院"),
        (26,"艺术与传媒学院"),
        (27,"教师教育学院"),
    }
    collage=models.SmallIntegerField(verbose_name="学院",choices=collage_choice)
    grade_choice={
        (1,"2019级"),
        (2,"2020级"),
        (3, "2021级"),
        (4, "2022级"),
    }
    grade=models.SmallIntegerField(verbose_name="年级",choices=grade_choice)

    pass
class len(models.Model):
    lenname=models.ForeignKey(verbose_name="借阅者",to="User",to_field="username",on_delete=models.CASCADE)
    lentime=models.DateField(verbose_name="借阅时间")