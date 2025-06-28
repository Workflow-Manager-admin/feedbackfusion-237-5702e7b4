from flask_smorest import Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields
from ..resume import match_resume


blp = Blueprint(
    "Resume", "resume", url_prefix="/", description="Resume Matcher"
)


class ResumeMatchSchema(Schema):
    resume_text = fields.String(required=True, description="Resume text or content")
    job_description = fields.String(required=True, description="Target job description")


class ResumeMatchResultSchema(Schema):
    matched = fields.Boolean(description="Whether resume matches")
    score = fields.Integer(description="Matching score (stub)")
    highlights = fields.List(fields.Dict(), description="List of highlights")
    message = fields.String(description="Stub message")


@blp.route("/match-resume")
class ResumeMatch(MethodView):
    """
    POST /match-resume endpoint (resume matcher stub).
    """
    # PUBLIC_INTERFACE
    @blp.arguments(ResumeMatchSchema, location="json")
    @blp.response(200, ResumeMatchResultSchema)
    @blp.doc(
        summary="Match Resume to Job",
        description="Matches resume vs job description (mock/stub AI implementation)"
    )
    def post(self, payload):
        resume_text = payload.get("resume_text")
        job_description = payload.get("job_description")
        if not resume_text or not job_description:
            abort(400, message="resume_text and job_description are required")
        result = match_resume(resume_text, job_description)
        return result, 200
