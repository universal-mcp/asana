# Asana MCP Server

An MCP Server for the Asana API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Asana API.


| Tool | Description |
|------|-------------|
| `get_an_allocation` | Retrieves a complete allocation record for a single allocation. |
| `update_an_allocation` | Updates an existing allocation by making a PUT request. Only specified fields are updated, and the complete updated allocation record is returned. |
| `delete_an_allocation` | Deletes a specific allocation by making a DELETE request to its URL and returns an empty data record upon success. |
| `get_multiple_allocations` | Fetches a list of allocations filtered by specific parameters like project, user, and pagination details. |
| `create_an_allocation` | Creates a new allocation and returns its full record. |
| `get_an_attachment` | Get the full record for a single attachment, optionally including additional fields and pretty-printed output. |
| `delete_an_attachment` | Deletes a specific, existing attachment and returns an empty data record. |
| `get_attachments_from_an_object` | Retrieves a list of attachments from a specified object, which can be a project, project brief, or task. |
| `get_audit_log_events` | Retrieve audit log events from your domain, with options to filter by various criteria such as actor ID, event type, and time range. |
| `submit_parallel_requests` | Submits multiple API requests in parallel to Asana's batch endpoints, enabling efficient batch processing of operations. |
| `create_acustom_field` | Creates a new custom field in a workspace with a unique name and valid type. |
| `get_acustom_field` | Retrieve complete metadata definition of a custom field, including type-specific properties and behaviors. |
| `update_acustom_field` | Updates an existing custom field with provided data, returning the complete updated record. Only specified fields are modified, preserving existing values. |
| `delete_acustom_field` | Deletes a specific existing custom field using a DELETE request to its URL. Locked fields can only be deleted by the locking user. |
| `get_aworkspace_scustom_fields` | Retrieves a list of compact representations of custom fields within a workspace. |
| `create_an_enum_option` | Creates an enum option for a custom field, adds it to the field's enum list, and returns the full record of the new option. |
| `reorder_acustom_field_senum` | Reorders a custom field's enum. Moves an enum option to be either before or after another specified enum option. |
| `update_an_enum_option` | Updates an existing enum option for custom fields and returns the full record. Locked fields can only be updated by the locking user. |
| `get_aproject_scustom_fields` | Fetches and returns a project's custom fields settings, allowing pagination and optional inclusion of additional fields. |
| `get_aportfolio_scustom_fields` | Fetches a portfolio's custom fields from the API, returning them in a compact form. |
| `get_events_on_aresource` | Retrieves a list of events that have occurred on a specified resource since the sync token was generated. |
| `get_agoal` | Retrieves a complete goal record for a single goal, allowing optional fields and pretty output. |
| `update_agoal` | Update an existing goal by sending a PUT request to the specified URL. Only provided fields are updated, leaving unspecified fields unchanged. |
| `delete_agoal` | Deletes a specific existing goal by sending a DELETE request to the goal's URL. |
| `get_goals` | Fetches compact goal records based on specified parameters. |
| `create_agoal` | Creates a new goal in a workspace or team and returns the full record of the newly created goal. |
| `create_agoal_metric` | Creates and adds a goal metric to a specified goal, replacing any existing metric. |
| `update_agoal_metric` | Update a goal's existing metric's current value and return the updated metric record. |
| `add_acollaborator_to_agoal` | Adds collaborators as followers to a goal and returns the updated goal data. |
| `remove_acollaborator_from_agoal` | Removes a collaborator from a goal and returns the updated goal record. |
| `get_parent_goals_from_agoal` | Retrieves parent goals from a specific goal, returning them in a compact format. |
| `get_agoal_relationship` | Retrieve a complete goal relationship record by making a GET request to the specified endpoint. |
| `update_agoal_relationship` | Updates an existing goal relationship by making a PUT request with specified data and returns the complete updated record. |
| `get_goal_relationships` | Retrieve goal relationships from the API, returning compact goal relationship records with optional pagination and filtering. |
| `add_asupporting_goal_relationship` | Creates a supporting goal relationship by adding a supporting resource to a specific goal and returns the new relationship record. |
| `removes_asupporting_goal_relationship` | Removes a supporting goal relationship between a parent goal and its dependent goal based on provided data. |
| `get_ajob_by_id` | Retrieve a job's full record by its ID. |
| `get_multiple_memberships` | Retrieve multiple membership records for goals, projects, or portfolios, with pagination and filtering options. |
| `create_amembership` | Creates a new membership in a goal or project for users or teams, returning the full membership record. |
| `get_amembership` | Fetches a compact project membership record. |
| `update_amembership` | Updates an existing membership by making a PUT request, modifying only the specified fields in the provided data. |
| `delete_amembership` | Deletes a specific membership for a goal or project by sending a DELETE request to the appropriate endpoint. |
| `create_an_organization_export_request` | Initiates an asynchronous export request for an Organization in Asana. |
| `get_details_on_an_org_export_request` | Retrieve details of a previously-requested Organization export, including optional fields and formatted output. |
| `get_multiple_portfolios` | Retrieve multiple portfolios, returning them in a compact representation. The portfolios are filtered by the specified workspace and can be further limited by owner, pagination parameters, and additional fields. |
| `create_aportfolio` | Creates a portfolio in the specified workspace, allowing custom initialization without automatic UI state like Priority fields. |
| `get_aportfolio` | Retrieves a portfolio record from the API, returning all fields unless filtered by optional parameters. |
| `update_aportfolio` | Updates an existing portfolio by modifying specified fields while preserving unspecified ones, returning the complete updated portfolio record. |
| `delete_aportfolio` | Deletes a portfolio by making a DELETE request. |
| `get_portfolio_items` | Fetches a list of portfolio items in compact form, retrieving them based on pagination parameters. |
| `add_aportfolio_item` | Adds an item to a portfolio and returns an empty data block. |
| `remove_aportfolio_item` | Remove an item from a portfolio via API request and return the response data. |
| `add_acustom_field_to_aportfolio` | Adds a custom field to a portfolio by creating a custom field setting. |
| `remove_acustom_field_from_aportfolio` | Remove a custom field setting from a portfolio. |
| `add_users_to_aportfolio` | Add users to a portfolio and return the updated portfolio record. |
| `remove_users_from_aportfolio` | Remove users from a portfolio and return the updated portfolio record. |
| `get_multiple_portfolio_memberships` | Retrieves multiple portfolio memberships, returning them in a compact representation. Requires specifying either `portfolio` and `user`, or `workspace` and `user`. Supports pagination and optional fields. |
| `get_aportfolio_membership` | Retrieves a portfolio membership, returning the complete portfolio record. |
| `get_memberships_from_aportfolio` | Get memberships from a portfolio, returning compact portfolio membership records. |
| `get_multiple_projects` | Retrieve multiple projects based on filtering criteria, returning compact project records. Handles pagination and allows specifying optional fields to include. |
| `create_aproject` | Create a new project in a workspace or team, returning its full record. |
| `get_aproject` | Fetches a project's complete record, optionally including additional fields and formatting the output for readability. |
| `update_aproject` | Updates a specific project by modifying provided fields, returning the complete updated project record while preserving unspecified fields. |
| `delete_aproject` | Deletes an existing project by making a DELETE request to the project's URL. |
| `duplicate_aproject` | Duplicates a project by creating and returning a job for asynchronous handling. |
| `get_projects_atask_is_in` | Retrieve a compact list of all projects that contain the specified task, formatted as paginated results. |
| `get_ateam_sprojects` | Fetches a team’s projects, returning compact project records with optional pagination, archival status filtering, and field inclusion control. |
| `create_aproject_in_ateam` | Creates a project shared with the specified team and returns the full record of the newly created project. |
| `get_all_projects_in_aworkspace` | Fetches all project records in a workspace, returning them as a dictionary. |
| `create_aproject_in_aworkspace` | Create a project in a workspace, returning the full record of the newly created project. |
| `add_acustom_field_to_aproject` | Add a custom field to a project, creating a custom field setting for the project. |
| `remove_acustom_field_from_aproject` | Remove a custom field setting from a specified project by sending a POST request with the required data. |
| `get_task_count_of_aproject` | Retrieves the task count of a project, returning an object with task count fields. All fields are excluded by default, requiring opt-in via the `opt_fields` parameter. |
| `add_users_to_aproject` | Adds users to a project as members, potentially setting them as followers based on notification settings, and returns the updated project record. |
| `remove_users_from_aproject` | Removes specified users from a project and returns the updated project record. |
| `add_followers_to_aproject` | Adds followers to a project, promoting specified users to members if not already part of the project. Returns the updated project record. |
| `remove_followers_from_aproject` | Remove followers from a project without affecting membership status. |
| `create_aproject_template_from_aproject` | Creates a project template from a project by sending a POST request and returns the response in JSON format, asynchronously handling the template creation. |
| `get_aproject_brief` | Retrieves a project brief by optionally including specified fields and formatting the response. |
| `update_aproject_brief` | Updates an existing project brief by making a PUT request and returns the complete updated record. |
| `delete_aproject_brief` | Failed to extract docstring information |
| `create_aproject_brief` | Creates a new project brief and returns the full record of the newly created brief. |
| `get_aproject_membership` | Retrieve a project membership and its associated project record. |
| `get_memberships_from_aproject` | Retrieves paginated project membership records for a specific project, returning compact data with optional fields. |
| `get_aproject_status` | Get the complete record for a single project status update. *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.* |
| `delete_aproject_status` | Deletes a specific existing project status update (deprecated: new integrations should use '/status_updates/{status_gid}'). |
| `get_statuses_from_aproject` | Retrieve compact project status update records from a project, providing pagination and query parameters. |
| `create_aproject_status` | Creates a new project status update (deprecated). |
| `get_aproject_template` | Retrieves the complete record for a single project template including optionally specified fields. |
| `delete_aproject_template` | Delete a project template from the system and return an empty data record. |
| `get_multiple_project_templates` | Retrieves multiple project templates based on specified filters like team and workspace. |
| `get_ateam_sproject_templates` | Retrieve paginated list of compact project template records for a team. |
| `instantiate_aproject_from_aproject_template` | Instantiates a project from a project template and returns an asynchronous job handle for the operation. |
| `trigger_arule` | Triggers a rule configured with an incoming web request trigger, sending provided data to the rule's endpoint. |
| `get_asection` | Retrieves a complete record for a single section, potentially including additional fields and optional formatting. |
| `update_asection` | Updates an existing section by making a PUT request to the specific section URL, updating only the provided fields. |
| `delete_asection` | Deletes a specific empty section by sending a DELETE request to its URL. The last remaining section cannot be deleted. |
| `get_sections_in_aproject` | Retrieve sections in a project, returning compact records. |
| `create_asection_in_aproject` | Creates a new section in a project and returns the full record of the newly created section. |
| `add_task_to_section` | Adds a task to a specific section in a project, removing it from other sections. Inserts the task at the top of the section unless position parameters are provided (insert_before/insert_after). Does not work for separator tasks (resource_subtype 'section'). |
| `move_or_insert_sections` | Move or insert sections by sending a POST request with provided data and optional 'pretty' formatting. |
| `get_astatus_update` | Get a status update by requesting a complete record from an endpoint. The response may include optional fields based on query parameters. |
| `delete_astatus_update` | Deletes a specific existing status update and returns an empty data record upon success. |
| `get_status_updates_from_an_object` | Fetches status updates from a specified object, returning compact status records. |
| `create_astatus_update` | Create a status update on an object and return the full record of the newly created status update. |
| `get_astory` | Retrieves a story's full record, returning all data fields except those excluded by default. Optional parameters allow expanding specific fields and formatting the response. |
| `update_astory` | Updates a story and returns the full record of the updated story. Only comment stories can have their text updated, and only comment/attachment stories can be pinned. Exactly one of `text` or `html_text` must be specified when updating a comment story. |
| `delete_astory` | Deletes a story created by the user. |
| `get_stories_from_atask` | Retrieve paginated stories associated with a task, returning compact records in a dictionary format. |
| `create_astory_on_atask` | Creates a comment story on a task as the authenticated user, returning the new story's full record. |
| `get_multiple_tags` | Retrieve multiple tags with optional pagination and filtering. Returns compact tag records based on provided query parameters. |
| `create_atag` | Create a new tag in a specific workspace or organization. |
| `get_atag` | Retrieve a single tag with optional properties and formatted output. |
| `update_atag` | Updates a tag's properties by sending a PUT request with specified optional fields. Only provided fields are modified; unspecified fields remain unchanged. |
| `delete_atag` | Deletes a specific, existing tag by making a DELETE request to the tag's URL. |
| `get_atask_stags` | Fetches a task's tags, returning a compact representation of all associated tags. |
| `get_tags_in_aworkspace` | Retrieve paginated tags from a workspace with optional filters and response formatting. |
| `create_atag_in_aworkspace` | Creates a new tag in a workspace or organization and returns its full record. |
| `get_multiple_tasks` | Retrieve multiple task records filtered by parameters such as assignee, project, or workspace. |
| `create_atask` | Creates a new task in a workspace, either explicitly specified or inferred from projects/parent task associations. |
| `get_atask` | Retrieve complete task record for a single task, including optional fields and formatted output. |
| `update_atask` | Updates a specific, existing task by making a PUT request. Only the fields provided in the `data` block are updated. |
| `delete_atask` | Deletes a specific task permanently after moving it to the user's trash (recoverable for 30 days). Returns an empty data record upon success. |
| `duplicate_atask` | Duplicates a task by creating and returning a job that asynchronously handles the duplication. |
| `get_tasks_from_aproject` | Get tasks from a project, returning compact task records ordered by their priority within the project. |
| `get_tasks_from_asection` | Retrieves tasks from a specified section, primarily designed for board views. Filters can include completion status, pagination limits, and optional field requests. |
| `get_tasks_from_atag` | Retrieve paginated tasks associated with a specific tag. Returns compact task records with optional field inclusion and formatted output. |
| `get_tasks_from_auser_task_list` | Retrieves tasks from a user's My Tasks list, returning a compact list of tasks with optional filtering and pagination. |
| `get_subtasks_from_atask` | Retrieve subtasks from a task, returning a compact representation of all task subtasks. |
| `create_asubtask` | Creates a new subtask and adds it to the parent task, returning the full record for the newly created subtask. |
| `set_the_parent_of_atask` | Sets the parent of a task, providing optional parameters for specifying additional fields and formatting the response. |
| `get_dependencies_from_atask` | Retrieve paginated dependencies of a task with optional filtering and formatting. |
| `set_dependencies_for_atask` | Set dependencies for a task by marking other tasks as its dependencies, up to a combined limit of 30 dependents and dependencies. |
| `unlink_dependencies_from_atask` | Unlink dependencies from a task by sending a request to the specified API endpoint. |
| `get_dependents_from_atask` | Retrieve the compact representations of all dependents of a task, optionally specifying pagination and optional fields. |
| `set_dependents_for_atask` | Sets dependents for a task by marking a set of tasks as dependents if they are not already. |
| `unlink_dependents_from_atask` | Unlinks dependent tasks from the current task via an API request. |
| `add_aproject_to_atask` | Associates a task with a project, optionally positioning it relative to other tasks or within a specific section. Returns the API response data. |
| `remove_aproject_from_atask` | Remove a project from a task, ensuring the task remains in the system but is no longer associated with the specified project. |
| `add_atag_to_atask` | Adds a tag to a task and returns the result in JSON format. |
| `remove_atag_from_atask` | Remove a tag from a task by sending a POST request with the task data. |
| `add_followers_to_atask` | Adds followers to a task, returning the updated task record. |
| `remove_followers_from_atask` | Remove specified followers from a task and return the updated task record. |
| `get_atask_for_agiven_custom_id` | Fetches a task associated with a given custom ID. |
| `search_tasks_in_aworkspace` | Searches for tasks in a workspace with extensive filtering capabilities based on task attributes, user interactions, dates, and custom parameters. |
| `get_multiple_task_templates` | Retrieve multiple task templates with pagination and filtering options. Returns compact records of task templates filtered by specified criteria, requiring a project parameter for filtering. |
| `get_atask_template` | Retrieves a complete task template record. |
| `delete_atask_template` | Deletes a specific task template by making a DELETE request and returns an empty data record. |
| `instantiate_atask_from_atask_template` | Instantiate a task from a task template, creating and returning a job to handle the task asynchronously. |
| `create_ateam` | Creates a team within the current workspace. |
| `get_ateam` | Retrieve detailed information about a team, including optional fields and formatted output as specified. |
| `update_ateam` | Update a team within the current workspace, including modifying team data and requesting optional fields in the response. |
| `get_teams_in_aworkspace` | Retrieve paginated records of teams in a workspace visible to the authorized user. |
| `get_teams_for_auser` | Retrieve paginated list of compact team records for a user based on workspace/organization filter. |
| `add_auser_to_ateam` | Adds a user to a team and returns the complete team membership record. Requires the calling user to be a team member and the added user to exist in the same organization. |
| `remove_auser_from_ateam` | Remove a user from a team, requiring team membership in the calling user. |
| `get_ateam_membership` | Get a team membership record. Returns the complete membership details for a single team. |
| `get_team_memberships` | Retrieve team membership records with pagination and optional field filtering. |
| `get_memberships_from_ateam` | Retrieve paginated team memberships with optional field inclusion and response formatting. |
| `get_memberships_from_auser` | Retrieves memberships for a user, returning compact team membership records. |
| `get_atime_period` | Retrieves a specific time period record with optional field inclusions and formatted output. |
| `get_time_periods` | Retrieve compact time period records based on specified date range and pagination parameters. |
| `get_time_tracking_entries_for_atask` | Retrieve paginated time tracking entries for a specific task. |
| `create_atime_tracking_entry` | Create a new time tracking entry for a given task. |
| `get_atime_tracking_entry` | Retrieves a complete time tracking entry record from the API, returning all available data in dictionary format. |
| `update_atime_tracking_entry` | Updates an existing time tracking entry by sending a PUT request with the specified fields. |
| `delete_atime_tracking_entry` | Delete a specific time tracking entry via DELETE request to its URL. |
| `get_objects_via_typeahead` | Retrieves objects from a workspace using a typeahead search algorithm, providing a limited set of results quickly for auto-completion features. |
| `get_multiple_users` | Retrieves multiple user records from accessible workspaces and organizations with pagination options. |
| `get_auser` | Get a user record by ID, returning the full user details. Supports optional field inclusion and formatted output. |
| `get_auser_sfavorites` | Get a user's favorites in the specified workspace and resource type, returning paginated results in the same order as Asana's sidebar. |
| `get_users_in_ateam` | Retrieve paginated list of team members, returning compact user records sorted alphabetically with a limit of 2000 results. For larger datasets, use the `/users` endpoint. |
| `get_users_in_aworkspace_or_organization` | Retrieve paginated list of users in a workspace or organization, sorted alphabetically and limited to 2000 records. For larger datasets, use the `/users` endpoint. |
| `get_auser_task_list` | Retrieves the full record for a user task list. Optionally includes additional fields and formats the response for readability. |
| `get_auser_stask_list` | Fetches a user's task list from a specified workspace. |
| `get_multiple_webhooks` | Get compact representations of all webhooks registered by the app for the authenticated user in a specific workspace. |
| `establish_awebhook` | Initiates a webhook creation process with a confirmation handshake, requiring asynchronous server handling to validate the webhook subscription. |
| `get_awebhook` | Retrieve the full record of a webhook including optional fields if specified. |
| `update_awebhook` | Update an existing webhook by making a PUT request and overwriting its filters with new data. |
| `delete_awebhook` | Permanently deletes a webhook. Once deleted, no further requests will be issued, though in-flight requests might still be received. |
| `get_multiple_workspaces` | Fetches multiple workspaces visible to the authorized user. Returns compact records with pagination support. |
| `get_aworkspace` | Get the full workspace record for a single workspace. |
| `update_aworkspace` | Updates an existing workspace by modifying specified fields and returns the updated workspace record. |
| `add_auser_to_aworkspace_or_organization` | Add a user to a workspace or organization by user ID or email and return the full user record. |
| `remove_auser_from_aworkspace_or_organization` | Remove a user from a workspace or organization. Requires admin privileges in the target workspace. Supports user identification by globally unique ID or email address. |
| `get_aworkspace_membership` | Retrieve a workspace membership and return its complete workspace record. |
| `get_workspace_memberships_for_auser` | Fetches the compact workspace membership records for a user, allowing pagination via limit and offset parameters. |
| `get_the_workspace_memberships_for_aworkspace` | Retrieve paginated workspace membership records for a specified workspace, including optional field selection and user filtering. |
