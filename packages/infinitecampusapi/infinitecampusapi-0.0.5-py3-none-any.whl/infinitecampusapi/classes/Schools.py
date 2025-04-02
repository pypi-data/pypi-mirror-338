from pydantic import UUID4, BaseModel
from datetime import datetime
from .Student import StudentModel


class SchoolModel(BaseModel):
    sourcedId: UUID4
    status: str
    dateLastMofified: datetime | None = None
    metadata: dict = {}
    name: str
    identifier: str
    children: list = []
    parent: dict
    type: str


class Schools:
    def __init__(self, api_call):
        self.api_call = api_call

    def get_schools(self) -> list[SchoolModel]:
        """Returns a list of all schools"""
        r = self.api_call("schools")
        schools = []
        for school in r["orgs"]:
            schools.append(SchoolModel(**school))
        return schools

    def get_school(self, pid: UUID4) -> SchoolModel:
        """Returns information about a school using it's SourcedID"""
        r = self.api_call(f"schools/{pid}")
        return SchoolModel(**r["org"])

    def get_school_students(self, pid: UUID4) -> list[StudentModel]:
        """Returns a list of Students by School"""
        r = self.api_call(f"schools/{pid}/students")
        students = []
        for student in r["users"]:
            students.append(StudentModel(**student))
        return students
