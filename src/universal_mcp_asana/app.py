from typing import Any, Annotated
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class AsanaApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='asanaapp', integration=integration, **kwargs)
        self.base_url = "https://app.asana.com/api/1.0"


    def get_an_allocation(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get an allocation. Returns the complete allocation record for a single allocation.
        
        Tags: Allocations
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_allocation(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update an allocation. An existing allocation can be updated by making a PUT request on the URL for
that allocation. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated allocation record.
        
        Tags: Allocations
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_allocation(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete an allocation. A specific, existing allocation can be deleted by making a DELETE request on the URL for that allocation.

Returns an empty data record.
        
        Tags: Allocations
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_allocations(self, assignee: Annotated[Any, 'Globally unique identifier for the user the allocation is assigned to.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, parent: Annotated[Any, 'Globally unique identifier for the project to filter allocations by.'] = None, workspace: Annotated[Any, 'Globally unique identifier for the workspace.'] = None) -> dict[str, Any]:
        """
        Get multiple allocations. Returns a list of allocations filtered to a specific project or user.
        
        Tags: Allocations
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "parent": parent,
                "assignee": assignee,
                "workspace": workspace,
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_allocation(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create an allocation. Creates a new allocation.

Returns the full record of the newly created allocation.
        
        Tags: Allocations
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_an_attachment(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get an attachment. Get the full record for a single attachment.
        
        Tags: Attachments
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_attachment(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete an attachment. Deletes a specific, existing attachment.

Returns an empty data record.
        
        Tags: Attachments
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachments_from_an_object(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, parent: Annotated[Any, '(Required) Globally unique identifier for object to fetch statuses from. Must be a GID for a `project`, `project_brief`, or `task`.'] = None) -> dict[str, Any]:
        """
        Get attachments from an object. Returns the compact records for all attachments on the object.

There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the "Key resources" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.

Note that within the Asana app, inline images in the task description do not appear in the index of image thumbnails nor as stories in the task. However, requests made to `GET /attachments` for a task will return all of the images in the task, including inline images.
        
        Tags: Attachments
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "parent": parent,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_an_attachment(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, request_body: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Upload an attachment. Upload an attachment.

This method uploads an attachment on an object and returns the compact
record for the created attachment object. This is possible by either:

- Providing the URL of the external resource being attached, or
- Downloading the file content first and then uploading it as any other attachment. Note that it is not possible to attach
files from third party services such as Dropbox, Box, Vimeo & Google Drive via the API

The 100MB size limit on attachments in Asana is enforced on this endpoint.

This endpoint expects a multipart/form-data encoded request containing the full contents of the file to be uploaded.

Requests made should follow the HTTP/1.1 specification that line
terminators are of the form `CRLF` or `\r\n` outlined
[here](http://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Basic-Rules) in order for the server to reliably and properly handle the request.
        
        Tags: Attachments
        
        """
        
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_audit_log_events(self, actor_gid: Annotated[Any, 'Filter to events triggered by the actor with this ID.'] = None, actor_type: Annotated[Any, 'Filter to events with an actor of this type.\nThis only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.'] = None, end_at: Annotated[Any, 'Filter to events created before this time (exclusive).'] = None, event_type: Annotated[Any, 'Filter to events of this type.\nRefer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, resource_gid: Annotated[Any, 'Filter to events with this resource ID.'] = None, start_at: Annotated[Any, 'Filter to events created after this time (inclusive).'] = None) -> dict[str, Any]:
        """
        Get audit log events. Retrieve the audit log events that have been captured in your domain.

This endpoint will return a list of [AuditLogEvent](/reference/audit-log-api) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.

There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/reference/audit-log-api) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.

The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.

*Note: If the filters you provided match events in your domain and `next_page` is present in the response, we will continue to send `next_page` on subsequent requests even when there are no more events that match the filters. This was put in place so that you can implement an audit log stream that will return future events that match these filters. If you are not interested in future events that match the filters you have defined, you can rely on checking empty `data` response for the end of current events that match your filters.*

When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/reference/audit-log-api) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.
        
        Tags: Audit log API
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "start_at": start_at,
                "end_at": end_at,
                "event_type": event_type,
                "actor_type": actor_type,
                "actor_gid": actor_gid,
                "resource_gid": resource_gid,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def submit_parallel_requests(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Submit parallel requests. Make multiple requests in parallel to Asana's API.
        
        Tags: Batch API
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_acustom_field(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a custom field. Creates a new custom field in a workspace. Every custom field is required
to be created in a specific workspace, and this workspace cannot be
changed once set.

A custom field’s name must be unique within a workspace and not conflict
with names of existing task properties such as `Due Date` or `Assignee`.
A custom field’s type must be one of `text`, `enum`, `multi_enum`, `number`,
`date`, or `people`.

Returns the full record of the newly created custom field.
        
        Tags: Custom fields
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_acustom_field(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a custom field. Get the complete definition of a custom field’s metadata.

Since custom fields can be defined for one of a number of types, and
these types have different data and behaviors, there are fields that are
relevant to a particular type. For instance, as noted above, enum_options
is only relevant for the enum type and defines the set of choices that
the enum could represent. The examples below show some of these
type-specific custom field definitions.
        
        Tags: Custom fields
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_acustom_field(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a custom field. A specific, existing custom field can be updated by making a PUT request on the URL for that custom field. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged
When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the custom field.
A custom field’s `type` cannot be updated.
An enum custom field’s `enum_options` cannot be updated with this endpoint. Instead see “Work With Enum Options” for information on how to update `enum_options`.
Locked custom fields can only be updated by the user who locked the field.
Returns the complete updated custom field record.
        
        Tags: Custom fields
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_acustom_field(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a custom field. A specific, existing custom field can be deleted by making a DELETE request on the URL for that custom field.
Locked custom fields can only be deleted by the user who locked the field.
Returns an empty data record.
        
        Tags: Custom fields
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace_scustom_fields(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a workspace's custom fields. Returns a list of the compact representation of all of the custom fields in a workspace.
        
        Tags: Custom fields
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_enum_option(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create an enum option. Creates an enum option and adds it to this custom field’s list of enum options. A custom field can have at most 500 enum options (including disabled options). By default new enum options are inserted at the end of a custom field’s list.
Locked custom fields can only have enum options added by the user who locked the field.
Returns the full record of the newly created enum option.
        
        Tags: Custom fields
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def reorder_acustom_field_senum(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Reorder a custom field's enum. Moves a particular enum option to be either before or after another specified enum option in the custom field.
Locked custom fields can only be reordered by the user who locked the field.
        
        Tags: Custom fields
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_enum_option(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update an enum option. Updates an existing enum option. Enum custom fields require at least one enabled enum option.
Locked custom fields can only be updated by the user who locked the field.
Returns the full record of the updated enum option.
        
        Tags: Custom fields
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_scustom_fields(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a project's custom fields. Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [documentation for input/output options](https://developers.asana.com/docs/inputoutput-options) for more information.
        
        Tags: Custom field settings
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio_scustom_fields(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a portfolio's custom fields. Returns a list of all of the custom fields settings on a portfolio, in compact form.
        
        Tags: Custom field settings
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_events_on_aresource(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, resource: Annotated[Any, '(Required) A resource ID to subscribe to. The resource can be a task, project, or goal.'] = None, sync: Annotated[Any, 'A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated.\n*Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a `412 Precondition Failed` error, and include a fresh sync token in the response.*'] = None) -> dict[str, Any]:
        """
        Get events on a resource. Returns the full record for all events that have occurred since the sync
token was created.

A `GET` request to the endpoint `/[path_to_resource]/events` can be made in
lieu of including the resource ID in the data for the request.

Asana limits a single sync token to 100 events. If more than 100 events exist
for a given resource, `has_more: true` will be returned in the response, indicating
that there are more events to pull.

*Note: The resource returned will be the resource that triggered the
event. This may be different from the one that the events were requested
for. For example, a subscription to a project will contain events for
tasks contained within the project.*
        
        Tags: Events
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "resource": resource,
                "sync": sync,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agoal(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a goal. Returns the complete goal record for a single goal.
        
        Tags: Goals
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a goal. An existing goal can be updated by making a PUT request on the URL for
that goal. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated goal record.
        
        Tags: Goals
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_agoal(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a goal. A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.

Returns an empty data record.
        
        Tags: Goals
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_goals(self, is_workspace_level: Annotated[Any, 'Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, portfolio: Annotated[Any, 'Globally unique identifier for supporting portfolio.'] = None, project: Annotated[Any, 'Globally unique identifier for supporting project.'] = None, task: Annotated[Any, 'Globally unique identifier for supporting task.'] = None, team: Annotated[Any, 'Globally unique identifier for the team.'] = None, time_periods: Annotated[Any, 'Globally unique identifiers for the time periods.'] = None, workspace: Annotated[Any, 'Globally unique identifier for the workspace.'] = None) -> dict[str, Any]:
        """
        Get goals. Returns compact goal records.
        
        Tags: Goals
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "portfolio": portfolio,
                "project": project,
                "task": task,
                "is_workspace_level": is_workspace_level,
                "team": team,
                "workspace": workspace,
                "time_periods": time_periods,
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_agoal(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a goal. Creates a new goal in a workspace or team.

Returns the full record of the newly created goal.
        
        Tags: Goals
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_agoal_metric(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a goal metric. Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.
        
        Tags: Goals
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal_metric(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a goal metric. Updates a goal's existing metric's `current_number_value` if one exists,
otherwise responds with a 400 status code.

Returns the complete updated goal metric record.
        
        Tags: Goals
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acollaborator_to_agoal(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a collaborator to a goal. Adds followers to a goal. Returns the goal the followers were added to.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.
        
        Tags: Goals
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acollaborator_from_agoal(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a collaborator from a goal. Removes followers from a goal. Returns the goal the followers were removed from.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.
        
        Tags: Goals
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_parent_goals_from_agoal(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get parent goals from a goal. Returns a compact representation of all of the parent goals of a goal.
        
        Tags: Goals
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agoal_relationship(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a goal relationship. Returns the complete updated goal relationship record for a single goal relationship.
        
        Tags: Goal relationships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal_relationship(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a goal relationship. An existing goal relationship can be updated by making a PUT request on the URL for
that goal relationship. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated goal relationship record.
        
        Tags: Goal relationships
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_goal_relationships(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, resource_subtype: Annotated[Any, 'If provided, filter to goal relationships with a given resource_subtype.'] = None, supported_goal: Annotated[Any, '(Required) Globally unique identifier for the supported goal in the goal relationship.'] = None) -> dict[str, Any]:
        """
        Get goal relationships. Returns compact goal relationship records.
        
        Tags: Goal relationships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
                "supported_goal": supported_goal,
                "resource_subtype": resource_subtype,
                "opt_fields": opt_fields,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_asupporting_goal_relationship(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a supporting goal relationship. Creates a goal relationship by adding a supporting resource to a given goal.

Returns the newly created goal relationship record.
        
        Tags: Goal relationships
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def removes_asupporting_goal_relationship(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Removes a supporting goal relationship. Removes a goal relationship for a given parent goal.
        
        Tags: Goal relationships
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ajob_by_id(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a job by id. Returns the full record for a job.
        
        Tags: Jobs
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_memberships(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, member: Annotated[Any, 'Globally unique identifier for `team` or `user`.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, parent: Annotated[Any, 'Globally unique identifier for `goal`, `project`, or `portfolio`.'] = None) -> dict[str, Any]:
        """
        Get multiple memberships. Returns compact `goal_membership`, `project_membership`, or `portfolio_membership` records. The possible types for `parent` in this request are `goal`, `project`, or `portfolio`. An additional member (user GID or team GID) can be passed in to filter to a specific membership. Teams are not supported for portfolios yet.
        
        Tags: Memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "parent": parent,
                "member": member,
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_amembership(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a membership. Creates a new membership in a `goal` or `project`. `Teams` or `users` can be a member
of `goals` or `projects`.

Returns the full record of the newly created membership.
        
        Tags: Memberships
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_amembership(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a membership. Returns compact `project_membership` record for a single membership. `GET` only supports project memberships currently
        
        Tags: Memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_amembership(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a membership. An existing membership can be updated by making a `PUT` request on the URL for
that goal. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged. Memberships on `goals` and `projects` can be updated.

Returns the full record of the updated membership.
        
        Tags: Memberships
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_amembership(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a membership. A specific, existing membership for a `goal` or `project` can be deleted by making a `DELETE` request
on the URL for that membership.

Returns an empty data record.
        
        Tags: Memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_organization_export_request(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create an organization export request. This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.
        
        Tags: Organization exports
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_details_on_an_org_export_request(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get details on an org export request. Returns details of a previously-requested Organization export.
        
        Tags: Organization exports
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_portfolios(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, owner: Annotated[Any, 'The user who owns the portfolio. Currently, API users can only get a list of portfolios that they themselves own, unless the request is made from a Service Account. In the case of a Service Account, if this parameter is specified, then all portfolios owned by this parameter are returned. Otherwise, all portfolios across the workspace are returned.'] = None, workspace: Annotated[Any, '(Required) The workspace or organization to filter portfolios on.'] = None) -> dict[str, Any]:
        """
        Get multiple portfolios. Returns a list of the portfolios in compact representation that are owned by the current API user.
        
        Tags: Portfolios
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "workspace": workspace,
                "owner": owner,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aportfolio(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a portfolio. Creates a new portfolio in the given workspace with the supplied name.

Note that portfolios created in the Asana UI may have some state
(like the “Priority” custom field) which is automatically added
to the portfolio when it is created. Portfolios created via our
API will *not* be created with the same initial state to allow
integrations to create their own starting state on a portfolio.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a portfolio. Returns the complete portfolio record for a single portfolio.
        
        Tags: Portfolios
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aportfolio(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a portfolio. An existing portfolio can be updated by making a PUT request on the URL for
that portfolio. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated portfolio record.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aportfolio(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a portfolio. An existing portfolio can be deleted by making a DELETE request on
the URL for that portfolio.

Returns an empty data record.
        
        Tags: Portfolios
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_portfolio_items(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get portfolio items. Get a list of the items in compact form in a portfolio.
        
        Tags: Portfolios
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_aportfolio_item(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a portfolio item. Add an item to a portfolio.
Returns an empty data block.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_aportfolio_item(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a portfolio item. Remove an item from a portfolio.
Returns an empty data block.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acustom_field_to_aportfolio(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a custom field to a portfolio. Custom fields are associated with portfolios by way of custom field settings.  This method creates a setting for the portfolio.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acustom_field_from_aportfolio(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a custom field from a portfolio. Removes a custom field setting from a portfolio.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_users_to_aportfolio(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add users to a portfolio. Adds the specified list of users as members of the portfolio.
Returns the updated portfolio record.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_users_from_aportfolio(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove users from a portfolio. Removes the specified list of users from members of the portfolio.
Returns the updated portfolio record.
        
        Tags: Portfolios
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_portfolio_memberships(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, portfolio: Annotated[Any, 'The portfolio to filter results on.'] = None, user: Annotated[Any, 'A string identifying a user. This can either be the string "me", an email, or the gid of a user.'] = None, workspace: Annotated[Any, 'The workspace to filter results on.'] = None) -> dict[str, Any]:
        """
        Get multiple portfolio memberships. Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.
        
        Tags: Portfolio memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "portfolio": portfolio,
                "workspace": workspace,
                "user": user,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio_membership(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a portfolio membership. Returns the complete portfolio record for a single portfolio membership.
        
        Tags: Portfolio memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_aportfolio(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, user: Annotated[Any, 'A string identifying a user. This can either be the string "me", an email, or the gid of a user.'] = None) -> dict[str, Any]:
        """
        Get memberships from a portfolio. Returns the compact portfolio membership records for the portfolio.
        
        Tags: Portfolio memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "user": user,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_projects(self, archived: Annotated[Any, 'Only return projects whose `archived` field takes on the value of this parameter.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, team: Annotated[Any, 'The team to filter projects on.'] = None, workspace: Annotated[Any, 'The workspace or organization to filter projects on.'] = None) -> dict[str, Any]:
        """
        Get multiple projects. Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned.
*Note: This endpoint may timeout for large domains. Try filtering by team!*
        
        Tags: Projects
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "workspace": workspace,
                "team": team,
                "archived": archived,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a project. Create a new project in a workspace or team.

Every project is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the `workspace` parameter regardless of whether or not it is an
organization.

If the workspace for your project is an organization, you must also
supply a `team` to share the project with.

Returns the full record of the newly created project.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a project. Returns the complete project record for a single project.
        
        Tags: Projects
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a project. A specific, existing project can be updated by making a PUT request on
the URL for that project. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated project record.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a project. A specific, existing project can be deleted by making a DELETE request on
the URL for that project.

Returns an empty data record.
        
        Tags: Projects
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Duplicate a project. Creates and returns a job that will asynchronously handle the duplication.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_projects_atask_is_in(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get projects a task is in. Returns a compact representation of all of the projects the task is in.
        
        Tags: Projects
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_sprojects(self, archived: Annotated[Any, 'Only return projects whose `archived` field takes on the value of this parameter.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a team's projects. Returns the compact project records for all projects in the team.
        
        Tags: Projects
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "archived": archived,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_in_ateam(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a project in a team. Creates a project shared with the given team.

Returns the full record of the newly created project.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_projects_in_aworkspace(self, archived: Annotated[Any, 'Only return projects whose `archived` field takes on the value of this parameter.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get all projects in a workspace. Returns the compact project records for all projects in the workspace.
*Note: This endpoint may timeout for large domains. Prefer the `/teams/{team_gid}/projects` endpoint.*
        
        Tags: Projects
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "archived": archived,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_in_aworkspace(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a project in a workspace. Creates a project in the workspace.

If the workspace for your project is an organization, you must also
supply a team to share the project with.

Returns the full record of the newly created project.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acustom_field_to_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a custom field to a project. Custom fields are associated with projects by way of custom field settings.  This method creates a setting for the project.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acustom_field_from_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a custom field from a project. Removes a custom field setting from a project.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_task_count_of_aproject(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get task count of a project. Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](/docs/inputoutput-options) using `opt_fields` to get any information from this endpoint.

This endpoint has an additional [rate limit](/docs/rate-limits) and each field counts especially high against our [cost limits](/docs/rate-limits#cost-limits).

Milestones are just tasks, so they are included in the `num_tasks`, `num_incomplete_tasks`, and `num_completed_tasks` counts.
        
        Tags: Projects
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_users_to_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add users to a project. Adds the specified list of users as members of the project. Note that a user being added as a member may also be added as a *follower* as a result of this operation. This is because the user's default notification settings (i.e., in the "Notifcations" tab of "My Profile Settings") will override this endpoint's default behavior of setting "Tasks added" notifications to `false`.
Returns the updated project record.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_users_from_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove users from a project. Removes the specified list of users from members of the project.
Returns the updated project record.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_followers_to_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add followers to a project. Adds the specified list of users as followers to the project. Followers are a subset of members who have opted in to receive "tasks added" notifications for a project. Therefore, if the users are not already members of the project, they will also become members as a result of this operation.
Returns the updated project record.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_followers_from_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove followers from a project. Removes the specified list of users from following the project, this will not affect project membership status.
Returns the updated project record.
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_template_from_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a project template from a project. Creates and returns a job that will asynchronously handle the project template creation. Note that
while the resulting project template can be accessed with the API, it won't be visible in the Asana
UI until Project Templates 2.0 is launched in the app. See more in [this forum post](https://forum.asana.com/t/a-new-api-for-project-templates/156432).
        
        Tags: Projects
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_brief(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a project brief. Get the full record for a project brief.
        
        Tags: Project briefs
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aproject_brief(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a project brief. An existing project brief can be updated by making a PUT request on the URL for
that project brief. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated project brief record.
        
        Tags: Project briefs
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_brief(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a project brief. Deletes a specific, existing project brief.

Returns an empty data record.
        
        Tags: Project briefs
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_brief(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a project brief. Creates a new project brief.

Returns the full record of the newly created project brief.
        
        Tags: Project briefs
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_membership(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a project membership. Returns the complete project record for a single project membership.
        
        Tags: Project memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_aproject(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, user: Annotated[Any, 'A string identifying a user. This can either be the string "me", an email, or the gid of a user.'] = None) -> dict[str, Any]:
        """
        Get memberships from a project. Returns the compact project membership records for the project.
        
        Tags: Project memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "user": user,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_status(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a project status. *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*

Returns the complete record for a single status update.
        
        Tags: Project statuses
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_status(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a project status. *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*

Deletes a specific, existing project status update.

Returns an empty data record.
        
        Tags: Project statuses
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_statuses_from_aproject(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get statuses from a project. *Deprecated: new integrations should prefer the `/status_updates` route.*

Returns the compact project status update records for all updates on the project.
        
        Tags: Project statuses
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_status(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a project status. *Deprecated: new integrations should prefer the `/status_updates` route.*

Creates a new status update on the project.

Returns the full record of the newly created project status update.
        
        Tags: Project statuses
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_template(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a project template. Returns the complete project template record for a single project template.
        
        Tags: Project templates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_template(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a project template. A specific, existing project template can be deleted by making a DELETE request on the URL for that project template.

Returns an empty data record.
        
        Tags: Project templates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_project_templates(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, team: Annotated[Any, 'The team to filter projects on.'] = None, workspace: Annotated[Any, 'The workspace to filter results on.'] = None) -> dict[str, Any]:
        """
        Get multiple project templates. Returns the compact project template records for all project templates in the given team or workspace.
        
        Tags: Project templates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "workspace": workspace,
                "team": team,
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_sproject_templates(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a team's project templates. Returns the compact project template records for all project templates in the team.
        
        Tags: Project templates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def instantiate_aproject_from_aproject_template(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Instantiate a project from a project template. Creates and returns a job that will asynchronously handle the project instantiation.

To form this request, it is recommended to first make a request to [get a project template](/reference/getprojecttemplate). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.

_Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/reference/workspaces) parameter._
        
        Tags: Project templates
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def trigger_arule(self, data: Annotated[dict[str, Any], ''] = None) -> dict[str, Any]:
        """
        Trigger a rule. Trigger a rule which uses an ["incoming web request"](/docs/incoming-web-requests) trigger.
        
        Tags: Rules
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_asection(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a section. Returns the complete record for a single section.
        
        Tags: Sections
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_asection(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a section. A specific, existing section can be updated by making a PUT request on
the URL for that project. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged. (note that
at this time, the only field that can be updated is the `name` field.)

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated section record.
        
        Tags: Sections
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_asection(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a section. A specific, existing section can be deleted by making a DELETE request on
the URL for that section.

Note that sections must be empty to be deleted.

The last remaining section cannot be deleted.

Returns an empty data block.
        
        Tags: Sections
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sections_in_aproject(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get sections in a project. Returns the compact records for all sections in the specified project.
        
        Tags: Sections
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_asection_in_aproject(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a section in a project. Creates a new section in a project.
Returns the full record of the newly created section.
        
        Tags: Sections
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_task_to_section(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add task to section. Add a task to a specific, existing section. This will remove the task from other sections of the project.

The task will be inserted at the top of a section unless an insert_before or insert_after parameter is declared.

This does not work for separators (tasks with the resource_subtype of section).
        
        Tags: Sections
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def move_or_insert_sections(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Move or Insert sections. Move sections relative to each other. One of
`before_section` or `after_section` is required.

Sections cannot be moved between projects.

Returns an empty data block.
        
        Tags: Sections
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_astatus_update(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a status update. Returns the complete record for a single status update.
        
        Tags: Status updates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_astatus_update(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a status update. Deletes a specific, existing status update.

Returns an empty data record.
        
        Tags: Status updates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_status_updates_from_an_object(self, created_since: Annotated[Any, 'Only return statuses that have been created since the given time.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, parent: Annotated[Any, '(Required) Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal.'] = None) -> dict[str, Any]:
        """
        Get status updates from an object. Returns the compact status update records for all updates on the object.
        
        Tags: Status updates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "parent": parent,
                "created_since": created_since,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_astatus_update(self, data: Annotated[dict[str, Any], ''] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a status update. Creates a new status update on an object.
Returns the full record of the newly created status update.
        
        Tags: Status updates
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_astory(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a story. Returns the full record for a single story.
        
        Tags: Stories
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_astory(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a story. Updates the story and returns the full record for the updated story. Only comment stories can have their text updated, and only comment stories and attachment stories can be pinned. Only one of `text` and `html_text` can be specified.
        
        Tags: Stories
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_astory(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a story. Deletes a story. A user can only delete stories they have created.

Returns an empty data record.
        
        Tags: Stories
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_stories_from_atask(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get stories from a task. Returns the compact records for all stories on the task.
        
        Tags: Stories
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_astory_on_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a story on a task. Adds a story to a task. This endpoint currently only allows for comment
stories to be created. The comment will be authored by the currently
authenticated user, and timestamped when the server receives the request.

Returns the full record for the new story added to the task.
        
        Tags: Stories
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_tags(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, workspace: Annotated[Any, 'The workspace to filter tags on.'] = None) -> dict[str, Any]:
        """
        Get multiple tags. Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.
        
        Tags: Tags
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "workspace": workspace,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atag(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a tag. Creates a new tag in a workspace or organization.

Every tag is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the workspace parameter regardless of whether or not it is an
organization.

Returns the full record of the newly created tag.
        
        Tags: Tags
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atag(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a tag. Returns the complete tag record for a single tag.
        
        Tags: Tags
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atag(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a tag. Updates the properties of a tag. Only the fields provided in the `data`
block will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the tag.

Returns the complete updated tag record.
        
        Tags: Tags
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atag(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a tag. A specific, existing tag can be deleted by making a DELETE request on
the URL for that tag.

Returns an empty data record.
        
        Tags: Tags
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_stags(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a task's tags. Get a compact representation of all of the tags the task has.
        
        Tags: Tags
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_in_aworkspace(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get tags in a workspace. Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.
        
        Tags: Tags
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atag_in_aworkspace(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a tag in a workspace. Creates a new tag in a workspace or organization.

Every tag is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the workspace parameter regardless of whether or not it is an
organization.

Returns the full record of the newly created tag.
        
        Tags: Tags
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_tasks(self, assignee: Annotated[Any, 'The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified.\n*Note: If you specify `assignee`, you must also specify the `workspace` to filter on.*'] = None, completed_since: Annotated[Any, 'Only return tasks that are either incomplete or that have been completed since this time.'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, modified_since: Annotated[Any, 'Only return tasks that have been modified since the given time.\n\n*Note: A task is considered “modified” if any of its properties\nchange, or associations between it and other objects are modified\n(e.g.  a task being added to a project). A task is not considered\nmodified just because another object it is associated with (e.g. a\nsubtask) is modified. Actions that count as modifying the task\ninclude assigning, renaming, completing, and adding stories.*'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, project: Annotated[Any, 'The project to filter tasks on.'] = None, section: Annotated[Any, 'The section to filter tasks on.'] = None, workspace: Annotated[Any, 'The workspace to filter tasks on.\n*Note: If you specify `workspace`, you must also specify the `assignee` to filter on.*'] = None) -> dict[str, Any]:
        """
        Get multiple tasks. Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.

For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/reference/searchtasksforworkspace).
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "assignee": assignee,
                "project": project,
                "section": section,
                "workspace": workspace,
                "completed_since": completed_since,
                "modified_since": modified_since,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a task. Creating a new task is as easy as POSTing to the `/tasks` endpoint with a
data block containing the fields you’d like to set on the task. Any
unspecified fields will take on default values.

Every task is required to be created in a specific workspace, and this
workspace cannot be changed once set. The workspace need not be set
explicitly if you specify `projects` or a `parent` task instead.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a task. Returns the complete task record for a single task.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a task. A specific, existing task can be updated by making a PUT request on the
URL for that task. Only the fields provided in the `data` block will be
updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated task record.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atask(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a task. A specific, existing task can be deleted by making a DELETE request on
the URL for that task. Deleted tasks go into the “trash” of the user
making the delete request. Tasks can be recovered from the trash within a
period of 30 days; afterward they are completely removed from the system.

Returns an empty data record.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Duplicate a task. Creates and returns a job that will asynchronously handle the duplication.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_aproject(self, completed_since: Annotated[Any, 'Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.\n'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get tasks from a project. Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "completed_since": completed_since,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_asection(self, completed_since: Annotated[Any, 'Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.\n'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get tasks from a section. *Board view only*: Returns the compact section records for all tasks within the given section.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
                "completed_since": completed_since,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_atag(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get tasks from a tag. Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_auser_task_list(self, completed_since: Annotated[Any, 'Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.\n'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get tasks from a user task list. Returns the compact list of tasks in a user’s My Tasks list.
*Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.*
*Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "completed_since": completed_since,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_subtasks_from_atask(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get subtasks from a task. Returns a compact representation of all of the subtasks of a task.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_asubtask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a subtask. Creates a new subtask and adds it to the parent task. Returns the full record for the newly created subtask.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_the_parent_of_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Set the parent of a task. parent, or no parent task at all. Returns an empty data block. When using `insert_before` and `insert_after`, at most one of those two options can be specified, and they must already be subtasks of the parent.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dependencies_from_atask(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get dependencies from a task. Returns the compact representations of all of the dependencies of a task.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_dependencies_for_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Set dependencies for a task. Marks a set of tasks as dependencies of this task, if they are not already dependencies. *A task can have at most 30 dependents and dependencies combined*.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unlink_dependencies_from_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Unlink dependencies from a task. Unlinks a set of dependencies from this task.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dependents_from_atask(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get dependents from a task. Returns the compact representations of all of the dependents of a task.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_dependents_for_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Set dependents for a task. Marks a set of tasks as dependents of this task, if they are not already dependents. *A task can have at most 30 dependents and dependencies combined*.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unlink_dependents_from_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Unlink dependents from a task. Unlinks a set of dependents from this task.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_aproject_to_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a project to a task. Adds the task to the specified project, in the optional location
specified. If no location arguments are given, the task will be added to
the end of the project.

`addProject` can also be used to reorder a task within a project or
section that already contains it.

At most one of `insert_before`, `insert_after`, or `section` should be
specified. Inserting into a section in an non-order-dependent way can be
done by specifying section, otherwise, to insert within a section in a
particular place, specify `insert_before` or `insert_after` and a task
within the section to anchor the position of this task.

A task can have at most 20 projects multi-homed to it.

Returns an empty data block.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_aproject_from_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a project from a task. Removes the task from the specified project. The task will still exist in
the system, but it will not be in the project anymore.

Returns an empty data block.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_atag_to_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a tag to a task. Adds a tag to a task. Returns an empty data block.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_atag_from_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a tag from a task. Removes a tag from a task. Returns an empty data block.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_followers_to_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add followers to a task. Adds followers to a task. Returns an empty data block.
Each task can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated task record, described above.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_followers_from_atask(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove followers from a task. Removes each of the specified followers from the task if they are following. Returns the complete, updated record for the affected task.
        
        Tags: Tasks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_for_agiven_custom_id(self, ) -> dict[str, Any]:
        """
        Get a task for a given custom ID. Returns a task given a custom ID shortcode.
        
        Tags: Tasks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_tasks_in_aworkspace(self, assigned_byany: Annotated[Any, 'Comma-separated list of user identifiers'] = None, assigned_bynot: Annotated[Any, 'Comma-separated list of user identifiers'] = None, assigneeany: Annotated[Any, 'Comma-separated list of user identifiers'] = None, assigneenot: Annotated[Any, 'Comma-separated list of user identifiers'] = None, commented_on_bynot: Annotated[Any, 'Comma-separated list of user identifiers'] = None, completed: Annotated[Any, 'Filter to completed tasks'] = None, completed_atafter: Annotated[Any, 'ISO 8601 datetime string'] = None, completed_atbefore: Annotated[Any, 'ISO 8601 datetime string'] = None, completed_on: Annotated[Any, 'ISO 8601 date string or `null`'] = None, completed_onafter: Annotated[Any, 'ISO 8601 date string'] = None, completed_onbefore: Annotated[Any, 'ISO 8601 date string'] = None, created_atafter: Annotated[Any, 'ISO 8601 datetime string'] = None, created_atbefore: Annotated[Any, 'ISO 8601 datetime string'] = None, created_byany: Annotated[Any, 'Comma-separated list of user identifiers'] = None, created_bynot: Annotated[Any, 'Comma-separated list of user identifiers'] = None, created_on: Annotated[Any, 'ISO 8601 date string or `null`'] = None, created_onafter: Annotated[Any, 'ISO 8601 date string'] = None, created_onbefore: Annotated[Any, 'ISO 8601 date string'] = None, due_atafter: Annotated[Any, 'ISO 8601 datetime string'] = None, due_atbefore: Annotated[Any, 'ISO 8601 datetime string'] = None, due_on: Annotated[Any, 'ISO 8601 date string or `null`'] = None, due_onafter: Annotated[Any, 'ISO 8601 date string'] = None, due_onbefore: Annotated[Any, 'ISO 8601 date string'] = None, followersnot: Annotated[Any, 'Comma-separated list of user identifiers'] = None, has_attachment: Annotated[Any, 'Filter to tasks with attachments'] = None, is_blocked: Annotated[Any, 'Filter to tasks with incomplete dependencies'] = None, is_blocking: Annotated[Any, 'Filter to incomplete tasks with dependents'] = None, is_subtask: Annotated[Any, 'Filter to subtasks'] = None, liked_bynot: Annotated[Any, 'Comma-separated list of user identifiers'] = None, modified_atafter: Annotated[Any, 'ISO 8601 datetime string'] = None, modified_atbefore: Annotated[Any, 'ISO 8601 datetime string'] = None, modified_on: Annotated[Any, 'ISO 8601 date string or `null`'] = None, modified_onafter: Annotated[Any, 'ISO 8601 date string'] = None, modified_onbefore: Annotated[Any, 'ISO 8601 date string'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, portfoliosany: Annotated[Any, 'Comma-separated list of portfolio IDs'] = None, projectsall: Annotated[Any, 'Comma-separated list of project IDs'] = None, projectsany: Annotated[Any, 'Comma-separated list of project IDs'] = None, projectsnot: Annotated[Any, 'Comma-separated list of project IDs'] = None, resource_subtype: Annotated[Any, "Filters results by the task's resource_subtype"] = None, sectionsall: Annotated[Any, 'Comma-separated list of section or column IDs'] = None, sectionsany: Annotated[Any, 'Comma-separated list of section or column IDs'] = None, sectionsnot: Annotated[Any, 'Comma-separated list of section or column IDs'] = None, sort_ascending: Annotated[Any, 'Default `false`'] = None, sort_by: Annotated[Any, 'One of `due_date`, `created_at`, `completed_at`, `likes`, or `modified_at`, defaults to `modified_at`'] = None, start_on: Annotated[Any, 'ISO 8601 date string or `null`'] = None, start_onafter: Annotated[Any, 'ISO 8601 date string'] = None, start_onbefore: Annotated[Any, 'ISO 8601 date string'] = None, tagsall: Annotated[Any, 'Comma-separated list of tag IDs'] = None, tagsany: Annotated[Any, 'Comma-separated list of tag IDs'] = None, tagsnot: Annotated[Any, 'Comma-separated list of tag IDs'] = None, teamsany: Annotated[Any, 'Comma-separated list of team IDs'] = None, text: Annotated[Any, 'Performs full-text search on both task name and description'] = None) -> dict[str, Any]:
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "text": text,
                "resource_subtype": resource_subtype,
                "assignee.any": assigneeany,
                "assignee.not": assigneenot,
                "portfolios.any": portfoliosany,
                "projects.any": projectsany,
                "projects.not": projectsnot,
                "projects.all": projectsall,
                "sections.any": sectionsany,
                "sections.not": sectionsnot,
                "sections.all": sectionsall,
                "tags.any": tagsany,
                "tags.not": tagsnot,
                "tags.all": tagsall,
                "teams.any": teamsany,
                "followers.not": followersnot,
                "created_by.any": created_byany,
                "created_by.not": created_bynot,
                "assigned_by.any": assigned_byany,
                "assigned_by.not": assigned_bynot,
                "liked_by.not": liked_bynot,
                "commented_on_by.not": commented_on_bynot,
                "due_on.before": due_onbefore,
                "due_on.after": due_onafter,
                "due_on": due_on,
                "due_at.before": due_atbefore,
                "due_at.after": due_atafter,
                "start_on.before": start_onbefore,
                "start_on.after": start_onafter,
                "start_on": start_on,
                "created_on.before": created_onbefore,
                "created_on.after": created_onafter,
                "created_on": created_on,
                "created_at.before": created_atbefore,
                "created_at.after": created_atafter,
                "completed_on.before": completed_onbefore,
                "completed_on.after": completed_onafter,
                "completed_on": completed_on,
                "completed_at.before": completed_atbefore,
                "completed_at.after": completed_atafter,
                "modified_on.before": modified_onbefore,
                "modified_on.after": modified_onafter,
                "modified_on": modified_on,
                "modified_at.before": modified_atbefore,
                "modified_at.after": modified_atafter,
                "is_blocking": is_blocking,
                "is_blocked": is_blocked,
                "has_attachment": has_attachment,
                "completed": completed,
                "is_subtask": is_subtask,
                "sort_by": sort_by,
                "sort_ascending": sort_ascending,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()
    
    def get_multiple_task_templates(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, project: Annotated[Any, 'The project to filter task templates on.'] = None) -> dict[str, Any]:
        """
        Get multiple task templates. Returns the compact task template records for some filtered set of task templates. You must specify a `project`
        
        Tags: Task templates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "project": project,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_template(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a task template. Returns the complete task template record for a single task template.
        
        Tags: Task templates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atask_template(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a task template. A specific, existing task template can be deleted by making a DELETE request on the URL for that task template. Returns an empty data record.
        
        Tags: Task templates
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def instantiate_atask_from_atask_template(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Instantiate a task from a task template. Creates and returns a job that will asynchronously handle the task instantiation.
        
        Tags: Task templates
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_ateam(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a team. Creates a team within the current workspace.
        
        Tags: Teams
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a team. Returns the full record for a single team.
        
        Tags: Teams
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_ateam(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a team. Updates a team within the current workspace.
        
        Tags: Teams
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_teams_in_aworkspace(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get teams in a workspace. Returns the compact records for all teams in the workspace visible to the authorized user.
        
        Tags: Teams
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_teams_for_auser(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, organization: Annotated[Any, '(Required) The workspace or organization to filter teams on.'] = None) -> dict[str, Any]:
        """
        Get teams for a user. Returns the compact records for all teams to which the given user is assigned.
        
        Tags: Teams
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
                "organization": organization,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_auser_to_ateam(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a user to a team. The user making this call must be a member of the team in order to add others. The user being added must exist in the same organization as the team.

Returns the complete team membership record for the newly added user.
        
        Tags: Teams
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_auser_from_ateam(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a user from a team. The user making this call must be a member of the team in order to remove themselves or others.
        
        Tags: Teams
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_membership(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a team membership. Returns the complete team membership record for a single team membership.
        
        Tags: Team memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_memberships(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, team: Annotated[Any, 'Globally unique identifier for the team.'] = None, user: Annotated[Any, 'A string identifying a user. This can either be the string "me", an email, or the gid of a user. This parameter must be used with the workspace parameter.'] = None, workspace: Annotated[Any, 'Globally unique identifier for the workspace. This parameter must be used with the user parameter.'] = None) -> dict[str, Any]:
        """
        Get team memberships. Returns compact team membership records.
        
        Tags: Team memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "team": team,
                "user": user,
                "workspace": workspace,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_ateam(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get memberships from a team. Returns the compact team memberships for the team.
        
        Tags: Team memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_auser(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, workspace: Annotated[Any, '(Required) Globally unique identifier for the workspace.'] = None) -> dict[str, Any]:
        """
        Get memberships from a user. Returns the compact team membership records for the user.
        
        Tags: Team memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "workspace": workspace,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atime_period(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a time period. Returns the full record for a single time period.
        
        Tags: Time periods
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_time_periods(self, end_on: Annotated[Any, 'ISO 8601 date string'] = None, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, start_on: Annotated[Any, 'ISO 8601 date string'] = None, workspace: Annotated[Any, '(Required) Globally unique identifier for the workspace.'] = None) -> dict[str, Any]:
        """
        Get time periods. Returns compact time period records.
        
        Tags: Time periods
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "start_on": start_on,
                "end_on": end_on,
                "workspace": workspace,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_time_tracking_entries_for_atask(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get time tracking entries for a task. Returns time tracking entries for a given task.
        
        Tags: Time tracking entries
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atime_tracking_entry(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Create a time tracking entry. Creates a time tracking entry on a given task.

Returns the record of the newly created time tracking entry.
        
        Tags: Time tracking entries
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atime_tracking_entry(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a time tracking entry. Returns the complete time tracking entry record for a single time tracking entry.
        
        Tags: Time tracking entries
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atime_tracking_entry(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a time tracking entry. A specific, existing time tracking entry can be updated by making a `PUT` request on
the URL for that time tracking entry. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated time tracking entry record.
        
        Tags: Time tracking entries
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atime_tracking_entry(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a time tracking entry. A specific, existing time tracking entry can be deleted by making a `DELETE` request on
the URL for that time tracking entry.

Returns an empty data record.
        
        Tags: Time tracking entries
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_objects_via_typeahead(self, count: Annotated[Any, 'The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned.'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, query: Annotated[Any, 'The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results.'] = None, resource_type: Annotated[Any, '(Required) The type of values the typeahead should return. You can choose from one of the following: `custom_field`, `goal`, `project`, `project_template`, `portfolio`, `tag`, `task`, `team`, and `user`. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. `task`). Using multiple types is not yet supported.'] = None, type: Annotated[Any, '*Deprecated: new integrations should prefer the resource_type field.*'] = None) -> dict[str, Any]:
        """
        Get objects via typeahead. Retrieves objects in the workspace based via an auto-completion/typeahead
search algorithm. This feature is meant to provide results quickly, so do
not rely on this API to provide extremely accurate search results. The
result set is limited to a single page of results with a maximum size, so
you won’t be able to fetch large numbers of results.

The typeahead search API provides search for objects from a single
workspace. This endpoint should be used to query for objects when
creating an auto-completion/typeahead search feature. This API is meant
to provide results quickly and should not be relied upon for accurate or
exhaustive search results. The results sets are limited in size and
cannot be paginated.

Queries return a compact representation of each object which is typically
the gid and name fields. Interested in a specific set of fields or all of
the fields?! Of course you are. Use field selectors to manipulate what
data is included in a response.

Resources with type `user` are returned in order of most contacted to
least contacted. This is determined by task assignments, adding the user
to projects, and adding the user as a follower to tasks, messages,
etc.

Resources with type `project` are returned in order of recency. This is
determined when the user visits the project, is added to the project, and
completes tasks in the project.

Resources with type `task` are returned with priority placed on tasks
the user is following, but no guarantee on the order of those tasks.

Resources with type `project_template` are returned with priority
placed on favorited project templates.

Leaving the `query` string empty or omitted will give you results, still
following the resource ordering above. This could be used to list users or
projects that are relevant for the requesting user's api token.
        
        Tags: Typeahead
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "resource_type": resource_type,
                "type": type,
                "query": query,
                "count": count,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_users(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, team: Annotated[Any, 'The team ID to filter users on.'] = None, workspace: Annotated[Any, 'The workspace or organization ID to filter users on.'] = None) -> dict[str, Any]:
        """
        Get multiple users. Returns the user records for all users in all workspaces and organizations accessible to the authenticated user. Accepts an optional workspace ID parameter.
Results are sorted by user ID.
        
        Tags: Users
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "workspace": workspace,
                "team": team,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a user. Returns the full user record for the single user with the provided ID.
        
        Tags: Users
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_sfavorites(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, resource_type: Annotated[Any, '(Required) The resource type of favorites to be returned.'] = None, workspace: Annotated[Any, '(Required) The workspace in which to get favorites.'] = None) -> dict[str, Any]:
        """
        Get a user's favorites. Returns all of a user's favorites in the given workspace, of the given type.
Results are given in order (The same order as Asana's sidebar).
        
        Tags: Users
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
                "resource_type": resource_type,
                "workspace": workspace,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_in_ateam(self, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get users in a team. Returns the compact records for all users that are members of the team.
Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.
        
        Tags: Users
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_in_aworkspace_or_organization(self, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get users in a workspace or organization. Returns the compact records for all users in the specified workspace or organization.
Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.
        
        Tags: Users
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_task_list(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a user task list. Returns the full record for a user task list.
        
        Tags: User task lists
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_stask_list(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, workspace: Annotated[Any, '(Required) The workspace in which to get the user task list.'] = None) -> dict[str, Any]:
        """
        Get a user's task list. Returns the full record for a user's task list.
        
        Tags: User task lists
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "workspace": workspace,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_webhooks(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, resource: Annotated[Any, 'Only return webhooks for the given resource.'] = None, workspace: Annotated[Any, '(Required) The workspace to query for webhooks in.'] = None) -> dict[str, Any]:
        """
        Get multiple webhooks. Get the compact representation of all webhooks your app has registered for the authenticated user in the given workspace.
        
        Tags: Webhooks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "workspace": workspace,
                "resource": resource,
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def establish_awebhook(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Establish a webhook. Establishing a webhook is a two-part process. First, a simple HTTP POST
request initiates the creation similar to creating any other resource.

Next, in the middle of this request comes the confirmation handshake.
When a webhook is created, we will send a test POST to the target with an
`X-Hook-Secret` header. The target must respond with a `200 OK` or `204
No Content` and a matching `X-Hook-Secret` header to confirm that this
webhook subscription is indeed expected. We strongly recommend storing
this secret to be used to verify future webhook event signatures.

The POST request to create the webhook will then return with the status
of the request. If you do not acknowledge the webhook’s confirmation
handshake it will fail to setup, and you will receive an error in
response to your attempt to create it. This means you need to be able to
receive and complete the webhook *while* the POST request is in-flight
(in other words, have a server that can handle requests asynchronously).

Invalid hostnames like localhost will receive a 403 Forbidden status code.

```
# Request
curl -H "Authorization: Bearer <personal_access_token>" \
-X POST https://app.asana.com/api/1.0/webhooks \
-d "resource=8675309" \
-d "target=https://example.com/receive-webhook/7654"
```

```
# Handshake sent to https://example.com/
POST /receive-webhook/7654
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Handshake response sent by example.com
HTTP/1.1 200
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Response
HTTP/1.1 201
{
  "data": {
    "gid": "43214",
    "resource": {
      "gid": "8675309",
      "name": "Bugs"
    },
    "target": "https://example.com/receive-webhook/7654",
    "active": false,
    "last_success_at": null,
    "last_failure_at": null,
    "last_failure_content": null
  },
  "X-Hook-Secret": "b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81"
}
```
        
        Tags: Webhooks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_awebhook(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a webhook. Returns the full record for the given webhook.
        
        Tags: Webhooks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_awebhook(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a webhook. An existing webhook's filters can be updated by making a PUT request on the URL for that webhook. Note that the webhook's previous `filters` array will be completely overwritten by the `filters` sent in the PUT request.
        
        Tags: Webhooks
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_awebhook(self, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Delete a webhook. This method *permanently* removes a webhook. Note that it may be possible to receive a request that was already in flight after deleting the webhook, but no further requests will be issued.
        
        Tags: Webhooks
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_workspaces(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get multiple workspaces. Returns the compact records for all workspaces visible to the authorized user.
        
        Tags: Workspaces
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a workspace. Returns the full workspace record for a single workspace.
        
        Tags: Workspaces
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aworkspace(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Update a workspace. A specific, existing workspace can be updated by making a PUT request on the URL for that workspace. Only the fields provided in the data block will be updated; any unspecified fields will remain unchanged.
Currently the only field that can be modified for a workspace is its name.
Returns the complete, updated workspace record.
        
        Tags: Workspaces
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_auser_to_aworkspace_or_organization(self, data: Annotated[dict[str, Any], ''] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Add a user to a workspace or organization. Add a user to a workspace or organization.
The user can be referenced by their globally unique user ID or their email address. Returns the full user record for the invited user.
        
        Tags: Workspaces
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_auser_from_aworkspace_or_organization(self, data: Annotated[dict[str, Any], ''] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Remove a user from a workspace or organization. Remove a user from a workspace or organization.
The user making this call must be an admin in the workspace. The user can be referenced by their globally unique user ID or their email address.
Returns an empty data record.
        
        Tags: Workspaces
        
        """
        
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace_membership(self, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get a workspace membership. Returns the complete workspace record for a single workspace membership.
        
        Tags: Workspace memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_workspace_memberships_for_auser(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None) -> dict[str, Any]:
        """
        Get workspace memberships for a user. Returns the compact workspace membership records for the user.
        
        Tags: Workspace memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_the_workspace_memberships_for_aworkspace(self, limit: Annotated[Any, 'Results per page.\nThe number of objects to return per page. The value must be between 1 and 100.'] = None, offset: Annotated[Any, 'Offset token.\nAn offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.\n*Note: You can only pass in an offset that was returned to you via a previously paginated request.*'] = None, opt_fields: Annotated[Any, 'This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.'] = None, opt_pretty: Annotated[Any, 'Provides “pretty” output.\nProvides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.'] = None, user: Annotated[Any, 'A string identifying a user. This can either be the string "me", an email, or the gid of a user.'] = None) -> dict[str, Any]:
        """
        Get the workspace memberships for a workspace. Returns the compact workspace membership records for the workspace.
        
        Tags: Workspace memberships
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "opt_fields": opt_fields,
                "user": user,
                "opt_pretty": opt_pretty,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()


    def list_tools(self):
        return [
            
            self.get_an_allocation,
            self.update_an_allocation,
            self.delete_an_allocation,
            self.get_multiple_allocations,
            self.create_an_allocation,
            self.get_an_attachment,
            self.delete_an_attachment,
            self.get_attachments_from_an_object,
            self.upload_an_attachment,
            self.get_audit_log_events,
            self.submit_parallel_requests,
            self.create_acustom_field,
            self.get_acustom_field,
            self.update_acustom_field,
            self.delete_acustom_field,
            self.get_aworkspace_scustom_fields,
            self.create_an_enum_option,
            self.reorder_acustom_field_senum,
            self.update_an_enum_option,
            self.get_aproject_scustom_fields,
            self.get_aportfolio_scustom_fields,
            self.get_events_on_aresource,
            self.get_agoal,
            self.update_agoal,
            self.delete_agoal,
            self.get_goals,
            self.create_agoal,
            self.create_agoal_metric,
            self.update_agoal_metric,
            self.add_acollaborator_to_agoal,
            self.remove_acollaborator_from_agoal,
            self.get_parent_goals_from_agoal,
            self.get_agoal_relationship,
            self.update_agoal_relationship,
            self.get_goal_relationships,
            self.add_asupporting_goal_relationship,
            self.removes_asupporting_goal_relationship,
            self.get_ajob_by_id,
            self.get_multiple_memberships,
            self.create_amembership,
            self.get_amembership,
            self.update_amembership,
            self.delete_amembership,
            self.create_an_organization_export_request,
            self.get_details_on_an_org_export_request,
            self.get_multiple_portfolios,
            self.create_aportfolio,
            self.get_aportfolio,
            self.update_aportfolio,
            self.delete_aportfolio,
            self.get_portfolio_items,
            self.add_aportfolio_item,
            self.remove_aportfolio_item,
            self.add_acustom_field_to_aportfolio,
            self.remove_acustom_field_from_aportfolio,
            self.add_users_to_aportfolio,
            self.remove_users_from_aportfolio,
            self.get_multiple_portfolio_memberships,
            self.get_aportfolio_membership,
            self.get_memberships_from_aportfolio,
            self.get_multiple_projects,
            self.create_aproject,
            self.get_aproject,
            self.update_aproject,
            self.delete_aproject,
            self.duplicate_aproject,
            self.get_projects_atask_is_in,
            self.get_ateam_sprojects,
            self.create_aproject_in_ateam,
            self.get_all_projects_in_aworkspace,
            self.create_aproject_in_aworkspace,
            self.add_acustom_field_to_aproject,
            self.remove_acustom_field_from_aproject,
            self.get_task_count_of_aproject,
            self.add_users_to_aproject,
            self.remove_users_from_aproject,
            self.add_followers_to_aproject,
            self.remove_followers_from_aproject,
            self.create_aproject_template_from_aproject,
            self.get_aproject_brief,
            self.update_aproject_brief,
            self.delete_aproject_brief,
            self.create_aproject_brief,
            self.get_aproject_membership,
            self.get_memberships_from_aproject,
            self.get_aproject_status,
            self.delete_aproject_status,
            self.get_statuses_from_aproject,
            self.create_aproject_status,
            self.get_aproject_template,
            self.delete_aproject_template,
            self.get_multiple_project_templates,
            self.get_ateam_sproject_templates,
            self.instantiate_aproject_from_aproject_template,
            self.trigger_arule,
            self.get_asection,
            self.update_asection,
            self.delete_asection,
            self.get_sections_in_aproject,
            self.create_asection_in_aproject,
            self.add_task_to_section,
            self.move_or_insert_sections,
            self.get_astatus_update,
            self.delete_astatus_update,
            self.get_status_updates_from_an_object,
            self.create_astatus_update,
            self.get_astory,
            self.update_astory,
            self.delete_astory,
            self.get_stories_from_atask,
            self.create_astory_on_atask,
            self.get_multiple_tags,
            self.create_atag,
            self.get_atag,
            self.update_atag,
            self.delete_atag,
            self.get_atask_stags,
            self.get_tags_in_aworkspace,
            self.create_atag_in_aworkspace,
            self.get_multiple_tasks,
            self.create_atask,
            self.get_atask,
            self.update_atask,
            self.delete_atask,
            self.duplicate_atask,
            self.get_tasks_from_aproject,
            self.get_tasks_from_asection,
            self.get_tasks_from_atag,
            self.get_tasks_from_auser_task_list,
            self.get_subtasks_from_atask,
            self.create_asubtask,
            self.set_the_parent_of_atask,
            self.get_dependencies_from_atask,
            self.set_dependencies_for_atask,
            self.unlink_dependencies_from_atask,
            self.get_dependents_from_atask,
            self.set_dependents_for_atask,
            self.unlink_dependents_from_atask,
            self.add_aproject_to_atask,
            self.remove_aproject_from_atask,
            self.add_atag_to_atask,
            self.remove_atag_from_atask,
            self.add_followers_to_atask,
            self.remove_followers_from_atask,
            self.get_atask_for_agiven_custom_id,
            self.search_tasks_in_aworkspace,
            self.get_multiple_task_templates,
            self.get_atask_template,
            self.delete_atask_template,
            self.instantiate_atask_from_atask_template,
            self.create_ateam,
            self.get_ateam,
            self.update_ateam,
            self.get_teams_in_aworkspace,
            self.get_teams_for_auser,
            self.add_auser_to_ateam,
            self.remove_auser_from_ateam,
            self.get_ateam_membership,
            self.get_team_memberships,
            self.get_memberships_from_ateam,
            self.get_memberships_from_auser,
            self.get_atime_period,
            self.get_time_periods,
            self.get_time_tracking_entries_for_atask,
            self.create_atime_tracking_entry,
            self.get_atime_tracking_entry,
            self.update_atime_tracking_entry,
            self.delete_atime_tracking_entry,
            self.get_objects_via_typeahead,
            self.get_multiple_users,
            self.get_auser,
            self.get_auser_sfavorites,
            self.get_users_in_ateam,
            self.get_users_in_aworkspace_or_organization,
            self.get_auser_task_list,
            self.get_auser_stask_list,
            self.get_multiple_webhooks,
            self.establish_awebhook,
            self.get_awebhook,
            self.update_awebhook,
            self.delete_awebhook,
            self.get_multiple_workspaces,
            self.get_aworkspace,
            self.update_aworkspace,
            self.add_auser_to_aworkspace_or_organization,
            self.remove_auser_from_aworkspace_or_organization,
            self.get_aworkspace_membership,
            self.get_workspace_memberships_for_auser,
            self.get_the_workspace_memberships_for_aworkspace
        ] 