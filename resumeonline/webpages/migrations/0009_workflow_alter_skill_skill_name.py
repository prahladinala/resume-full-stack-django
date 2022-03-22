# Generated by Django 4.0.3 on 2022-03-20 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0008_interests_skill_alter_education_branch_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(choices=[('fab fa-java', 'Java'), ('fab fa-python', 'Python'), ('fab fa-php', 'PHP'), ('fab fa-html5', 'HTML'), ('fab fa-css3-alt', 'CSS'), ('fab fa-js-square', 'JavaScript'), ('fab fa-bootstrap', 'Bootstrap'), ('fab fa-angular', 'Angular'), ('fab fa-react', 'React'), ('fab fa-node-js', 'Node'), ('fab fa-aws', 'AWS'), ('fab fa-git', 'Git'), ('fab fa-github', 'GitHub'), ('fab fa-gitlab', 'GitLab'), ('fab fa-bitbucket', 'BitBucket'), ('fab fa-sass', 'Sass'), ('fab fa-less', 'LESS'), ('fab fa-wordpress', 'WordPress'), ('fab fa-gulp', 'Gulp'), ('fab fa-grunt', 'Grunt'), ('fab fa-npm', 'NPM'), ('fab fa-jekyll', 'Jekyll'), ('fab fa-digital-ocean', 'Digital Ocean'), ('fab fa-docker', 'Docker'), ('fab fa-figma', 'Figma'), ('fab fa-jenkins', 'Jenkins'), ('fab fa-jira', 'Jira'), ('fab fa-joomla', 'Joomla'), ('fab fa-laravel', 'Laravel'), ('fab fa-linode', 'Linode'), ('fab fa-linux', 'Linux'), ('fab fa-markdown', 'Markdown'), ('fas fa-unity', 'Unity')], max_length=100),
        ),
    ]
