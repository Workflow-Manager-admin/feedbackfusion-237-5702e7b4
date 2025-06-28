from flask_smorest import Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields
from ..feedback_analysis import analyze_feedback


blp = Blueprint(
    "FeedbackAnalysis", "feedback_analysis", url_prefix="/", description="Feedback Analyzer"
)


class FeedbackAnalysisSchema(Schema):
    feedback_text = fields.String(
        required=True,
        description="Feedback to analyze",
        allow_none=False
    )


class FeedbackAnalysisResultSchema(Schema):
    sentiment = fields.String(description="Detected sentiment")
    tags = fields.List(fields.String(), description="List of topic tags")
    message = fields.String(description="Stub message")


@blp.route("/analyze-feedback")
class FeedbackAnalyze(MethodView):
    """
    POST /analyze-feedback endpoint (feedback sentiment/tags stub).
    """
    # PUBLIC_INTERFACE
    @blp.arguments(FeedbackAnalysisSchema, location="json")
    @blp.response(200, FeedbackAnalysisResultSchema)
    @blp.doc(
        summary="Analyze Feedback (Stub AI)",
        description="Analyze feedback for sentiment and tags (stub/mocked AI)."
    )
    def post(self, payload):
        text = payload.get("feedback_text")
        if not text or not isinstance(text, str) or not text.strip():
            abort(400, message="feedback_text is required")
        result = analyze_feedback(text)
        return result, 200
