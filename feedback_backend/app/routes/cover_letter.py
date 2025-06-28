from flask_smorest import Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields
from ..cover_letter import generate_cover_letter


blp = Blueprint(
    "CoverLetter", "cover_letter", url_prefix="/", description="Cover Letter Generator"
)


class CoverLetterRequestSchema(Schema):
    resume_text = fields.String(required=True, description="Resume text or content")
    job_description = fields.String(required=True, description="Target job description")


class CoverLetterResultSchema(Schema):
    cover_letter = fields.String(description="Generated cover letter")
    message = fields.String(description="Stub message")


@blp.route("/cover-letter")
class CoverLetter(MethodView):
    """
    POST /cover-letter endpoint (cover letter generator stub).
    """
    # PUBLIC_INTERFACE
    @blp.arguments(CoverLetterRequestSchema, location="json")
    @blp.response(200, CoverLetterResultSchema)
    @blp.doc(
        summary="Generate Cover Letter",
        description="Generate a cover letter for the job using the resume (mock/stub AI)."
    )
    def post(self, payload):
        resume_text = payload.get("resume_text")
        job_description = payload.get("job_description")
        if not resume_text or not job_description:
            abort(400, message="resume_text and job_description are required")
        result = generate_cover_letter(resume_text, job_description)
        return result, 200
