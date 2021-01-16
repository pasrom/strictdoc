from jinja2 import Environment, PackageLoader

from strictdoc.export.html.document_type import DocumentType


class DocumentTableHTMLGenerator:
    env = Environment(
        loader=PackageLoader("strictdoc", "export/html/templates")
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(document, traceability_index, markup_renderer, link_renderer):
        output = ""

        template = DocumentTableHTMLGenerator.env.get_template(
            "single_document_table/document.jinja.html"
        )

        output += template.render(
            document=document,
            traceability_index=traceability_index,
            renderer=markup_renderer,
            link_renderer=link_renderer,
            document_type=DocumentType.table(),
        )

        return output
