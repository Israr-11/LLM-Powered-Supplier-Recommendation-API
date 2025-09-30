from flask import Blueprint
from controllers.query_controller import QueryController

query_bp = Blueprint('query', __name__, url_prefix='/api')
controller = QueryController()

@query_bp.route('/query', methods=['POST'])
def process_query():
    """Endpoint to process a query."""
    return controller.process_query()

@query_bp.route('/history', methods=['GET'])
def get_history():
    """Endpoint to get query history."""
    return controller.get_history()