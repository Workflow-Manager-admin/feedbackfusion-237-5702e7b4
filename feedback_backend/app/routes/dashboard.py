from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields
from ..dashboard import list_jobs, add_job


blp = Blueprint(
    "Dashboard", "dashboard", url_prefix="/", description="Jobs Dashboard APIs"
)


class JobSchema(Schema):
    title = fields.String(required=True, description="Job title")
    company = fields.String(required=True, description="Company name")
    description = fields.String(required=True, description="Job description")
    location = fields.String(required=True, description="Job location (e.g., remote, on-site)")


class JobResultSchema(JobSchema):
    id = fields.Integer(description="Job ID")


class JobListSchema(Schema):
    jobs = fields.List(fields.Nested(JobResultSchema))


@blp.route("/jobs")
class JobsAPI(MethodView):
    """
    GET/POST /jobs endpoint (job dashboard, stub logic).
    """
    # PUBLIC_INTERFACE
    @blp.response(200, JobResultSchema(many=True))
    @blp.doc(
        summary="List All Jobs",
        description="Returns all jobs (dummy list, not persisted as DB)."
    )
    def get(self):
        all_jobs = list_jobs()
        return all_jobs, 200

    # PUBLIC_INTERFACE
    @blp.arguments(JobSchema, location="json")
    @blp.response(201, JobResultSchema)
    @blp.doc(
        summary="Add Job (Stub Only)",
        description="Adds a job to the in-memory list (non-persistent, for demo only)."
    )
    def post(self, payload):
        # For now, results are not persisted
        result = add_job(payload)
        return result["job"], 201
