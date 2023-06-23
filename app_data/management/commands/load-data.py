import csv

from django.core.management import BaseCommand, CommandError, call_command

from app_auth.serializers import UserSerializer
from app_course.serializers import CourseSerializer


def format_course(course_dict):
    course_dict["start_date"] = "2020-12-12"
    course_dict["end_date"] = "2021-12-12"
    return course_dict


class Command(BaseCommand):
    serializer_list = [
        {"serializer": UserSerializer, "file_path": "users.csv", "formatter": None},
        {
            "serializer": CourseSerializer,
            "file_path": "courses.csv",
            "formatter": format_course,
        },
    ]
    counter = 0

    def load_data(self, serializer, file_path: str, formatter):
        f = csv.DictReader(
            open(f"./lms_backend/dummydata/{file_path}", "r"), delimiter=","
        )
        self.stdout.write(f"Creating data using {serializer.__name__}: ", ending="")
        for i in f:
            if formatter is not None:
                i = formatter(i)
            x = serializer(data=i)
            if x.is_valid():
                x.save()
                self.counter += 1
                self.stdout.write(f"{x.data['id']} ", ending="")

            else:
                raise CommandError(
                    f"Validation error, check your dummy data. {x.errors}"
                )
        self.stdout.write(f"Complete.", ending="\n\n")

    def handle(self, *args, **options):
        call_command("flush", "--verbosity=1")
        for i in self.serializer_list:
            self.load_data(i["serializer"], i["file_path"], i["formatter"])
        self.stdout.write(
            self.style.SUCCESS(f"Successfully inserted {self.counter} rows.")
        )
