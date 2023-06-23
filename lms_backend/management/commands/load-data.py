import csv

from django.core.management import BaseCommand, CommandError, call_command

from app_auth.serializers import UserSerializer


class Command(BaseCommand):
    serializer_list = [
        {"serializer": UserSerializer, "file_path": "users.csv"},
    ]
    counter = 0

    def load_data(self, serializer, file_path: str):
        f = csv.DictReader(
            open(f"./lms_backend/dummydata/{file_path}", "r"), delimiter=","
        )
        self.stdout.write(f"Creating data using {serializer.__name__}: ", ending="")
        for i in f:
            x = serializer(data=i)
            if x.is_valid():
                x.save()
                self.counter += 1
                self.stdout.write(f"{i['id']} ", ending="")

            else:
                raise CommandError(
                    f"Validation error, check your dummy data. {x.errors}"
                )
        self.stdout.write(f"Complete.", ending="\n\n")

    def handle(self, *args, **options):
        call_command("flush", "--verbosity=1")
        for i in self.serializer_list:
            self.load_data(i["serializer"], i["file_path"])
        self.stdout.write(
            self.style.SUCCESS(f"Successfully inserted {self.counter} rows.")
        )
