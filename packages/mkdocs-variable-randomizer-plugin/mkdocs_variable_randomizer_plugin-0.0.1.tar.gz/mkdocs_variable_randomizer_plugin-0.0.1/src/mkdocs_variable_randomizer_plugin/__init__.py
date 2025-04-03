# builtin

import os
from html import escape
from pathlib import PurePath
import random
import re
from typing import Optional
import urllib.parse
# pip
from mkdocs.config.base import Config
from mkdocs.config.config_options import Type, ListOfItems
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin, get_plugin_logger
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

LOGGER = get_plugin_logger(__name__)
SCRIPT = """
<script>
const cached_names = new Map();

const generateRandomVariableName = () => {
    const randomValues = new Uint8Array(5);
    window.crypto.getRandomValues(randomValues);
    const binaryString = String.fromCharCode.apply(null, randomValues);
    return btoa(binaryString).replace(/[0-9+/=]/g, "");
}

const isValidName = (new_value) => {
    // Ensure that there are no duplicate entries
    if ([...cached_names.values()].includes(new_value)) {
        return false;
    }

    // check against empty name
    if (!new_value) {
        return false;
    }

    return true;
}

const replacePlaceholder = (elem) => {
    const var_name = elem.getAttribute("randomize_variable");
    let new_value = cached_names.get(var_name);
    if (new_value === undefined) {
        do {
            new_value = generateRandomVariableName();
        } while (!isValidName(new_value));

        cached_names.set(var_name, new_value);
    }
    elem.innerText = new_value;
};

window.addEventListener("load", () => {
    console.debug("Replacing variables with random names");
    document.querySelectorAll("span[randomize_variable]").forEach(replacePlaceholder); 
});
</script>
"""

class VariableRandomizerConfig(Config):
    search_regex = Type(str, default="rand_[a-zA-Z_]+")

class VariableRandomizerPlugin(BasePlugin[VariableRandomizerConfig]):    
    def on_config(self, config: MkDocsConfig):
        self.search_regex = re.compile(self.config.search_regex)

    def on_page_content(self, html: str, page: Page, config: MkDocsConfig, files: Files) -> str:
        og_html = str(html)
        matches = self.search_regex.finditer(html)
        for match in reversed(list(matches)):
            start, end = match.span()
            old_value = match.group(0)
            replace_value = f'<span randomize_variable="{escape(old_value)}">{escape(old_value)}</span>'
            html = html[:start] + replace_value + html[end:]

        # If we replaced something with an placeholder, we need to add the script to replace the placeholders
        if og_html != html:
            html += SCRIPT

        return html

