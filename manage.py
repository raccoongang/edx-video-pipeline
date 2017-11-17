#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VEDA.settings.production')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)




# CREATE USER 'pipeline001'@'localhost'  IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON pipeline.* TO 'pipeline001'@'localhost'
# db name pipeline
# CREATE DATABASE pipeline;

