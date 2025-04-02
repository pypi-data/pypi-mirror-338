import re
import json
import logging
from unittest.mock import AsyncMock, patch
from pytest import mark, fixture, raises
from aiohttp import WSMessage, WSMsgType

import proximl.projects as specimen
from proximl.exceptions import (
    ApiError,
    SpecificationError,
    ProxiMLException,
)

pytestmark = [mark.sdk, mark.unit, mark.projects]


@fixture
def projects(mock_proximl):
    yield specimen.Projects(mock_proximl)


@fixture
def project(mock_proximl):
    yield specimen.Project(
        mock_proximl,
        id="1",
        name="My Mock Project",
        owner=True,
        owner_name="Me",
        created_name="Me",
        job_all=True,
        dataset_all=True,
        model_all=True,
        createdAt="2020-12-31T23:59:59.000Z",
    )


class ProjectsTests:
    @mark.asyncio
    async def test_get_project(
        self,
        projects,
        mock_proximl,
    ):
        api_response = dict()
        mock_proximl._query = AsyncMock(return_value=api_response)
        await projects.get("1234")
        mock_proximl._query.assert_called_once_with("/project/1234", "GET", dict())

    @mark.asyncio
    async def test_list_projects(
        self,
        projects,
        mock_proximl,
    ):
        api_response = dict()
        mock_proximl._query = AsyncMock(return_value=api_response)
        await projects.list()
        mock_proximl._query.assert_called_once_with("/project", "GET", dict())

    @mark.asyncio
    async def test_remove_project(
        self,
        projects,
        mock_proximl,
    ):
        api_response = dict()
        mock_proximl._query = AsyncMock(return_value=api_response)
        await projects.remove("4567")
        mock_proximl._query.assert_called_once_with("/project/4567", "DELETE", dict())

    @mark.asyncio
    async def test_create_project_simple(self, projects, mock_proximl):
        requested_config = dict(
            name="new project",
        )
        expected_payload = dict(name="new project")
        api_response = {
            "id": "project-id-1",
            "name": "new project",
            "owner": True,
            "owner_name": "Me",
            "created_name": "Me",
            "job_all": True,
            "dataset_all": True,
            "model_all": True,
            "createdAt": "2020-12-31T23:59:59.000Z",
        }

        mock_proximl._query = AsyncMock(return_value=api_response)
        response = await projects.create(**requested_config)
        mock_proximl._query.assert_called_once_with(
            "/project", "POST", None, expected_payload
        )
        assert response.id == "project-id-1"


class ProjectTests:
    def test_project_properties(self, project):
        assert isinstance(project.id, str)
        assert isinstance(project.name, str)
        assert isinstance(project.owner_name, str)
        assert isinstance(project.is_owner, bool)

    def test_project_str(self, project):
        string = str(project)
        regex = r"^{.*\"id\": \"" + project.id + r"\".*}$"
        assert isinstance(string, str)
        assert re.match(regex, string)

    def test_project_repr(self, project):
        string = repr(project)
        regex = r"^Project\( proximl , \*\*{.*'id': '" + project.id + r"'.*}\)$"
        assert isinstance(string, str)
        assert re.match(regex, string)

    def test_project_bool(self, project, mock_proximl):
        empty_project = specimen.Project(mock_proximl)
        assert bool(project)
        assert not bool(empty_project)

    @mark.asyncio
    async def test_project_remove(self, project, mock_proximl):
        api_response = dict()
        mock_proximl._query = AsyncMock(return_value=api_response)
        await project.remove()
        mock_proximl._query.assert_called_once_with("/project/1", "DELETE")
