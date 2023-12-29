from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

from tests.end2end.helpers.screens.document.form_edit_grammar import (
    Form_EditGrammar,
)
from tests.end2end.helpers.screens.screen import Screen


class Screen_Document(Screen):  # pylint: disable=invalid-name
    def __init__(self, test_case: BaseCase) -> None:
        assert isinstance(test_case, BaseCase)
        super().__init__(test_case)

    # overridden for Screen_Document

    def assert_on_screen_document(self) -> None:
        super().assert_on_screen("document")

    def assert_empty_document(self) -> None:
        super().assert_empty_view("document-root-placeholder")

    def assert_not_empty_document(self) -> None:
        super().assert_not_empty_view("document-root-placeholder")

    def assert_target_by_anchor(self, anchor) -> None:
        # check if the link was successfully clicked
        # and that the target is highlighted
        targeted_anchor = f"sdoc-anchor[id='{anchor}']:target"
        self.test_case.assert_element_present(targeted_anchor)

    # Actions on the page

    def do_export_reqif(self) -> None:
        self.test_case.click_xpath(
            '(//*[@data-testid="document-export-reqif-action"])'
        )

    # Open forms

    def do_open_modal_form_edit_grammar(self) -> Form_EditGrammar:
        self.test_case.assert_element_not_present("//sdoc-modal", by=By.XPATH)
        self.test_case.click_xpath(
            '(//*[@data-testid="document-edit-grammar-action"])'
        )
        self.test_case.assert_element(
            "//sdoc-modal",
            by=By.XPATH,
        )
        return Form_EditGrammar(self.test_case)

    def do_drag_first_toc_node_to_the_second(self) -> None:
        first_toc_node = '(//li[@draggable="true"])[1]'
        second_toc_node = '(//li[@draggable="true"])[2]'
        self.test_case.drag_and_drop(first_toc_node, second_toc_node)
