"""
PDX-License-Identifier: Apache-2.0
Copyright Contributors to the ODPi Egeria project.

This module contains an initial version of the glossary_browser omvs module. There are additional methods that will be
added in subsequent versions of the glossary_omvs module.

"""

import asyncio
from datetime import datetime

from pyegeria import NO_GLOSSARIES_FOUND, NO_CATEGORIES_FOUND, NO_TERMS_FOUND
import json
from pyegeria._client import Client
from pyegeria._validators import validate_guid, validate_name, validate_search_string
from pyegeria.utils import body_slimmer
from pyegeria._globals import NO_ELEMENTS_FOUND, NO_CATALOGS_FOUND, NO_CATEGORIES_FOUND, NO_TERMS_FOUND
MD_SEPERATOR = "\n---\n\n"

class GlossaryBrowser(Client):
    """
    GlossaryBrowser is a class that extends the Client class. It provides methods to search and retrieve glossaries,
    terms and categories.

    Attributes:

        view_server: str
            The name of the View Server to connect to.
        platform_url : str
            URL of the server platform to connect to
        user_id : str
            The identity of the user calling the method - this sets a default optionally used by the methods
            when the user doesn't pass the user_id on a method call.
        user_pwd: str
            The password associated with the user_id. Defaults to None

    """

    def __init__(
        self,
        view_server: str,
        platform_url: str,
        user_id: str,
        user_pwd: str = None,
        token: str = None,
    ):
        self.view_server = view_server
        self.platform_url = platform_url
        self.user_pwd = user_pwd
        self.user_id = user_id
        self.g_browser_command_root: str

        Client.__init__(self, view_server, platform_url, user_id, user_pwd, token)


    def make_preamble(self, obj_type, search_string, output_format: str = 'MD')-> tuple[str, str | None]:
        """
        Creates a preamble string and an elements action based on the given object type, search string,
        and output format. The preamble provides a descriptive header based on the intent: To make a form,
        a report, or unadorned markdwon. The elements action specifies the action to be taken on the object type.

        Args:
            obj_type: The type of object being updated or reported on (e.g., "Product", "Category").
            search_string: The search string used to filter objects. Defaults to "All Terms" if None.
            output_format: A format identifier determining the output structure.
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report

        Returns:
            tuple: A tuple containing:
                - A string representing the formatted update or report preamble.
                - A string or None indicating the action description for the elements,
                  depending on the output format.
        """
        search_string = search_string if search_string else "All Elements"
        elements_action = "Update " + obj_type
        if output_format == "FORM":
            preamble = (f"\n# Update {obj_type} Form - created at {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                        f"\t {obj_type} found from the search string:  `{search_string}`\n\n")

            return preamble, elements_action
        elif output_format == "REPORT":
            elements_md = (f"# {obj_type} Report - created at {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                           f"\t{obj_type}  found from the search string:  `{search_string}`\n\n")
            elements_action = None
            return elements_md, elements_action

        else:
            return "\n", elements_action

    def make_md_attribute(self, attribute_name: str, attribute_value: str, output_type: str) -> str | None:
        output = ""
        attribute_value = attribute_value.strip() if attribute_value else ""
        attribute_title = attribute_name.title() if attribute_name else ""
        if output_type in ["FORM", "MD"]:
            output = f"## {attribute_title}\n{attribute_value}\n\n"
        elif output_type == "REPORT":
            if attribute_value:
                output = f"## {attribute_title}\n{attribute_value}\n\n"
        return output


    def generate_glossaries_md(self, elements: list | dict, search_string: str, output_format: str = 'MD')-> str:
        elements_md, elements_action = self.make_preamble(obj_type="Glossary", search_string=search_string,
                                                          output_format=output_format)
        if isinstance(elements, dict):
            elements = [elements]

        for element in elements:
            guid = element['elementHeader'].get("guid", None)
            properties = element['glossaryProperties']
            display_name = properties.get("displayName", None)
            description = properties.get("description", None)
            language = properties.get("language", None)
            usage = properties.get("usage", None)
            qualified_name = properties.get("qualifiedName", None)

            if output_format in ['FORM','MD']:
                elements_md += f"# {elements_action}\n\n"
                elements_md += f"## Glossary Name \n\n{display_name}\n\n"

            elif output_format == 'REPORT':
                elements_md += f"# Glossary Name: {display_name}\n\n"
            else:
                elements_md += f"## Glossary Name \n\n{display_name}\n\n"

            elements_md += self.make_md_attribute( "description", description, output_format)
            elements_md += self.make_md_attribute("language", language, output_format)
            elements_md += self.make_md_attribute("usage", usage, output_format)
            elements_md += self.make_md_attribute("qualified name", qualified_name, output_format)
            elements_md += self.make_md_attribute("GUID", guid, output_format)
            # elements_md += MD_SEPERATOR

        return elements_md

    def generate_terms_md(self, elements: list | dict, search_string: str, output_format: str = 'MD') -> str:
        elements_md, elements_action = self.make_preamble(obj_type="Term", search_string=search_string, output_format=output_format)
        if isinstance(elements, dict):
            elements = [elements]

        for element in elements:
            guid = element['elementHeader'].get("guid", None)
            element_properties = element['glossaryTermProperties']
            display_name = element_properties.get("displayName", None)
            summary = element_properties.get("summary", None)
            description = element_properties.get("description", None)
            examples = element_properties.get("examples", None)
            usage = element_properties.get("usage", None)
            pub_version = element_properties.get("publishfinVersionIdentifier", None)
            qualified_name = element_properties.get("qualifiedName", None)
            status = element['elementHeader'].get('status', None)

            glossary_guid = element['elementHeader'].get('classifications', [{}])[0].get('classificationProperties', {}).get('anchorGUID', None)
            glossary_qualified_name = self.get_glossary_by_guid(glossary_guid)['glossaryProperties']['qualifiedName']

            category_list_md = "\n"
            category_list = self.get_categories_for_term(guid)
            if type(category_list) is str and category_list == NO_CATEGORIES_FOUND:
                category_list_md = ['---']
            elif isinstance(category_list, list) and len(category_list) > 0:
                first_cat = True
                for category in category_list:
                    category_name = category["glossaryCategoryProperties"].get("qualifiedName", '---')
                    if first_cat:
                        category_list_md += f" {category_name}\n"
                        first_cat = False
                    else:
                        category_list_md += f", {category_name}\n"

            if output_format in ['FORM', 'MD']:
                elements_md += f"# {elements_action}\n\n"
                elements_md += f"## Term Name \n\n{display_name}\n\n"
            elif output_format == 'REPORT':
                elements_md += f"# Term Name: {display_name}\n\n"
            else:
                elements_md += f"## Term Name \n\n{display_name}\n\n"

            elements_md += self.make_md_attribute("summary", summary, output_format)
            elements_md += self.make_md_attribute("in glossary", glossary_qualified_name, output_format)
            elements_md += self.make_md_attribute( "categories", category_list_md, output_format)
            elements_md += self.make_md_attribute( "status", status, output_format)
            elements_md += self.make_md_attribute( "description", description, output_format)
            elements_md += self.make_md_attribute( "examples", examples, output_format)
            elements_md += self.make_md_attribute("usage", usage, output_format)
            elements_md += self.make_md_attribute("version", pub_version, output_format)
            elements_md += self.make_md_attribute("qualified name", qualified_name, output_format)
            elements_md += self.make_md_attribute("GUID", guid, output_format)
            elements_md += MD_SEPERATOR

        return elements_md

    def generate_categories_md(self, elements: list | dict, search_string: str, output_format: str = 'MD')-> str:
        elements_md, elements_action = self.make_preamble(obj_type="Categories", search_string=search_string,
                                                          output_format=output_format)
        if isinstance(elements, dict):
            elements = [elements]

        for element in elements:
            guid = element['elementHeader'].get("guid", None)
            properties = element['glossaryCategoryProperties']
            display_name = properties.get("displayName", None)
            description = properties.get("description", None)
            qualified_name = properties.get("qualifiedName", None)

            classification_props = element["elementHeader"]['classifications'][0].get('classificationProperties', None)
            glossary_qualified_name = '---'
            if classification_props is not None:
                glossary_guid = classification_props.get('anchorGUID', '---')
                glossary_qualified_name = (
                    self.get_glossary_by_guid(glossary_guid))['glossaryProperties']['qualifiedName']

            if output_format in ['FORM', 'MD']:
                elements_md += f"# {elements_action}\n\n"
                elements_md += f"## Category Name \n\n{display_name}\n\n"

            elif output_format == 'REPORT':
                elements_md += f"# Category Name: {display_name}\n\n"
            else:
                elements_md += f"## Category Name \n\n{display_name}\n\n"


            elements_md += self.make_md_attribute("description", description, output_format)
            elements_md += self.make_md_attribute("in glossary", glossary_qualified_name, output_format)
            elements_md += self.make_md_attribute("qualified name", qualified_name, output_format)
            elements_md += self.make_md_attribute("GUID", guid, output_format)
            elements_md += MD_SEPERATOR

        return elements_md

    #
    #       Get Valid Values for Enumerations
    #

    async def _async_get_glossary_term_statuses(self) -> [str]:
        """Return the list of glossary term status enum values. Async version.

        Parameters
        ----------


        Returns
        -------
        List[str]
            A list of glossary term statuses retrieved from the server.

        """

        url = (
            f"{self.platform_url}/servers/{self.view_server}"
            f"/api/open-metadata/glossary-browser/glossaries/terms/status-list"
        )

        response = await self._async_make_request("GET", url)
        return response.json().get("statuses", [])

    def get_glossary_term_statuses(self) -> [str]:
        """Return the list of glossary term status enum values.

        Parameters
        ----------


        Returns
        -------
        list of str
            A list of glossary term statuses. Each status is represented as a string.

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self._async_get_glossary_term_statuses())
        return response

    async def _async_get_glossary_term_rel_statuses(self) -> [str]:
        """Return the list of glossary term relationship status enum values.  These values are stored in a
        term-to-term, or term-to-category, relationship and are used to indicate how much the relationship should be
        trusted. Async version.

        Parameters
        ----------


        Returns
        -------
        List[str]
            A list of glossary term statuses retrieved from the server.

        """

        url = (
            f"{self.platform_url}/servers/{self.view_server}"
            f"/api/open-metadata/glossary-browser/glossaries/terms/relationships/status-list"
        )

        response = await self._async_make_request("GET", url)
        return response.json().get("statuses", [])

    def get_glossary_term_rel_statuses(self) -> [str]:
        """Return the list of glossary term relationship status enum values.  These values are stored in a
        term-to-term, or term-to-category, relationship and are used to indicate how much the relationship should be
        trusted.

        Parameters
        ----------


        Returns
        -------
        list of str
            A list of glossary term statuses. Each status is represented as a string.

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self._async_get_glossary_term_rel_statuses())
        return response

    async def _async_get_glossary_term_activity_types(self) -> [str]:
        """Return the list of glossary term activity type enum values. Async version.

        Parameters
        ----------


        Returns
        -------
        List[str]
            A list of glossary term statuses retrieved from the server.

        """

        url = (
            f"{self.platform_url}/servers/{self.view_server}"
            f"/api/open-metadata/glossary-browser/glossaries/terms/activity-types"
        )

        response = await self._async_make_request("GET", url)
        return response.json().get("types", [])

    def get_glossary_term_activity_types(self) -> [str]:
        """Return the list of glossary term activity type enum values.

        Parameters
        ----------


        Returns
        -------
        list of str
            A list of glossary term statuses. Each status is represented as a string.

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self._async_get_glossary_term_statuses())
        return response

    #
    #       Glossaries
    #

    async def _async_find_glossaries(
        self,
        search_string: str,
        effective_time: str = None,
        starts_with: bool = False,
        ends_with: bool = False,
        ignore_case: bool = False,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
        type_name: str = None,
        start_from: int = 0,
        page_size: int = None,
        output_format: str = 'JSON'
    ) -> list | str:
        """Retrieve the list of glossary metadata elements that contain the search string. Async version.
            The search string is located in the request body and is interpreted as a plain string.
            The request parameters, startsWith, endsWith and ignoreCase can be used to allow a fuzzy search.

        Parameters
        ----------
        search_string: str,
            Search string to use to find matching glossaries. If the search string is '*' then all glossaries returned.

        effective_time: str, [default=None], optional
            Effective time of the query. If not specified will default to any time. Time format is
            "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.
        starts_with : bool, [default=False], optional
            Starts with the supplied string.
        ends_with : bool, [default=False], optional
            Ends with the supplied string
        ignore_case : bool, [default=False], optional
            Ignore case when searching
        for_lineage : bool, [default=False], optional

        for_duplicate_processing : bool, [default=False], optional
        type_name: str, [default=None], optional
            An optional parameter indicating the subtype of the glossary to filter by.
            Values include 'ControlledGlossary', 'EditingGlossary', and 'StagingGlossary'
        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        output_format: str, default = 'JSON'
            Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report

        Returns
        -------
        List | str

        A list of glossary definitions active in the server.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """

        if page_size is None:
            page_size = self.page_size
        starts_with_s = str(starts_with).lower()
        ends_with_s = str(ends_with).lower()
        ignore_case_s = str(ignore_case).lower()
        for_lineage_s = str(for_lineage).lower()
        for_duplicate_processing_s = str(for_duplicate_processing).lower()

        validate_search_string(search_string)

        if search_string == "*":
            search_string = None

        body = {
            "class": "SearchStringRequestBody",
            "searchString": search_string,
            "effectiveTime": effective_time,
            "typeName": type_name,
        }
        body = body_slimmer(body)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"by-search-string?startFrom={start_from}&pageSize={page_size}&startsWith={starts_with_s}&"
            f"endsWith={ends_with_s}&ignoreCase={ignore_case_s}&forLineage={for_lineage_s}&"
            f"forDuplicateProcessing={for_duplicate_processing_s}"
        )

        response = await self._async_make_request("POST", url, body_slimmer(body))
        element = response.json().get("elementList", NO_GLOSSARIES_FOUND)
        if element == NO_GLOSSARIES_FOUND:
            return NO_GLOSSARIES_FOUND
        if output_format != 'JSON':  # return a simplified markdown representation
            return self.generate_glossaries_md(element, search_string, output_format)
        return response.json().get("elementList", NO_GLOSSARIES_FOUND)


    def find_glossaries(
        self,
        search_string: str,
        effective_time: str = None,
        starts_with: bool = False,
        ends_with: bool = False,
        ignore_case: bool = False,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
        type_name: str = None,
        start_from: int = 0,
        page_size: int = None,
        output_format: str = "JSON"
    ) -> list | str:
        """Retrieve the list of glossary metadata elements that contain the search string.
                The search string is located in the request body and is interpreted as a plain string.
                The request parameters, startsWith, endsWith and ignoreCase can be used to allow a fuzzy search.

        Parameters
        ----------
        search_string: str,
            Search string to use to find matching glossaries. If the search string is '*',
            then all glossaries returned.

        effective_time: str, [default=None], optional
            Effective time of the query. If not specified will default to any time. Time format is
            "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.
        starts_with : bool, [default=False], optional
            Starts with the supplied string.
        ends_with : bool, [default=False], optional
            Ends with the supplied string
        ignore_case : bool, [default=False], optional
            Ignore case when searching
        for_lineage : bool, [default=False], optional
             Indicates the search is for lineage.
        for_duplicate_processing : bool, [default=False], optional
        type_name: str, [default=None], optional
            An optional parameter indicating the subtype of the glossary to filter by.
            Values include 'ControlledGlossary', 'EditingGlossary', and 'StagingGlossary'
         start_from : int, [default=0], optional
             When multiple pages of results are available, the page number to start from.
         page_size: int, [default=None]
             The number of items to return in a single page. If not specified, the default will be taken from
             the class instance.
         output_format: str, default = 'JSON'
            Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report
        Returns
        -------
        List | str

        A list of glossary definitions active in the server.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_find_glossaries(
                search_string,
                effective_time,
                starts_with,
                ends_with,
                ignore_case,
                for_lineage,
                for_duplicate_processing,
                type_name,
                start_from,
                page_size,
                output_format
            )
        )

        return response

    async def _async_get_glossary_by_guid(
        self, glossary_guid: str, effective_time: str = None, output_format: str = "JSON"
    ) -> dict|str:
        """Retrieves information about a glossary
        Parameters
        ----------
            glossary_guid : str
                Unique idetifier for the glossary
            effective_time: str, optional
                Effective time of the query. If not specified will default to any time. Time format is
                "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
            output_format: str, default = 'JSON'
            Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report

        Returns
        -------
        dict | str
            if output format is JSON: The glossary definition associated with the glossary_guid
            if output format is MD: A markdown string with the same information.
        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """
        output_format = output_format.upper()
        validate_guid(glossary_guid)

        body = {
            "class": "EffectiveTimeQueryRequestBody",
            "effectiveTime" : effective_time
        }
        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"{glossary_guid}/retrieve"
        )
        response = await self._async_make_request("POST", url, body_slimmer(body))
        element = response.json().get("element", NO_GLOSSARIES_FOUND)
        if element == NO_GLOSSARIES_FOUND:
            return NO_GLOSSARIES_FOUND
        if output_format != 'JSON':  # return a simplified markdown representation
            return self.generate_glossaries_md(element, "GUID", output_format)
        return response.json().get("element", NO_GLOSSARIES_FOUND)


    def get_glossary_by_guid(
        self, glossary_guid: str, effective_time: str = None, output_format: str = "JSON"
    ) -> dict:
        """Retrieves information about a glossary
        Parameters
        ----------
            glossary_guid : str
                Unique idetifier for the glossary
            effective_time: str, optional
                Effective time of the query. If not specified will default to any time. Time format is
                "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
            output_format: str, default = 'JSON'
                Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report

        Returns
        -------
        dict
            The glossary definition associated with the glossary_guid

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_glossary_by_guid(glossary_guid, effective_time, output_format)
        )
        return response

    async def _async_get_glossaries_by_name(
        self,
        glossary_name: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> dict | str:
        """Retrieve the list of glossary metadata elements with an exactly matching qualified or display name.
            There are no wildcards supported on this request.

        Parameters
        ----------
        glossary_name: str,
            Name of the glossary to be retrieved
        effective_time: datetime, [default=None], optional
            Effective time of the query. If not specified will default to any effective time. Time format is
            "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.
        start_from: int, [default=0], optional
             When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.

        Returns
        -------
        None

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action
        ConfigurationErrorException
          Raised when configuration parameters passed on earlier calls turn out to be
          invalid or make the new call invalid.
        """

        if page_size is None:
            page_size = self.page_size
        validate_name(glossary_name)

        if effective_time is None:
            body = {"name": glossary_name}
        else:
            body = {"name": glossary_name, "effectiveTime": effective_time}

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"by-name?startFrom={start_from}&pageSize={page_size}"
        )

        response = await self._async_make_request("POST", url, body)
        return response.json().get("elementList", "No glossaries found")

    def get_glossaries_by_name(
        self,
        glossary_name: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> dict | str:
        """Retrieve the list of glossary metadata elements with an exactly matching qualified or display name.
            There are no wildcards supported on this request.

        Parameters
        ----------
        glossary_name: str,
            Name of the glossary to be retrieved
        effective_time: datetime, [default=None], optional
            Effective time of the query. If not specified will default to any effective time.

            If not provided, the server name associated with the instance is used.
        start_from: int, [default=0], optional
            When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.

        Returns
        -------
        None

        Raises
        ------
        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action
        ConfigurationErrorException
          Raised when configuration parameters passed on earlier calls turn out to be
          invalid or make the new call invalid.
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_glossaries_by_name(
                glossary_name, effective_time, start_from, page_size
            )
        )
        return response

    #
    # Glossary Categories
    #

    async def _async_get_glossary_for_category(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
    ) -> dict | str:
        """Retrieve the glossary metadata element for the requested category.  The optional request body allows you to
        specify that the glossary element should only be returned if it was effective at a particular time.

        Parameters
        ----------
        glossary_category_guid: str,
            Unique identifier for the glossary category.
        effective_time: datetime, [default=None], optional
            Effective time of the query. If not specified will default to any effective time. Time format is
            "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.

        Returns
        -------
        A dict structure with the glossary metadata element for the requested category.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action
        ConfigurationErrorException
          Raised when configuration parameters passed on earlier calls turn out to be
          invalid or make the new call invalid.
        """

        body = {
            "class": "EffectiveTimeQueryRequestBody",
            "effectiveTime": effective_time,
        }

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"for-category/{glossary_category_guid}/retrieve"
        )

        response = await self._async_make_request("POST", url, body)
        return response.json().get("elementList", "No categories found")

    def get_glossary_for_category(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
    ) -> dict | str:
        """Retrieve the glossary metadata element for the requested category.  The optional request body allows you to
        specify that the glossary element should only be returned if it was effective at a particular time.

        Parameters
        ----------
        glossary_category_guid: str,
            Unique identifier for the glossary category.
        effective_time: datetime, [default=None], optional
            Effective time of the query. If not specified will default to any effective time. Time format is
            "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.

        Returns
        -------
        A dict structure with the glossary metadata element for the requested category.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action
        ConfigurationErrorException
          Raised when configuration parameters passed on earlier calls turn out to be
          invalid or make the new call invalid.
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_glossary_for_category(
                glossary_category_guid, effective_time
            )
        )
        return response

    async def _async_find_glossary_categories(
        self,
        search_string: str,
        effective_time: str = None,
        starts_with: bool = False,
        ends_with: bool = False,
        ignore_case: bool = False,
        start_from: int = 0,
        page_size: int = None,
        output_format: str = "JSON"
    ) -> list | str:
        """Retrieve the list of glossary category metadata elements that contain the search string.
            The search string is located in the request body and is interpreted as a plain string.
            The request parameters, startsWith, endsWith and ignoreCase can be used to allow a fuzzy search.
            Async version.

        Parameters
        ----------
        search_string: str,
            Search string to use to find matching glossaries. If the search string is '*' then all glossaries returned.

        effective_time: str, [default=None], optional
            Effective time of the query. If not specified will default to any time. Time format is
            "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.
        starts_with : bool, [default=False], optional
            Starts with the supplied string.
        ends_with : bool, [default=False], optional
            Ends with the supplied string
        ignore_case : bool, [default=False], optional
            Ignore case when searching
        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        output_format: str, default = 'JSON'
            Type of output to produce:
            JSON - output standard json
            MD - output standard markdown with no preamble
            FORM - output markdown with a preamble for a form
            REPORT - output markdown with a preamble for a report

        Returns
        -------
        List | str

        A list of glossary definitions active in the server.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """

        if page_size is None:
            page_size = self.page_size
        starts_with_s = str(starts_with).lower()
        ends_with_s = str(ends_with).lower()
        ignore_case_s = str(ignore_case).lower()

        validate_search_string(search_string)

        if search_string == "*":
            search_string = None

        body = {
            "class": "SearchStringRequestBody",
            "searchString": search_string,
            "effectiveTime": effective_time,
        }

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"categories/by-search-string?startFrom={start_from}&pageSize={page_size}&startsWith={starts_with_s}&"
            f"endsWith={ends_with_s}&ignoreCase={ignore_case_s}"
        )
        response = await self._async_make_request("POST", url, body_slimmer(body))
        element = response.json().get("elementList", NO_CATEGORIES_FOUND)
        if element == NO_CATEGORIES_FOUND:
            return NO_CATEGORIES_FOUND
        if output_format != 'JSON':  # return a simplified markdown representation
            return self.generate_categories_md(element, search_string, output_format)
        return response.json().get("elementList", NO_CATEGORIES_FOUND)






    def find_glossary_categories(
        self,
        search_string: str,
        effective_time: str = None,
        starts_with: bool = False,
        ends_with: bool = False,
        ignore_case: bool = False,
        start_from: int = 0,
        page_size: int = None,
        output_format: str = "JSON"
    ) -> list | str:
        """Retrieve the list of glossary category metadata elements that contain the search string.
         The search string is located in the request body and is interpreted as a plain string.
         The request parameters, startsWith, endsWith and ignoreCase can be used to allow a fuzzy search.

        Parameters
        ----------
        search_string: str,
            Search string to use to find matching glossaries. If the search string is '*' then all
             glossaries returned.

        effective_time: str, [default=None], optional
            Effective time of the query. If not specified will default to any time. Time format is
            "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.
        starts_with : bool, [default=False], optional
            Starts with the supplied string.
        ends_with : bool, [default=False], optional
            Ends with the supplied string
        ignore_case : bool, [default=False], optional
            Ignore case when searching
        start_from: int, [default=0], optional
             When multiple pages of results are available, the page number to start from.
     page_size: int, [default=None]
             The number of items to return in a single page. If not specified, the default will be taken from
             the class instance.
        output_format: str, default = 'JSON'
            Type of output to produce:
            JSON - output standard json
            MD - output standard markdown with no preamble
            FORM - output markdown with a preamble for a form
            REPORT - output markdown with a preamble for a report

        Returns
        -------
        List | str

        A list of glossary definitions active in the server.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_find_glossary_categories(
                search_string,
                effective_time,
                starts_with,
                ends_with,
                ignore_case,
                start_from,
                page_size,
                output_format
            )
        )

        return response

    async def _async_get_categories_for_glossary(
        self,
        glossary_guid: str,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Return the list of categories associated with a glossary.
            Async version.

        Parameters
        ----------
        glossary_guid: str,
            Unique identity of the glossary

            If not provided, the server name associated with the instance is used.
        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        Returns
        -------
        List | str

        A list of categories associated with a glossary.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """

        if page_size is None:
            page_size = self.page_size

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"{glossary_guid}/categories/retrieve?startFrom={start_from}&pageSize={page_size}"
        )

        response = await self._async_make_request("POST", url)
        return response.json().get("elementList", "No Categories found")

    def get_categories_for_glossary(
        self,
        glossary_guid: str,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Return the list of categories associated with a glossary.

        Parameters
        ----------
        glossary_guid: str,
            Unique identity of the glossary

            If not provided, the server name associated with the instance is used.
        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        Returns
        -------
        List | str

        A list of categories associated with a glossary.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_categories_for_glossary(
                glossary_guid, start_from, page_size
            )
        )
        return response

    async def _async_get_categories_for_term(
        self,
        glossary_term_guid: str,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Return the list of categories associated with a glossary term.
            Async version.

        Parameters
        ----------
        glossary_term_guid: str,
            Unique identity of a glossary term

        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        Returns
        -------
        List | str

        A list of categories associated with a glossary term.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """

        if page_size is None:
            page_size = self.page_size

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/terms/"
            f"{glossary_term_guid}/categories/retrieve?startFrom={start_from}&pageSize={page_size}"
        )

        response = await self._async_make_request("POST", url)
        return response.json().get("elementList", "No Categories found")

    def get_categories_for_term(
        self,
        glossary_term_guid: str,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Return the list of categories associated with a glossary term.

        Parameters
        ----------
        glossary_term_guid: str,
            Unique identity of a glossary term

        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        Returns
        -------
        List | str

        A list of categories associated with a glossary term.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_categories_for_term(
                glossary_term_guid, start_from, page_size
            )
        )
        return response

    async def _async_get_categories_by_name(
        self,
        name: str,
        glossary_guid: str = None,
        status: [str] = ["ACTIVE"],
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Retrieve the list of glossary category metadata elements that either have the requested qualified name or
            display name. The name to search for is located in the request body and is interpreted as a plain string.
            The request body also supports the specification of a glossaryGUID to restrict the search to within a single
            glossary.

            Async version.

        Parameters
        ----------
        name: str,
            category name to search for.
        glossary_guid: str, optional
            The identity of the glossary to search. If not specified, all glossaries will be searched.
        status: [str], optional
            A list of statuses to optionally restrict results. Default is Active

            If not provided, the server name associated with the instance is used.
        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        Returns
        -------
        List | str

        A list of categories with the corresponding display name or qualified name.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """

        if page_size is None:
            page_size = self.page_size
        validate_name(name)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/categories/"
            f"by-name?startFrom={start_from}&pageSize={page_size}"
        )

        body = {
            "class": "GlossaryNameRequestBody",
            "name": name,
            "glossaryGUID": glossary_guid,
            "limitResultsByStatus": status,
        }

        response = await self._async_make_request("POST", url, body)
        return response.json().get("elementList", NO_CATEGORIES_FOUND)

    def get_categories_by_name(
        self,
        name: str,
        glossary_guid: str = None,
        status: [str] = ["ACTIVE"],
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Retrieve the list of glossary category metadata elements that either have the requested qualified name or
            display name. The name to search for is located in the request body and is interpreted as a plain string.
            The request body also supports the specification of a glossaryGUID to restrict the search to within a
            single glossary.

        Parameters
        ----------
        name: str,
            category name to search for.
        glossary_guid: str, optional
            The identity of the glossary to search. If not specified, all glossaries will be searched.
        status: [str], optional
            A list of statuses to optionally restrict results. Default is Active

            If not provided, the server name associated with the instance is used.
        start_from: int, [default=0], optional
                    When multiple pages of results are available, the page number to start from.
        page_size: int, [default=None]
            The number of items to return in a single page. If not specified, the default will be taken from
            the class instance.
        Returns
        -------
        List | str

        A list of categories with the corresponding display name or qualified name.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_categories_by_name(
                name, glossary_guid, status, start_from, page_size
            )
        )
        return response

    async def _async_get_categories_by_guid(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
        output_format: str = 'JSON',
    ) -> list | str:
        """Retrieve the requested glossary category metadata element.  The optional request body contain an effective
        time for the query..

        Async version.

        Parameters
        ----------
        glossary_category_guid: str
            The identity of the glossary category to search.
        effective_time: str, optional
            If specified, the category should only be returned if it was effective at the specified time.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

        output_format: str, default = 'JSON'
            Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report

        Returns
        -------
        List | str

        Details for the category with the glossary category GUID.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        output_format = output_format.upper()
        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/categories/"
            f"{glossary_category_guid}/retrieve"
        )

        body = {
            "class": "EffectiveTimeQueryRequestBody",
            "effectiveTime": effective_time,
        }

        response = await self._async_make_request("POST", url, body_slimmer(body))
        element = response.json().get("element", NO_CATEGORIES_FOUND)
        if element == NO_CATEGORIES_FOUND:
            return NO_CATEGORIES_FOUND
        if output_format != 'JSON':  # return a simplified markdown representation
            return self.generate_categories_md(element, "GUID", output_format)
        return response.json().get("element", NO_CATEGORIES_FOUND)

    def get_categories_by_guid(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
        output_format: str = 'JSON',
    ) -> list | str:
        """Retrieve the requested glossary category metadata element.  The optional request body contain an effective
        time for the query..

        Parameters
        ----------
        glossary_category_guid: str
            The identity of the glossary category to search.
        effective_time: str, optional
            If specified, the category should only be returned if it was effective at the specified time.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

        output_format: str, default = 'JSON'
            Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report

        Returns
        -------
        List | str

        Details for the category with the glossary category GUID.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_categories_by_guid(glossary_category_guid, effective_time, output_format)
        )
        return response

    async def _async_get_category_parent(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
    ) -> list | str:
        """Glossary categories can be organized in a hierarchy. Retrieve the parent glossary category metadata
            element for the glossary category with the supplied unique identifier.  If the requested category
            does not have a parent category, null is returned.  The optional request body contain an effective time
            for the query.

        Async version.

        Parameters
        ----------
        glossary_category_guid: str
            The identity of the glossary category to search.
        effective_time: str, optional
            If specified, the category should only be returned if it was effective at the specified time.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.

        Returns
        -------
        List | str

        Details for the parent category with the glossary category GUID.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/categories/"
            f"{glossary_category_guid}/parent/retrieve"
        )

        body = {
            "class": "EffectiveTimeQueryRequestBody",
            "effectiveTime": effective_time,
        }

        response = await self._async_make_request("POST", url, body)
        return response.json().get("element", "No Parent Category found")

    def get_category_parent(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
    ) -> list | str:
        """Glossary categories can be organized in a hierarchy. Retrieve the parent glossary category metadata
            element for the glossary category with the supplied unique identifier.  If the requested category
            does not have a parent category, null is returned.  The optional request body contain an effective time
            for the query.

        Parameters
        ----------
        glossary_category_guid: str
            The identity of the glossary category to search.
        effective_time: str, optional
            If specified, the category should only be returned if it was effective at the specified time.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601).

            If not provided, the server name associated with the instance is used.

        Returns
        -------
        List | str

        Details for the parent category with the glossary category GUID.

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_category_parent(glossary_category_guid, effective_time)
        )
        return response

    #
    #  Terms
    #

    async def _async_get_terms_for_category(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Retrieve ALL the glossary terms in a category.
            The request body also supports the specification of an effective time for the query.

            Async Version.

        Parameters
        ----------
            glossary_category_guid : str
                Unique identifier for the glossary category to retrieve terms from.
            effective_time : str, optional
                If specified, the terms are returned if they are active at the `effective_time
                Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
            start_from: int, optional defaults to 0
                The page number to start retrieving elements from
            page_size : int, optional defaults to None
                The number of elements to retrieve
        Returns
        -------
        [dict]
            The glossary definition associated with the glossary_guid

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.

        """

        validate_guid(glossary_category_guid)

        if page_size is None:
            page_size = self.page_size

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/categories/"
            f"{glossary_category_guid}/terms/retrieve?startFrom={start_from}&pageSize={page_size}"
        )

        if effective_time is not None:
            body = {"effectiveTime": effective_time}
            response = await self._async_make_request("POST", url, body)
        else:
            response = await self._async_make_request("POST", url)

        return response.json().get("elementList", "No terms found")

    def get_terms_for_category(
        self,
        glossary_category_guid: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Retrieve ALL the glossary terms in a category.
            The request body also supports the specification of an effective time for the query.

            Async Version.

        Parameters
        ----------
            glossary_category_guid : str
                Unique identifier for the glossary category to retrieve terms from.

            effective_time : str, optional
                If specified, the terms are returned if they are active at the `effective_time.
                Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)`.
            start_from: int, optional defaults to 0
                The page number to start retrieving elements from
            page_size : int, optional defaults to None
                The number of elements to retrieve
        Returns
        -------
        dict
            The glossary definition associated with the glossary_guid

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_terms_for_category(
                glossary_category_guid,
                effective_time,
                start_from,
                page_size,
            )
        )

        return response

    async def _async_get_terms_for_glossary(
        self,
        glossary_guid: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Retrieve the list of glossary terms associated with a glossary.
            The request body also supports the specification of an effective time for the query.
        Parameters
        ----------
            glossary_guid : str
                Unique identifier for the glossary

            effective_time : str, optional
                If specified, terms are potentially included if they are active at the`effective_time.
                Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)`
            start_from: int, optional defaults to 0
                The page number to start retrieving elements from
            page_size : int, optional defaults to None
                The number of elements to retrieve
        Returns
        -------
        dict
            The glossary definition associated with the glossary_guid

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """

        validate_guid(glossary_guid)

        if page_size is None:
            page_size = self.page_size

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"{glossary_guid}/terms/retrieve?startFrom={start_from}&pageSize={page_size}"
        )

        if effective_time is not None:
            body = {"effectiveTime": effective_time}
            response = await self._async_make_request("POST", url, body)
        else:
            response = await self._async_make_request("POST", url)

        return response.json().get("elementList", "No terms found")

    def get_terms_for_glossary(
        self,
        glossary_guid: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """Retrieve the list of glossary terms associated with a glossary.
            The request body also supports the specification of an effective time for the query.
        Parameters
        ----------
            glossary_guid : str
                Unique identifier for the glossary

            effective_time : str, optional
                If specified, terms are potentially returned if they are active at the `effective_time`
                Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
            start_from: int, optional defaults to 0
                The page number to start retrieving elements from
            page_size : int, optional defaults to None
                The number of elements to retrieve
        Returns
        -------
        dict
            The glossary definition associated with the glossary_guid

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_terms_for_glossary(
                glossary_guid, effective_time, start_from, page_size
            )
        )

        return response

    async def _async_get_term_relationships(
        self,
        term_guid: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """This call retrieves details of the glossary terms linked to this glossary term.
        Notice the original org 1 glossary term is linked via the "SourcedFrom" relationship..
        Parameters
        ----------
            term_guid : str
                Unique identifier for the glossary term

            effective_time : str, optional
                If specified, term relationships are included if they are active at the `effective_time`.
                Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
            start_from: int, optional defaults to 0
                The page number to start retrieving elements from
            page_size : int, optional defaults to None
                The number of elements to retrieve
        Returns
        -------
        dict
            The glossary definition associated with the glossary_guid

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """

        validate_guid(term_guid)

        if page_size is None:
            page_size = self.page_size

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/terms/"
            f"{term_guid}/related-terms?startFrom={start_from}&pageSize={page_size}"
        )

        if effective_time is not None:
            body = {"effectiveTime": effective_time}
            response = await self._async_make_request("POST", url, body)
        else:
            response = await self._async_make_request("POST", url)

        return response.json().get("elementList", "No terms found")

    def get_term_relationships(
        self,
        term_guid: str,
        effective_time: str = None,
        start_from: int = 0,
        page_size: int = None,
    ) -> list | str:
        """This call retrieves details of the glossary terms linked to this glossary term.
        Notice the original org 1 glossary term is linked via the "SourcedFrom" relationship..
        Parameters
        ----------
            term_guid : str
                Unique identifier for the glossary term

            effective_time : str, optional
                If specified, term relationships are included if they are active at the `effective_time`.
                Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
            start_from: int, optional defaults to 0
                The page number to start retrieving elements from
            page_size : int, optional defaults to None
                The number of elements to retrieve
        Returns
        -------
        dict
            The glossary definition associated with the glossary_guid

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_term_relationships(
                term_guid, effective_time, start_from, page_size
            )
        )

        return response

    async def _async_get_glossary_for_term(
        self, term_guid: str, effective_time: str = None
    ) -> dict | str:
        """Retrieve the glossary metadata element for the requested term.  The optional request body allows you to
            specify that the glossary element should only be returned if it was effective at a particular time.

            Async Version.

        Parameters
        ----------
        term_guid : str
            The unique identifier for the term.

        effective_time : datetime, optional
            If specified, the term information will be retrieved if it is active at the `effective_time`.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

        Returns
        -------
        dict
            The glossary information retrieved for the specified term.
        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """

        validate_guid(term_guid)

        body = {
            "class": "EffectiveTimeQueryRequestBody",
            "effectiveTime": effective_time,
        }
        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"for-term/{term_guid}/retrieve"
        )

        response = await self._async_make_request("POST", url, body)
        return response.json().get("element", "No glossary found")

    def get_glossary_for_term(
        self, term_guid: str, effective_time: str = None
    ) -> dict | str:
        """Retrieve the glossary metadata element for the requested term.  The optional request body allows you to
            specify that the glossary element should only be returned if it was effective at a particular time.

            Async Version.

        Parameters
        ----------
        term_guid : str
            The unique identifier for the term.

        effective_time : datetime, optional
            TIf specified, the term information will be retrieved if it is active at the `effective_time`.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601).

        Returns
        -------
        dict
            The glossary information retrieved for the specified term.
        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        Notes
        -----
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_glossary_for_term(term_guid, effective_time)
        )
        return response

    async def _async_get_terms_by_name(
        self,
        term: str,
        glossary_guid: str = None,
        status_filter: list = [],
        effective_time: str = None,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
        start_from: int = 0,
        page_size: int = None,
    ) -> list:
        """Retrieve glossary terms by display name or qualified name. Async Version.

        Parameters
        ----------
        term : str
            The term to search for in the glossaries.
        glossary_guid : str, optional
            The GUID of the glossary to search in. If not provided, the search will be performed in all glossaries.
        status_filter : list, optional
            A list of status values to filter the search results. Default is an empty list, which means no filtering.

        effective_time : datetime, optional
            If specified, the term information will be retrieved if it is active at the `effective_time`.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
        for_lineage : bool, optional
            Flag to indicate whether the search should include lineage information. Default is False.
        for_duplicate_processing : bool, optional
            Flag to indicate whether the search should include duplicate processing information. Default is False.
        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.

        Returns
        -------
        list
            A list of terms matching the search criteria. If no terms are found, it returns the string "No terms found".

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        """

        if page_size is None:
            page_size = self.page_size

        validate_name(term)

        for_lineage_s = str(for_lineage).lower()
        for_duplicate_processing_s = str(for_duplicate_processing).lower()

        body = {
            "class": "GlossaryNameRequestBody",
            "glossaryGUID": glossary_guid,
            "name": term,
            "effectiveTime": effective_time,
            "limitResultsByStatus": status_filter,
        }
        # body = body_slimmer(body)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"terms/by-name?startFrom={start_from}&pageSize={page_size}&"
            f"&forLineage={for_lineage_s}&forDuplicateProcessing={for_duplicate_processing_s}"
        )

        # print(f"\n\nURL is: \n {url}\n\nBody is: \n{body}")

        response = await self._async_make_request("POST", url, body)
        return response.json().get("elementList", "No terms found")

    def get_terms_by_name(
        self,
        term: str,
        glossary_guid: str = None,
        status_filter: list = [],
        effective_time: str = None,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
        start_from: int = 0,
        page_size: int = None,
    ) -> list:
        """Retrieve glossary terms by display name or qualified name.

        Parameters
        ----------
        term : str
            The term to search for in the glossaries.
        glossary_guid : str, optional
            The GUID of the glossary to search in. If not provided, the search will be performed in all glossaries.
        status_filter : list, optional
            A list of status values to filter the search results. Default is an empty list, which means no filtering.

        effective_time : datetime, optional
            If specified, the term information will be retrieved if it is active at the `effective_time`.
             Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)
        for_lineage : bool, optional
            Flag to indicate whether the search should include lineage information. Default is False.
        for_duplicate_processing : bool, optional
            Flag to indicate whether the search should include duplicate processing information. Default is False.
        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.

        Returns
        -------
        list
            A list of terms matching the search criteria. If no terms are found,
            it returns the string "No terms found".

        Raises
        ------
         InvalidParameterException
             If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
         PropertyServerException
             Raised by the server when an issue arises in processing a valid request.
         NotAuthorizedException
             The principle specified by the user_id does not have authorization for the requested action.
        """
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_terms_by_name(
                term,
                glossary_guid,
                status_filter,
                effective_time,
                for_lineage,
                for_duplicate_processing,
                start_from,
                page_size,
            )
        )
        return response

    async def _async_get_terms_by_guid(self, term_guid: str, output_format: str = 'JSON') -> dict | str:
        """Retrieve a term using its unique id. Async version.
        Parameters
        ----------
        term_guid : str
            The GUID of the glossary term to retrieve.
        output_format: str, default = 'JSON'
            Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report

        Returns
        -------
        dict | str
            A dict detailing the glossary term represented by the GUID. If no term is found, the string
            "No term found" will be returned.

        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.
        """
        output_format = output_format.upper()
        validate_guid(term_guid)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/terms/"
            f"{term_guid}/retrieve"
        )
        response = await self._async_make_request("POST", url)
        term_element = response.json().get("element", NO_TERMS_FOUND)
        if term_element == NO_TERMS_FOUND:
            return NO_TERMS_FOUND
        if output_format != 'JSON':  # return a simplified markdown representation
            return self.generate_terms_md(term_element, "GUID", output_format)
        return response.json().get("element", NO_TERMS_FOUND)


    def get_terms_by_guid(self, term_guid: str, output_format: str = 'JSON') -> dict | str:
        """Retrieve a term using its unique id. Async version.
        Parameters
        ----------
        term_guid : str
            The GUID of the glossary term to retrieve.
        output_format: str, default = 'JSON'
            Type of output to produce:
                JSON - output standard json
                MD - output standard markdown with no preamble
                FORM - output markdown with a preamble for a form
                REPORT - output markdown with a preamble for a report
        Returns
        -------
        dict | str
            A dict detailing the glossary term represented by the GUID. If no term is found, the string
            "No term found" will be returned.
        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.
        """

        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self._async_get_terms_by_guid(term_guid, output_format))

        return response

    async def _async_get_terms_versions(
        self,
        term_guid: str,
        start_from: int = 0,
        page_size=None,
    ) -> dict | str:
        """Retrieve the versions of a glossary term. Async version.
        Parameters
        ----------
        term_guid : str
            The GUID of the glossary term to retrieve.

        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.
        Returns
        -------
        dict | str
            A dict detailing the glossary term represented by the GUID. If no term is found, the string
            "No term found" will be returned.

        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.
        """

        if page_size is None:
            page_size = self.page_size

        validate_guid(term_guid)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/terms/"
            f"{term_guid}/history?startFrom={start_from}&pageSize={page_size}"
        )

        response = await self._async_make_request("POST", url)
        return response.json().get("element", "No term found")

    def get_terms_versions(
        self,
        term_guid: str,
        start_from: int = 0,
        page_size=None,
    ) -> dict | str:
        """Retrieve the versions of a glossary term.
        Parameters
        ----------
        term_guid : str
            The GUID of the glossary term to retrieve.

        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.
        Returns
        -------
        dict | str
            A dict detailing the glossary term represented by the GUID. If no term is found, the string
            "No term found" will be returned.

        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.
        """

        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_terms_versions(term_guid, start_from, page_size)
        )

        return response

    async def _async_get_term_revision_logs(
        self,
        term_guid: str,
        start_from: int = 0,
        page_size=None,
    ) -> dict | str:
        """Retrieve the revision log history for a term. Async version.
        Parameters
        ----------
        term_guid : str
            The GUID of the glossary term to retrieve.

        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.
        Returns
        -------
        dict | str
            A dict detailing the glossary term revision log history. If no term is found, the string
            "No log found" will be returned.

        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.
        """

        if page_size is None:
            page_size = self.page_size

        validate_guid(term_guid)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/elements/"
            f"{term_guid}/notes/retrieve?startFrom={start_from}&pageSize={page_size}"
        )

        response = await self._async_make_request("POST", url)
        return response.json().get("elementList", "No log found")

    def get_term_revision_logs(
        self,
        term_guid: str,
        start_from: int = 0,
        page_size=None,
    ) -> dict | str:
        """Retrieve the revision log history for a term.
        Parameters
        ----------
        term_guid : str
            The GUID of the glossary term to retrieve.

        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.
        Returns
        -------
        dict | str
            A dict detailing the glossary term revision log history. If no term is found, the string
            "No log found" will be returned.

        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.
        """

        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_term_revision_logs(term_guid, start_from, page_size)
        )

        return response

    async def _async_get_term_revision_history(
        self,
        term_revision_log_guid: str,
        start_from: int = 0,
        page_size=None,
    ) -> dict | str:
        """Retrieve the revision history for a glossary term. Async version.

        Parameters
        ----------
        term_revision_log_guid : str
            The GUID of the glossary term revision log to retrieve.

        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.
        Returns
        -------
        dict | str
            A dict detailing the glossary term revision history.

        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.


        Notes
        -----
        This revision history is created automatically.  The text is supplied on the update request.
        If no text is supplied, the value "None" is show.
        """

        if page_size is None:
            page_size = self.page_size

        validate_guid(term_revision_log_guid)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/note-logs/"
            f"{term_revision_log_guid}/notes/retrieve?startFrom={start_from}&pageSize={page_size}"
        )

        response = await self._async_make_request("POST", url)
        return response.json().get("elementList", "No logs found")

    def get_term_revision_history(
        self,
        term_revision_log_guid: str,
        start_from: int = 0,
        page_size=None,
    ) -> dict | str:
        """Retrieve the revision history for a glossary term.

        Parameters
        ----------
        term_revision_log_guid : str
            The GUID of the glossary term revision log to retrieve.

        start_from : int, optional
            The index of the first term to retrieve. Default is 0.
        page_size : int, optional
            The number of terms to retrieve per page. If not provided, it will use the default page size.
        Returns
        -------
        dict | str
            A dict detailing the glossary term revision history.

        Raises
        ------
        InvalidParameterException
            If the client passes incorrect parameters on the request - such as bad URLs or invalid values.
        PropertyServerException
            Raised by the server when an issue arises in processing a valid request.
        NotAuthorizedException
            The principle specified by the user_id does not have authorization for the requested action.


        Notes
        -----
        This revision history is created automatically.  The text is supplied on the update request.
        If no text is supplied, the value "None" is show.
        """

        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_get_term_revision_history(
                term_revision_log_guid, start_from, page_size
            )
        )

        return response

    async def _async_find_glossary_terms(
        self,
        search_string: str,
        glossary_guid: str = None,
        status_filter: list = [],
        effective_time: str = None,
        starts_with: bool = False,
        ends_with: bool = False,
        ignore_case: bool = False,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
        start_from: int = 0,
        page_size: int = None,
        output_format: str = "JSON",
    ) -> list | str:
        """Retrieve the list of glossary term metadata elements that contain the search string.

        Parameters
        ----------
        search_string: str
            Search string to use to find matching glossaries. If the search string is '*' then all glossaries returned.
        glossary_guid str
            Identifier of the glossary to search within. If None, then all glossaries are searched.
        status_filter: list, default = [], optional
            Filters the results by the included Term statuses (such as 'ACTIVE', 'DRAFT'). If not specified,
            the results will not be filtered.
        effective_time: str, [default=None], optional
            If specified, the term information will be retrieved if it is active at the `effective_time`.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.
        starts_with : bool, [default=False], optional
            Starts with the supplied string.
        ends_with : bool, [default=False], optional
            Ends with the supplied string
        ignore_case : bool, [default=False], optional
            Ignore case when searching
        for_lineage : bool, [default=False], optional

        for_duplicate_processing : bool, [default=False], optional

        start_from: str, [default=0], optional
            Page of results to start from
        page_size : int, optional
            Number of elements to return per page - if None, then default for class will be used.
        output_format: str, default = 'JSON'
          Type of output to produce:
            JSON - output standard json
            MD - output standard markdown with no preamble
            FORM - output markdown with a preamble for a form
            REPORT - output markdown with a preamble for a report

        Returns
        -------
        List | str

        A list of term definitions

        Raises
        ------
        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        Notes
        -----
        The search string is located in the request body and is interpreted as a plain string.
        The request parameters, startsWith, endsWith and ignoreCase can be used to allow a fuzzy search.
        The request body also supports the specification of a glossaryGUID to restrict the search to within a single
        glossary.
        """

        if page_size is None:
            page_size = self.page_size
        if effective_time is None:
            effective_time = datetime.now().isoformat()
        starts_with_s = str(starts_with).lower()
        ends_with_s = str(ends_with).lower()
        ignore_case_s = str(ignore_case).lower()
        for_lineage_s = str(for_lineage).lower()
        for_duplicate_processing_s = str(for_duplicate_processing).lower()
        if search_string == "*":
            search_string = None

        # validate_search_string(search_string)

        body = {
            "class": "GlossarySearchStringRequestBody",
            "glossaryGUID": glossary_guid,
            "searchString": search_string,
            "effectiveTime": effective_time,
            "limitResultsByStatus": status_filter,
        }

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"terms/by-search-string?startFrom={start_from}&pageSize={page_size}&startsWith={starts_with_s}&"
            f"endsWith={ends_with_s}&ignoreCase={ignore_case_s}&forLineage={for_lineage_s}&"
            f"forDuplicateProcessing={for_duplicate_processing_s}"
        )


        response = await self._async_make_request("POST", url, body_slimmer(body))
        term_elements = response.json().get("elementList", NO_TERMS_FOUND)
        if term_elements == NO_TERMS_FOUND:
            return NO_TERMS_FOUND
        if output_format != "JSON":  # return a simplified markdown representation
            return self.generate_terms_md(term_elements, search_string, output_format)
        return response.json().get("elementList", NO_TERMS_FOUND)


    def find_glossary_terms(
        self,
        search_string: str,
        glossary_guid: str = None,
        status_filter: list = [],
        effective_time: str = None,
        starts_with: bool = False,
        ends_with: bool = False,
        ignore_case: bool = False,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
        start_from: int = 0,
        page_size: int = None,
        output_format: str = "JSON",
    ) -> list | str:
        """Retrieve the list of glossary term metadata elements that contain the search string.

        Parameters
        ----------
        search_string: str
            Search string to use to find matching glossaries. If the search string is '*' then all glossaries
            returned.
        glossary_guid str
            Identifier of the glossary to search within. If None, then all glossaries are searched.
        status_filter: list, default = [], optional
            Filters the results by the included Term statuses (such as 'ACTIVE', 'DRAFT'). If not specified,
            the results will not be filtered.
        effective_time: str, [default=None], optional
            If specified, the term information will be retrieved if it is active at the `effective_time`.
            Time format is "YYYY-MM-DDTHH:MM:SS" (ISO 8601)

            If not provided, the server name associated with the instance is used.
        starts_with : bool, [default=False], optional
            Starts with the supplied string.
        ends_with : bool, [default=False], optional
            Ends with the supplied string
        ignore_case : bool, [default=False], optional
            Ignore case when searching
        for_lineage : bool, [default=False], optional

        for_duplicate_processing : bool, [default=False], optional

        start_from: str, [default=0], optional
            Page of results to start from
        page_size : int, optional
            Number of elements to return per page - if None, then default for class will be used.
        output_format: str, default = 'JSON'
            Type of output to produce:
            JSON - output standard json
            MD - output standard markdown with no preamble
            FORM - output markdown with a preamble for a form
            REPORT - output markdown with a preamble for a report

        Returns
        -------
        List | str

        A list of term definitions

        Raises
        ------
        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

        Notes
        -----
        The search string is located in the request body and is interpreted as a plain string.
        The request parameters, startsWith, endsWith and ignoreCase can be used to allow a fuzzy search.
        The request body also supports the specification of a glossaryGUID to restrict the search to within a
        single glossary.
        """

        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self._async_find_glossary_terms(
                search_string,
                glossary_guid,
                status_filter,
                effective_time,
                starts_with,
                ends_with,
                ignore_case,
                for_lineage,
                for_duplicate_processing,
                start_from,
                page_size,
                output_format
            )
        )

        return response

    #
    #   Feedback
    #
    async def _async_get_comment(
        self,
        commemt_guid: str,
        effective_time: str,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
    ) -> dict | list:
        """Retrieve the comment specified by the comment GUID"""

        validate_guid(commemt_guid)

        if effective_time is None:
            effective_time = datetime.now().isoformat()

        for_lineage_s = str(for_lineage).lower()
        for_duplicate_processing_s = str(for_duplicate_processing).lower()

        body = {"effective_time": effective_time}

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/comments/"
            f"{commemt_guid}?forLineage={for_lineage_s}&"
            f"forDuplicateProcessing={for_duplicate_processing_s}"
        )

        # print(f"\n\nURL is: \n {url}\n\nBody is: \n{body}")

        response = await self._async_make_request("POST", url, body)
        return response.json()

    async def _async_add_comment_reply(
        self,
        comment_guid: str,
        is_public: bool,
        comment_type: str,
        comment_text: str,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
    ) -> str:
        """Reply to a comment"""

        validate_guid(comment_guid)
        validate_name(comment_type)

        is_public_s = str(is_public).lower()
        for_lineage_s = str(for_lineage).lower()
        for_duplicate_processing_s = str(for_duplicate_processing).lower()

        body = {
            "class": "CommentRequestBody",
            "commentType": comment_type,
            "commentText": comment_text,
            "isPublic": is_public,
        }

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/comments/"
            f"{comment_guid}/replies?isPublic={is_public_s}&forLineage={for_lineage_s}&"
            f"forDuplicateProcessing={for_duplicate_processing_s}"
        )

        # print(f"\n\nURL is: \n {url}\n\nBody is: \n{body}")

        response = await self._async_make_request("POST", url, body)
        return response

    async def _async_update_comment(
        self,
        comment_guid: str,
        is_public: bool,
        comment_type: str,
        comment_text: str,
        is_merge_update: bool = False,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
    ) -> str:
        """Update the specified comment"""

        validate_guid(comment_guid)
        validate_name(comment_type)

        is_public_s = str(is_public).lower()
        for_lineage_s = str(for_lineage).lower()
        for_duplicate_processing_s = str(for_duplicate_processing).lower()

        body = {
            "class": "CommentRequestBody",
            "commentType": comment_type,
            "commentText": comment_text,
            "isPublic": is_public,
        }

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/comments/"
            f"{comment_guid}/replies?isPublic={is_public_s}&forLineage={for_lineage_s}&"
            f"forDuplicateProcessing={for_duplicate_processing_s}"
        )

        # print(f"\n\nURL is: \n {url}\n\nBody is: \n{body}")

        response = await self._async_make_request("POST", url, body)
        return response

    async def _async_find_comment(
        self,
        search_string: str,
        glossary_guid: str = None,
        status_filter: list = [],
        effective_time: str = None,
        starts_with: bool = False,
        ends_with: bool = False,
        ignore_case: bool = False,
        for_lineage: bool = False,
        for_duplicate_processing: bool = False,
        start_from: int = 0,
        page_size: int = None,
    ):
        """Find comments by search string"""

        if page_size is None:
            page_size = self.page_size
        if effective_time is None:
            effective_time = datetime.now().isoformat()
        starts_with_s = str(starts_with).lower()
        ends_with_s = str(ends_with).lower()
        ignore_case_s = str(ignore_case).lower()
        for_lineage_s = str(for_lineage).lower()
        for_duplicate_processing_s = str(for_duplicate_processing).lower()
        if search_string == "*":
            search_string = None

        # validate_search_string(search_string)

        body = {
            "class": "GlossarySearchStringRequestBody",
            "glossaryGUID": glossary_guid,
            "searchString": search_string,
            "effectiveTime": effective_time,
            "limitResultsByStatus": status_filter,
        }
        # body = body_slimmer(body)

        url = (
            f"{self.platform_url}/servers/{self.view_server}/api/open-metadata/glossary-browser/glossaries/"
            f"terms/by-search-string?startFrom={start_from}&pageSize={page_size}&startsWith={starts_with_s}&"
            f"endsWith={ends_with_s}&ignoreCase={ignore_case_s}&forLineage={for_lineage_s}&"
            f"forDuplicateProcessing={for_duplicate_processing_s}"
        )

        # print(f"\n\nURL is: \n {url}\n\nBody is: \n{body}")

        response = await self._async_make_request("POST", url, body)
        return response.json().get("elementList", "No terms found")


if __name__ == "__main__":
    print("Main-Glosssary Browser")
