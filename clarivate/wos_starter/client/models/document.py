# coding: utf-8

"""
    Web of Science™ Starter API

    The Web of Science™ Starter API provides basic metadata and search functionality for Web of Science™ Documents and Journals. Based on your subscription, this API can return times cited of documents.  ## Resouces This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.  The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-starter). You can find more details about the subscription and the Plans.  ## Content  You can learn more about content at [Web of Science™ Product Page](https://clarivate.com/webofsciencegroup/solutions/web-of-science/) or in the [Web of Science™ Help](https://webofscience.help.clarivate.com/en-us/Content/home.htm). The following attributes are available from in the API. * UID (Unique Identifier) * Title * Issue * Pages * DOI * Volume * Times Cited * ISSN/eISSN * ISBN * PubMed ID * Source * Web of Science URL * Citing Articles Web of Science URL * Publication Date * Authors * Author Keywords * [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html) * Cited References Web of Science URL * ResearcherID * Book DOI * Related Records Web of Science URL * Journal Citations Reports URL    ## Credentials  All requests require authentication with an API Key authentication flow. For more details, check the [Guide][https://developer.clarivate.com/help/api-access#key_access].  ## Search and field tags for Web of Science documents Web of Science™ offers [advanced search query builder](https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html). This API does not support all field tags for documents. [Web of Science API Expanded](https://developer.clarivate.com/apis/wos) offers all available field tags. The following table lists the field tags that are supported by this API. | Field Tag | Description                                                                                                                                                 | |-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------| | TI        | Title of document                                                                                                                                           | | IS        | ISSN or ISBN                                                                                                                                                | | SO        | Source title - The result contains all source titles within product database (for example, journal titles and/or book titles if the product includes books) | | VL        | Volume                                                                                                                                                      | | PG        | Page                                                                                                                                                        | | CS        | Issue                                                                                                                                                       | | PY        | Year Published                                                                                                                                              | | AU        | Author                                                                                                                                                      | | AI        | Author Identifier                                                                                                                                                      | | UT        | Accession Number                                                                                                                                            | | DO        | DOI                                                                                                                                                         | | DT        | [Document Type](https://webofscience.help.clarivate.com/en-us/Content/document-types.html)                                                                                                                                                         | | PMID      | PubMed ID                                                                                                                                                   | | OG        | Search for preferred organization names and/or their name variants from the Preferred Organization Index. <p> A search on a preferred organization name returns all records that contain the preferred name and all records that contain its name variants. A search on a name variant returns all records that contain the variant. For example, Cornell Law Sch returns all records that contain Cornell Law Sch in the Addresses field. <p> When searching for organization names that contain a Boolean (AND, NOT, NEAR, and SAME), always enclose the word in quotation marks ( \" \" ). For example: <p>   - OG=(Japan Science \"and\" Technology Agency (JST))      <br>   - OG=(\"Near\" East Univ)         <br> - OG=(\"OR\" Hlth Sci Univ)                           | | TS        | Searches for topic terms in the following fields within a document: <p> - Title <br> - Abstract <br> - Author keywords <br> - Keywords Plus | SUR       | Searches records in DRCI by repository \"SourceURL\". Search values must be inside double quotes  ## Pagination To ensure fast response time, each search or multiple entity calls (such as `/documents`) retrieve only a certain number of hits/records.  There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.  - limit&#58; Number of returned results, ranging from 0 to 50 (default **10**) - page&#58; Specifying a page to retrieve (default **1**)  Moreover, this information is shown in the response body, in the tag **metadata**&#58;  ```json \"metadata\": {   \"total\": 91,   \"page\": 1,   \"limit\": 10 } ```  ## Errors The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.  | Code  | Title  | Description | |---|---|---| | 400  | Bad request  | Request syntax error | | 401  | Unauthorized  | The API key is invalid or missed | | 404  | Not found  | The resource is not found | | 405 | Method not allowed | Method other than GET is not allowed | | 50X  | Server errors  | Technical error with servers| Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:  ```json   \"error\": {     \"status\": 404,     \"title\": \"Resource couldn't be found\",     \"details\": \"There is no record found in the Web of Science database. Please check your query.\"   } ``` For the `401 Unauthorized` error the response body is a little bit different: ```json {   \"error_description\": \"The access token is missing\",   \"error\": \"invalid_request\" } 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from clarivate.wos_starter.client.models.document_citations_inner import DocumentCitationsInner
from clarivate.wos_starter.client.models.document_identifiers import DocumentIdentifiers
from clarivate.wos_starter.client.models.document_keywords import DocumentKeywords
from clarivate.wos_starter.client.models.document_links import DocumentLinks
from clarivate.wos_starter.client.models.document_names import DocumentNames
from clarivate.wos_starter.client.models.document_source import DocumentSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Document(BaseModel):
    """
    Document
    """ # noqa: E501
    uid: StrictStr = Field(description="Web of Science Unique Identifier")
    title: Optional[StrictStr] = Field(default=None, description="Document title")
    types: Optional[List[StrictStr]] = Field(default=None, description="Normalized Document Types")
    source_types: Optional[List[StrictStr]] = Field(default=None, description="Source Document Types", alias="sourceTypes")
    source: Optional[DocumentSource] = None
    names: Optional[DocumentNames] = None
    links: Optional[DocumentLinks] = None
    citations: Optional[List[DocumentCitationsInner]] = Field(default=None, description="Times Cited")
    identifiers: Optional[DocumentIdentifiers] = None
    keywords: Optional[DocumentKeywords] = None
    __properties: ClassVar[List[str]] = ["uid", "title", "types", "sourceTypes", "source", "names", "links", "citations", "identifiers", "keywords"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Document from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of names
        if self.names:
            _dict['names'] = self.names.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in citations (list)
        _items = []
        if self.citations:
            for _item in self.citations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['citations'] = _items
        # override the default output from pydantic by calling `to_dict()` of identifiers
        if self.identifiers:
            _dict['identifiers'] = self.identifiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords
        if self.keywords:
            _dict['keywords'] = self.keywords.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uid": obj.get("uid"),
            "title": obj.get("title"),
            "types": obj.get("types"),
            "sourceTypes": obj.get("sourceTypes"),
            "source": DocumentSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "names": DocumentNames.from_dict(obj.get("names")) if obj.get("names") is not None else None,
            "links": DocumentLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "citations": [DocumentCitationsInner.from_dict(_item) for _item in obj.get("citations")] if obj.get("citations") is not None else None,
            "identifiers": DocumentIdentifiers.from_dict(obj.get("identifiers")) if obj.get("identifiers") is not None else None,
            "keywords": DocumentKeywords.from_dict(obj.get("keywords")) if obj.get("keywords") is not None else None
        })
        return _obj


