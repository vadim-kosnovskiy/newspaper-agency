from django.test import TestCase

from content.forms import RedactorCreationForm


class FormsTests(TestCase):

    def test_redactor_creation_form_years_of_experience(self):
        form_data = {
            "username": "testusername",
            "password1": "TESTpassword123",
            "password2": "TESTpassword123",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 22,
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
