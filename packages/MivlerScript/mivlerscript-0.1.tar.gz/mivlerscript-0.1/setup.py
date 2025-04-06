import setuptools
from setuptools import setup, find_packages
import os
import shutil


# Класс для выполнения действий после установки
class PostInstallCommand(setuptools.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Путь к шаблону в установленном пакете
        template_path = os.path.join(os.path.dirname(__file__), "MivlerScript", "templates", "main.py")
        # Куда копируем (текущая директория)
        dest_path = os.path.join(os.getcwd(), "main.py")

        # Копируем файл
        shutil.copy2(template_path, dest_path)
        print(f"Файл main.py создан в {dest_path}!")


setup(
    name="MivlerScript",
    version="0.1",
    packages=find_packages(),
    cmdclass={
        "install": PostInstallCommand,
    },
)