import csv
import json
from http import HTTPStatus
from xmlrpc.client import boolean

import click

from .cli import cli
from ..api import _create, _delete, _get, _list, _update, _poll_response
from ..options import (
    query_opt,
    limit_opt,
    offset_opt,
    export_opt
)
from ..output import output_result, output_message
from ..types import JSON
from ..utils import create_parameters


@cli.group(help='Organization management.')
@click.pass_context
def organization(ctx):
    pass

@organization.command(name='create', help='Create an Organization.')
@click.option('--display-name', 'display_name', type=str, required=True, help='Friendly name of the organization.')
@click.option('--name', 'name', type=str, required=True, help='The name of this organization.')
@click.option('--metadata', 'org_metadata', type=str, required=False, help='Metadata associated with the organization, in the form of an object with string values (max 255 chars).')
@click.pass_context
def create_organization(ctx, display_name, name, org_metadata):
    data = {'display_name': display_name, 'name': name}
    if org_metadata:
        data['org_metadata'] = org_metadata
    _, result = _create(ctx.obj['access_token'], 'organization', data=data)
    output_result(ctx, result)


@organization.command(name='update', help='Update an Organization.')
@click.option('--display-name', 'display_name', type=str, required=False, help='Friendly name of the organization.')
@click.option('--name', 'name', type=str, required=False, help='The name of this organization.')
@click.option('--metadata', 'org_metadata', type=str, required=False, help='Metadata associated with the organization, in the form of an object with string values (max 255 chars).')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to fetch. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.pass_context
def update_organization(ctx, display_name, name, org_metadata, org_id):
    params = {'org_id': org_id}
    data = {}
    if display_name:
        data['display_name'] = display_name
    if name:
        data['name'] = name
    if org_metadata:
        data['org_metadata'] = org_metadata
    result = _update(ctx.obj['access_token'], 'organization', data=data, params=params)
    output_result(ctx, result)


@organization.command(name='list', help='List Organizations.')
@click.option('--name', 'name', type=str, required=False, help='Filter organizations by name')
@click.option('--metadata', 'metadata', type=JSON, required=False, help='Filter organizations by field in metadata')
@query_opt
@offset_opt
@limit_opt
@export_opt
@click.pass_context
def list_organizations(ctx, query, limit, offset, name, metadata, output_file):
    param_mapping = [
        (name, 'name'),
        (metadata, 'org_metadata'),
        (limit, 'limit'),
        (offset, 'offset'),
        (query, 'search')
    ]
    params = create_parameters(param_mapping)
    _, result = _list(
        ctx.obj['access_token'], 'organizations', params=params
    )
    output_result(ctx, result, output_file=output_file)


@organization.command(name='get', help='Get Organization.')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to fetch. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@export_opt
@click.pass_context
def get_organization(ctx, org_id, output_file):
    params = {'org_id': org_id}
    _, result = _get(
        ctx.obj['access_token'], 'organization', params=params
    )
    output_result(ctx, result, output_file=output_file)

@organization.group(help='User bulk operations.')
@click.pass_context
def users(ctx):
    pass


@users.command(name='list', help='Retrieve users from an organization.')
@click.option('--user-id', 'user_id', type=str, required=False, help='Filter users by user id')
@click.option('--email', 'email', type=str, required=False, help='Filter users by email')
@click.option('--user-metadata', 'user_metadata', type=JSON, required=False, help='Filter users by field in user metadata')
@click.option('--app-metadata', 'app_metadata', type=JSON, required=False, help='Filter users by field in app metadata')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@query_opt
@offset_opt
@limit_opt
@export_opt
@click.pass_context
def list_users(ctx, org_id, limit, offset, query, user_metadata, app_metadata, user_id, email, output_file):
    param_mapping = [
        (user_id, 'user_id'),
        (email, 'email'),
        (user_metadata, 'user_metadata'),
        (app_metadata, 'app_metadata'),
        (limit, 'limit'),
        (offset, 'offset'),
        (query, 'search'),
        (org_id, 'org_id')
    ]
    params = create_parameters(param_mapping)

    _, result = _list(
        ctx.obj['access_token'], 'organization/users', params=params
    )
    output_result(ctx, result, output_file=output_file)


