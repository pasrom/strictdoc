import filecmp
import os
import shutil

from seleniumbase import BaseCase

from tests.end2end.server import SDocTestServer

path_to_this_test_file_folder = os.path.dirname(os.path.abspath(__file__))


class Test_UC12_T02_MoveFieldUp(BaseCase):
    def test_01(self):
        path_to_sandbox = os.path.join(
            path_to_this_test_file_folder, ".sandbox"
        )

        test_server = SDocTestServer.create(path_to_sandbox)
        shutil.copyfile(
            os.path.join(path_to_this_test_file_folder, "document.sdoc"),
            os.path.join(path_to_sandbox, "document.sdoc"),
        )

        test_server.run()

        self.open(test_server.get_host_and_port())

        self.assert_text("Document 1")
        self.assert_text("PROJECT INDEX")

        self.click_xpath('//*[@data-testid="tree-file-link"]')
        self.assert_text_visible("Requirement title")

        self.click_xpath('(//*[@data-testid="document-edit-grammar-action"])')

        self.click_xpath(
            "(//*[@data-testid="
            '"form-move-up-document_grammar[CUSTOM_FIELD]-field-action"])'
        )

        self.click_xpath('//*[@data-testid="form-submit-action"]')
        self.assert_element_not_present('[data-testid="form-submit-action"]')

        assert os.path.exists(os.path.join(path_to_sandbox, "document.sdoc"))
        assert filecmp.cmp(
            os.path.join(path_to_sandbox, "document.sdoc"),
            os.path.join(
                path_to_this_test_file_folder, "document.expected.sdoc"
            ),
        )
