"""
Custom django command to wait for database to fully load before running backend services
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for database to be ready to retry connection"""
    
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Waiting for database to finish configuring ..."))
        is_db_up = False
        
        while is_db_up is False:
            try:
                self.check(databases=["default"])
                is_db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.WARNING(
                    "Database still configuring, waiting 1 second before trying again ..."
                ))
                time.sleep(1)
                
        self.stdout.write(self.style.SUCCESS("Database is now ready."))
