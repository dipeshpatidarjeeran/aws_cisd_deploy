from django.test import TestCase
import unittest
import subprocess
from .models import Student
from django.urls import reverse

class CodeIndentationTestCase(TestCase):

    def setUp(self):
        # Create a test student for use in the tests
        self.student = Student.objects.create(
            name='John Doe',
            roll=101,
            city='New York'
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_list.html')
        # self.assertContains(response, 'List of Students')
        self.assertContains(response, self.student.name)

    # def test_no_indentation_errors(self):
    #     # Define the paths to check for indentation errors
    #     project_path = '/home/thoughtwin/Django/excel_data_read'
    #     app_path = project_path + '/myapp --exclude=~/.env/newdb'
    #     # Run the 'flake8' command using subprocess
    #     process = subprocess.run(
    #         ['flake8', '--exclude=venv,migrations', app_path],
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE,
    #         text=True,
    #     )
    #     print(f"****************************Indentation errors found:\n{process.stderr}")
    #     # Assert that the return code is 0 (no errors)
    #     self.assertEqual(process.returncode, 0, msg=f"Indentation errors found:\n{process.stderr}")