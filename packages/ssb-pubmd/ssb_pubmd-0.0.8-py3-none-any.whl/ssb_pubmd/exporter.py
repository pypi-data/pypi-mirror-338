import json
import os

import nbformat
import requests
from nbformat import NotebookNode


class _Exporter:
    """Helper class for exporting notebook content."""

    ID_KEY = "_id"

    def __init__(self, post_url: str) -> None:
        self.post_url: str = post_url
        self.notebook_folder: str = ""
        self.notebook_filename: str = ""

    @property
    def parent_folder(self) -> str:
        """The parent folder path, defaults to current working directory."""
        if self.notebook_folder:
            return self.notebook_folder
        else:
            return os.getcwd()

    @property
    def notebook_path(self) -> str:
        """The absolute path of the notebook file."""
        return os.path.join(self.parent_folder, self.notebook_filename)

    @property
    def basename(self) -> str:
        """The name of the notebook file without extension."""
        return os.path.splitext(self.notebook_filename)[0]

    @property
    def data_path(self) -> str:
        """The absolute path of the file to store data returned from the CMS."""
        return os.path.join(self.parent_folder, self.basename + ".json")

    @property
    def display_name(self) -> str:
        """Generate a display name for the content."""
        return self.basename.replace("_", " ").title()

    def _save_content_id(self, content_id: str) -> None:
        """Saves the content id to the data file."""
        filename = self.data_path
        with open(filename, "w") as file:
            json.dump({self.ID_KEY: content_id}, file)

    def _get_content_id(self) -> str:
        """Returns the content id from the data file if it exists, otherwise an empty string."""
        content_id = ""

        filename = self.data_path
        if os.path.exists(filename):
            with open(filename) as file:
                content_id = json.load(file)[self.ID_KEY]
        return content_id

    def _read_notebook(self) -> NotebookNode:
        """Reads the notebook file and returns its content."""
        return nbformat.read(self.notebook_path, as_version=nbformat.NO_CONVERT)  # type: ignore

    def _get_content_from_notebook(self) -> str:
        """Extracts all markdown cells from the notebook and returns it as a merged string."""
        notebook = self._read_notebook()

        markdown_cells = []
        for cell in notebook.cells:
            if cell.cell_type == "markdown":
                markdown_cells.append(cell.source)

        markdown_content = "\n\n".join(markdown_cells)

        return markdown_content

    def _request_data(self) -> dict[str, str]:
        """Prepares the request data to be sent to the CMS post_url."""
        return {
            "_id": self._get_content_id(),
            "displayName": self.display_name,
            "markdown": self._get_content_from_notebook(),
        }

    def _send_request(self) -> str:
        """Sends the request to the CMS endpoint and returns the content id from the response."""
        response = requests.post(
            self.post_url,
            data=self._request_data(),
        )
        content_id = response.json()[self.ID_KEY]
        return content_id  # type: ignore

    def set_notebook(self, notebook_filename: str, notebook_folder: str) -> None:
        """Sets the notebook filename and notebook folder."""
        self.notebook_filename = notebook_filename
        self.notebook_folder = notebook_folder

    def export(self) -> str:
        """Main method to export the notebook content to the CMS post_url."""
        content_id = self._send_request()
        self._save_content_id(content_id)
        return content_id


def notebook_to_cms(
    post_url: str,
    notebook_filename: str,
    notebook_folder: str = "",
) -> str:
    r"""Sends all the markdown content of a notebook to a CMS endpoint.

    The CMS endpoint must satisfy two constraints:

    -   It must accept a post request with fields *_id*, *displayName* and *markdown*.
    -   The response body must have a key *_id* whose value should be
        a unique string identifier of the content.

    Creating and updating content is handled in the following way:

    -   On the first request, an empty string is sent as *id*.
    -   If the request succeeds, the value of *_id* (in the response) is stored in a JSON file
        (created in the same directory as the notebook file).
    -   On subsequent requests, the stored value is sent as *id*.

    Args:
        post_url (str): The URL of the CMS endpoint.
        notebook_filename (str): The name of the notebook file, e.g. `"my_notebook.ipynb"`.
        notebook_folder (str): Sets a custom notebook folder (as absolute path) containing the notebook file.
            If not set, the current folder is used.

    Returns:
        str: The identifier of the content returned by the CMS endpoint.
    """
    exporter = _Exporter(post_url)
    exporter.set_notebook(notebook_filename, notebook_folder)
    return exporter.export()
