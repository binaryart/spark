from shutil import rmtree

from spark.core.create import CreateCommand, CreateUseCase
from test import expected_folder, assert_folder, template_folder, tmp_folder


class TestCreate:
    def setup(self):
        self._tmp_folder = tmp_folder()
        self._use_case = CreateUseCase()

    def teardown(self):
        rmtree(self._tmp_folder, ignore_errors=True)

    def test_create_simple(self):
        create_command = CreateCommand(
            template=template_folder("simple_template"), output=self._tmp_folder
        )
        self._use_case.execute(create_command)
        assert_folder(expected_folder("create_simple"), self._tmp_folder)