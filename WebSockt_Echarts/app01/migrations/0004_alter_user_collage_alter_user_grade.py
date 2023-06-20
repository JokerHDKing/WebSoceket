# Generated by Django 4.1.6 on 2023-02-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0003_alter_user_collage_alter_user_grade_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="collage",
            field=models.SmallIntegerField(
                choices=[
                    (9, "物理与光电工程学院"),
                    (26, "艺术与传媒学院"),
                    (20, "农学院"),
                    (19, "石油工程学院"),
                    (14, "计算机科学学院"),
                    (1, "人文与新媒体学院"),
                    (17, "地球物理与石油资源学院"),
                    (13, "电子信息学院"),
                    (18, "地球科学学院"),
                    (25, "第二临床医学院"),
                    (23, "医学部"),
                    (11, "生命科学学院"),
                    (12, "机械工程学院"),
                    (24, "第一临床医学院"),
                    (8, "信息与数学学院"),
                    (5, "经济与管理学院"),
                    (16, "资源与环境学院"),
                    (4, "教育与体育学院"),
                    (21, "园艺园林学院"),
                    (7, "马克思主义学院"),
                    (3, "艺术学院"),
                    (6, "法学院"),
                    (15, "城市建设学院"),
                    (10, "化学与环境工程学院"),
                    (27, "教师教育学院"),
                    (22, "动物科学学院"),
                    (2, "外国语学院"),
                ],
                verbose_name="学院",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="grade",
            field=models.SmallIntegerField(
                choices=[(1, "2019级"), (4, "2022级"), (2, "2020级"), (3, "2021级")],
                verbose_name="年级",
            ),
        ),
    ]
