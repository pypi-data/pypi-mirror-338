import json
import os

import nbformat
import requests
from nbformat import NotebookNode


class _Exporter:
    """Helper class for exporting markdown-based content."""

    def __init__(self, endpoint: str) -> None:
        self.endpoint: str = endpoint
        self.notebook_folder: str = ""
        self.notebook_filename: str = ""
        self.content_id: str = ""

    def _set_working_directory(self) -> None:
        """Set the working directory to the notebook folder."""
        if self.notebook_folder:
            os.chdir(self.notebook_folder)
        else:
            os.chdir(os.getcwd())

    def _get_basename(self) -> str:
        """Returns the name of the notebook file without extension."""
        return os.path.splitext(self.notebook_filename)[0]

    def _get_display_name(self) -> str:
        """Generate a display name to send to the CMS endpoint."""
        return self._get_basename().replace("_", " ").title()

    def _get_data_filename(self) -> str:
        """Returns the data filename to store the content id returned from the CMS."""
        return self._get_basename() + ".json"

    def _get_content_id(self) -> str:
        """Get the content id from the JSON file if it exists."""
        content_id = ""
        data_filename = self._get_data_filename()
        if os.path.exists(data_filename):
            with open(data_filename) as file:
                content_id = json.load(file)["_id"]
        return content_id

    def _read_notebook(self) -> NotebookNode:
        """Reads the notebook file and returns its content."""
        return nbformat.read(self.notebook_filename, as_version=nbformat.NO_CONVERT)  # type: ignore

    def _get_content_from_notebook(self) -> str:
        """Extracts all markdown cells from the notebook and returns it as a merged string."""
        notebook = self._read_notebook()
        markdown_content = ""
        for cell in notebook.cells:
            if cell.cell_type == "markdown":
                markdown_content += cell.source + "\n\n"
        return markdown_content

    def _prepare_request_data(self) -> dict[str, str]:
        """Prepares the request data to be sent to the CMS endpoint."""
        return {
            "_id": self._get_content_id(),
            "displayName": self._get_display_name(),
            "markdown": self._get_content_from_notebook(),
        }

    def _prepare_headers(self) -> dict[str, str]:
        """Prepares the headers for the request."""
        return {"Content-Type": "application/json"}

    def _send_request(self) -> None:
        """Sends the request to the CMS endpoint and returns the content id."""
        data = self._prepare_request_data()
        response = requests.post(
            self.endpoint,
            data=json.dumps(data),
            headers=self._prepare_headers(),
        )
        self.content_id = response.json()["_id"]

    def _save_content_id(self) -> None:
        """Saves the content id to a JSON file."""
        with open(self._get_data_filename(), "w") as file:
            json.dump({"_id": self.content_id}, file)

    def set_notebook(self, notebook_filename: str, notebook_folder: str) -> None:
        """Uses the notebook_filename and working directory."""
        self.notebook_filename = notebook_filename
        self.notebook_folder = notebook_folder
        self._set_working_directory()

    def export(self) -> str:
        """Main method to export the notebook content to the CMS endpoint."""
        self._send_request()
        self._save_content_id()
        return self.content_id


def notebook_to_cms(
    notebook_filename: str,
    endpoint: str,
    notebook_folder: str = "",
) -> str:
    r"""Sends all the markdown content of a notebook to a CMS endpoint.

    The CMS endpoint must satisfy two constraints:

    -   It must accept a post request with fields *id*, *displayName* and *markdown*.
    -   The response body must have a key *_id* whose value should be
        a unique string identifier of the content.

    Creating and updating content is handled in the following way:

    -   On the first request, an empty string is sent as *id*.
    -   If the request succeeds, the value of *_id* (in the response) is stored in a JSON file
        (created in the same directory as the notebook file).
    -   On subsequent requests, the stored value is sent as *id*.

    Args:
        notebook_filename (str): The name of the notebook file, e.g. `"my_notebook.ipynb"`.
        endpoint (str): The URL of the CMS endpoint.
        notebook_folder (str): Sets a custom notebook folder (as absolute path) containing the notebook file.
            If not set, the current folder is used.

    Returns:
        str: The identifier of the content returned by the CMS endpoint.
    """
    exporter = _Exporter(endpoint)
    exporter.set_notebook(notebook_filename, notebook_folder)
    return exporter.export()