@users.command(name='add', help='Add users to an organization.')
@click.option(
    '--file', '_file', type=click.Path(
        exists=True,
        file_okay=True,
        resolve_path=True,
        readable=True,
        writable=True,
    ),
    required=True, help='Csv file containing list of users to create. First row must be the header')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.pass_context
def add_users(ctx, _file, org_id):
    params = {'org_id': org_id}
    data = {'users': []}
    with open(_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            _record = {}
            for k, v in row.items():
                if k in ['app_metadata', 'user_metadata']:
                    _record[k] = json.loads(v)
                else:
                    _record[k] = v
            data['users'].append(_record)
    status_code, data = _create(ctx.obj['access_token'], 'organization/users', data=data, params=params)
    if status_code == HTTPStatus.ACCEPTED:
        data = _poll_response(ctx.obj['access_token'], job_id=data)
    if data.get('status') == 'Finished':
        output_message('Users created successfully!')
    else:
        output_message('Users failed to create!')


@users.command(name='remove', help='Remove users from an organization.')
@click.option('--user', 'user_ids', multiple=True, type=str, required=True, help='Users to add. Pass this parameter multiple times for more than one user. ')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.pass_context
def remove_users(ctx, user_ids, org_id):
    params = {'org_id': org_id}

    data = {'users': [u for u in user_ids]}
    status_code, data = _delete(ctx.obj['access_token'], 'organization/users', data=data, params=params)
    if status_code == HTTPStatus.ACCEPTED:
        data = _poll_response(ctx.obj['access_token'], job_id=data)
    if data.get('status') == 'Finished':
        output_message('Users deleted successfully!')
    else:
        output_message('Users failed to delete!')


@users.command(name='update', help='Update users in an organization.')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.option('--user-metadata', 'user_metadata', type=JSON, required=False, help='User metadata json.')
@click.option('--app-metadata', 'app_metadata', type=JSON, required=False, help='App metadata json.')
@click.option('--blocked', 'blocked', type=boolean, required=False, help='Block status.')
@click.pass_context
def update_users(ctx, app_metadata, user_metadata, blocked, org_id):
    data = {'action': 'organization_update_users', 'data': {}}
    params = {'org_id': org_id}

    data['data'].update(
        {k: v for k, v in [('app_metadata', app_metadata), ('user_metadata', user_metadata), ('blocked', blocked)] if v})
    status_code, data = _update(ctx.obj['access_token'], 'organization/users', data=data, params=params)
    if status_code == HTTPStatus.ACCEPTED:
        data = _poll_response(ctx.obj['access_token'], job_id=data)
    if data.get('status') == 'Finished':
        output_message('Users updated successfully!')
    else:
        output_message('Users failed to update!')


@users.command(name='add-roles', help='Add roles to all users of an organization.')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.option('--role', 'roles', multiple=True, type=str, required=True, help='Role ids. Add this parameter multiple times for multiple roles.')
@click.pass_context
def add_roles(ctx, roles, org_id):
    data = {'action': 'organization_add_roles', 'roles': roles}
    params = {'org_id': org_id}

    status_code, data = _update(ctx.obj['access_token'], 'organization/users', data=data, params=params)
    if status_code == HTTPStatus.ACCEPTED:
        data = _poll_response(ctx.obj['access_token'], job_id=data)
    if data.get('status') == 'Finished':
        output_message('Roles added successfully!')
    else:
        output_message('Failed to add roles!')


@users.command(name='remove-roles', help='Add roles to all users of an organization.')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.option('--role', 'roles', multiple=True, type=str, required=True, help='Role ids. Add this parameter multiple times for multiple roles.')
@click.pass_context
def remove_roles(ctx, roles, org_id):
    data = {'action': 'organization_remove_roles', 'roles': roles}
    params = {'org_id': org_id}

    status_code, data = _update(ctx.obj['access_token'], 'organization/users', data=data, params=params)
    if status_code == HTTPStatus.ACCEPTED:
        data = _poll_response(ctx.obj['access_token'], job_id=data)
    if data.get('status') == 'Finished':
        output_message('Roles removed successfully!')
    else:
        output_message('Failed to remove roles!')


@users.command(name='reset-password', help='Reset password to all users of an organization.')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.pass_context
def reset_password(ctx, org_id):
    data = {'action': 'organization_reset_password'}
    params = {'org_id': org_id}

    status_code, data = _update(ctx.obj['access_token'], 'organization/users', data=data, params=params)
    if status_code == HTTPStatus.ACCEPTED:
        data = _poll_response(ctx.obj['access_token'], job_id=data)
    if data.get('status') == 'Finished':
        output_message('Passwords reset successfully!')
    else:
        output_message('Failed to reset passwords!')


@organization.group(help='Role CRUD inside an organization.')
@click.pass_context
def roles(ctx):
    pass

@roles.command(name='list', help='List Roles.')
@click.option('--name', 'name', type=str, required=False, help='Filter by name')
@click.option('--description', 'description', type=str, required=False, help='Filter by description')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@query_opt
@offset_opt
@limit_opt
@export_opt
@click.pass_context
def list_roles(ctx, query, limit, offset, org_id, name, description, output_file):
    param_mapping = [
        (name, 'name'),
        (description, 'description'),
        (limit, 'limit'),
        (offset, 'offset'),
        (query, 'search'),
        (org_id, 'org_id')
    ]

    params = create_parameters(param_mapping)
    _, result = _list(
        ctx.obj['access_token'], 'organization/roles', params=params
    )
    output_result(ctx, result, output_file=output_file)


@roles.command(name='create', help='Create a Role in the context of an Organization.')
@click.option('--description', 'description', type=str, required=True, help='Description of the role.')
@click.option('--name', 'name', type=str, required=True, help='The name of this role.')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.pass_context
def create_role(ctx, description, name, org_id):
    data = {'description': description, 'name': name}
    params = {'org_id': org_id}
    _, result = _create(ctx.obj['access_token'], 'organization/roles', data=data, params=params)
    output_result(ctx, result)


@roles.command(name='update', help='Update a Role in the context of an Organization.')
@click.option('--description', 'description', type=str, required=False, help='Description of the role.')
@click.option('--name', 'name', type=str, required=False, help='The name of this role.')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.option('--role-id', 'role_id', type=str, required=True, help='Role id to update. This field is the role_id field from get/list')
@click.pass_context
def update_role(ctx, description, name, org_id, role_id):
    data = {'description': description, 'name': name}
    params = {'org_id': org_id}
    _, result = _update(ctx.obj['access_token'], f'organization/role/{role_id}', data=data, params=params)
    output_result(ctx, result)


@roles.command(name='get', help='Get a Role in the context of an Organization.')
@click.option('--role-id', 'role_id', type=str, required=True, help='The id of the role. This field is the role_id field from get/list')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.pass_context
def get_role(ctx, org_id, role_id):
    params = {'org_id': org_id}
    _, result = _get(ctx.obj['access_token'], f'organization/role/{role_id}', params=params)
    output_result(ctx, result)

@roles.command(name='delete', help='Delete a Role in the context of an Organization.')
@click.option('--role-id', 'role_id', type=str, required=True, help='The id of the role. This field is the role_id field from get/list')
@click.option('--org-id', 'org_id', type=str, required=False, help='Organization id to use. If not specified, it will return your own organization. This is the field org_id returned in the list method.')
@click.pass_context
def delete_role(ctx, org_id, role_id):
    params = {'org_id': org_id}
    _delete(ctx.obj['access_token'], f'organization/role/{role_id}', params=params)
    output_message('Role deleted successfully!')
