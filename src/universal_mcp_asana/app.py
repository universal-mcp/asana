from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class AsanaApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='asanaapp', integration=integration, **kwargs)
        self.base_url = "https://app.asana.com/api/1.0"

    def get_an_allocation(self, allocation_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a complete allocation record for a single allocation.
        
        Args:
            opt_fields: Optional fields to include in the response. Pass a comma-separated list to include additional properties.
            opt_pretty: Returns the response in a 'pretty' format, useful for debugging.
        
        Returns:
            A dictionary containing the allocation record.
        
        Tags:
            allocation, management, important
        """
        if allocation_gid is None:
            raise ValueError("Missing required parameter 'allocation_gid'")
        url = f"{self.base_url}/allocations/{allocation_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_allocation(self, allocation_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing allocation by making a PUT request. Only specified fields are updated, and the complete updated allocation record is returned.
        
        Args:
            data: Dictionary containing fields to update. Only fields provided here will be changed.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Boolean to get the response in a formatted, human-readable format.
        
        Returns:
            A dictionary representing the complete updated allocation record.
        
        Raises:
            HTTPError: Raised if there is a problem with the request, such as a 4xx or 5xx status code.
        
        Tags:
            update, allocation, important, management
        """
        if allocation_gid is None:
            raise ValueError("Missing required parameter 'allocation_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/allocations/{allocation_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_allocation(self, allocation_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific allocation by making a DELETE request to its URL and returns an empty data record upon success.
        
        Args:
            opt_pretty: Provides 'pretty' output formatting for the response. Enables proper line breaking and indentation in JSON output, which increases response size and processing time. Recommended for debugging purposes only.
        
        Returns:
            dict[str, Any]: An empty dictionary representing the deleted allocation's data record.
        
        Raises:
            HTTPError: Raises HTTP errors for unsuccessful API requests (4xx/5xx status codes).
        
        Tags:
            delete, allocations, management, important
        """
        if allocation_gid is None:
            raise ValueError("Missing required parameter 'allocation_gid'")
        url = f"{self.base_url}/allocations/{allocation_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_allocations(self, parent=None, assignee=None, workspace=None, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Fetches a list of allocations filtered by specific parameters like project, user, and pagination details.
        
        Args:
            assignee: Globally unique identifier for the user the allocation is assigned to.
            limit: Number of objects to return per page (between 1 and 100).
            offset: Offset token for pagination to retrieve the next page of results.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Flag to provide the response in a pretty format (for debugging purposes).
            parent: Globally unique identifier for the project to filter allocations by.
            workspace: Globally unique identifier for the workspace.
        
        Returns:
            A dictionary containing the list of filtered allocations.
        
        Raises:
            HTTPError: Raised if the HTTP request fails (e.g., due to an invalid response code).
        
        Tags:
            fetch, allocations, pagination, management, important
        """
        url = f"{self.base_url}/allocations"
        query_params = {k: v for k, v in [('parent', parent), ('assignee', assignee), ('workspace', workspace), ('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_allocation(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new allocation and returns its full record.
        
        Args:
            data: Dictionary containing allocation data. Required fields should be provided here.
            opt_fields: Optional comma-separated list of fields to include in the response.
            opt_pretty: Provides formatted output for better readability during debugging (increases response size).
        
        Returns:
            Dictionary containing the full record of the newly created allocation.
        
        Raises:
            HTTPError: If the API request fails due to invalid data or server errors.
        
        Tags:
            create, allocation, http-post, management, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/allocations"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_an_attachment(self, attachment_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Get the full record for a single attachment, optionally including additional fields and pretty-printed output.
        
        Args:
            opt_fields: Optional comma-separated list of properties to include in the response, beyond the default set.
            opt_pretty: Flag to provide 'pretty' output with proper line breaks and indentation, primarily useful for debugging.
        
        Returns:
            A dictionary containing the attachment record, formatted as requested.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            attachments, fetch, get, api-call, important
        """
        if attachment_gid is None:
            raise ValueError("Missing required parameter 'attachment_gid'")
        url = f"{self.base_url}/attachments/{attachment_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_an_attachment(self, attachment_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific, existing attachment and returns an empty data record.
        
        Args:
            opt_pretty: Provides the response in a 'pretty' format. This means proper line breaking and indentation for JSON, which is advisable for debugging only.
        
        Returns:
            An empty data record as a dictionary.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, attachment, management
        """
        if attachment_gid is None:
            raise ValueError("Missing required parameter 'attachment_gid'")
        url = f"{self.base_url}/attachments/{attachment_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_attachments_from_an_object(self, limit=None, offset=None, parent=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a list of attachments from a specified object, which can be a project, project brief, or task.
        
        Args:
            limit: Results per page. The number of objects to return per page (1-100). Defaults to None.
            offset: Offset token. Used for pagination; must be obtained from a previous API call.
            opt_fields: Optional properties to include. Pass a comma-separated list of properties to include.
            opt_pretty: Provides pretty output. Useful for debugging, makes JSON more readable but increases response size.
            parent: Globally unique identifier for the object (project, project brief, or task). Required.
        
        Returns:
            A dictionary containing compact records for all attachments on the object.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails with an HTTP error.
        
        Tags:
            attachments, pagination, important
        """
        url = f"{self.base_url}/attachments"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('parent', parent), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_audit_log_events(self, workspace_gid, start_at=None, end_at=None, event_type=None, actor_type=None, actor_gid=None, resource_gid=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve audit log events from your domain, with options to filter by various criteria such as actor ID, event type, and time range.
        
        Args:
            actor_gid: Filter to events triggered by the actor with this ID.
            actor_type: Filter to events with an actor of this type. Used when actor_gid is not provided.
            end_at: Filter to events created before this time (exclusive).
            event_type: Filter to events of this type. Refer to supported audit log events for full list.
            limit: Results per page. Must be between 1 and 100.
            offset: Offset token for pagination. Returned in the API response.
            resource_gid: Filter to events with this resource ID.
            start_at: Filter to events created after this time (inclusive).
        
        Returns:
            A dictionary containing paginated audit log events. Events are sorted by creation time in ascending order.
        
        Raises:
            HTTPError: If the request to the API fails due to an HTTP error.
        
        Tags:
            audit, log, api, pagination, filtering, important, management
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/audit_log_events"
        query_params = {k: v for k, v in [('start_at', start_at), ('end_at', end_at), ('event_type', event_type), ('actor_type', actor_type), ('actor_gid', actor_gid), ('resource_gid', resource_gid), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def submit_parallel_requests(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Submits multiple API requests in parallel to Asana's batch endpoints, enabling efficient batch processing of operations.
        
        Args:
            data: Dictionary containing request payload data to be submitted to Asana's batch API endpoints.
            opt_fields: Comma-separated list of optional fields to include in response. Specify properties to return when default compact responses are insufficient.
            opt_pretty: Enables pretty-printed JSON output at the cost of performance. Recommended only for debugging.
        
        Returns:
            Dictionary containing API response data parsed from JSON, including results from parallel requests processing.
        
        Raises:
            requests.exceptions.HTTPError: Raised when API request fails with non-2XX status code, typically indicating authorization errors (4XX) or server issues (5XX).
        
        Tags:
            batch, async-job, request, api, asana, parallel-processing, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/batch"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_acustom_field(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new custom field in a workspace with a unique name and valid type.
        
        Args:
            data: Dictionary containing custom field definition. Must include required fields for creation according to API specifications.
            opt_fields: Comma-separated list of optional properties to include in response. Excluded properties return in compact resource by default.
            opt_pretty: Enables formatted JSON output for readability during debugging.
        
        Returns:
            Full record of the newly created custom field as a dictionary containing all configured properties.
        
        Raises:
            HTTPError: Raised for invalid requests, name conflicts with existing fields, or invalid custom field types (e.g., non-supported type values).
        
        Tags:
            create, custom-field, workspace, management, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_acustom_field(self, custom_field_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve complete metadata definition of a custom field, including type-specific properties and behaviors.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include (default excludes some properties)
            opt_pretty: Enable pretty-printed JSON output for human readability (increases response time and size)
        
        Returns:
            Dictionary containing full custom field metadata with requested fields included
        
        Raises:
            HTTPError: If API request fails due to server error or invalid parameters
        
        Tags:
            custom-fields, metadata, get, api, resource, important
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        url = f"{self.base_url}/custom_fields/{custom_field_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_acustom_field(self, custom_field_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing custom field with provided data, returning the complete updated record. Only specified fields are modified, preserving existing values.
        
        Args:
            data: Dictionary containing custom field properties to update. Unspecified fields remain unchanged.
            opt_fields: Comma-separated string of optional properties to include in the response.
            opt_pretty: Boolean flag for formatted JSON output (increases response size).
        
        Returns:
            Dictionary containing full updated custom field record including all specified fields.
        
        Raises:
            HTTPError: Raised for failed API requests (4XX/5XX status codes), typically due to invalid input data or authorization issues.
            ValueError: May occur if attempting to modify read-only fields like 'type' or locked fields without proper permissions.
        
        Tags:
            custom-fields, update, management, important, api
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields/{custom_field_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_acustom_field(self, custom_field_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific existing custom field using a DELETE request to its URL. Locked fields can only be deleted by the locking user.
        
        Args:
            opt_pretty: If True, returns formatted JSON response (recommended for debugging only). Adds line breaks and indentation, increasing response size and processing time.
        
        Returns:
            dict[str, Any]: Empty dictionary on successful deletion ({}), representing an empty data record
        
        Raises:
            requests.HTTPError: Raised for invalid permissions (locked fields deleted by non-owner), non-existent fields, or server errors
        
        Tags:
            delete, custom-field, api-client, management, important
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        url = f"{self.base_url}/custom_fields/{custom_field_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace_scustom_fields(self, workspace_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves a list of compact representations of custom fields within a workspace.
        
        Args:
            limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
            offset: Offset token. An offset to the next page returned by the API. Used for pagination.
            opt_fields: Optional fields to include in the response. A comma-separated list of properties.
            opt_pretty: Provides the response in a 'pretty' format: properly formatted JSON for readability.
        
        Returns:
            A dictionary containing the list of custom fields.
        
        Raises:
            requests.HTTPError: Raised if there is an HTTP request issue, such as a 4xx or 5xx status code.
        
        Tags:
            custom-fields, list, management, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/custom_fields"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_enum_option(self, custom_field_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates an enum option for a custom field, adds it to the field's enum list, and returns the full record of the new option.
        
        Args:
            data: A dictionary containing the data required to create the enum option. Must include mandatory fields for enum creation.
            opt_fields: Comma-separated list of optional properties to include in the response. By default, the endpoint returns a compact resource.
            opt_pretty: When True, formats the JSON response with indentation and line breaks for improved readability (use only during debugging due to performance impact).
        
        Returns:
            A dictionary containing the full record of the newly created enum option.
        
        Raises:
            HTTPError: Raised if the API request fails, e.g., due to exceeding the 500-enum-option limit, unauthorized modification of locked fields, or invalid input data.
        
        Tags:
            custom-fields, enum-options, create, management, important
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields/{custom_field_gid}/enum_options"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def reorder_acustom_field_senum(self, custom_field_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Reorders a custom field's enum. Moves an enum option to be either before or after another specified enum option.
        
        Args:
            data: The data used to update the custom field; an annotated dictionary with potential enum reordering specifications.
            opt_fields: Optional fields to include in the response, specified as a comma-separated list of property names.
            opt_pretty: Boolean indicating whether the response should be in a pretty format (e.g., JSON with line breaks and indentation).
        
        Returns:
            A dictionary containing the updated custom field data.
        
        Raises:
            RequestException: Raised if there is an issue with the HTTP request (e.g., network errors or server errors).
            HTTPError: Raised if the HTTP response indicates an error (e.g., a non-successful status code).
        
        Tags:
            custom_fields, enum_reorder, management, important
        """
        if custom_field_gid is None:
            raise ValueError("Missing required parameter 'custom_field_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/custom_fields/{custom_field_gid}/enum_options/insert"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_an_enum_option(self, enum_option_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing enum option for custom fields and returns the full record. Locked fields can only be updated by the locking user.
        
        Args:
            data: Dictionary containing the updated enum option data
            opt_fields: Comma-separated list of optional properties to include. Excludes some properties by default.
            opt_pretty: Provides formatted output. Increases response time and size, recommended for debugging.
        
        Returns:
            Full record of the updated enum option as a dictionary
        
        Raises:
            HTTPError: Raised on API request failure (e.g., invalid data, insufficient permissions)
        
        Tags:
            update, enum, custom-fields, async-job, api-call, important
        """
        if enum_option_gid is None:
            raise ValueError("Missing required parameter 'enum_option_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/enum_options/{enum_option_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_scustom_fields(self, project_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Fetches and returns a project's custom fields settings, allowing pagination and optional inclusion of additional fields.
        
        Args:
            limit: Results per page. The number of objects to return per page, between 1 and 100.
            offset: Offset token. Used for pagination to retrieve the next page of results.
            opt_fields: A comma-separated list of optional fields to include beyond the compact form.
            opt_pretty: Enables pretty formatting for the response, primarily for debugging purposes.
        
        Returns:
            A dictionary containing the custom fields settings for a project.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request encounters a status-related error.
        
        Tags:
            custom-fields, pagination, api-call, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/custom_field_settings"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio_scustom_fields(self, portfolio_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Fetches a portfolio's custom fields from the API, returning them in a compact form.
        
        Args:
            limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
            offset: Offset token. An offset to the next page returned by the API.
            opt_fields: Optional fields to include in the response. Pass a comma-separated list of properties to include.
            opt_pretty: Provides 'pretty' output for debugging purposes, such as proper line breaking and indentation in JSON responses.
        
        Returns:
            A dictionary containing the custom fields settings.
        
        Raises:
            HTTPError: If the HTTP request returns an unsuccessful status code.
        
        Tags:
            custom, portfolio, fetch, pagination, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}/custom_field_settings"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_events_on_aresource(self, opt_fields=None, resource=None, sync=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a list of events that have occurred on a specified resource since the sync token was generated.
        
        Args:
            opt_fields: Optional fields to include in the response, specified as a comma-separated list.
            opt_pretty: Provides 'pretty' output for debugging purposes, adding line breaks and indentation to the response.
            resource: Required resource ID for tasks, projects, or goals.
            sync: Sync token for retrieving events from the point in time it was generated; omit on first request.
        
        Returns:
            A dictionary containing full event records and metadata.
        
        Raises:
            HTTPError: Raised if the HTTP request fails, such as a 412 Precondition Failed error due to an expired sync token.
        
        Tags:
            events, sync, async_job, management, important
        """
        url = f"{self.base_url}/events"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('resource', resource), ('sync', sync), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agoal(self, goal_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a complete goal record for a single goal, allowing optional fields and pretty output.
        
        Args:
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: Enables pretty output for debugging purposes.
        
        Returns:
            A dictionary containing the goal record.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request does not return a successful status code.
        
        Tags:
            goal, management, fetch, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        url = f"{self.base_url}/goals/{goal_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal(self, goal_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Update an existing goal by sending a PUT request to the specified URL. Only provided fields are updated, leaving unspecified fields unchanged.
        
        Args:
            data: A dictionary containing the fields to be updated in the goal.
            opt_fields: A comma-separated list of optional properties to include in the response.
            opt_pretty: Flag to provide the response in a readable, pretty format, useful for debugging.
        
        Returns:
            The complete updated goal record as a dictionary.
        
        Raises:
            requests.exceptions.HTTPError: Raised if an HTTP request error occurs, such as a bad status code.
        
        Tags:
            update, goals, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_agoal(self, goal_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific existing goal by sending a DELETE request to the goal's URL.
        
        Args:
            opt_pretty: If True, returns response in a human-readable format at the cost of performance and response size. Recommended only for debugging purposes.
        
        Returns:
            A dictionary containing the empty data record of the deleted goal.
        
        Raises:
            HTTPError: Raised if the HTTP request fails, typically due to invalid goal ID, insufficient permissions, or server issues.
        
        Tags:
            delete, async_job, goals, management, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        url = f"{self.base_url}/goals/{goal_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_goals(self, portfolio=None, project=None, task=None, is_workspace_level=None, team=None, workspace=None, time_periods=None, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Fetches compact goal records based on specified parameters.
        
        Args:
            is_workspace_level: Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter.
            limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
            offset: Offset token. Used for pagination, it must be obtained from a previous paginated request.
            opt_fields: Optional fields to include in the response. Specify as a comma-separated list.
            opt_pretty: Provides the response in a readable format. Advisable only for debugging.
            portfolio: Globally unique identifier for supporting portfolio.
            project: Globally unique identifier for supporting project.
            task: Globally unique identifier for supporting task.
            team: Globally unique identifier for the team.
            time_periods: Globally unique identifiers for the time periods.
            workspace: Globally unique identifier for the workspace.
        
        Returns:
            A dictionary containing compact goal records.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            fetch, goals, list, management, important
        """
        url = f"{self.base_url}/goals"
        query_params = {k: v for k, v in [('portfolio', portfolio), ('project', project), ('task', task), ('is_workspace_level', is_workspace_level), ('team', team), ('workspace', workspace), ('time_periods', time_periods), ('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_agoal(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new goal in a workspace or team and returns the full record of the newly created goal.
        
        Args:
            data: Dictionary containing goal creation data. Optional.
            opt_fields: Optional comma-separated list of properties to include in the response.
            opt_pretty: Option to format the response in a 'pretty' format for readability.
        
        Returns:
            The full record of the newly created goal as a dictionary.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as network errors.
        
        Tags:
            create, goal, management, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_agoal_metric(self, goal_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates and adds a goal metric to a specified goal, replacing any existing metric.
        
        Args:
            data: The data dictionary for the goal metric; may be None if not provided.
            opt_fields: Optional fields to include in the request; a comma-separated list of properties.
            opt_pretty: Option to enable pretty output, useful for debugging with formatted JSON.
        
        Returns:
            A dictionary containing the response data for the created goal metric.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as network errors or invalid responses.
        
        Tags:
            create, goal-metric, management, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/setMetric"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal_metric(self, goal_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Update a goal's existing metric's current value and return the updated metric record.
        
        Args:
            data: Dictionary containing the goal metric data to be updated. Must include the current_number_value for existing metrics.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Flag to enable pretty-printed JSON output for debugging purposes.
        
        Returns:
            Dictionary representing the complete updated goal metric record.
        
        Raises:
            HTTPError: If the request fails, typically with 400 status code when no existing metric is found.
        
        Tags:
            update, goals, metric, management, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/setMetricCurrentValue"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acollaborator_to_agoal(self, goal_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds collaborators as followers to a goal and returns the updated goal data.
        
        Args:
            data: Dictionary containing collaborator data to associate with the goal.
            opt_fields: Optional comma-separated list of fields to include (provides compact responses by default).
            opt_pretty: Provides formatted output for readability during debugging (increases response size).
        
        Returns:
            Dictionary containing the updated goal data with new collaborators/followers.
        
        Raises:
            HTTPError: Raised for failed API requests (4XX/5XX status codes).
        
        Tags:
            add, collaborator, goal, followers, update, management, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/addFollowers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acollaborator_from_agoal(self, goal_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Removes a collaborator from a goal and returns the updated goal record.
        
        Args:
            data: Dictionary containing data for the removal request. It can be None if no specific data is required.
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: Provides 'pretty' output with proper formatting, suitable for debugging.
        
        Returns:
            A dictionary representing the updated goal record.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            remove, collaborator, goal, management, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/removeFollowers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_parent_goals_from_agoal(self, goal_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves parent goals from a specific goal, returning them in a compact format.
        
        Args:
            opt_fields: Optional comma-separated list of fields to include beyond the default compact resource.
            opt_pretty: Optional parameter for formatting the output in a more readable format.
        
        Returns:
            A dictionary containing the parent goals.
        
        Raises:
            HTTPError: Raised if the request fails, indicating an issue with the HTTP request.
        
        Tags:
            goals, management, scrape, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        url = f"{self.base_url}/goals/{goal_gid}/parentGoals"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agoal_relationship(self, goal_relationship_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve a complete goal relationship record by making a GET request to the specified endpoint.
        
        Args:
            opt_fields: Comma-separated list of optional fields to include in response (excludes some properties by default if omitted).
            opt_pretty: Enable formatted output with line breaks/indentation for readability (increases response size, recommended for debugging only).
        
        Returns:
            Dictionary containing the complete goal relationship record data as returned by the API.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with a 4XX or 5XX status code.
        
        Tags:
            goal-relationships, get, api, important
        """
        if goal_relationship_gid is None:
            raise ValueError("Missing required parameter 'goal_relationship_gid'")
        url = f"{self.base_url}/goal_relationships/{goal_relationship_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_agoal_relationship(self, goal_relationship_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing goal relationship by making a PUT request with specified data and returns the complete updated record.
        
        Args:
            data: A dictionary containing fields to update in the goal relationship.
            opt_fields: A comma-separated list of optional properties to include in the response.
            opt_pretty: Enables 'pretty' output formatting for easier readability.
        
        Returns:
            A dictionary representing the complete updated goal relationship record.
        
        Raises:
            HTTPRequestError: Raised if the HTTP request fails, for example, due to network errors or invalid responses.
        
        Tags:
            update, goal-relationships, management, important
        """
        if goal_relationship_gid is None:
            raise ValueError("Missing required parameter 'goal_relationship_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goal_relationships/{goal_relationship_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_goal_relationships(self, opt_pretty=None, limit=None, offset=None, supported_goal=None, resource_subtype=None, opt_fields=None) -> dict[str, Any]:
        """
        Retrieve goal relationships from the API, returning compact goal relationship records with optional pagination and filtering.
        
        Args:
            limit: Results per page. The number of objects to return per page. Must be between 1 and 100.
            offset: Offset token. An offset to the next page returned by the API. It must come from a previous paginated request.
            opt_fields: Optional properties to include in the response. Provide a comma-separated list of properties to expand the returned resource.
            opt_pretty: Provides the response in a pretty format for debugging purposes.
            resource_subtype: Filter goal relationships by this resource subtype.
            supported_goal: Globally unique identifier of the supported goal for the goal relationship.
        
        Returns:
            A dictionary containing goal relationship records.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            goal-relationships, pagination, async_job, api-requests, important
        """
        url = f"{self.base_url}/goal_relationships"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset), ('supported_goal', supported_goal), ('resource_subtype', resource_subtype), ('opt_fields', opt_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_asupporting_goal_relationship(self, goal_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a supporting goal relationship by adding a supporting resource to a specific goal and returns the new relationship record.
        
        Args:
            data: Dictionary containing the supporting goal relationship data to be added. Must include required fields for relationship creation.
            opt_fields: Comma-separated string of optional fields to include in the response. Expands default compact resource representation.
            opt_pretty: Boolean flag to enable pretty-printed JSON output for human readability during debugging.
        
        Returns:
            Dictionary containing the newly created goal relationship record data.
        
        Raises:
            HTTPError: Raised when the API request fails due to network errors, invalid parameters, or server-side issues.
        
        Tags:
            goal-relationships, create, management, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/addSupportingRelationship"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def removes_asupporting_goal_relationship(self, goal_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Removes a supporting goal relationship between a parent goal and its dependent goal based on provided data.
        
        Args:
            data: Dictionary containing goal relationship details to be removed (exact structure depends on API requirements)
            opt_pretty: Enables formatted JSON output with proper indentation and line breaks for human-readable debugging
        
        Returns:
            Dictionary containing API response data after processing the removal request
        
        Raises:
            HTTPError: When the API request fails (non-2xx status code), contains response details
        
        Tags:
            goal-relationships, remove, management, api, important
        """
        if goal_gid is None:
            raise ValueError("Missing required parameter 'goal_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/goals/{goal_gid}/removeSupportingRelationship"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ajob_by_id(self, job_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve a job's full record by its ID.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response (default excludes some properties).
            opt_pretty: Enables formatted output for readability at the cost of performance (recommended for debugging only).
        
        Returns:
            Dictionary containing the complete job record data.
        
        Raises:
            HTTPError: If the HTTP request fails (e.g., invalid job ID, network issues).
        
        Tags:
            get, fetch, job, async-job, management, important
        """
        if job_gid is None:
            raise ValueError("Missing required parameter 'job_gid'")
        url = f"{self.base_url}/jobs/{job_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_memberships(self, parent=None, member=None, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve multiple membership records for goals, projects, or portfolios, with pagination and filtering options.
        
        Args:
            limit: Results per page (1-100). Controls the number of objects returned per page.
            member: Globally unique identifier for `team` or `user` to filter memberships.
            offset: Offset token for pagination. Use the token from prior paginated responses.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Enable pretty JSON output formatting (useful for debugging).
            parent: Globally unique identifier for `goal`, `project`, or `portfolio` to filter memberships.
        
        Returns:
            Dictionary containing compact membership records (goal_membership, project_membership, or portfolio_membership).
        
        Raises:
            HTTPError: Raised if the API request fails due to invalid parameters or server errors.
        
        Tags:
            memberships, pagination, filtering, api-client, important
        """
        url = f"{self.base_url}/memberships"
        query_params = {k: v for k, v in [('parent', parent), ('member', member), ('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_amembership(self, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new membership in a goal or project for users or teams, returning the full membership record.
        
        Args:
            data: Dictionary containing membership details to be created [1][5].
            opt_pretty: Provides formatted output for readability during debugging (increases response size and processing time) [1][5].
        
        Returns:
            Dictionary containing the complete record of the newly created membership [1][5].
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters, authorization errors, or server issues [1][5].
        
        Tags:
            create, membership, management, api-integration, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/memberships"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_amembership(self, membership_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Fetches a compact project membership record.
        
        Args:
            opt_fields: Optional fields to include in the response. Specify a comma-separated list of properties.
            opt_pretty: Flag to provide the response in a pretty, formatted output.
        
        Returns:
            A dictionary containing the membership record.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            membership, fetch, important, management
        """
        if membership_gid is None:
            raise ValueError("Missing required parameter 'membership_gid'")
        url = f"{self.base_url}/memberships/{membership_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_amembership(self, membership_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing membership by making a PUT request, modifying only the specified fields in the provided data.
        
        Args:
            data: A dictionary containing the fields to be updated in the membership.
            opt_pretty: A flag to specify if the response should be in a 'pretty' format, useful for debugging.
        
        Returns:
            The full record of the updated membership.
        
        Raises:
            requests.exceptions.RequestException: Raised when there is an issue with the HTTP request.
        
        Tags:
            update, membership, management, important
        """
        if membership_gid is None:
            raise ValueError("Missing required parameter 'membership_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/memberships/{membership_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_amembership(self, membership_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific membership for a goal or project by sending a DELETE request to the appropriate endpoint.
        
        Args:
            opt_pretty: Provides 'pretty' output formatting for JSON responses. Enables proper line breaking and indentation to improve readability, but increases response size and processing time. Recommended for debugging purposes only.
        
        Returns:
            Empty dictionary indicating successful deletion of the membership. The response body typically contains no data beyond a success status.
        
        Raises:
            HTTPError: Raised when the DELETE request fails, such as when the membership does not exist or the user lacks sufficient permissions.
        
        Tags:
            delete, membership, api, management, important
        """
        if membership_gid is None:
            raise ValueError("Missing required parameter 'membership_gid'")
        url = f"{self.base_url}/memberships/{membership_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_an_organization_export_request(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Initiates an asynchronous export request for an Organization in Asana.
        
        Args:
            data: Dictionary containing export parameters/settings for the organization.
            opt_fields: Comma-separated list of optional fields to include in the response. Omitted fields are excluded by default.
            opt_pretty: Whether to return formatted JSON output (increases response size and processing time). Recommended for debugging only.
        
        Returns:
            Dictionary containing the created export request details and associated metadata.
        
        Raises:
            HTTPError: If the underlying API request fails (e.g., invalid parameters, authentication errors, or server issues).
        
        Tags:
            async-job, export, organization-management, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organization_exports"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_details_on_an_org_export_request(self, organization_export_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve details of a previously-requested Organization export, including optional fields and formatted output.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response. Excludes some properties by default.
            opt_pretty: Format the response with indentation and line breaks for readability. May increase response size and processing time.
        
        Returns:
            Dictionary containing Organization export details from the API response.
        
        Raises:
            requests.HTTPError: Raised when the API request fails due to network errors, authentication issues, or invalid endpoints.
        
        Tags:
            export, organization, retrieve, details, important
        """
        if organization_export_gid is None:
            raise ValueError("Missing required parameter 'organization_export_gid'")
        url = f"{self.base_url}/organization_exports/{organization_export_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_portfolios(self, limit=None, offset=None, workspace=None, owner=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve multiple portfolios, returning them in a compact representation. The portfolios are filtered by the specified workspace and can be further limited by owner, pagination parameters, and additional fields.
        
        Args:
            limit: Results per page; the number of objects to return per page, which must be between 1 and 100.
            offset: Offset token; used for pagination to fetch the next page of results.
            opt_fields: Optional properties to include; a comma-separated list of fields to return beyond the default compact resource.
            opt_pretty: Provides pretty output; formats the response to be more readable, such as line breaks and indentation for JSON.
            owner: The owner of the portfolios; currently limited to portfolios owned by the API user unless using a Service Account.
            workspace: The workspace to filter portfolios by; this parameter is required.
        
        Returns:
            A dictionary containing the portfolios. The exact structure may vary based on the included optional fields.
        
        Raises:
            requests.RequestException: Raised when there is an issue with the HTTP request, such as a connection error or invalid response.
        
        Tags:
            list, portfolios, management, important
        """
        url = f"{self.base_url}/portfolios"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('workspace', workspace), ('owner', owner), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aportfolio(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a portfolio in the specified workspace, allowing custom initialization without automatic UI state like Priority fields.
        
        Args:
            data: Dictionary containing portfolio data (e.g., name, workspace). Required fields depend on API requirements.
            opt_fields: Comma-separated list of optional fields to include in the response. Excluded properties by default.
            opt_pretty: Format response with improved readability/indentation. Recommended for debugging only due to performance impact.
        
        Returns:
            Dictionary containing the created portfolio details and associated metadata.
        
        Raises:
            HTTPError: If the API request fails due to invalid data, authentication issues, or server errors.
        
        Tags:
            create, portfolio-management, api-endpoint, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio(self, portfolio_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a portfolio record from the API, returning all fields unless filtered by optional parameters.
        
        Args:
            opt_fields: Comma-separated list of optional fields to include. Excludes non-specified properties by default.
            opt_pretty: Provides formatted output for improved readability at the cost of performance. Recommended for debugging only.
        
        Returns:
            dict[str, Any]: Complete portfolio record as a dictionary, containing requested data fields and metadata.
        
        Raises:
            HTTPError: Raised when the API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            get, portfolio, api, async_job, management, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aportfolio(self, portfolio_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing portfolio by modifying specified fields while preserving unspecified ones, returning the complete updated portfolio record.
        
        Args:
            data: Dictionary containing portfolio data to update. Only provided fields will be modified.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Provides formatted output for readability during debugging.
        
        Returns:
            Dictionary containing the complete updated portfolio record.
        
        Raises:
            requests.HTTPError: Raised for invalid requests, authorization failures, or server errors based on the HTTP response.
        
        Tags:
            update, portfolio, management, important, put-request
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aportfolio(self, portfolio_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a portfolio by making a DELETE request.
        
        Args:
            opt_pretty: Provides the response in a pretty format, including line breaks and indentation for readability. Optional and defaults to None.
        
        Returns:
            An empty data record returned as a dictionary.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, portfolio, management, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_portfolio_items(self, portfolio_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Fetches a list of portfolio items in compact form, retrieving them based on pagination parameters.
        
        Args:
            limit: The number of results to return per page, between 1 and 100.
            offset: Pagination offset token for retrieving the next page of results.
            opt_fields: Optional fields to include in the response, specified as a comma-separated list.
            opt_pretty: Flag to format the response output (e.g., JSON) for readability.
        
        Returns:
            A dictionary containing the list of portfolio items.
        
        Raises:
            HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, portfolio, pagination, portfolio-management, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}/items"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_aportfolio_item(self, portfolio_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds an item to a portfolio and returns an empty data block.
        
        Args:
            data: Data to be added to the portfolio. It should be a dictionary.
            opt_pretty: Option to return the response in a 'pretty' format, useful for debugging.
        
        Returns:
            An empty data block returned as a dictionary.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request, such as a 4xx or 5xx status code.
        
        Tags:
            add, portfolio, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/addItem"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_aportfolio_item(self, portfolio_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove an item from a portfolio via API request and return the response data.
        
        Args:
            data: Dictionary containing portfolio item data to be removed. Must include required item identifiers.
            opt_pretty: Optional flag to format response with indentation and line breaks for readability. Use only for debugging.
        
        Returns:
            Parsed JSON response as dictionary. Returns empty data block on success with no content.
        
        Raises:
            requests.HTTPError: Raised when the API request fails due to invalid data, authentication errors, or server issues.
        
        Tags:
            portfolio, management, remove, delete, api, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/removeItem"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acustom_field_to_aportfolio(self, portfolio_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds a custom field to a portfolio by creating a custom field setting.
        
        Args:
            data: A dictionary containing data for the custom field. If not provided, it defaults to None.
            opt_pretty: A boolean or other value to control whether the response is in a 'pretty' format. Defaults to None.
        
        Returns:
            A dictionary containing the response data for the added custom field.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            portfolios, management, custom_fields, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/addCustomFieldSetting"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acustom_field_from_aportfolio(self, portfolio_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove a custom field setting from a portfolio.
        
        Args:
            data: Dictionary containing request data for custom field removal from the portfolio.
            opt_pretty: Provides 'pretty' JSON output formatting (increases response size and processing time).
        
        Returns:
            Dictionary containing the response data after custom field removal operation.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request returns a non-success status code (4xx/5xx).
        
        Tags:
            remove, custom-field, portfolio, management, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/removeCustomFieldSetting"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_users_to_aportfolio(self, portfolio_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Add users to a portfolio and return the updated portfolio record.
        
        Args:
            data: Dictionary containing user data for adding members to the portfolio. Required for member addition.
            opt_fields: Comma-separated list of optional fields to include in the response. Excludes some properties by default if not specified.
            opt_pretty: If true, returns response with improved formatting and readability. Recommended for debugging only due to performance impact.
        
        Returns:
            Updated portfolio record as a dictionary with the added users.
        
        Raises:
            HTTPError: Raised when the API request fails, such as invalid input data, authentication issues, or server errors.
        
        Tags:
            add, users, portfolio, management, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/addMembers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_users_from_aportfolio(self, portfolio_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove users from a portfolio and return the updated portfolio record.
        
        Args:
            data: Dictionary containing user removal data with relevant user identifiers (required).
            opt_fields: Comma-separated string specifying optional properties to include in the response (increases response detail).
            opt_pretty: Boolean flag to enable formatted JSON output (use for debugging only).
        
        Returns:
            Dictionary representing the updated portfolio record after user removal.
        
        Raises:
            HTTPError: Raised when the HTTP request fails, typically due to invalid input data or server errors.
        
        Tags:
            portfolios, user-management, batch-update, api, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/portfolios/{portfolio_gid}/removeMembers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_portfolio_memberships(self, opt_fields=None, portfolio=None, workspace=None, user=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves multiple portfolio memberships, returning them in a compact representation. Requires specifying either `portfolio` and `user`, or `workspace` and `user`. Supports pagination and optional fields.
        
        Args:
            limit: The number of results per page. Must be between 1 and 100.
            offset: An offset token for pagination, returned by previous API requests.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Enables pretty formatting of the response, primarily for debugging.
            portfolio: The portfolio to filter results on.
            user: A string identifying a user, which can be 'me', an email, or a user's gid.
            workspace: The workspace to filter results on.
        
        Returns:
            A dictionary containing a list of portfolio memberships.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, portfolio, membership, pagination, important
        """
        url = f"{self.base_url}/portfolio_memberships"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('portfolio', portfolio), ('workspace', workspace), ('user', user), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aportfolio_membership(self, portfolio_membership_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a portfolio membership, returning the complete portfolio record.
        
        Args:
            opt_fields: Optional query parameter to include additional properties in the response. It accepts a comma-separated list of the properties to include.
            opt_pretty: Optional flag to provide the response in a readable 'pretty' format, useful for debugging.
        
        Returns:
            A dictionary containing the portfolio membership details.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            portfolio, membership, retrieve, important
        """
        if portfolio_membership_gid is None:
            raise ValueError("Missing required parameter 'portfolio_membership_gid'")
        url = f"{self.base_url}/portfolio_memberships/{portfolio_membership_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_aportfolio(self, portfolio_gid, opt_fields=None, user=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Get memberships from a portfolio, returning compact portfolio membership records.
        
        Args:
            limit: The number of objects to return per page (between 1 and 100).
            offset: Offset token for pagination, used to retrieve the next page of results.
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: Provides the response in a "pretty" format, useful for debugging.
            user: A string identifying a user (e.g., "me", email, or gid).
        
        Returns:
            A dictionary containing the membership records.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request (e.g., non-successful response status).
        
        Tags:
            fetch, portfolio, membership, pagination, important
        """
        if portfolio_gid is None:
            raise ValueError("Missing required parameter 'portfolio_gid'")
        url = f"{self.base_url}/portfolios/{portfolio_gid}/portfolio_memberships"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('user', user), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_projects(self, limit=None, offset=None, workspace=None, team=None, archived=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve multiple projects based on filtering criteria, returning compact project records. Handles pagination and allows specifying optional fields to include.
        
        Args:
            archived: Only return projects whose `archived` field matches this parameter (True/False).
            limit: Results per page (integer between 1-100). Controls pagination batch size.
            offset: Pagination token from previous response. Required to fetch subsequent pages.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Enable pretty-printed JSON output (debugging use only).
            team: Team filter to scope retrieved projects.
            workspace: Workspace/organization filter to scope retrieved projects.
        
        Returns:
            Dictionary containing paginated project data and metadata, with structure dictated by `opt_fields`.
        
        Raises:
            HTTPError: For invalid parameters (e.g., out-of-range limit) or API request failures.
        
        Tags:
            projects, search, pagination, data-retrieval, management, important
        """
        url = f"{self.base_url}/projects"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('workspace', workspace), ('team', team), ('archived', archived), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Create a new project in a workspace or team, returning its full record.
        
        Args:
            data: Dictionary containing project data including workspace/team associations. Must specify workspace (organization or workspace), and team if the workspace is an organization.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Enables pretty-printed JSON output for readability during debugging.
        
        Returns:
            Dictionary containing the full record of the newly created project.
        
        Raises:
            HTTPError: If the API request fails due to invalid data, permissions issues, or server errors.
        
        Tags:
            create, projects, management, workspace, team, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject(self, project_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Fetches a project's complete record, optionally including additional fields and formatting the output for readability.
        
        Args:
            opt_fields: Optional fields to include in the response. Specify a comma-separated list of properties to be included.
            opt_pretty: If set, formats the response in a pretty format with line breaks and indentation.
        
        Returns:
            A dictionary containing the project's details.
        
        Raises:
            Exception: Raises an exception if the HTTP request or JSON parsing fails.
        
        Tags:
            projects, fetch, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates a specific project by modifying provided fields, returning the complete updated project record while preserving unspecified fields.
        
        Args:
            data: Dictionary containing fields to update. Only specified fields will be modified (keys: field names, values: new values).
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Provides formatted output (line breaks/indentation) at the cost of performance. Recommended for debugging only.
        
        Returns:
            Dictionary representing the complete updated project resource with current field values.
        
        Raises:
            HTTPError: Raised for invalid requests, authentication failures, or server errors during the API call.
        
        Tags:
            projects, update, api, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject(self, project_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes an existing project by making a DELETE request to the project's URL.
        
        Args:
            opt_pretty: Provides the response in a ‘pretty’ format; useful for debugging purposes.
        
        Returns:
            An empty data record in JSON format.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, project, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Duplicates a project by creating and returning a job for asynchronous handling.
        
        Args:
            data: Dictionary containing project data (optional).
            opt_fields: Comma-separated list of optional fields to include in the response (optional).
            opt_pretty: Request 'pretty' output (e.g., properly formatted JSON) for debugging (optional).
        
        Returns:
            A dictionary representing the job for project duplication.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an error (e.g., 4xx or 5xx status codes).
        
        Tags:
            async_job, project, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/duplicate"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_projects_atask_is_in(self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve a compact list of all projects that contain the specified task, formatted as paginated results.
        
        Args:
            limit: Results per page (1-100). Controls the number of projects returned per response.
            offset: Offset token for paginated requests. Use the token from previous responses to fetch subsequent pages.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Format response with indentation/line breaks for readability (debugging only).
        
        Returns:
            Dictionary containing paginated project data in compact format, with projects as values.
        
        Raises:
            HTTPError: Raised when the API request fails (e.g., invalid parameters or authentication errors).
        
        Tags:
            projects, retrieve, pagination, compact-format, task-management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/projects"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_sprojects(self, team_gid, limit=None, offset=None, archived=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Fetches a team’s projects, returning compact project records with optional pagination, archival status filtering, and field inclusion control.
        
        Args:
            archived: Only return projects whose `archived` field matches this parameter's value. If None, returns all projects regardless of archival status.
            limit: Results per page (1-100). Controls the number of projects returned per request.
            offset: Offset token for pagination. Use the token from a prior paginated response to fetch subsequent pages.
            opt_fields: Comma-separated list of optional properties to include in the response. Omitting this returns compact resources by default.
            opt_pretty: If True, formats the JSON response for readability (increases response size and processing time). Primarily for debugging.
        
        Returns:
            Dictionary containing a list of compact project records and pagination metadata (if applicable).
        
        Raises:
            HTTPError: Raised when the API request fails, such as due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            projects, list, pagination, api-client, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/projects"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('archived', archived), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_in_ateam(self, team_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a project shared with the specified team and returns the full record of the newly created project.
        
        Args:
            data: A dictionary containing the project data to be created.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Whether to return formatted JSON for improved readability (use sparingly for debugging).
        
        Returns:
            A dictionary containing the full record of the created project, including all requested fields.
        
        Raises:
            HTTPError: If the HTTP request fails due to authorization issues, invalid data, or server errors.
        
        Tags:
            project, create, async-job, team, management, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}/projects"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_projects_in_aworkspace(self, workspace_gid, limit=None, offset=None, archived=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Fetches all project records in a workspace, returning them as a dictionary.
        
        Args:
            archived: Only return projects whose `archived` field matches this parameter.
            limit: Number of objects to return per page, between 1 and 100.
            offset: Offset token for pagination, returned by a previous API request.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Flag to enable pretty JSON output, useful for debugging.
        
        Returns:
            A dictionary containing the compact project records.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails with a status code indicating an error.
        
        Tags:
            list, projects, workspace, management, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/projects"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('archived', archived), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_in_aworkspace(self, workspace_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Create a project in a workspace, returning the full record of the newly created project.
        
        Args:
            data: Dictionary containing project data. If not provided, it defaults to None.
            opt_fields: Optional fields to include in the response. Specify as a comma-separated list of property names.
            opt_pretty: Optional flag to provide pretty-printed output, useful for debugging purposes.
        
        Returns:
            A dictionary representing the full record of the newly created project.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request or response, such as a non-success status code.
        
        Tags:
            create, project, workspace, api-call, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/projects"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_acustom_field_to_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Add a custom field to a project, creating a custom field setting for the project.
        
        Args:
            data: Dictionary containing custom field data for the project.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Boolean indicating whether the response should be formatted for readability.
        
        Returns:
            A dictionary containing the response from the API.
        
        Raises:
            HTTPError: Raised if the API request encounters an HTTP error, such as a 404 or 500 status code.
        
        Tags:
            customization, projects, async_job, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/addCustomFieldSetting"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_acustom_field_from_aproject(self, project_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove a custom field setting from a specified project by sending a POST request with the required data.
        
        Args:
            data: Dictionary containing the custom field data to be removed from the project. Must include necessary identifiers.
            opt_pretty: Provides 'pretty' output formatting (readable JSON with indentation). Use only during debugging due to performance impact.
        
        Returns:
            Dictionary containing the API response data after removing the custom field.
        
        Raises:
            requests.HTTPError: Raised when the API request fails (non-2xx status code), indicating unsuccessful removal.
        
        Tags:
            remove, custom-field, project, management, async_job, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/removeCustomFieldSetting"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_task_count_of_aproject(self, project_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves the task count of a project, returning an object with task count fields. All fields are excluded by default, requiring opt-in via the `opt_fields` parameter.
        
        Args:
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: Provides the response in a "pretty" format; advisable only for debugging due to increased response time and size.
        
        Returns:
            A dictionary containing the task count fields of the project.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters a problem, such as a bad status code.
        
        Tags:
            task, count, project, important, management
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/task_counts"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_users_to_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds users to a project as members, potentially setting them as followers based on notification settings, and returns the updated project record.
        
        Args:
            data: Dictionary of user data specifying which users to add to the project.
            opt_fields: Comma-separated list of fields to include in addition to the compact resource.
            opt_pretty: Sets the response format to pretty-printed JSON for readability.
        
        Returns:
            Updated project record as a JSON object.
        
        Raises:
            requests.RequestException: Raised if a problem occurs during the request, such as network errors or invalid responses.
        
        Tags:
            add, projects, members, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/addMembers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_users_from_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Removes specified users from a project and returns the updated project record.
        
        Args:
            data: A dictionary containing details of users to remove from the project.
            opt_fields: A comma-separated list of optional properties to include in the response.
            opt_pretty: Provides the response in a 'pretty' format for debugging purposes.
        
        Returns:
            A dictionary representing the updated project record.
        
        Raises:
            Exception: An exception may be raised if the HTTP request fails or if the server returns an error status.
        
        Tags:
            remove, project, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/removeMembers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_followers_to_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds followers to a project, promoting specified users to members if not already part of the project. Returns the updated project record.
        
        Args:
            data: Dictionary containing data required to add followers (exact structure depends on API requirements).
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: If True, formats the response with improved readability at the cost of performance.
        
        Returns:
            Dictionary containing the updated project record with new followers.
        
        Raises:
            HTTPError: If the API request fails, typically due to invalid data, authentication issues, or server errors.
        
        Tags:
            projects, add-followers, membership, api-client, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/addFollowers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_followers_from_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove followers from a project without affecting membership status.
        
        Args:
            data: Dictionary containing user data to remove followers. Can be None if no users are specified.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Provides the response in a readable format, primarily for debugging.
        
        Returns:
            The updated project record as a dictionary.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            remove, followers, project, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/removeFollowers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_template_from_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a project template from a project by sending a POST request and returns the response in JSON format, asynchronously handling the template creation.
        
        Args:
            data: Dictionary containing project data. Defaults to None.
            opt_fields: Optional fields to include in the response. Pass as a comma-separated list. Defaults to None.
            opt_pretty: Use this to format the JSON output for readability. Defaults to None.
        
        Returns:
            Dictionary containing the created project template details.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, project, template, async_job, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/saveAsTemplate"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_brief(self, project_brief_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a project brief by optionally including specified fields and formatting the response.
        
        Args:
            opt_fields: An optional comma-separated list of properties to include beyond the default compact resource.
            opt_pretty: Provides the response in a human-readable format, useful for debugging.
        
        Returns:
            A dictionary containing the project brief details.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            project-brief, data-fetch, api-call, important
        """
        if project_brief_gid is None:
            raise ValueError("Missing required parameter 'project_brief_gid'")
        url = f"{self.base_url}/project_briefs/{project_brief_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aproject_brief(self, project_brief_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing project brief by making a PUT request and returns the complete updated record.
        
        Args:
            data: Dictionary containing fields to update in the project brief. Only specified fields will be updated.
            opt_fields: Optional comma-separated list of fields to include in the response beyond the default compact resource.
            opt_pretty: Provides 'pretty' output in a readable format, advisable for debugging purposes only.
        
        Returns:
            The complete updated project brief record as a dictionary.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, project-briefs, management, important
        """
        if project_brief_gid is None:
            raise ValueError("Missing required parameter 'project_brief_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/project_briefs/{project_brief_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_brief(self, project_brief_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Failed to extract docstring information
        
        Args:
            None: This function takes no arguments
        
        Returns:
            Unknown return value
        """
        if project_brief_gid is None:
            raise ValueError("Missing required parameter 'project_brief_gid'")
        url = f"{self.base_url}/project_briefs/{project_brief_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_brief(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new project brief and returns the full record of the newly created brief.
        
        Args:
            data: A dictionary containing the data required to create a project brief.
            opt_fields: A comma-separated list of properties to include in the response that are excluded by default.
            opt_pretty: A query parameter that provides the response in a readable format, useful for debugging.
        
        Returns:
            A dictionary representing the full record of the newly created project brief.
        
        Raises:
            Exception: An exception may be raised if there is an issue with the request (e.g., network errors or HTTP errors).
        
        Tags:
            create, project, brief, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/project_briefs"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_membership(self, project_membership_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve a project membership and its associated project record.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response. Excluded by default in compact resources.
            opt_pretty: When true, returns JSON with proper formatting and indentation for readability. Use sparingly due to performance implications.
        
        Returns:
            A dictionary containing the complete project record for the requested membership.
        
        Raises:
            HTTPError: Raised if the API request fails, typically due to invalid parameters or authentication issues.
        
        Tags:
            project-memberships, get, api-client, management, important
        """
        if project_membership_gid is None:
            raise ValueError("Missing required parameter 'project_membership_gid'")
        url = f"{self.base_url}/project_memberships/{project_membership_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_aproject(self, project_gid, opt_fields=None, user=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves paginated project membership records for a specific project, returning compact data with optional fields.
        
        Args:
            limit: Results per page (1-100). Controls the number of objects returned per page.
            offset: Pagination token. Use the offset from a previous paginated response to retrieve the next page.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Return formatted JSON output for readability (increases response size and processing time).
            user: User identifier ("me", email, or user GID). Filters memberships for the specified user.
        
        Returns:
            Dictionary containing paginated project membership records in compact format.
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            project-memberships, pagination, list, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/project_memberships"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('user', user), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_status(self, project_status_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Get the complete record for a single project status update. *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response (excluded by default).
            opt_pretty: Provides formatted output with proper line breaks and indentation for readability during debugging.
        
        Returns:
            Dictionary containing the complete status update record.
        
        Raises:
            HTTPError: If the API request fails, as determined by `response.raise_for_status()`.
        
        Tags:
            project-statuses, get, management, deprecated, important
        """
        if project_status_gid is None:
            raise ValueError("Missing required parameter 'project_status_gid'")
        url = f"{self.base_url}/project_statuses/{project_status_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_status(self, project_status_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific existing project status update (deprecated: new integrations should use '/status_updates/{status_gid}').
        
        Args:
            opt_pretty: Provides 'pretty' output formatting for JSON responses, increasing readability and size. Recommended only for debugging purposes.
        
        Returns:
            Empty dictionary representing successful deletion, after parsing the JSON response.
        
        Raises:
            HTTPError: If the HTTP request fails due to client (4XX) or server (5XX) errors.
        
        Tags:
            delete, deprecated, project-statuses, management, api, important
        """
        if project_status_gid is None:
            raise ValueError("Missing required parameter 'project_status_gid'")
        url = f"{self.base_url}/project_statuses/{project_status_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_statuses_from_aproject(self, project_gid, opt_pretty=None, limit=None, offset=None, opt_fields=None) -> dict[str, Any]:
        """
        Retrieve compact project status update records from a project, providing pagination and query parameters.
        
        Args:
            limit: The number of objects to return per page. Must be between 1 and 100.
            offset: An offset token for pagination. This should be an offset returned by a previous paginated request.
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: A boolean indicating whether to provide 'pretty' output, useful for debugging.
        
        Returns:
            A dictionary containing project status update records.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            status, project, pagination, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/project_statuses"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset), ('opt_fields', opt_fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_aproject_status(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new project status update (deprecated).
        
        Args:
            data: Dictionary containing the project status data. Must not be None.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Enable pretty formatting for human-readable output (debugging use).
        
        Returns:
            Full record of the newly created project status update as a dictionary.
        
        Raises:
            HTTPError: Raised for unsuccessful API responses (non-2xx status codes).
        
        Tags:
            create, project-status, deprecated, async-job, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/project_statuses"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aproject_template(self, project_template_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves the complete record for a single project template including optionally specified fields.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include (default None). Excluded properties are omitted by default in compact responses.
            opt_pretty: Enables formatted output with proper line breaks/indentation. Use sparingly due to performance impact (default None).
        
        Returns:
            dict[str, Any]: Complete project template record as a dictionary.
        
        Raises:
            HTTPError: If the API request fails or returns a non-2xx status code.
        
        Tags:
            project-templates, get, management, api-call, important
        """
        if project_template_gid is None:
            raise ValueError("Missing required parameter 'project_template_gid'")
        url = f"{self.base_url}/project_templates/{project_template_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_aproject_template(self, project_template_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Delete a project template from the system and return an empty data record.
        
        Args:
            opt_pretty: Provides formatted output with proper line breaks and indentation for readability. Recommended for debugging only as it increases response size and processing time.
        
        Returns:
            Empty dictionary after successful deletion, as returned by the server's JSON response.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails, typically due to invalid permissions, non-existent project template, or connection issues.
        
        Tags:
            delete, project-templates, management, api, important
        """
        if project_template_gid is None:
            raise ValueError("Missing required parameter 'project_template_gid'")
        url = f"{self.base_url}/project_templates/{project_template_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_project_templates(self, workspace=None, team=None, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves multiple project templates based on specified filters like team and workspace.
        
        Args:
            limit: Results per page. It must be between 1 and 100.
            offset: Offset token for pagination. Used to retrieve the next page of results.
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: Flag to provide the response in a readable format.
            team: Team to filter projects on.
            workspace: Workspace to filter results on.
        
        Returns:
            A dictionary containing the compact project template records.
        
        Raises:
            HTTPError: Raised if the HTTP request to the API fails.
        
        Tags:
            list, project-templates, api, important
        """
        url = f"{self.base_url}/project_templates"
        query_params = {k: v for k, v in [('workspace', workspace), ('team', team), ('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_sproject_templates(self, team_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve paginated list of compact project template records for a team.
        
        Args:
            limit: Results per page between 1-100. Controls the number of objects returned per page.
            offset: Pagination token from a prior response. Required to fetch subsequent pages. Omit to get the first page.
            opt_fields: Optional comma-separated field list to include additional properties excluded by default.
            opt_pretty: Format response for readability (increases response size and processing time). Recommended only for debugging.
        
        Returns:
            Dictionary containing parsed JSON response with project template records.
        
        Raises:
            HTTPError: When the API request fails (e.g., network issues, invalid credentials, or server errors).
        
        Tags:
            list, project-templates, pagination, api, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/project_templates"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def instantiate_aproject_from_aproject_template(self, project_template_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Instantiates a project from a project template and returns an asynchronous job handle for the operation.
        
        Args:
            data: Dictionary containing project instantiation parameters. Typically includes 'gid' from template's 'requested_dates' array.
            opt_fields: Comma-separated list of optional fields to include in the compact response.
            opt_pretty: Format the response body for readability (may impact performance).
        
        Returns:
            Dictionary containing the asynchronous job resource that manages the project instantiation process.
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP request failures (e.g., invalid template ID, insufficient permissions).
        
        Tags:
            project-templates, async-job, start, create, management, important
        """
        if project_template_gid is None:
            raise ValueError("Missing required parameter 'project_template_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/project_templates/{project_template_gid}/instantiateProject"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def trigger_arule(self, rule_trigger_gid, data=None) -> dict[str, Any]:
        """
        Triggers a rule configured with an incoming web request trigger, sending provided data to the rule's endpoint.
        
        Args:
            data: Dictionary containing data payload for the rule (keys/values determined by rule configuration). Use None for empty payload.
        
        Returns:
            Dictionary containing the parsed JSON response from the triggered rule's endpoint
        
        Raises:
            requests.HTTPError: Raised for HTTP 4XX/5XX responses from the API endpoint
        
        Tags:
            rules, trigger, web-request, http-client, async-job, important
        """
        if rule_trigger_gid is None:
            raise ValueError("Missing required parameter 'rule_trigger_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/rule_triggers/{rule_trigger_gid}/run"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_asection(self, section_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a complete record for a single section, potentially including additional fields and optional formatting.
        
        Args:
            opt_fields: A comma-separated list of properties to include that are excluded by default.
            opt_pretty: A flag to provide 'pretty' formatted output, useful for debugging by adding line breaks and indentation.
        
        Returns:
            A dictionary containing the section's record.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            section, data-fetch, important, resource-management
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        url = f"{self.base_url}/sections/{section_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_asection(self, section_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing section by making a PUT request to the specific section URL, updating only the provided fields.
        
        Args:
            data: A dict of fields to update in the section; currently, only the 'name' field is supported.
            opt_fields: Optional fields to include in the response, provided as a comma-separated list.
            opt_pretty: Enables 'pretty' output, useful for debugging purposes.
        
        Returns:
            The complete updated section record.
        
        Raises:
            requests.RequestException: Raised if the HTTP request fails for any reason.
        
        Tags:
            update, section, management, important
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/sections/{section_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_asection(self, section_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific empty section by sending a DELETE request to its URL. The last remaining section cannot be deleted.
        
        Args:
            opt_pretty: Provides formatted output (e.g., indentation for readability in JSON responses). Recommended only for debugging due to performance impact.
        
        Returns:
            Dictionary containing the server response data, or an empty data block if successful.
        
        Raises:
            HTTPError: Raised when the request fails (e.g., invalid section ID, non-empty section, or attempting to delete the last remaining section).
        
        Tags:
            delete, section, management, http, important
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        url = f"{self.base_url}/sections/{section_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sections_in_aproject(self, project_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve sections in a project, returning compact records.
        
        Args:
            limit: The number of objects to return per page. Must be between 1 and 100. Defaults to None.
            offset: Offset token for pagination. Should be used if a next page is requested.
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: Enable 'pretty' formatting for the JSON output. Useful for debugging.
        
        Returns:
            A dictionary containing compact section records.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, management, project, sections, pagination, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/sections"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_asection_in_aproject(self, project_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new section in a project and returns the full record of the newly created section.
        
        Args:
            data: Dictionary containing section data to create.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Enables pretty-printed JSON output for readability during debugging.
        
        Returns:
            Full JSON record of the created section as a dictionary.
        
        Raises:
            HTTPError: If the API request fails, including invalid project/section data or authentication issues.
        
        Tags:
            sections, create, management, api-call, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/sections"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_task_to_section(self, section_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds a task to a specific section in a project, removing it from other sections. Inserts the task at the top of the section unless position parameters are provided (insert_before/insert_after). Does not work for separator tasks (resource_subtype 'section').
        
        Args:
            data: Dictionary containing task data including section ID (keys: 'section' or positional parameters if applicable). Must not include separator tasks.
            opt_pretty: Enables pretty-printed JSON output for debugging (increases response time and size).
        
        Returns:
            Dictionary containing the API response with the updated section/task details.
        
        Raises:
            HTTPError: When the API request fails (network issues, invalid data, or unauthorized access).
        
        Tags:
            task-management, sections, modify, async_job, important
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/sections/{section_gid}/addTask"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def move_or_insert_sections(self, project_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Move or insert sections by sending a POST request with provided data and optional 'pretty' formatting.
        
        Args:
            data: A dictionary containing section data. Either 'before_section' or 'after_section' is required.
            opt_pretty: A flag to provide formatted output, useful for debugging purposes.
        
        Returns:
            An empty dictionary representing the response data.
        
        Raises:
            HTTPError: Raised if there's an HTTP error in the request.
        
        Tags:
            move, insert, sections, management, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/projects/{project_gid}/sections/insert"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_astatus_update(self, status_update_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Get a status update by requesting a complete record from an endpoint. The response may include optional fields based on query parameters.
        
        Args:
            opt_fields: A comma-separated list of optional properties to include in the response. Default is None.
            opt_pretty: Enables pretty output by formatting the response, such as proper line breaking in JSON. Advisable only for debugging. Default is None.
        
        Returns:
            A dictionary containing the status update record.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the request returns an unsuccessful status code.
        
        Tags:
            status, get, management, important
        """
        if status_update_gid is None:
            raise ValueError("Missing required parameter 'status_update_gid'")
        url = f"{self.base_url}/status_updates/{status_update_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_astatus_update(self, status_update_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific existing status update and returns an empty data record upon success.
        
        Args:
            opt_pretty: Provides 'pretty' output formatting for JSON responses. Enables human-readable formatting with line breaks and indentation, recommended for debugging purposes only due to performance overhead.
        
        Returns:
            Empty dictionary indicating successful deletion, parsed from the response JSON.
        
        Raises:
            HTTPError: If the API request fails (non-2xx status code), raised through response.raise_for_status().
        
        Tags:
            status-updates, delete, important, http
        """
        if status_update_gid is None:
            raise ValueError("Missing required parameter 'status_update_gid'")
        url = f"{self.base_url}/status_updates/{status_update_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_status_updates_from_an_object(self, parent=None, created_since=None, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Fetches status updates from a specified object, returning compact status records.
        
        Args:
            created_since: Only return statuses that have been created since the given time.
            limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
            offset: Offset token. An offset to the next page returned by the API.
            opt_fields: Optional fields to include. A comma-separated list of properties to include beyond the default compact resource.
            opt_pretty: Provides 'pretty' output, such as line-breaking and indentation for JSON responses.
            parent: Globally unique identifier for the object to fetch statuses from. Must be a GID for a project, portfolio, or goal.
        
        Returns:
            A dictionary containing status updates for the given object.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            status-updates, fetch, management, async_job, important
        """
        url = f"{self.base_url}/status_updates"
        query_params = {k: v for k, v in [('parent', parent), ('created_since', created_since), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_astatus_update(self, opt_fields=None, opt_pretty=None, limit=None, offset=None, data=None) -> dict[str, Any]:
        """
        Create a status update on an object and return the full record of the newly created status update.
        
        Args:
            data: Dictionary containing status update data to be created.
            limit: Results per page (between 1-100). Controls the number of objects returned per page.
            offset: Pagination token for retrieving subsequent pages. Must be a valid token from a previous paginated response.
            opt_fields: Comma-separated list of optional fields to include in the compact response.
            opt_pretty: If true, returns formatted JSON output for readability (use only during debugging).
        
        Returns:
            Full record of the created status update as a dictionary.
        
        Raises:
            HTTPError: Raised for invalid requests, authentication errors, or server issues during API communication.
        
        Tags:
            create, status-updates, async, management, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/status_updates"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_astory(self, story_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a story's full record, returning all data fields except those excluded by default. Optional parameters allow expanding specific fields and formatting the response.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response. By default excludes some resource properties.
            opt_pretty: Formats response with proper line breaks and indentation for readability. Increases processing time and response size.
        
        Returns:
            dict[str, Any]: Complete story record with requested optional fields included.
        
        Raises:
            HTTPError: Raised for invalid API requests, authentication failures, or server errors via response.raise_for_status().
        
        Tags:
            stories, retrieve, api, get, management, important
        """
        if story_gid is None:
            raise ValueError("Missing required parameter 'story_gid'")
        url = f"{self.base_url}/stories/{story_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_astory(self, story_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates a story and returns the full record of the updated story. Only comment stories can have their text updated, and only comment/attachment stories can be pinned. Exactly one of `text` or `html_text` must be specified when updating a comment story.
        
        Args:
            data: Dictionary containing story data to update. Must include required fields for the story type.
            opt_fields: Comma-separated list of optional properties to include in the response
            opt_pretty: If true, returns formatted JSON output (increases response size and processing time)
        
        Returns:
            Full updated story record as a dictionary containing all data fields
        
        Raises:
            HTTPError: If the API request fails due to invalid data, permissions, or server errors
        
        Tags:
            update, stories, async_job, management, important
        """
        if story_gid is None:
            raise ValueError("Missing required parameter 'story_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/stories/{story_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_astory(self, story_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a story created by the user.
        
        Args:
            opt_pretty: Optional parameter to provide the response in a pretty format. Useful for debugging.
        
        Returns:
            An empty dictionary as a result of the deletion operation.
        
        Raises:
            HTTPError: Raised when the HTTP request fails, indicating an unsuccessful deletion.
        
        Tags:
            delete, story, management, important
        """
        if story_gid is None:
            raise ValueError("Missing required parameter 'story_gid'")
        url = f"{self.base_url}/stories/{story_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_stories_from_atask(self, task_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve paginated stories associated with a task, returning compact records in a dictionary format.
        
        Args:
            limit: Results per page (1-100). Controls the number of stories returned per API call.
            offset: Pagination token from prior API response. Omit to get first page of results.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Format response for readability (increases processing time).
        
        Returns:
            Dictionary containing the API response with story data, typically including 'data' and 'next_page' fields.
        
        Raises:
            HTTPError: When API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            stories, pagination, api, retrieve, async_job, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/stories"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_astory_on_atask(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a comment story on a task as the authenticated user, returning the new story's full record.
        
        Args:
            data: Dictionary containing story data (currently only supports comment stories)
            opt_fields: Comma-separated list of optional fields to include in response
            opt_pretty: Enable formatted JSON output (use for debugging only)
        
        Returns:
            dict[str, Any]: Complete record of the newly created story including all requested fields
        
        Raises:
            requests.HTTPError: Raised for invalid requests or server errors (4xx/5xx status codes)
        
        Tags:
            stories, create, comment, tasks, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/stories"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_tags(self, limit=None, offset=None, workspace=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve multiple tags with optional pagination and filtering. Returns compact tag records based on provided query parameters.
        
        Args:
            limit: Results per page (1-100). Controls the number of objects returned per page.
            offset: Offset token for pagination. Use the token returned by previous paginated responses to fetch subsequent pages.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Provides formatted output for readability at the cost of performance.
            workspace: The workspace identifier to filter tags.
        
        Returns:
            Dictionary containing paginated tag records as key-value pairs. Includes metadata and tag data.
        
        Raises:
            HTTPError: When the API request fails due to network issues or invalid parameters.
        
        Tags:
            retrieve, pagination, filter, tags, workspace, management, important
        """
        url = f"{self.base_url}/tags"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('workspace', workspace), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atag(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Create a new tag in a specific workspace or organization.
        
        Args:
            data: Dictionary containing the data for the new tag. Must be provided to create a tag.
            opt_fields: Optional fields to include in the response. Specify as a comma-separated list.
            opt_pretty: Flag to return the response in a 'pretty' format. Useful for debugging.
        
        Returns:
            The full record of the newly created tag.
        
        Raises:
            requests.RequestException: Raised if there is an error with the HTTP request.
        
        Tags:
            create, tag, important, management
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tags"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atag(self, tag_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve a single tag with optional properties and formatted output.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response (excluded by default).
            opt_pretty: Enable formatted output (increases response size, recommended for debugging only).
        
        Returns:
            Complete tag record as a dictionary containing all requested fields.
        
        Raises:
            requests.HTTPError: Raised for non-2xx HTTP status codes from the API.
        
        Tags:
            tag, get, retrieve, api, important
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atag(self, tag_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Updates a tag's properties by sending a PUT request with specified optional fields. Only provided fields are modified; unspecified fields remain unchanged.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response. Excludes certain properties by default.
            opt_pretty: Enables formatted output for readability (increases response size and processing time). Recommended for debugging only.
        
        Returns:
            dict[str, Any]: Complete updated tag record containing all fields after modification.
        
        Raises:
            requests.HTTPError: Raised for invalid requests, authorization failures, or server errors (4XX/5XX status codes).
            ValueError: Raised if provided `opt_fields` or `opt_pretty` values are invalid.
        
        Tags:
            update, tag, management, async_job, important
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atag(self, tag_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific, existing tag by making a DELETE request to the tag's URL.
        
        Args:
            opt_pretty: Provides the response in a 'pretty' format, useful for debugging purposes.
        
        Returns:
            An empty data record returned as a JSON response.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, tag-management, important
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_stags(self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Fetches a task's tags, returning a compact representation of all associated tags.
        
        Args:
            limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
            offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request.
            opt_fields: Optional fields to include in the response. A comma-separated list of properties to include.
            opt_pretty: Provides "pretty" output. Returns the response in a formatted JSON with proper line breaking and indentation.
        
        Returns:
            A dictionary containing the task's tags.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            fetch, tags, pagination, api, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/tags"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_in_aworkspace(self, workspace_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve paginated tags from a workspace with optional filters and response formatting.
        
        Args:
            limit: Results per page. The number of objects to return, between 1-100.
            offset: Offset token for pagination. Use the token from prior paginated responses.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Enable formatted JSON output (increases response time and size).
        
        Returns:
            Dictionary containing compact tag records and pagination details.
        
        Raises:
            requests.HTTPError: Raised when the API request fails (e.g., invalid parameters or authentication errors).
        
        Tags:
            retrieve, paginated, workspace-tags, management, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/tags"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atag_in_aworkspace(self, workspace_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new tag in a workspace or organization and returns its full record.
        
        Args:
            data: Dictionary containing tag creation parameters (required fields depend on the API specification).
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Enables formatted output for improved readability during debugging.
        
        Returns:
            Dictionary containing the full record of the created tag.
        
        Raises:
            HTTPError: Raised for HTTP request failures (4XX/5XX status codes).
        
        Tags:
            create, management, tags, async-job, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/tags"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_tasks(self, limit=None, offset=None, assignee=None, project=None, section=None, workspace=None, completed_since=None, modified_since=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve multiple task records filtered by parameters such as assignee, project, or workspace.
        
        Args:
            assignee: The assignee to filter tasks on. Set to `any` with `null` value to search for unassigned tasks. Requires `workspace` to be specified.
            completed_since: Only return tasks that are incomplete or have been completed since this time.
            limit: Number of results per page (between 1 and 100).
            modified_since: Only return tasks modified since this time.
            offset: Offset token for pagination. Must be from a previous request.
            opt_fields: Optional fields to include in the response (comma-separated list).
            opt_pretty: Provide 'pretty' output for better readability.
            project: The project to filter tasks on.
            section: The section to filter tasks on.
            workspace: The workspace to filter tasks on. Requires `assignee` to be specified.
        
        Returns:
            A dictionary containing compact task records for the filtered set of tasks.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request. It may occur due to network issues or invalid response from the server.
        
        Tags:
            tasks, list, filter, important
        """
        url = f"{self.base_url}/tasks"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('assignee', assignee), ('project', project), ('section', section), ('workspace', workspace), ('completed_since', completed_since), ('modified_since', modified_since), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atask(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new task in a workspace, either explicitly specified or inferred from projects/parent task associations.
        
        Args:
            data: Dictionary containing task data fields to set (unspecified fields use defaults). Required workspace may be inferred from projects/parent.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Enables human-readable formatting for JSON responses (increases response size).
        
        Returns:
            Dictionary containing the created task details, including server-generated fields like ID and timestamps.
        
        Raises:
            HTTPError: When the POST request fails due to invalid data, permissions, or server errors.
        
        Tags:
            create, task, async-job, management, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask(self, task_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve complete task record for a single task, including optional fields and formatted output.
        
        Args:
            opt_fields: Comma-separated property list to include optional fields (excluded by default in compact responses)
            opt_pretty: Enable human-readable formatting (increases response size and processing time)
        
        Returns:
            Dictionary containing the complete task record with requested fields
        
        Raises:
            requests.HTTPError: If API request fails (e.g., invalid task ID or server error)
        
        Tags:
            retrieve, tasks, api, get, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atask(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates a specific, existing task by making a PUT request. Only the fields provided in the `data` block are updated.
        
        Args:
            data: Dictionary containing the fields to be updated in the task. Only the specified fields are modified.
            opt_fields: Optional query parameter to include additional properties in the response.
            opt_pretty: Optional query parameter to format the JSON response for readability.
        
        Returns:
            The complete updated task record as a dictionary.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, task, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atask(self, task_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific task permanently after moving it to the user's trash (recoverable for 30 days). Returns an empty data record upon success.
        
        Args:
            opt_pretty: Controls formatted response output (JSON pretty-printing). Use only during debugging due to performance impact.
        
        Returns:
            Empty dictionary representing a successful deletion, as the task will reside in trash until permanent removal.
        
        Raises:
            HTTPError: Raised for API request failures (e.g., task doesn't exist, authentication errors, or server issues).
        
        Tags:
            delete, tasks, async_job, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def duplicate_atask(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Duplicates a task by creating and returning a job that asynchronously handles the duplication.
        
        Args:
            data: The data required for duplicating the task. It should be a dictionary of string keys to any type values.
            opt_fields: Optional fields to include in the response. Specify as a comma-separated list of properties.
            opt_pretty: Set to True for a pretty output format. This is useful during debugging and may increase response time and size.
        
        Returns:
            A dictionary containing information about the job created for duplicating the task.
        
        Raises:
            requests.HTTPError: If the HTTP request fails due to a server error or an unexpected status code.
        
        Tags:
            duplicate, async_job, task-management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/duplicate"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_aproject(self, project_gid, opt_fields=None, completed_since=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Get tasks from a project, returning compact task records ordered by their priority within the project.
        
        Args:
            completed_since: Only return tasks that are either incomplete or have been completed since this time. Accepts a date-time string or the keyword 'now'.
            limit: The number of objects to return per page. Must be between 1 and 100.
            offset: Offset token for pagination. An offset returned by a previous paginated request.
            opt_fields: A comma-separated list of properties to include beyond the default compact resource.
            opt_pretty: Provides response in a 'pretty' format, with proper line breaking and indentation.
        
        Returns:
            A dictionary with task records for the project.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request or response (e.g., unauthorized access or server errors).
        
        Tags:
            get, tasks, project, api, async, important
        """
        if project_gid is None:
            raise ValueError("Missing required parameter 'project_gid'")
        url = f"{self.base_url}/projects/{project_gid}/tasks"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('completed_since', completed_since), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_asection(self, section_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None, completed_since=None) -> dict[str, Any]:
        """
        Retrieves tasks from a specified section, primarily designed for board views. Filters can include completion status, pagination limits, and optional field requests.
        
        Args:
            completed_since: Restricts results to incomplete tasks or those completed after this time. Accepts a datetime string or 'now'.
            limit: Maximum number of tasks per page (1-100). Defaults to API's initial page settings if unspecified.
            offset: Pagination token from prior API responses. Omit to start at the first page.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Enables formatted JSON output for readability. Recommended for debugging due to performance impact.
        
        Returns:
            Dictionary containing task records in compact format and pagination details.
        
        Raises:
            requests.HTTPError: Raised for invalid parameters, authentication failures, or server errors (e.g., 4xx/5xx status codes).
        
        Tags:
            tasks, board-view, pagination, async-job, important
        """
        if section_gid is None:
            raise ValueError("Missing required parameter 'section_gid'")
        url = f"{self.base_url}/sections/{section_gid}/tasks"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset), ('completed_since', completed_since)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_atag(self, tag_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve paginated tasks associated with a specific tag. Returns compact task records with optional field inclusion and formatted output.
        
        Args:
            limit: Results per page (1-100). Determines the number of tasks returned per request.
            offset: Offset token for pagination. Use the token returned by previous API responses to fetch subsequent pages.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Enable pretty-printed JSON output for improved readability (increases response size).
        
        Returns:
            Dictionary containing paginated task records and API metadata in JSON format.
        
        Raises:
            HTTPError: Raised when the API request fails due to client or server errors (e.g., invalid parameters, authentication issues).
        
        Tags:
            tasks, pagination, async, management, important
        """
        if tag_gid is None:
            raise ValueError("Missing required parameter 'tag_gid'")
        url = f"{self.base_url}/tags/{tag_gid}/tasks"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tasks_from_auser_task_list(self, user_task_list_gid, opt_fields=None, completed_since=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves tasks from a user's My Tasks list, returning a compact list of tasks with optional filtering and pagination.
        
        Args:
            completed_since: Filters tasks to incomplete or those completed after this time. Accepts a date-time string or 'now'.
            limit: Number of tasks per page (1-100). Controls pagination batch size.
            offset: Pagination token for accessing subsequent result pages from a prior response.
            opt_fields: Comma-separated list of optional fields to include in the compact response.
            opt_pretty: Formats JSON output with indentation for human readability (debugging use only).
        
        Returns:
            Dictionary containing the JSON response with tasks and pagination metadata.
        
        Raises:
            HTTPError: Raised when the API request fails due to network issues, invalid parameters, or authentication errors.
        
        Tags:
            tasks, list, retrieve, pagination, management, important
        """
        if user_task_list_gid is None:
            raise ValueError("Missing required parameter 'user_task_list_gid'")
        url = f"{self.base_url}/user_task_lists/{user_task_list_gid}/tasks"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('completed_since', completed_since), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_subtasks_from_atask(self, task_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve subtasks from a task, returning a compact representation of all task subtasks.
        
        Args:
            limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
            offset: Offset token. An offset to the next page returned by the API. Used for pagination.
            opt_fields: Optional fields to include. Comma-separated list of properties to include beyond the default compact resource.
            opt_pretty: Provides 'pretty' output. Formats response in a human-readable format, primarily for debugging.
        
        Returns:
            A dictionary containing a compact representation of all subtasks.
        
        Raises:
            requests.HTTPError: Raised when an HTTP request error occurs, such as a bad status code.
        
        Tags:
            tasks, management, pagination, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/subtasks"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_asubtask(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a new subtask and adds it to the parent task, returning the full record for the newly created subtask.
        
        Args:
            data: A dictionary containing the data for the new subtask.
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: Providing 'pretty' output in formats like JSON, useful for debugging.
        
        Returns:
            A dictionary containing the full record for the newly created subtask.
        
        Tags:
            create, subtask, tasks, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/subtasks"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_the_parent_of_atask(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Sets the parent of a task, providing optional parameters for specifying additional fields and formatting the response.
        
        Args:
            data: A dictionary containing task data with a parent specification (e.g., 'parent_id').
            opt_fields: Optional fields to include in the response, specified as a comma-separated list.
            opt_pretty: Indicates whether the response should be formatted for readability, useful during debugging.
        
        Returns:
            A dictionary representing the response data from setting the parent of a task.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            tasks, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/setParent"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dependencies_from_atask(self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve paginated dependencies of a task with optional filtering and formatting.
        
        Args:
            limit: Results per page (1-100). Determines the number of dependencies to return per request.
            offset: Offset token for pagination. Use the token returned by previous paginated requests to fetch subsequent pages.
            opt_fields: Comma-separated list of optional fields to include in the compact response.
            opt_pretty: Format response for readability. May increase latency and response size (recommended for debugging only).
        
        Returns:
            Dictionary containing paginated compact dependency representations and API response metadata.
        
        Raises:
            requests.HTTPError: Raised for unsuccessful HTTP responses (e.g., 4XX/5XX status codes) during API communication.
        
        Tags:
            dependencies, paginated, task-management, get, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/dependencies"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_dependencies_for_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Set dependencies for a task by marking other tasks as its dependencies, up to a combined limit of 30 dependents and dependencies.
        
        Args:
            data: Dictionary containing task dependency details.
            opt_pretty: Provide ‘pretty’ output for the response, with proper line breaking and indentation, suitable for debugging.
        
        Returns:
            A dictionary response representing the result of setting task dependencies.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as network errors or invalid responses.
        
        Tags:
            tasks, dependencies, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addDependencies"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unlink_dependencies_from_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Unlink dependencies from a task by sending a request to the specified API endpoint.
        
        Args:
            data: Dictionary containing dependency data to unlink (empty dict if no data provided).
            opt_pretty: Provides formatted output for readability during debugging.
        
        Returns:
            Dictionary containing the API response after successful execution.
        
        Raises:
            HTTPError: Raised when the API request fails (non-2xx status code).
        
        Tags:
            unlink, dependencies, async_job, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeDependencies"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_dependents_from_atask(self, task_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve the compact representations of all dependents of a task, optionally specifying pagination and optional fields.
        
        Args:
            limit: The number of results to return per page, between 1 and 100.
            offset: An offset token for pagination, returned by a previous paginated request.
            opt_fields: A comma-separated list of optional fields to include in the response.
            opt_pretty: A flag to format the response in a 'pretty' (human-readable) format.
        
        Returns:
            A dictionary containing the compact representations of the dependents.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            get, dependents, task, pagination, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/dependents"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_dependents_for_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Sets dependents for a task by marking a set of tasks as dependents if they are not already.
        
        Args:
            data: Dictionary containing task data. This is optional and defaults to None.
            opt_pretty: Option to provide 'pretty' output, such as formatted JSON for debugging purposes. This is optional and defaults to None.
        
        Returns:
            A dictionary response containing the result of setting dependents.
        
        Raises:
            requests.exceptions.HTTPError: Raised when an HTTP error occurs during the request.
        
        Tags:
            tasks, management, important, async_job
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addDependents"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unlink_dependents_from_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Unlinks dependent tasks from the current task via an API request.
        
        Args:
            data: Dictionary containing data required for unlinking dependents. Typically includes identifiers for dependents to remove.
            opt_pretty: If provided, returns formatted JSON output for readability. Impacts performance and response size.
        
        Returns:
            Dictionary containing API response data after processing the unlink request.
        
        Raises:
            HTTPError: Raised for unsuccessful API responses (non-2xx status codes)
        
        Tags:
            tasks, dependents, unlink, api, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeDependents"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_aproject_to_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Associates a task with a project, optionally positioning it relative to other tasks or within a specific section. Returns the API response data.
        
        Args:
            data: Dictionary containing the task and project identifiers, along with optional placement parameters (insert_before, insert_after, section).
            opt_pretty: When True, formats the API response for human readability (increases response size and processing time). Recommended for debugging only.
        
        Returns:
            dict[str, Any]: Parsed JSON response from the API containing operation results (typically an empty data block for successful operations).
        
        Raises:
            requests.HTTPError: Raised when the API request fails, including invalid project/task IDs, placement conflicts, or exceeding the 20-project limit per task.
        
        Tags:
            task, project, add, update, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addProject"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_aproject_from_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove a project from a task, ensuring the task remains in the system but is no longer associated with the specified project.
        
        Args:
            data: A dictionary containing data related to the project removal (optional).
            opt_pretty: Optional parameter to format the response in a readable format, useful for debugging.
        
        Returns:
            An empty data block in JSON format.
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request (e.g., server error).
        
        Tags:
            remove, project, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeProject"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_atag_to_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds a tag to a task and returns the result in JSON format.
        
        Args:
            data: A dictionary containing the data to be added; can be None.
            opt_pretty: Optional flag to provide 'pretty' output, which includes proper line breaking and indentation for readability.
        
        Returns:
            A JSON response containing the result of adding a tag to a task.
        
        Raises:
            requests.exceptions.HTTPError: Raised if an HTTP request returns an unsuccessful status code.
        
        Tags:
            modify, task, management, async_job
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addTag"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_atag_from_atask(self, task_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove a tag from a task by sending a POST request with the task data.
        
        Args:
            data: An optional dictionary containing data for the task
            opt_pretty: An optional flag to provide the response in a pretty format
        
        Returns:
            An empty data block returned as a dictionary
        
        Raises:
            requests.exceptions.HTTPError: Raised if the server returns an unsuccessful status code
        
        Tags:
            remove, task, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeTag"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_followers_to_atask(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds followers to a task, returning the updated task record.
        
        Args:
            data: Dictionary containing data for the followers to add. Default value: None.
            opt_fields: Optional fields to include in the response, specified as a comma-separated list. Default value: None.
            opt_pretty: Flag to format the response output. Default value: None.
        
        Returns:
            The updated task record with added followers.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails, indicating a status code that signifies an error.
        
        Tags:
            add, followers, task, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/addFollowers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_followers_from_atask(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove specified followers from a task and return the updated task record.
        
        Args:
            data: Dictionary containing follower removal data; expects a structured format of follower identifiers to remove.
            opt_fields: Optional fields to include in response as comma-separated list. Used to expand default-compact responses.
            opt_pretty: Enables pretty-printed JSON output at the cost of performance and response size.
        
        Returns:
            Dictionary containing the complete updated task record after follower removal.
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP responses (e.g., 4XX/5XX status codes).
        
        Tags:
            remove, followers, task, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/removeFollowers"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_for_agiven_custom_id(self, workspace_gid, custom_id) -> dict[str, Any]:
        """
        Fetches a task associated with a given custom ID.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A dictionary containing the task details.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request.
        
        Tags:
            task-retrieval, custom-id, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        if custom_id is None:
            raise ValueError("Missing required parameter 'custom_id'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/tasks/custom_id/{custom_id}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def search_tasks_in_aworkspace(self, workspace_gid, opt_fields=None, opt_pretty=None, text=None, resource_subtype=None, assignee_any=None, assignee_not=None, portfolios_any=None, projects_any=None, projects_not=None, projects_all=None, sections_any=None, sections_not=None, sections_all=None, tags_any=None, tags_not=None, tags_all=None, teams_any=None, followers_not=None, created_by_any=None, created_by_not=None, assigned_by_any=None, assigned_by_not=None, liked_by_not=None, commented_on_by_not=None, due_on_before=None, due_on_after=None, due_on=None, due_at_before=None, due_at_after=None, start_on_before=None, start_on_after=None, start_on=None, created_on_before=None, created_on_after=None, created_on=None, created_at_before=None, created_at_after=None, completed_on_before=None, completed_on_after=None, completed_on=None, completed_at_before=None, completed_at_after=None, modified_on_before=None, modified_on_after=None, modified_on=None, modified_at_before=None, modified_at_after=None, is_blocking=None, is_blocked=None, has_attachment=None, completed=None, is_subtask=None, sort_by=None, sort_ascending=None) -> dict[str, Any]:
        """
        Searches for tasks in a workspace with extensive filtering capabilities based on task attributes, user interactions, dates, and custom parameters.
        
        Args:
            assigned_byany: Comma-separated list of user identifiers from which assigned tasks should be included
            assigned_bynot: Comma-separated list of user identifiers from which assigned tasks should be excluded
            assigneeany: Comma-separated list of user identifiers for included assignees
            assigneenot: Comma-separated list of user identifiers for excluded assignees
            commented_on_bynot: Comma-separated list of user identifiers who should not have commented
            completed: Filter to include only completed tasks (true) or exclude them (false)
            completed_atafter: ISO 8601 datetime string for filtering tasks completed after this time
            completed_atbefore: ISO 8601 datetime string for filtering tasks completed before this time
            completed_on: ISO 8601 date string or `null` for filtering tasks completed on a specific date
            completed_onafter: ISO 8601 date string for filtering tasks completed after this date
            completed_onbefore: ISO 8601 date string for filtering tasks completed before this date
            created_atafter: ISO 8601 datetime string for filtering tasks created after this time
            created_atbefore: ISO 8601 datetime string for filtering tasks created before this time
            created_byany: Comma-separated list of user identifiers for task creators to include
            created_bynot: Comma-separated list of user identifiers for task creators to exclude
            created_on: ISO 8601 date string or `null` for filtering tasks created on a specific date
            created_onafter: ISO 8601 date string for filtering tasks created after this date
            created_onbefore: ISO 8601 date string for filtering tasks created before this date
            due_atafter: ISO 8601 datetime string for filtering tasks due after this time
            due_atbefore: ISO 8601 datetime string for filtering tasks due before this time
            due_on: ISO 8601 date string or `null` for filtering tasks due on a specific date
            due_onafter: ISO 8601 date string for filtering tasks due after this date
            due_onbefore: ISO 8601 date string for filtering tasks due before this date
            followersnot: Comma-separated list of user identifiers who should not be followers
            has_attachment: Filter to include only tasks with attachments (true) or exclude them (false)
            is_blocked: Filter to include only tasks with incomplete dependencies (true) or exclude them (false)
            is_blocking: Filter to include only incomplete tasks with dependents (true) or exclude them (false)
            is_subtask: Filter to include only subtasks (true) or exclude them (false)
            liked_bynot: Comma-separated list of user identifiers who should not have liked the task
            modified_atafter: ISO 8601 datetime string for filtering tasks modified after this time
            modified_atbefore: ISO 8601 datetime string for filtering tasks modified before this time
            modified_on: ISO 8601 date string or `null` for filtering tasks modified on a specific date
            modified_onafter: ISO 8601 date string for filtering tasks modified after this date
            modified_onbefore: ISO 8601 date string for filtering tasks modified before this date
            opt_fields: Comma-separated list of optional properties to include in the response
            opt_pretty: Controls pretty JSON output formatting (recommended for debugging only)
            portfoliosany: Comma-separated list of portfolio IDs to include
            projectsall: Comma-separated list of project IDs for tasks belonging to ALL specified projects
            projectsany: Comma-separated list of project IDs to include
            projectsnot: Comma-separated list of project IDs to exclude
            resource_subtype: Filters results by specific task subtype
            sectionsall: Comma-separated list of section/column IDs for tasks in ALL specified sections
            sectionsany: Comma-separated list of section/column IDs to include
            sectionsnot: Comma-separated list of section/column IDs to exclude
            sort_ascending: Sort results in ascending order (default: false)
            sort_by: Sort field (due_date, created_at, completed_at, likes, or modified_at)
            start_on: ISO 8601 date string or `null` for filtering tasks starting on a specific date
            start_onafter: ISO 8601 date string for filtering tasks starting after this date
            start_onbefore: ISO 8601 date string for filtering tasks starting before this date
            tagsall: Comma-separated list of tag IDs for tasks containing ALL specified tags
            tagsany: Comma-separated list of tag IDs to include
            tagsnot: Comma-separated list of tag IDs to exclude
            teamsany: Comma-separated list of team IDs to include
            text: Full-text search term for task name and description
        
        Returns:
            Dictionary containing task data matching the specified filters. Exact structure depends on opt_fields parameter and API implementation.
        
        Raises:
            HTTPError: Raised when the API request fails due to network issues, authentication problems, or invalid parameters.
        
        Tags:
            search, task-management, filtering, api-client, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/tasks/search"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('text', text), ('resource_subtype', resource_subtype), ('assignee.any', assignee_any), ('assignee.not', assignee_not), ('portfolios.any', portfolios_any), ('projects.any', projects_any), ('projects.not', projects_not), ('projects.all', projects_all), ('sections.any', sections_any), ('sections.not', sections_not), ('sections.all', sections_all), ('tags.any', tags_any), ('tags.not', tags_not), ('tags.all', tags_all), ('teams.any', teams_any), ('followers.not', followers_not), ('created_by.any', created_by_any), ('created_by.not', created_by_not), ('assigned_by.any', assigned_by_any), ('assigned_by.not', assigned_by_not), ('liked_by.not', liked_by_not), ('commented_on_by.not', commented_on_by_not), ('due_on.before', due_on_before), ('due_on.after', due_on_after), ('due_on', due_on), ('due_at.before', due_at_before), ('due_at.after', due_at_after), ('start_on.before', start_on_before), ('start_on.after', start_on_after), ('start_on', start_on), ('created_on.before', created_on_before), ('created_on.after', created_on_after), ('created_on', created_on), ('created_at.before', created_at_before), ('created_at.after', created_at_after), ('completed_on.before', completed_on_before), ('completed_on.after', completed_on_after), ('completed_on', completed_on), ('completed_at.before', completed_at_before), ('completed_at.after', completed_at_after), ('modified_on.before', modified_on_before), ('modified_on.after', modified_on_after), ('modified_on', modified_on), ('modified_at.before', modified_at_before), ('modified_at.after', modified_at_after), ('is_blocking', is_blocking), ('is_blocked', is_blocked), ('has_attachment', has_attachment), ('completed', completed), ('is_subtask', is_subtask), ('sort_by', sort_by), ('sort_ascending', sort_ascending)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_task_templates(self, limit=None, offset=None, project=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve multiple task templates with pagination and filtering options. Returns compact records of task templates filtered by specified criteria, requiring a project parameter for filtering.
        
        Args:
            limit: Results per page. Must be between 1 and 100. Defaults to API's default page size if not specified.
            offset: Offset token for pagination. Must use a token returned by a previous paginated request. Omit to retrieve first page.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Enable pretty-printed JSON output (for debugging only, increases response size/time).
            project: Project ID to filter task templates. Required for successful filtering.
        
        Returns:
            Dictionary containing the JSON response with compact task template records and pagination details.
        
        Raises:
            requests.HTTPError: Raised for API request failures (e.g., invalid project ID, authentication errors, or server issues).
        
        Tags:
            task-templates, list, pagination, async-job, management, important
        """
        url = f"{self.base_url}/task_templates"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('project', project), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atask_template(self, task_template_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a complete task template record.
        
        Args:
            opt_fields: A comma-separated list of optional properties to include in the response.
            opt_pretty: Enables 'pretty' output for the response, useful for debugging.
        
        Returns:
            A dictionary containing the task template record.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            template, task-management, async_job, fetch, important
        """
        if task_template_gid is None:
            raise ValueError("Missing required parameter 'task_template_gid'")
        url = f"{self.base_url}/task_templates/{task_template_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atask_template(self, task_template_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Deletes a specific task template by making a DELETE request and returns an empty data record.
        
        Args:
            opt_pretty: Provides the response in a 'pretty' format. In the case of JSON, this means proper line breaking and indentation. Advisable only during debugging.
        
        Returns:
            An empty data record in JSON format.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, task-template, important, management
        """
        if task_template_gid is None:
            raise ValueError("Missing required parameter 'task_template_gid'")
        url = f"{self.base_url}/task_templates/{task_template_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def instantiate_atask_from_atask_template(self, task_template_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Instantiate a task from a task template, creating and returning a job to handle the task asynchronously.
        
        Args:
            data: A dictionary containing task data used for instantiation. This is optional and defaults to None.
            opt_fields: Optional fields to include in the response. This should be a comma-separated list of properties.
            opt_pretty: Determines if the output should be in a pretty format. Useful for debugging.
        
        Returns:
            A dictionary representing the job details.
        
        Raises:
            requests.exceptions.HTTPError: Raised when an HTTP request returns an unsuccessful status code.
        
        Tags:
            instantiate, task-template, async-job, job-management, important
        """
        if task_template_gid is None:
            raise ValueError("Missing required parameter 'task_template_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/task_templates/{task_template_gid}/instantiateTask"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_ateam(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Creates a team within the current workspace.
        
        Args:
            data: Dictionary containing team creation data.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Flag to provide response in a pretty format.
        
        Returns:
            Dictionary representing the created team.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, team, management, important
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam(self, team_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve detailed information about a team, including optional fields and formatted output as specified.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response (excluded by default).
            opt_pretty: Format response with improved readability at the cost of performance. Recommended only for debugging.
        
        Returns:
            A dictionary containing the full record of the requested team, including specified optional fields.
        
        Raises:
            HTTPError: If the API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            teams, get, api-endpoint, management, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_ateam(self, team_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Update a team within the current workspace, including modifying team data and requesting optional fields in the response.
        
        Args:
            data: dict containing team data to update. 'None' results in no data being submitted.
            opt_fields: comma-separated list of optional properties to include in the response (excluded by default).
            opt_pretty: enable formatted JSON output with proper indentation (increases response size and processing time).
        
        Returns:
            dict containing the updated team resource, with fields determined by opt_fields parameter.
        
        Raises:
            requests.HTTPError: raised for unsuccessful HTTP responses (e.g., 4XX/5XX status codes)
        
        Tags:
            teams, update, management, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_teams_in_aworkspace(self, workspace_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve paginated records of teams in a workspace visible to the authorized user.
        
        Args:
            limit: Results per page (1-100). Controls the number of objects returned per page.
            offset: Offset token for pagination. Use the token from a previous paginated response to fetch subsequent pages.
            opt_fields: Comma-separated list of optional properties to include in the compact resource response.
            opt_pretty: If true, returns a formatted JSON response for readability during debugging (increases response size and processing time).
        
        Returns:
            Dictionary containing the JSON response with compact team records and pagination details.
        
        Raises:
            requests.HTTPError: Raised for failed API requests (e.g., invalid credentials, rate limiting, or server errors).
        
        Tags:
            teams, workspace, pagination, api-client, list, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/teams"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_teams_for_auser(self, user_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None, organization=None) -> dict[str, Any]:
        """
        Retrieve paginated list of compact team records for a user based on workspace/organization filter.
        
        Args:
            limit: Results per page (1-100). Controls number of objects returned per API call.
            offset: Pagination token from previous response. Required for subsequent pages.
            opt_fields: Comma-separated optional properties to include in response.
            opt_pretty: Format response for readability (debugging only).
            organization: Required workspace/organization identifier to filter teams.
        
        Returns:
            Dictionary containing paginated API response with team records and metadata.
        
        Raises:
            HTTPError: When API request fails (4XX/5XX status codes).
        
        Tags:
            teams, user-management, pagination, api-client, important
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/teams"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset), ('organization', organization)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_auser_to_ateam(self, team_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Adds a user to a team and returns the complete team membership record. Requires the calling user to be a team member and the added user to exist in the same organization.
        
        Args:
            data: Dictionary containing required data for user-to-team association (specific fields not disclosed in annotation)
            opt_fields: Comma-separated list of optional fields to include in response (enhanced detail)
            opt_pretty: Formats JSON output with indentation for human readability (performance-intensive)
        
        Returns:
            Complete team membership record (dictionary) for the newly added user, including optional fields when specified
        
        Raises:
            HTTPError: When the POST request fails (4XX/5XX status) or authorization requirements aren't met
        
        Tags:
            add, user-management, team-management, membership, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}/addUser"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_auser_from_ateam(self, team_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove a user from a team, requiring team membership in the calling user.
        
        Args:
            data: Dictionary containing user/team data (specific fields not specified). Must include required identifiers.
            opt_pretty: Provides formatted output (line breaks/indentation) at performance cost. Recommended for debugging only.
        
        Returns:
            JSON response dictionary containing operation results.
        
        Raises:
            requests.HTTPError: Raised for failed API requests (4XX/5XX status codes) during removal.
        
        Tags:
            teams, user-management, remove, api, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/teams/{team_gid}/removeUser"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_ateam_membership(self, team_membership_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Get a team membership record. Returns the complete membership details for a single team.
        
        Args:
            opt_fields: Optional fields to include in the response. Pass a comma-separated list of properties to include.
            opt_pretty: Optional parameter to format the JSON response for readability.
        
        Returns:
            A dictionary containing the team membership record.
        
        Raises:
            requests.HTTPError: Raised if there is an HTTP error with the request (e.g., network error, server returns a non-200 status code).
        
        Tags:
            team, membership, retrieve, important
        """
        if team_membership_gid is None:
            raise ValueError("Missing required parameter 'team_membership_gid'")
        url = f"{self.base_url}/team_memberships/{team_membership_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_memberships(self, team=None, user=None, workspace=None, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve team membership records with pagination and optional field filtering.
        
        Args:
            limit: Results per page. The number of objects to return (1-100).
            offset: Offset token for pagination. Use the token from a prior paginated response.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Format response with indentation/line-breaks for readability (debugging use only).
            team: Globally unique identifier for the team.
            user: User identifier ('me', email, or gid). Must be used with workspace parameter.
            workspace: Globally unique workspace identifier. Must be used with user parameter.
        
        Returns:
            Dictionary containing paginated compact team membership records, typically including 'data' array and 'next_page' metadata.
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters, authentication, or server errors.
        
        Tags:
            team-memberships, pagination, api-call, retrieval, management, collaboration, important
        """
        url = f"{self.base_url}/team_memberships"
        query_params = {k: v for k, v in [('team', team), ('user', user), ('workspace', workspace), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_ateam(self, team_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve paginated team memberships with optional field inclusion and response formatting.
        
        Args:
            limit: Results per page, between 1-100. Controls the number of objects returned per page.
            offset: Offset token for pagination. Use the token returned from a previous paginated request to fetch subsequent pages.
            opt_fields: Comma-separated list of optional fields to include in the response. Excluded by default.
            opt_pretty: Format response for readability (increases processing time and response size). Recommended for debugging only.
        
        Returns:
            Dictionary containing paginated team membership data retrieved from the API.
        
        Raises:
            HTTPError: When the API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            team-memberships, pagination, api-client, get, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/team_memberships"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_memberships_from_auser(self, user_gid, workspace=None, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves memberships for a user, returning compact team membership records.
        
        Args:
            limit: Results per page; must be between 1 and 100. Defaults to None.
            offset: Offset token for pagination; returned by a previous API request. Defaults to None.
            opt_fields: Comma-separated list of optional fields to include in the response. Defaults to None.
            opt_pretty: Provides response in a formatted (pretty) JSON format, which may slow down the response. Defaults to None.
            workspace: Globally unique identifier for the workspace. Required.
        
        Returns:
            A dictionary containing membership records for the user.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request fails due to a status code error.
        
        Tags:
            memberships, team, user-data, important
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/team_memberships"
        query_params = {k: v for k, v in [('workspace', workspace), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atime_period(self, time_period_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a specific time period record with optional field inclusions and formatted output.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response (excluded by default).
            opt_pretty: Format response with indentation/line breaks for readability (increases response size and processing time).
        
        Returns:
            Full time period record as a dictionary containing all available data fields.
        
        Raises:
            HTTPError: When the request returns a non-2xx status code, indicating server/client errors.
        
        Tags:
            time-periods, get, record, api, important
        """
        if time_period_gid is None:
            raise ValueError("Missing required parameter 'time_period_gid'")
        url = f"{self.base_url}/time_periods/{time_period_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_time_periods(self, start_on=None, end_on=None, workspace=None, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve compact time period records based on specified date range and pagination parameters.
        
        Args:
            end_on: ISO 8601 date string for the end of the period (inclusive). If not provided, default behavior applies.
            limit: Number of results per page (1-100). Determines pagination size when multiple pages exist.
            offset: Token from previous paginated response to get next page. Required for subsequent pages after initial request.
            opt_fields: Comma-separated property names to include in response instead of default compact format.
            opt_pretty: Pretty-print JSON output with formatting for human readability (debugging only).
            start_on: ISO 8601 date string for the period start (inclusive). If not provided, default behavior applies.
            workspace: (Required) Globally unique workspace identifier to scope the request.
        
        Returns:
            Dictionary containing paginated time period records in JSON format from the API response.
        
        Raises:
            HTTPError: Raised for invalid API requests, authentication failures, or server errors.
        
        Tags:
            time-periods, pagination, api-client, data-retrieval, important
        """
        url = f"{self.base_url}/time_periods"
        query_params = {k: v for k, v in [('start_on', start_on), ('end_on', end_on), ('workspace', workspace), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_time_tracking_entries_for_atask(self, task_gid, limit=None, offset=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve paginated time tracking entries for a specific task.
        
        Args:
            limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
            offset: Offset token for pagination. Use the token returned from a prior paginated request.
            opt_fields: Optional properties to include in the response as a comma-separated list.
            opt_pretty: Enable pretty output formatting for readability (may impact performance).
        
        Returns:
            A dictionary containing the time tracking entries and pagination details.
        
        Raises:
            HTTPError: If the API request fails or returns an error status code.
        
        Tags:
            time-tracking, entries, pagination, async-job, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        url = f"{self.base_url}/tasks/{task_gid}/time_tracking_entries"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_atime_tracking_entry(self, task_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Create a new time tracking entry for a given task.
        
        Args:
            data: Dictionary of data for the time tracking entry. Defaults to None.
            opt_fields: A comma-separated list of optional fields to include in the response. Defaults to None.
            opt_pretty: Boolean or string to format the response in a pretty format. Defaults to None.
        
        Returns:
            A dictionary representing the newly created time tracking entry.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            time-tracking, asynchronous, create-entry, management, important
        """
        if task_gid is None:
            raise ValueError("Missing required parameter 'task_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/tasks/{task_gid}/time_tracking_entries"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_atime_tracking_entry(self, time_tracking_entry_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves a complete time tracking entry record from the API, returning all available data in dictionary format.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response. Excludes certain properties by default.
            opt_pretty: Formats the response with improved readability (e.g., indentation and line breaks) at the cost of performance and response size.
        
        Returns:
            Dictionary containing the full time tracking entry record with requested fields.
        
        Raises:
            HTTPError: If the API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            time-tracking, get, api-client, management, important
        """
        if time_tracking_entry_gid is None:
            raise ValueError("Missing required parameter 'time_tracking_entry_gid'")
        url = f"{self.base_url}/time_tracking_entries/{time_tracking_entry_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_atime_tracking_entry(self, time_tracking_entry_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing time tracking entry by sending a PUT request with the specified fields.
        
        Args:
            data: Dictionary of fields to update in the time tracking entry. Only specified fields are updated.
            opt_fields: A comma-separated list of optional properties to include in the response.
            opt_pretty: If set, returns the response in a pretty format for debugging purposes.
        
        Returns:
            The complete updated time tracking entry record.
        
        Raises:
            HTTPError: Raised if the HTTP request fails for any reason, such as a connection error or a non-200 status code.
        
        Tags:
            update, time-tracking, async_job, management, important
        """
        if time_tracking_entry_gid is None:
            raise ValueError("Missing required parameter 'time_tracking_entry_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/time_tracking_entries/{time_tracking_entry_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_atime_tracking_entry(self, time_tracking_entry_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Delete a specific time tracking entry via DELETE request to its URL.
        
        Args:
            opt_pretty: Provides 'pretty' JSON output with formatting for readability. Increases response size and processing time (recommended for debugging only).
        
        Returns:
            Empty dictionary representing successful deletion confirmation.
        
        Raises:
            HTTPError: Raised for failed requests (4XX/5XX status codes)
        
        Tags:
            delete, time-tracking, management, important
        """
        if time_tracking_entry_gid is None:
            raise ValueError("Missing required parameter 'time_tracking_entry_gid'")
        url = f"{self.base_url}/time_tracking_entries/{time_tracking_entry_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_objects_via_typeahead(self, workspace_gid, opt_fields=None, resource_type=None, type=None, query=None, count=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves objects from a workspace using a typeahead search algorithm, providing a limited set of results quickly for auto-completion features.
        
        Args:
            count: The number of results to return. Defaults to 20 if omitted, with a minimum of 1 and a maximum of 100.
            opt_fields: A comma-separated list of optional properties to include in the response, beyond the default compact representation.
            opt_pretty: Flag to provide the response in a 'pretty' format, which may increase response size and processing time.
            query: The search string used for typeahead queries. Leaving it empty still yields ordered results based on resource types.
            resource_type: The type of objects to return (e.g., custom_field, goal, project, portfolio, tag, task, team, user).
            type: *Deprecated*; new integrations should use the resource_type field instead.
        
        Returns:
            A dictionary containing the search results.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            typeahead, search, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/typeahead"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('resource_type', resource_type), ('type', type), ('query', query), ('count', count), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_users(self, opt_fields=None, workspace=None, team=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieves multiple user records from accessible workspaces and organizations with pagination options.
        
        Args:
            limit: Results per page; must be between 1 and 100.
            offset: Offset token for pagination; must be from a previous API response.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Provides ‘pretty’ output, with proper line breaking and indentation.
            team: The team ID to filter users.
            workspace: The workspace or organization ID to filter users.
        
        Returns:
            Dictionary containing user records sorted by user ID.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            users, pagination, async_job, management, important
        """
        url = f"{self.base_url}/users"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('workspace', workspace), ('team', team), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser(self, user_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Get a user record by ID, returning the full user details. Supports optional field inclusion and formatted output.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include in the response (e.g., 'name,email'). Excludes some properties by default if not specified.
            opt_pretty: Enables formatted output (e.g., line breaks, indentation) for readability. Recommended only for debugging due to performance impact.
        
        Returns:
            Dictionary containing the full user record, including all requested fields.
        
        Raises:
            HTTPError: When the API request fails due to invalid user ID, network issues, or server errors.
        
        Tags:
            users, get, api, record, important
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_sfavorites(self, user_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None, resource_type=None, workspace=None) -> dict[str, Any]:
        """
        Get a user's favorites in the specified workspace and resource type, returning paginated results in the same order as Asana's sidebar.
        
        Args:
            limit: Results per page. Must be between 1 and 100.
            offset: Offset token for pagination. Use tokens returned from previous paginated requests.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Provides formatted output at the cost of performance. Recommended for debugging only.
            resource_type: (Required) Type of resources to fetch favorites for.
            workspace: (Required) Workspace ID containing the favorites.
        
        Returns:
            Dictionary containing paginated favorites data, typically including a 'data' array and pagination metadata.
        
        Raises:
            HTTPError: Raised for invalid requests, authentication failures, or server errors (via response.raise_for_status())
        
        Tags:
            user, favorites, pagination, workspace, get, management, important
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/favorites"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset), ('resource_type', resource_type), ('workspace', workspace)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_in_ateam(self, team_gid, opt_fields=None, opt_pretty=None, offset=None) -> dict[str, Any]:
        """
        Retrieve paginated list of team members, returning compact user records sorted alphabetically with a limit of 2000 results. For larger datasets, use the `/users` endpoint.
        
        Args:
            offset: Offset token for pagination. Requires a token from a prior paginated response to fetch subsequent pages. Omit to retrieve first page.
            opt_fields: Comma-separated optional property list to include in response. Defaults return compact records.
            opt_pretty: Enable formatted output for readability (increases processing time and response size). Recommended for debugging only.
        
        Returns:
            Dictionary containing API response with user records and pagination metadata.
        
        Raises:
            requests.exceptions.HTTPError: Raised for failed API responses (4XX/5XX status codes).
        
        Tags:
            users, retrieve, pagination, team-management, important
        """
        if team_gid is None:
            raise ValueError("Missing required parameter 'team_gid'")
        url = f"{self.base_url}/teams/{team_gid}/users"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_users_in_aworkspace_or_organization(self, workspace_gid, opt_fields=None, opt_pretty=None, offset=None) -> dict[str, Any]:
        """
        Retrieve paginated list of users in a workspace or organization, sorted alphabetically and limited to 2000 records. For larger datasets, use the `/users` endpoint.
        
        Args:
            offset: Offset token for pagination. Use the token from a previous paginated response to fetch the next page. Omit to start from the first page.
            opt_fields: Comma-separated list of optional properties to include in the response (excluded by default in compact resources).
            opt_pretty: Format response with improved readability (increases processing time and response size). Recommended for debugging only.
        
        Returns:
            Dictionary containing compact user records and pagination metadata.
        
        Raises:
            HTTPError: When API request fails due to network issues, invalid parameters, or server errors (handled via response.raise_for_status()).
        
        Tags:
            list, users, pagination, workspace, organization, management, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/users"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_task_list(self, user_task_list_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieves the full record for a user task list. Optionally includes additional fields and formats the response for readability.
        
        Args:
            opt_fields: A comma-separated list of optional properties to include in the response.
            opt_pretty: Enables 'pretty' formatting for JSON responses, improving readability but potentially increasing response time.
        
        Returns:
            A dictionary containing the user task list data.
        
        Raises:
            HTTPError: Raised by the response object if the HTTP request returns a status indicating an error.
        
        Tags:
            list, management, user-task, important
        """
        if user_task_list_gid is None:
            raise ValueError("Missing required parameter 'user_task_list_gid'")
        url = f"{self.base_url}/user_task_lists/{user_task_list_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_auser_stask_list(self, user_gid, opt_fields=None, opt_pretty=None, workspace=None) -> dict[str, Any]:
        """
        Fetches a user's task list from a specified workspace.
        
        Args:
            opt_fields: Optional fields to include in the response. Specify as a comma-separated list of properties.
            opt_pretty: Whether to return the response in a readable 'pretty' format. Advisable for debugging.
            workspace: The workspace from which to retrieve the task list.
        
        Returns:
            A dictionary containing the user's task list.
        
        Raises:
            HTTPError: Raised if the HTTP request fails.
        
        Tags:
            fetch, task-list, user-management, workspace, important
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/user_task_list"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('workspace', workspace)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_webhooks(self, limit=None, offset=None, workspace=None, resource=None, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Get compact representations of all webhooks registered by the app for the authenticated user in a specific workspace.
        
        Args:
            limit: Results per page (1-100). Controls the number of objects to return per page.
            offset: Offset token for pagination. Use the token from a prior paginated response to fetch subsequent pages. Omitting returns the first page.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Provides formatted output for readability, increasing response time and size (recommended for debugging only).
            resource: Filters webhooks to only those associated with the specified resource.
            workspace: (Required) Workspace identifier to query for registered webhooks.
        
        Returns:
            Dictionary containing paginated webhook data in compact format, including metadata about the pagination state.
        
        Raises:
            requests.HTTPError: Raised for invalid requests, including unauthorized workspace access, nonexistent resources, or server-side errors.
        
        Tags:
            get, webhooks, pagination, management, important
        """
        url = f"{self.base_url}/webhooks"
        query_params = {k: v for k, v in [('limit', limit), ('offset', offset), ('workspace', workspace), ('resource', resource), ('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def establish_awebhook(self, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Initiates a webhook creation process with a confirmation handshake, requiring asynchronous server handling to validate the webhook subscription.
        
        Args:
            data: Dictionary containing webhook configuration details such as resource (the resource ID to monitor) and target (URL receiving webhook events).
            opt_fields: Comma-separated string of optional fields to include in the response. Default excludes some properties.
            opt_pretty: Boolean flag to enable formatted JSON output (increases response size and processing time).
        
        Returns:
            Dictionary containing webhook metadata including gid, resource details, target URL, and activation status. Includes X-Hook-Secret header for future event verification.
        
        Raises:
            requests.HTTPError: Raised for invalid hostnames (403 Forbidden), failed handshake validation, or API request failures.
        
        Tags:
            webhooks, async-handshake, important, api-integration
        """
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhooks"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_awebhook(self, webhook_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve the full record of a webhook including optional fields if specified.
        
        Args:
            opt_fields: Comma-separated list of optional properties to include (excluded by default).
            opt_pretty: Enables formatted JSON output for readability during debugging. Increases response size/processing time.
        
        Returns:
            Dictionary containing the complete webhook record with included fields.
        
        Raises:
            HTTPError: If the API request fails due to network issues, authentication errors, or invalid parameters.
        
        Tags:
            webhook, get, async_job, management, important
        """
        if webhook_gid is None:
            raise ValueError("Missing required parameter 'webhook_gid'")
        url = f"{self.base_url}/webhooks/{webhook_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_awebhook(self, webhook_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Update an existing webhook by making a PUT request and overwriting its filters with new data.
        
        Args:
            data: The data to be sent in the request body. It should include the updated filters for the webhook.
            opt_fields: A comma-separated list of optional fields to be included in the response.
            opt_pretty: A flag to provide the response in a pretty format, useful for debugging.
        
        Returns:
            A dictionary containing the updated webhook data.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, webhook, important, http_request
        """
        if webhook_gid is None:
            raise ValueError("Missing required parameter 'webhook_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhooks/{webhook_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_awebhook(self, webhook_gid, opt_pretty=None) -> dict[str, Any]:
        """
        Permanently deletes a webhook. Once deleted, no further requests will be issued, though in-flight requests might still be received.
        
        Args:
            opt_pretty: Provides 'pretty' output with proper formatting (line breaks, indentation) for readability. This increases response size and processing time - recommended only for debugging.
        
        Returns:
            dict[str, Any]: Parsed JSON response containing the deletion result.
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures (4XX/5XX status codes).
        
        Tags:
            delete, webhooks, api-management, important
        """
        if webhook_gid is None:
            raise ValueError("Missing required parameter 'webhook_gid'")
        url = f"{self.base_url}/webhooks/{webhook_gid}"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_multiple_workspaces(self, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Fetches multiple workspaces visible to the authorized user. Returns compact records with pagination support.
        
        Args:
            limit: Number of results per page. Must be between 1 and 100.
            offset: Offset token for pagination. Use the value returned by a previous request.
            opt_fields: Comma-separated list of optional properties to include.
            opt_pretty: Provides response in a readable format, useful for debugging.
        
        Returns:
            A dictionary containing workspace records.
        
        Raises:
            HTTPError: Raised if the API request encounters any HTTP errors.
        
        Tags:
            list, workspaces, pagination, api-call, important
        """
        url = f"{self.base_url}/workspaces"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace(self, workspace_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Get the full workspace record for a single workspace.
        
        Args:
            opt_fields: Optional fields to include, specified as a comma-separated list. This endpoint returns a compact resource by default, excluding some properties.
            opt_pretty: Enables pretty output, making the response more readable with proper line breaks and indentation.
        
        Returns:
            A dictionary containing the full workspace record.
        
        Raises:
            requests.RequestException: Raised if an HTTP request issue occurs, such as connection errors or invalid responses.
        
        Tags:
            get, workspace, management, api-call, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_aworkspace(self, workspace_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Updates an existing workspace by modifying specified fields and returns the updated workspace record.
        
        Args:
            data: Dictionary containing workspace data to update. Currently only the 'name' field is modifiable.
            opt_fields: Comma-separated list of optional fields to include in the response.
            opt_pretty: Enables formatted JSON output for debugging purposes, increasing response size and processing time.
        
        Returns:
            Complete updated workspace record as a dictionary.
        
        Raises:
            HTTPError: Raised when the API request fails, such as invalid input data or server errors.
        
        Tags:
            update, workspace, management, important, async-job
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_auser_to_aworkspace_or_organization(self, workspace_gid, opt_fields=None, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Add a user to a workspace or organization by user ID or email and return the full user record.
        
        Args:
            data: Dictionary containing user data. Required for the operation.
            opt_fields: Optional query parameter to include additional properties in the response. Specify as a comma-separated list of properties.
            opt_pretty: Return the response in a human-readable format.
        
        Returns:
            A dictionary representing the full user record for the invited user.
        
        Raises:
            RequestException: Raised if there is a problem with the HTTP request, such as network issues or server errors.
        
        Tags:
            add, management, user, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/addUser"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_auser_from_aworkspace_or_organization(self, workspace_gid, opt_pretty=None, data=None) -> dict[str, Any]:
        """
        Remove a user from a workspace or organization. Requires admin privileges in the target workspace. Supports user identification by globally unique ID or email address.
        
        Args:
            data: Dictionary containing user removal parameters (e.g., user identifiers and workspace details)
            opt_pretty: Provides formatted response output. Recommended only for debugging due to performance impact
        
        Returns:
            Empty dictionary confirming successful operation. Actual removal confirmation should be verified through status codes.
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP responses (4xx/5xx status codes) from the API endpoint
        
        Tags:
            remove, user-management, workspaces, organizations, admin, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        request_body = {
            'data': data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/workspaces/{workspace_gid}/removeUser"
        query_params = {k: v for k, v in [('opt_pretty', opt_pretty)] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_aworkspace_membership(self, workspace_membership_gid, opt_fields=None, opt_pretty=None) -> dict[str, Any]:
        """
        Retrieve a workspace membership and return its complete workspace record.
        
        Args:
            opt_fields: Comma-separated list of optional fields to include in the response (excludes some properties by default without this parameter).
            opt_pretty: Return formatted JSON with indentation and line breaks for readability (recommended only for debugging).
        
        Returns:
            Dictionary containing the full workspace membership record.
        
        Raises:
            HTTPError: Raised if the API request fails (e.g., invalid permissions or workspace membership ID).
        
        Tags:
            workspace, membership, get, management, important
        """
        if workspace_membership_gid is None:
            raise ValueError("Missing required parameter 'workspace_membership_gid'")
        url = f"{self.base_url}/workspace_memberships/{workspace_membership_gid}"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_workspace_memberships_for_auser(self, user_gid, opt_fields=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Fetches the compact workspace membership records for a user, allowing pagination via limit and offset parameters.
        
        Args:
            limit: Results per page; must be between 1 and 100.
            offset: Offset token for pagination; must be returned by a previous request.
            opt_fields: Comma-separated list of properties to include beyond the default compact resource.
            opt_pretty: Enables 'pretty' output, typically for debugging purposes.
        
        Returns:
            A dictionary containing the workspace membership records for the user.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request fails due to a status code in the 4xx or 5xx range.
        
        Tags:
            workspace, memberships, pagination, management, important
        """
        if user_gid is None:
            raise ValueError("Missing required parameter 'user_gid'")
        url = f"{self.base_url}/users/{user_gid}/workspace_memberships"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_the_workspace_memberships_for_aworkspace(self, workspace_gid, opt_fields=None, user=None, opt_pretty=None, limit=None, offset=None) -> dict[str, Any]:
        """
        Retrieve paginated workspace membership records for a specified workspace, including optional field selection and user filtering.
        
        Args:
            limit: Results per page (1-100). Controls pagination size.
            offset: Pagination token from a previous response to fetch specific pages.
            opt_fields: Comma-separated list of optional properties to include in the response.
            opt_pretty: Format response with human-readable spacing/indentation (debugging use only).
            user: User identifier ('me', email, or gid) for membership filtering.
        
        Returns:
            Dictionary containing paginated workspace membership records with requested fields.
        
        Raises:
            requests.exceptions.HTTPError: Raised for API response failures (4XX/5XX status codes).
        
        Tags:
            workspace-memberships, pagination, filter, management, important
        """
        if workspace_gid is None:
            raise ValueError("Missing required parameter 'workspace_gid'")
        url = f"{self.base_url}/workspaces/{workspace_gid}/workspace_memberships"
        query_params = {k: v for k, v in [('opt_fields', opt_fields), ('user', user), ('opt_pretty', opt_pretty), ('limit', limit), ('offset', offset)] if v is not None}
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
