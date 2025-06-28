from flask_smorest import Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields, validate
from ..feedback_service import submit_feedback, list_feedback

# For OpenAPI grouping
blp = Blueprint(
    "Feedback", "feedback", url_prefix="/",
    description="Feedback submission and retrieval"
)


class FeedbackSubmitSchema(Schema):
    user = fields.String(
        description="User submitting the feedback",
        required=False, allow_none=True
    )
    message = fields.String(
        required=True, description="The feedback message",
        validate=validate.Length(min=1)
    )
    perform_ai = fields.Boolean(
        missing=True,
        description="Whether to perform AI sentiment/summarization (default True)"
    )


class FeedbackResultSchema(Schema):
    id = fields.Integer(description="Feedback ID")
    user = fields.String(allow_none=True, description="User submitting the feedback")
    message = fields.String(description="Feedback message")
    created_at = fields.DateTime(description="Feedback creation timestamp")
    sentiment = fields.String(allow_none=True, description="AI sentiment classification")
    summary = fields.String(allow_none=True, description="AI summary (if any)")


@blp.route("/submit")
class FeedbackSubmit(MethodView):
    """
    POST endpoint to submit new feedback.
    """

    # PUBLIC_INTERFACE
    @blp.arguments(FeedbackSubmitSchema, location="json")
    @blp.response(200, schema={"id": fields.Integer()})
    @blp.doc(
        summary="Submit Feedback",
        description="Submit feedback, optionally with AI sentiment/summarization."
    )
    def post(self, payload):
        """
        Accepts feedback from users; stores to DB and returns new record id.
        """
        user = payload.get("user")
        message = payload.get("message")
        perform_ai = payload.get("perform_ai", True)
        if not message or not isinstance(message, str) or not message.strip():
            abort(400, message="Message text is required.")
        feedback_id = submit_feedback(user, message, perform_ai=perform_ai)
        return {"id": feedback_id}, 200


@blp.route("/feedback")
class FeedbackList(MethodView):
    """
    GET endpoint to retrieve all feedback entries.
    """

    # PUBLIC_INTERFACE
    @blp.response(200, FeedbackResultSchema(many=True))
    @blp.doc(
        summary="List All Feedback",
        description=(
            "Returns all feedback entries, including any sentiment/summary info."
        )
    )
    def get(self):
        """
        Fetch all feedback records in the DB.
        """
        entries = list_feedback()
        return entries, 200
